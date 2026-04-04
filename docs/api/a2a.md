# A2A API

## Endpoints

### GET `/a2a/v1/agent/getCard`

Get agent card.

**Response:**
```json
{
  "name": "researcher",
  "capabilities": ["research", "analyze"],
  "url": "https://agent.example.com/a2a/v1",
  "version": "1.0.0"
}
```

### POST `/a2a/v1/message/send`

Send A2A message.

**Request:**
```json
{
  "type": "request",
  "task": "Research AI trends",
  "priority": "high",
  "data": { "topic": "AI agents" }
}
```

**Response:**
```json
{
  "status": "success",
  "data": { "result": "..." }
}
```

### GET `/a2a/v1/message/status`

Get message status.

**Response:**
```json
{
  "status": "completed",
  "timestamp": "2026-04-04T04:00:00Z"
}
```
