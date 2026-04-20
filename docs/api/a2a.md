---
title: A2A Protocol API
description: Agent-to-Agent communication protocol
---

# A2A Protocol API

Direct communication between OpenSIN agents.

> [!WARNING]
> `api.opensin.ai` is documented in the registry as internal/unverified. Use the endpoint examples below only when the backend surface is verified for the environment you are working in.

## Overview

The A2A (Agent-to-Agent) protocol enables agents to communicate directly without going through a central coordinator.

## Endpoints

### Get Agent Card

```http
GET /v1/a2a/{agent_url}/card
```

**Response:**
```json
{
  "name": "researcher",
  "version": "1.0.0",
  "capabilities": ["web_search", "summarization"],
  "protocols": ["a2a"],
  "endpoints": {
    "a2a": "https://api.opensin.ai/v1/a2a/researcher"
  }
}
```

### Send A2A Message

```http
POST /v1/a2a/message
```

**Request:**
```json
{
  "version": "1.0.0",
  "type": "request",
  "from_agent": "writer",
  "to_agent": "researcher",
  "content": "Research AI trends for 2026",
  "priority": "high"
}
```

## Message Types

| Type | Description |
|------|-------------|
| request | Request information or action |
| response | Response to a request |
| notification | One-way notification |
| error | Error message |

## Next Steps

- [Agent API](/api/agent)
- [Team API](/api/team)

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
