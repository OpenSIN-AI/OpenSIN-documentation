# Agent Deployment Strategies

Deploy agents safely with zero-downtime strategies.

## Deployment Strategies

### 1. Blue-Green Deployment

```bash
# Deploy new version alongside old
opensin agent deploy my-agent --version 2.0.0 --strategy blue-green

# Switch traffic
opensin agent switch my-agent --to 2.0.0

# Rollback if needed
opensin agent switch my-agent --to 1.2.0
```

### 2. Canary Deployment

```bash
# Deploy to 10% of traffic
opensin agent deploy my-agent --version 2.0.0 --canary 10

# Monitor metrics
opensin agent metrics my-agent --version 2.0.0

# Gradually increase
opensin agent deploy my-agent --version 2.0.0 --canary 25
opensin agent deploy my-agent --version 2.0.0 --canary 50
opensin agent deploy my-agent --version 2.0.0 --canary 100
```

### 3. Rolling Update

```bash
# Update instances one by one
opensin agent deploy my-agent --version 2.0.0 --strategy rolling --max-unavailable 1
```

### 4. Shadow Deployment

```bash
# Send traffic to both versions, but only return old version responses
opensin agent deploy my-agent --version 2.0.0 --strategy shadow

# Compare responses
opensin agent compare my-agent --old 1.2.0 --new 2.0.0
```

## Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: opensin
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    spec:
      containers:
      - name: opensin
        image: ghcr.io/opensin-ai/opensin:latest
        ports:
        - containerPort: 8000
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

## Rollback Procedures

```bash
# Automatic rollback on health check failure
opensin agent deploy my-agent --version 2.0.0 --auto-rollback

# Manual rollback
opensin agent rollback my-agent

# Rollback to specific version
opensin agent rollback my-agent --to 1.2.0
```

## Best Practices

1. Always use health checks — Liveness and readiness probes
2. Start with canary — Test with small traffic first
3. Monitor metrics — Track key metrics during deployment
4. Have rollback plan — Be ready to rollback quickly
5. Automate everything — CI/CD pipeline for deployments

## Next Steps

- [Deployment Automation](/guide/deployment-automation)
- [Production Deployment](/guide/deployment-production)
