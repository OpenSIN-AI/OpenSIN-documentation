# Agent Scaling Patterns

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
```

## Request Queue

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

## Connection Pooling

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

## Multi-Region Deployment

```yaml
regions:
  - us-east-1
  - eu-west-1
  - ap-southeast-1

routing:
  type: geo
  fallback: us-east-1
```

## Best Practices

1. Start small — Scale only when needed
2. Monitor everything — Track key metrics
3. Auto-scale — Don't manually manage replicas
4. Use CDN — Cache static responses
5. Test at scale — Load test before production

## Next Steps

- [Production Deployment](/guide/deployment-production)
- [Performance Benchmarking](/guide/performance-benchmarking)
