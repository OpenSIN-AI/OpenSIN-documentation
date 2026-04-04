# Mcps Logs API Endpoint — Detailed Reference

> **Method:** GET | **Resource:** Mcps | **Action:** Logs | **Version:** v1

## Endpoint

```
GET /api/v1/mcps/logs
```

## Description

Detailed reference for the mcps logs endpoint.

## Request Specification

### Headers

| Header | Required | Type | Description |
|--------|----------|------|-------------|
| Authorization | Yes | string | Bearer token for authentication |
| Content-Type | Yes | string | application/json |
| X-Request-ID | No | string | Unique request identifier for tracing |
| X-Correlation-ID | No | string | Correlation ID for distributed tracing |
| Accept | No | string | Response format (application/json) |

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | string | Yes (for get/update/delete) | Resource identifier |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| page | integer | No | 1 | Page number for pagination |
| limit | integer | No | 20 | Items per page (max: 100) |
| sort | string | No | created_at | Field to sort by |
| order | string | No | desc | Sort order (asc/desc) |
| filter | string | No | — | Filter expression |
| fields | string | No | * | Fields to include in response |

### Request Body (for POST/PUT)

```json
{
  "data": {
    // Resource-specific fields
  },
  "meta": {
    "requestId": "unique-request-id"
  }
}
```

## Response Specification

### Success Response (200 OK)

```json
{
  "status": "success",
  "data": {
    // Resource data
  },
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "requestId": "unique-request-id",
    "timestamp": "2026-04-04T10:00:00Z"
  }
}
```

### Error Responses

| Status | Code | Description |
|--------|------|-------------|
| 400 | BAD_REQUEST | Invalid request parameters or body |
| 401 | UNAUTHORIZED | Missing or invalid authentication token |
| 403 | FORBIDDEN | Insufficient permissions for this operation |
| 404 | NOT_FOUND | Resource not found |
| 409 | CONFLICT | Resource conflict (duplicate, version mismatch) |
| 422 | UNPROCESSABLE | Request body validation failed |
| 429 | RATE_LIMITED | Too many requests |
| 500 | INTERNAL_ERROR | Internal server error |
| 503 | SERVICE_UNAVAILABLE | Service temporarily unavailable |

## Rate Limits

| Tier | Requests/Minute | Requests/Hour | Requests/Day |
|------|-----------------|---------------|--------------|
| Free | 60 | 1,000 | 10,000 |
| Standard | 300 | 10,000 | 100,000 |
| Enterprise | 1,000 | 100,000 | 1,000,000 |

## Code Examples

### cURL

```bash
curl -X GET https://api.opensin.ai/api/v1/mcps/logs \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -H "X-Request-ID: ${REQUEST_ID}"
```

### Python

```python
import requests

response = requests.get(
    "https://api.opensin.ai/api/v1/mcps/logs",
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
    'https://api.opensin.ai/api/v1/mcps/logs',
    {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${TOKEN}`,
            'Content-Type': 'application/json',
            'X-Request-ID': requestId
        }
    }
);
const data = await response.json();
```

### Go

```go
req, _ := http.NewRequest("GET", "https://api.opensin.ai/api/v1/mcps/logs", nil)
req.Header.Set("Authorization", "Bearer "+token)
req.Header.Set("Content-Type", "application/json")
req.Header.Set("X-Request-ID", requestId)

client := &http.Client{}
resp, err := client.Do(req)
```

## Testing

```bash
# Test with mock server
curl -X GET http://localhost:3000/api/v1/mcps/logs

# Test with staging
curl -X GET https://staging-api.opensin.ai/api/v1/mcps/logs
```

## Related Endpoints

- [Mcps List](./mcps-list-detailed.md)
- [Mcps Health](./mcps-health-detailed.md)

---

*Last updated: 2026-04-04 by SIN-Zeus*
