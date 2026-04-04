# A2A API

## Overview

The Agent-to-Agent (A2A) protocol enables agents to communicate directly with each other.

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

## Agent Card

```json
{
  "name": "researcher",
  "capabilities": ["research", "analyze"],
  "url": "https://agent.example.com/a2a/v1",
  "version": "1.0.0"
}
```

## Sending Messages

```javascript
const response = await agentA.sendTo(agentB, {
  type: 'request',
  task: 'Research AI trends',
  priority: 'high',
  data: { topic: 'AI agents', year: 2026 }
});
```

## Message Types

| Type | Description |
|------|-------------|
| `request` | Request information or action |
| `response` | Response to a request |
| `notification` | One-way notification |
| `error` | Error message |

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
- [Agent API](/api/agent)
- [Message API](/api/message)
- [Security Architecture](/architecture/security)
