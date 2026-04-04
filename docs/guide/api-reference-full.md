# Complete API Reference

Full specification of all OpenSIN API endpoints.

## Base URL

```
https://api.opensin.ai/v1
```

## Authentication

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" https://api.opensin.ai/v1/agents
```

## Agents API

### List Agents

```
GET /agents
```

**Response:**
```json
{
  "agents": [
    {
      "id": "agent_123",
      "name": "researcher",
      "model": "gpt-4",
      "status": "active",
      "created_at": "2026-04-04T10:00:00Z"
    }
  ],
  "total": 1,
  "page": 1,
  "per_page": 20
}
```

### Create Agent

```
POST /agents
```

**Request:**
```json
{
  "name": "researcher",
  "model": "gpt-4",
  "system_prompt": "You are an expert researcher.",
  "temperature": 0.7,
  "max_tokens": 4000,
  "tools": ["web_search", "summarizer"],
  "memory_enabled": true
}
```

### Get Agent

```
GET /agents/{agent_id}
```

### Update Agent

```
PUT /agents/{agent_id}
```

### Delete Agent

```
DELETE /agents/{agent_id}
```

### Send Message

```
POST /agents/{agent_id}/send
```

**Request:**
```json
{
  "message": "Research AI trends for 2026",
  "stream": false,
  "max_tokens": 4000
}
```

**Response:**
```json
{
  "id": "msg_123",
  "content": "Based on my research...",
  "tokens_used": 1250,
  "cost": 0.0375,
  "duration_ms": 2340
}
```

## Teams API

### Create Team

```
POST /teams
```

**Request:**
```json
{
  "name": "research-team",
  "agents": ["agent_123", "agent_456"],
  "strategy": "sequential",
  "max_iterations": 10
}
```

### Execute Team

```
POST /teams/{team_id}/execute
```

**Request:**
```json
{
  "task": "Research and write a report on AI trends",
  "context": {"focus": "enterprise applications"}
}
```

## A2A API

### Get Agent Card

```
GET /a2a/{agent_url}/card
```

### Send A2A Message

```
POST /a2a/message
```

**Request:**
```json
{
  "version": "1.0.0",
  "type": "request",
  "from": "writer",
  "to": "researcher",
  "content": "Research AI trends",
  "priority": "high"
}
```

## Events API

### List Events

```
GET /events?agent_id=agent_123&limit=50
```

### Subscribe to Events

```
POST /events/subscribe
```

**Request:**
```json
{
  "url": "https://your-server.com/webhook",
  "events": ["agent.completed", "agent.failed"],
  "secret": "your-webhook-secret"
}
```

## Webhooks API

### Create Webhook

```
POST /webhooks
```

### List Webhooks

```
GET /webhooks
```

### Delete Webhook

```
DELETE /webhooks/{webhook_id}
```

## Error Responses

```json
{
  "error": {
    "code": "invalid_request",
    "message": "The request was invalid.",
    "details": {"field": "model", "issue": "Unknown model: gpt-5"}
  }
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|------------|-------------|
| `invalid_request` | 400 | Bad request |
| `unauthorized` | 401 | Invalid API key |
| `forbidden` | 403 | Insufficient permissions |
| `not_found` | 404 | Resource not found |
| `rate_limited` | 429 | Rate limit exceeded |
| `internal_error` | 500 | Server error |
| `budget_exceeded` | 402 | Budget limit reached |

## Rate Limits

| Plan | Requests/min | Tokens/day |
|------|-------------|------------|
| Free | 60 | 100,000 |
| Pro | 600 | 1,000,000 |
| Enterprise | Unlimited | Unlimited |

## Next Steps

- [SDK Overview](/api/sdk-overview)
- [Authentication](/integrations/platform-auth)
- [Webhooks & Events](/guide/webhooks-events)
