# Teams Create — API Reference

> **Endpoint:** `POST /api/v1/teams` | **Method:** POST | **Version:** 1.0

## Overview

Detailed API reference for the teams create endpoint.

## Request

### URL

```
POST /api/v1/teams
```

### Headers

| Header | Required | Type | Description |
|--------|----------|------|-------------|
| Authorization | Yes | string | Bearer token for authentication |
| Content-Type | Yes | string | application/json |
| Accept | No | string | application/json |
| X-Request-ID | No | string | Unique request ID for tracing |
| X-Correlation-ID | No | string | Correlation ID for distributed tracing |

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | string | Yes | Resource identifier |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| page | integer | No | 1 | Page number for pagination |
| limit | integer | No | 20 | Items per page (max: 100) |
| sort | string | No | created_at | Field to sort by |
| order | string | No | desc | Sort order (asc/desc) |
| filter | string | No | — | Filter expression |
| fields | string | No | * | Fields to include in response |

### Request Body

```json
{
  "data": {
    "field1": "string",
    "field2": "integer",
    "field3": "boolean",
    "field4": ["array", "of", "strings"],
    "field5": {"nested": "object"}
  },
  "meta": {
    "requestId": "unique-request-id",
    "timestamp": "2026-04-04T10:00:00Z"
  }
}
```

## Response

### Success Response (200 OK)

```json
{
  "status": "success",
  "data": {},
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "totalPages": 5,
    "requestId": "unique-request-id",
    "timestamp": "2026-04-04T10:00:00Z",
    "duration": "45ms"
  }
}
```

### Error Responses

| Status | Code | Description | Resolution |
|--------|------|-------------|------------|
| 400 | BAD_REQUEST | Invalid request parameters | Check request format |
| 401 | UNAUTHORIZED | Missing or invalid token | Verify authentication |
| 403 | FORBIDDEN | Insufficient permissions | Check role permissions |
| 404 | NOT_FOUND | Resource not found | Verify resource ID |
| 409 | CONFLICT | Resource conflict | Check for duplicates |
| 422 | UNPROCESSABLE | Validation failed | Check request body |
| 429 | RATE_LIMITED | Too many requests | Wait and retry |
| 500 | INTERNAL_ERROR | Server error | Contact support |
| 503 | SERVICE_UNAVAILABLE | Service temporarily down | Wait and retry |

## Rate Limits

| Tier | Requests/Minute | Requests/Hour | Requests/Day |
|------|-----------------|---------------|--------------|
| Free | 60 | 1,000 | 10,000 |
| Standard | 300 | 10,000 | 100,000 |
| Enterprise | 1,000 | 100,000 | 1,000,000 |

## Code Examples

### cURL

```bash
curl -X POST https://api.opensin.ai/api/v1/teams \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -H "X-Request-ID: ${REQUEST_ID}"
```

### Python

```python
import requests

response = requests.post(
    "https://api.opensin.ai/api/v1/teams",
    headers={
        "Authorization": f"Bearer ${TOKEN}",
        "Content-Type": "application/json",
        "X-Request-ID": REQUEST_ID
    }
)
response.raise_for_status()
data = response.json()
```

### JavaScript/TypeScript

```typescript
const response = await fetch(
    'https://api.opensin.ai/api/v1/teams',
    {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${TOKEN}`,
            'Content-Type': 'application/json',
            'X-Request-ID': requestId
        }
    }
);
const data = await response.json();
```

## Testing

```bash
# Test with mock server
curl -X POST http://localhost:3000/api/v1/teams

# Test with staging
curl -X POST https://staging-api.opensin.ai/api/v1/teams
```

## Related Endpoints

- [Teams List](./teams-list.md)
- [Teams Health](./teams-health.md)
- [Teams Metrics](./teams-metrics.md)

---

*Last updated: 2026-04-04 by SIN-Zeus*
