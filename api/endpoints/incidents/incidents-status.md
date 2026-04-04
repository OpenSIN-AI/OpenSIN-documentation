# Incidents Status API Endpoint

> **Method:** GET | **Resource:** Incidents | **Version:** v1

## Endpoint

```
GET /api/v1/incidents/status
```

## Description

Incidents Status endpoint for the OpenSIN-AI API.

## Request

### Headers

| Header | Required | Value |
|--------|----------|-------|
| Authorization | Yes | Bearer {token} |
| Content-Type | Yes | application/json |
| X-Request-ID | No | Unique request ID |

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer | No | Page number (default: 1) |
| limit | integer | No | Items per page (default: 20) |
| sort | string | No | Sort field |
| order | string | No | Sort order (asc/desc) |

## Response

### Success Response (200 OK)

```json
{
  "status": "success",
  "data": {},
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 100
  }
}
```

### Error Responses

| Status | Code | Description |
|--------|------|-------------|
| 400 | BAD_REQUEST | Invalid request parameters |
| 401 | UNAUTHORIZED | Missing or invalid token |
| 403 | FORBIDDEN | Insufficient permissions |
| 404 | NOT_FOUND | Resource not found |
| 429 | RATE_LIMITED | Too many requests |
| 500 | INTERNAL_ERROR | Internal server error |

## Rate Limits

| Tier | Requests/Minute | Requests/Hour |
|------|-----------------|---------------|
| Free | 60 | 1,000 |
| Standard | 300 | 10,000 |
| Enterprise | 1,000 | 100,000 |

## Examples

### cURL

```bash
curl -X GET https://api.opensin.ai/api/v1/incidents/status \
  -H "Authorization: Bearer ${token}" \
  -H "Content-Type: application/json"
```

### Python

```python
import requests
response = requests.get(
    "https://api.opensin.ai/api/v1/incidents/status",
    headers={"Authorization": f"Bearer ${token}"}
)
print(response.json())
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
