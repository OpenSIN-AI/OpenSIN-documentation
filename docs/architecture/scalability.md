# Scalability Architecture

## Horizontal Scaling

```bash
docker-compose up -d --scale opensin-core=3
```

## Load Balancing

Configure nginx or HAProxy to distribute traffic.

## Database Scaling

- Read replicas for read-heavy workloads
- Sharding for write-heavy workloads
- Connection pooling

## Caching

- Redis for frequently accessed data
- CDN for static assets
- In-memory caching for sessions

## Monitoring

- Prometheus for metrics
- Grafana for visualization
- Alertmanager for alerting

## Next Steps
- [Deployment](/guide/deployment)
- [Best Practices](/best-practices/agent-design)
