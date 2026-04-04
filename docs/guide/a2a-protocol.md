# A2A Protocol

## What is A2A?

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
| `/a2a/v1/message/send` | POST | Send A2A message |
| `/a2a/v1/message/status` | GET | Get message status |

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

All A2A communications are authenticated using API keys.

```javascript
const agent = new Agent({
  name: 'my-agent',
  auth: {
    type: 'api-key',
    key: process.env.AGENT_API_KEY
  }
});
```

## Next Steps
- [MCP Integration](/guide/mcp-integration)
- [Deployment](/guide/deployment)
