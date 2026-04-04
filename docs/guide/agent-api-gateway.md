# Agent API Gateway

Configure and manage the OpenSIN API Gateway.

## Overview

The API Gateway is the entry point for all requests to OpenSIN agents. It handles authentication, rate limiting, routing, and response formatting.

## Architecture

```
Client → API Gateway → Auth → Rate Limit → Router → Agent → Response
```

## Configuration

### Basic Config

```yaml
# gateway.yml
server:
  port: 8000
  host: 0.0.0.0
  tls:
    enabled: true
    cert: /etc/ssl/certs/opensin.crt
    key: /etc/ssl/private/opensin.key

auth:
  type: bearer
  jwks_url: https://auth.opensin.ai/.well-known/jwks.json

rate_limit:
  requests_per_minute: 60
  requests_per_hour: 1000
  tokens_per_day: 100000

logging:
  level: INFO
  format: json
  output: stdout
```

### Routing Rules

```yaml
routes:
  - path: /v1/agents/:id/send
    method: POST
    agent: "*"
    timeout: 30
    
  - path: /v1/teams/:id/execute
    method: POST
    team: "*"
    timeout: 120
    
  - path: /v1/a2a/message
    method: POST
    protocol: a2a
    timeout: 60
```

### Middleware

```python
from opensin.gateway import Middleware

middleware = Middleware([
    AuthenticationMiddleware(),
    RateLimitMiddleware(),
    RequestLoggingMiddleware(),
    ResponseFormattingMiddleware(),
    CORSMiddleware(),
])
```

## Authentication

### API Key Auth

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.opensin.ai/v1/agents/researcher/send
```

### OAuth2

```python
from opensin.gateway import OAuth2Middleware

oauth = OAuth2Middleware(
    issuer="https://auth.opensin.ai",
    audience="api.opensin.ai",
    scopes=["agents:read", "agents:write"]
)
```

### JWT Validation

```python
from opensin.gateway import JWTMiddleware

jwt = JWTMiddleware(
    jwks_url="https://auth.opensin.ai/.well-known/jwks.json",
    algorithms=["RS256"],
    issuer="https://auth.opensin.ai"
)
```

## Rate Limiting

### Per-User Limits

```yaml
rate_limits:
  free:
    requests_per_minute: 10
    tokens_per_day: 10000
    
  pro:
    requests_per_minute: 60
    tokens_per_day: 100000
    
  enterprise:
    requests_per_minute: 600
    tokens_per_day: 1000000
```

### Sliding Window

```python
from opensin.gateway import SlidingWindowLimiter

limiter = SlidingWindowLimiter(
    window_size=60,  # seconds
    max_requests=60,
    storage="redis"
)
```

## Response Formatting

### Standard Response

```json
{
  "status": "success",
  "data": {
    "id": "msg_123",
    "content": "Response text",
    "tokens_used": 1250,
    "cost": 0.0375,
    "duration_ms": 2340
  },
  "meta": {
    "request_id": "req_456",
    "timestamp": "2026-04-04T10:00:00Z"
  }
}
```

### Error Response

```json
{
  "status": "error",
  "error": {
    "code": "rate_limited",
    "message": "Rate limit exceeded",
    "details": {
      "retry_after": 30
    }
  },
  "meta": {
    "request_id": "req_456",
    "timestamp": "2026-04-04T10:00:00Z"
  }
}
```

## Best Practices

1. **Always use TLS** — Never expose HTTP endpoints
2. **Validate all input** — Never trust client input
3. **Rate limit everything** — Protect against abuse
4. **Log all requests** — Essential for debugging
5. **Use standard responses** — Consistent API format
6. **Monitor gateway** — Track gateway health separately

## Next Steps

- [API Reference](/api/overview)
- [Security Hardening](/guide/security-hardening)
