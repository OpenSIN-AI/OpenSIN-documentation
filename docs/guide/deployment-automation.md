# Deployment Automation Guide

Automate OpenSIN deployments with CI/CD pipelines.

## Overview

Automated deployments ensure consistent, repeatable, and safe releases of OpenSIN agents and services.

## CI/CD Pipeline Architecture

```
[Code Push] → [Lint & Test] → [Build Image] → [Security Scan]
                                          ↓
                              [Deploy to Staging] → [Integration Tests]
                                          ↓
                              [Manual Approval] → [Deploy to Production]
                                          ↓
                              [Smoke Tests] → [Monitor & Alert]
```

## GitHub Actions Pipeline

### Complete Workflow

```yaml
# .github/workflows/deploy.yml
name: Deploy OpenSIN Agent

on:
  push:
    branches: [main]
  workflow_dispatch:

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements-dev.txt
      - run: pytest tests/ -v --cov=opensin --cov-report=xml
      - run: ruff check .
      - run: mypy opensin/
      - uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml

  build:
    needs: test
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  security-scan:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-results.sarif'
      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v2
        if: always()
        with:
          sarif_file: 'trivy-results.sarif'

  deploy-staging:
    needs: [build, security-scan]
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: azure/k8s-deploy@v4
        with:
          namespace: staging
          manifests: k8s/staging/
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}

  integration-tests:
    needs: deploy-staging
    runs-on: ubuntu-latest
    steps:
      - run: pytest tests/integration/ -v --staging-url=${{ secrets.STAGING_URL }}

  deploy-production:
    needs: integration-tests
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: azure/k8s-deploy@v4
        with:
          namespace: production
          manifests: k8s/production/
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
          strategy: blue-green

  smoke-tests:
    needs: deploy-production
    runs-on: ubuntu-latest
    steps:
      - run: pytest tests/smoke/ -v --prod-url=${{ secrets.PROD_URL }}
```

## Docker Deployment

### Multi-stage Dockerfile

```dockerfile
# Build stage
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

# Production stage
FROM python:3.11-slim

WORKDIR /app

# Copy installed dependencies
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  opensin:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - REDIS_URL=redis://redis:6379
      - DATABASE_URL=postgresql://user:pass@db:5432/opensin
    depends_on:
      redis:
        condition: service_healthy
      db:
        condition: service_healthy
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=opensin
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 3

volumes:
  postgres_data:
```

## Kubernetes Deployment

### Production Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: opensin
  labels:
    app: opensin
    version: ${VERSION}
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: opensin
  template:
    metadata:
      labels:
        app: opensin
        version: ${VERSION}
    spec:
      serviceAccountName: opensin
      containers:
      - name: opensin
        image: ghcr.io/opensin-ai/opensin:${VERSION}
        ports:
        - containerPort: 8000
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: opensin-secrets
              key: api-key
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health/ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

## Rollback Strategy

### Automatic Rollback

```yaml
# Rollback on health check failure
apiVersion: apps/v1
kind: Deployment
metadata:
  name: opensin
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  # Kubernetes will automatically rollback if health checks fail
```

### Manual Rollback

```bash
# Rollback to previous version
kubectl rollout undo deployment/opensin

# Rollback to specific version
kubectl rollout undo deployment/opensin --to-revision=3

# Check rollout status
kubectl rollout status deployment/opensin
```

## Best Practices

1. **Immutable deployments** — Each deployment is a new version
2. **Health checks** — Always define liveness and readiness probes
3. **Resource limits** — Prevent resource exhaustion
4. **Blue-green deployments** — Zero-downtime releases
5. **Automated rollbacks** — Rollback on health check failures
6. **Canary releases** — Test with small traffic percentage first
7. **Feature flags** — Enable/disable features without deployment

## Next Steps

- [Production Deployment](/guide/deployment-production)
- [Monitoring Guide](/guide/monitoring)
- [Security Hardening](/guide/security-hardening)
