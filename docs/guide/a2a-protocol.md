# A2A Protocol

The Agent-to-Agent (A2A) protocol enables direct communication between OpenSIN agents.

## Overview

A2A allows agents to:
- Send messages to each other
- Request information or actions
- Share context and state
- Coordinate complex workflows

## Message Types

| Type | Description |
|------|-------------|
| request | Request information or action |
| response | Response to a request |
| notification | One-way notification |
| error | Error message |

## Using A2A

```bash
opensin a2a send --from agent1 --to agent2 --message "Research AI trends"
```

## Next Steps

- [Team Orchestration](/guide/team-orchestration)
- [MCP Integration](/guide/mcp-integration)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **LLM via opencode CLI** | -2.5 | `opencode run --format json` — KEINE direkten API-Calls |
| **A2A-Agenten-Pflicht** | -200.0 | SELBST MACHEN via `create-a2a-sin-agent` |
| **Kommentar-Pflicht** | -6.0 | EXTREM umfangreiche Kommentare |

→ [Alle Mandate](/best-practices/a2a-communication)
