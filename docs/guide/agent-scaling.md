# Agent Scaling Guide

Scale OpenSIN agents from single instance to millions of requests.

## Scaling Dimensions

| Dimension | How to Scale | When |
|-----------|-------------|------|
| Requests | Add replicas | > 100 req/min |
| Context | Increase memory | > 8000 tokens |
| Throughput | Parallel agents | > 1000 req/min |
| Availability | Multi-region | > 99.9% uptime |
| Cost | Model tiering | Budget constraints |

## Horizontal Scaling

### Kubernetes Auto-Scaling

```yaml
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
  maxReplicas: 50
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

### Load Balancing

```yaml
apiVersion: v1
kind: Service
metadata:
  name: opensin
spec:
  type: LoadBalancer
  selector:
    app: opensin
  ports:
  - port: 80
    targetPort: 8000
  sessionAffinity: ClientIP
```

## Vertical Scaling

### Resource Optimization

```python
# Optimize agent for high throughput
agent = Agent(
    name="high-throughput",
    model="gpt-3.5-turbo",  # Fast and cheap
    max_tokens=500,  # Short responses
    streaming=True,  # Faster perceived latency
    prompt_caching=True,  # Reduce token usage
    batch_processing=True  # Process multiple requests
)
```

## Multi-Region Deployment

```yaml
# Deploy to multiple regions
regions:
  - us-east-1
  - eu-west-1
  - ap-southeast-1

# Route to nearest region
routing:
  type: geo
  fallback: us-east-1
```

## Scaling Patterns

### Request Queue

```python
from opensin import RequestQueue

queue = RequestQueue(
    max_size=10000,
    workers=10,
    priority_enabled=True
)

# Add requests
await queue.add(request, priority="high")

# Process requests
async for request in queue:
    result = await agent.process(request)
    await queue.complete(request, result)
```

### Connection Pooling

```python
from opensin import ConnectionPool

pool = ConnectionPool(
    max_connections=100,
    min_connections=10,
    timeout=30
)

async with pool.connection() as conn:
    response = await conn.request("POST", "/agents/send", data=prompt)
```

## Monitoring Scale

```python
from opensin import ScaleMonitor

monitor = ScaleMonitor(
    metrics=["requests_per_second", "latency_p99", "error_rate"],
    thresholds={
        "requests_per_second": {"scale_up": 100, "scale_down": 20},
        "latency_p99": {"scale_up": 5000, "scale_down": 1000},
        "error_rate": {"scale_up": 0.05, "scale_down": 0.01}
    }
)

# Auto-scale based on metrics
await monitor.auto_scale()
```

## Best Practices

1. **Start small** — Scale only when needed
2. **Monitor everything** — Track key metrics
3. **Auto-scale** — Don't manually manage replicas
4. **Use CDN** — Cache static responses
5. **Test at scale** — Load test before production

## Next Steps

- [Production Deployment](/guide/deployment-production)
- [Performance Benchmarking](/guide/performance-benchmarking)
