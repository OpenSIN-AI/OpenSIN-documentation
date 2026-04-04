# A2A Protocol

## Overview

The Agent-to-Agent (A2A) protocol enables direct agent communication.

## Message Format

```json
{
  "version": "1.0.0",
  "type": "request|response|notification|error",
  "id": "unique-message-id",
  "from": "sender",
  "to": "recipient",
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

All requests require API key in `Authorization` header.

## Next Steps
- [Security](/architecture/security)
- [Scalability](/architecture/scalability)
