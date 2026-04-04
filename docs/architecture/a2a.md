# A2A Protocol

## Overview

The Agent-to-Agent (A2A) protocol specification.

## Protocol Version

Current version: 1.0.0

## Message Format

```json
{
  "version": "1.0.0",
  "type": "request|response|notification|error",
  "id": "unique-message-id",
  "from": "sender-agent",
  "to": "recipient-agent",
  "timestamp": "2026-04-04T04:00:00Z",
  "data": {}
}
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/a2a/v1/agent/getCard` | GET | Get agent card |
| `/a2a/v1/message/send` | POST | Send message |
| `/a2a/v1/message/status` | GET | Get message status |

## Authentication

All requests must include an API key in the `Authorization` header.

```
Authorization: Bearer YOUR_API_KEY
```

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Internal Server Error |

## Next Steps
- [Security](/architecture/security)
- [Scalability](/architecture/scalability)
