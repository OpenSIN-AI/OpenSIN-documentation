# Production Deployment Guide

Deploy OpenSIN to production with best practices for reliability, security, and scale.

## Deployment Options

| Platform | Best For | Cost | Setup Time |
|----------|----------|------|------------|
| Hugging Face Spaces | Quick prototyping | Free | 10 min |
| AWS EC2 | Production workloads | $$ | 1 hour |
| Google Cloud Run | Serverless scaling | $$ | 30 min |
| Azure Container Apps | Enterprise | $$$ | 1 hour |
| Oracle Cloud (OCI) | Cost optimization | $ | 1 hour |
| Self-hosted | Full control | Variable | 2 hours |

## Option 1: Hugging Face Spaces

### Quick Deploy

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Create new Space with Docker SDK
3. Upload your OpenSIN app
4. Set environment variables
5. Deploy

### app.py

```python
from opensin import Agent, Team
import gradio as gr

agent = Agent(
    name="assistant",
    model="gpt-4",
    system_prompt="You are a helpful assistant."
)

def chat(message, history):
    response = agent.send(message)
    return response.content

demo = gr.ChatInterface(chat)
demo.launch()
```

### requirements.txt

```
opensin-sdk
gradio
```

## Option 2: Docker Deployment

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### docker-compose.yml

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
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./certs:/etc/nginx/certs
```

## Option 3: Kubernetes

### deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: opensin
spec:
  replicas: 3
  selector:
    matchLabels:
      app: opensin
  template:
    metadata:
      labels:
        app: opensin
    spec:
      containers:
      - name: opensin
        image: opensin/agent:latest
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
```

## Production Checklist

### Pre-Deployment

- [ ] Environment variables configured
- [ ] API keys secured (not hardcoded)
- [ ] Database migrations run
- [ ] TLS/SSL certificates installed
- [ ] Firewall rules configured
- [ ] Monitoring enabled
- [ ] Logging configured
- [ ] Backup strategy in place
- [ ] Rate limiting enabled
- [ ] Health checks configured

### Post-Deployment

- [ ] Smoke tests pass
- [ ] Monitoring alerts active
- [ ] Error tracking enabled
- [ ] Performance baseline established
- [ ] Load testing completed
- [ ] Incident response plan ready
- [ ] Rollback procedure tested

## Monitoring Setup

### Prometheus + Grafana

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'opensin'
    static_configs:
      - targets: ['opensin:8000']
    metrics_path: '/metrics'
```

### Health Checks

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "agents": await get_agent_status(),
        "database": await check_database(),
        "cache": await check_cache()
    }

@app.get("/health/ready")
async def readiness():
    if await all_systems_ready():
        return {"status": "ready"}
    return {"status": "not ready"}, 503
```

## Scaling Strategies

### Auto-Scaling

```yaml
# Kubernetes HPA
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: opensin-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: opensin
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### Load Balancing

```nginx
# nginx.conf
upstream opensin {
    least_conn;
    server opensin-1:8000;
    server opensin-2:8000;
    server opensin-3:8000;
}

server {
    listen 80;
    server_name api.opensin.ai;

    location / {
        proxy_pass http://opensin;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Backup & Recovery

### Database Backup

```bash
# Daily backup cron
0 2 * * * pg_dump opensin_db | gzip > /backups/opensin_$(date +\%Y\%m\%d).sql.gz

# Restore
gunzip -c /backups/opensin_20260404.sql.gz | psql opensin_db
```

### Configuration Backup

```bash
# Backup environment and config
tar czf /backups/config_$(date +%Y%m%d).tar.gz \
  .env \
  nginx.conf \
  docker-compose.yml \
  k8s/
```

## Next Steps

- [HF Spaces Deployment](/deployment/hf-spaces)
- [Monitoring Guide](/guide/monitoring)
- [Scaling Guide](/guide/scaling)
- [Security Hardening](/guide/security-hardening)
