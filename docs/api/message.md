# Message API

## Overview

Message API reference for sending and receiving messages between agents.

## Message Format

```json
{
  "id": "unique-message-id",
  "type": "text|image|file",
  "content": "Message content",
  "sender": "agent-name",
  "recipient": "recipient-name",
  "timestamp": "2026-04-04T04:00:00Z",
  "metadata": {}
}
```

## Sending Messages

```javascript
const response = await agent.send({
  type: 'text',
  content: 'Hello!',
  recipient: 'other-agent'
});
```

## Receiving Messages

```javascript
agent.on('message', async (msg) => {
  console.log('Received:', msg.content);
  await agent.respond('Response');
});
```

## Message Types

| Type | Description |
|------|-------------|
| `text` | Text message |
| `image` | Image message |
| `file` | File attachment |
| `command` | Command message |
| `response` | Response message |
| `error` | Error message |

## Next Steps
- [Events API](/api/events)
- [A2A API](/api/a2a)
