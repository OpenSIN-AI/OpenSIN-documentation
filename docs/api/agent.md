---
title: Agent API
description: API reference for OpenSIN agents
---

# Agent API

Create and manage OpenSIN agents.

## Endpoints

### Create Agent

```http
POST /v1/agents
```

**Request:**
```json
{
  "name": "researcher",
  "model": "openai/gpt-5.4",
  "system_prompt": "You are an expert researcher.",
  "temperature": 0.7,
  "max_tokens": 4000,
  "tools": ["web_search", "summarizer"]
}
```

**Response:**
```json
{
  "id": "agent_123",
  "name": "researcher",
  "model": "openai/gpt-5.4",
  "is_active": true,
  "created_at": "2026-04-04T10:00:00Z"
}
```

### List Agents

```http
GET /v1/agents
```

### Get Agent

```http
GET /v1/agents/{agent_id}
```

### Send Message

```http
POST /v1/agents/{agent_id}/send
```

**Request:**
```json
{
  "message": "Research AI trends for 2026",
  "stream": false,
  "max_tokens": 4000
}
```

### Delete Agent

```http
DELETE /v1/agents/{agent_id}
```

## Next Steps

- [Team API](/api/team)
- [A2A Protocol](/api/a2a)
