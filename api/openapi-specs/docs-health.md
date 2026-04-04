# Docs Health — OpenAPI Specification

> **Endpoint:** /api/v1/docs | **Method:** HEALTH | **Version:** 1.0

## Overview

OpenAPI specification for the docs health endpoint.

## Request

### URL

```
HEALTH /api/v1/docs
```

### Headers

| Header | Required | Type | Description |
|--------|----------|------|-------------|
| Authorization | Yes | string | Bearer token |
| Content-Type | Yes | string | application/json |
| Accept | No | string | application/json |
| X-Request-ID | No | string | Request ID for tracing |

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | string | Yes | Resource identifier |

### Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| page | integer | No | 1 | Page number |
| limit | integer | No | 20 | Items per page |
| sort | string | No | created_at | Sort field |
| order | string | No | desc | Sort order |
| filter | string | No | — | Filter expression |

### Request Body

```json
{
  "data": {
    "field1": "string",
    "field2": "integer",
    "field3": "boolean"
  },
  "meta": {
    "requestId": "string"
  }
}
```

## Response

### Success (200 OK)

```json
{
  "status": "success",
  "data": {},
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "requestId": "string",
    "timestamp": "2026-04-04T10:00:00Z"
  }
}
```

### Error Responses

| Status | Code | Description |
|--------|------|-------------|
| 400 | BAD_REQUEST | Invalid request |
| 401 | UNAUTHORIZED | Missing token |
| 403 | FORBIDDEN | No permission |
| 404 | NOT_FOUND | Resource not found |
| 429 | RATE_LIMITED | Too many requests |
| 500 | INTERNAL_ERROR | Server error |

## Rate Limits

| Tier | Requests/Minute | Requests/Hour |
|------|-----------------|---------------|
| Free | 60 | 1,000 |
| Standard | 300 | 10,000 |
| Enterprise | 1,000 | 100,000 |

---

*Last updated: 2026-04-04 by SIN-Zeus*
