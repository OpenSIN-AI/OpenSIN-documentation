# Scaling

Scale OpenSIN agents for high-throughput workloads.

## Horizontal Scaling

Add more agent replicas to handle increased load.

## Vertical Scaling

Increase resources (memory, CPU) for individual agents.

## Auto-Scaling

Configure auto-scaling based on metrics:

```yaml
minReplicas: 2
maxReplicas: 50
targetCPU: 70%
```

## Next Steps

- [Monitoring](/guide/monitoring)
- [Deployment](/guide/deployment)
