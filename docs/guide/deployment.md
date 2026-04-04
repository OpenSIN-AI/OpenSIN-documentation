# Deployment

## Docker Deployment

```bash
# Using Docker Compose
docker-compose up -d

# Using Docker
docker build -t opensin .
docker run -p 3000:3000 opensin
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `NODE_ENV` | Environment (development/production) | No |
| `PORT` | Server port (default: 3000) | No |
| `OPENAI_API_KEY` | OpenAI API key | Yes |
| `ANTHROPIC_API_KEY` | Anthropic API key | No |

## Production Checklist

- [ ] Set `NODE_ENV=production`
- [ ] Configure all required API keys
- [ ] Set up monitoring and logging
- [ ] Configure rate limiting
- [ ] Set up SSL/TLS
- [ ] Configure backup strategy
- [ ] Test disaster recovery

## Scaling

### Horizontal Scaling

```bash
docker-compose up -d --scale opensin-core=3
```

### Load Balancing

Configure a load balancer to distribute traffic across instances.

## Next Steps
- [Best Practices](/best-practices/agent-design)
- [Security](/architecture/security)
