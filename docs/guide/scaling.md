# Scaling Guide

## Overview

This guide covers scaling OpenSIN for production workloads.

## Horizontal Scaling

```bash
docker-compose up -d --scale opensin-core=3
```

## Load Balancing

Configure a load balancer (nginx, HAProxy, etc.):

```nginx
upstream opensin {
    server opensin-core-1:3000;
    server opensin-core-2:3000;
    server opensin-core-3:3000;
}

server {
    listen 80;
    location / {
        proxy_pass http://opensin;
    }
}
```

## Database Scaling

- Use read replicas for read-heavy workloads
- Use sharding for write-heavy workloads
- Use connection pooling for efficient database connections

## Caching

- Use Redis for caching frequently accessed data
- Use CDN for static assets
- Use in-memory caching for session data

## Performance Tuning

- Increase Node.js heap size
- Use connection pooling
- Enable compression
- Use HTTP/2

## Next Steps
- [Monitoring](/guide/monitoring)
- [Troubleshooting](/guide/troubleshooting)
