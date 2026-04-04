# Scaling Guide

## Horizontal Scaling

```bash
docker-compose up -d --scale opensin-core=3
```

## Load Balancing

```nginx
upstream opensin {
    server opensin-core-1:3000;
    server opensin-core-2:3000;
    server opensin-core-3:3000;
}
```

## Database Scaling

- Read replicas
- Sharding
- Connection pooling

## Caching

- Redis for data
- CDN for static assets

## Next Steps
- [Monitoring](/guide/monitoring)
- [Troubleshooting](/guide/troubleshooting)
