# API Overview

## Overview

OpenSIN provides a comprehensive API for building and managing AI agents.

## Core API

| Class | Description |
|-------|-------------|
| `Agent` | Create and manage individual agents |
| `Team` | Create and manage agent teams |
| `Orchestrator` | Coordinate agent workflows |
| `Message` | Handle agent-to-agent messages |

## REST API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/agents` | GET | List all agents |
| `/api/agents/:id` | GET | Get agent details |
| `/api/agents/:id/message` | POST | Send message to agent |
| `/api/teams` | GET | List all teams |
| `/api/teams/:id` | GET | Get team details |
| `/api/teams/:id/assign` | POST | Assign task to team |

## A2A API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/a2a/v1/agent/getCard` | GET | Get agent card |
| `/a2a/v1/message/send` | POST | Send A2A message |
| `/a2a/v1/message/status` | GET | Get message status |

## Next Steps

- [Agent API](/api/agent) — Agent API reference
- [Team API](/api/team) — Team API reference
- [A2A API](/api/a2a) — A2A protocol reference
- [Message API](/api/message) — Message API reference
- [Events API](/api/events) — Events API reference
- [Orchestrator API](/api/orchestrator) — Orchestrator API reference
- [MCP API](/api/mcp) — MCP API reference
