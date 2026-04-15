# Monitoring

Monitor OpenSIN agents in production.

## Key Metrics

| Metric | Description |
|--------|-------------|
| Request Rate | Number of requests per second |
| Error Rate | Percentage of failed requests |
| Latency (p50/p99) | Response time percentiles |
| Token Usage | Input and output tokens |
| Cost | API costs per hour/day |

## Health Checks

```bash
bun run health  # Run health checks
bun run health  # Run health checks agents
```

## Next Steps

- [Deployment](/guide/deployment)
- [Scaling](/guide/scaling)
