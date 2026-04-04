# Event Bridge

> **Status:** ✅ Active | **Type:** Event-Driven Communication

## Overview

Event bridge enables event-driven communication between OpenSIN components using pub/sub patterns.

## Event Types

| Event | Source | Consumers |
|-------|--------|-----------|
| `task.created` | Task Manager | Agents, n8n |
| `task.completed` | Agent | Task Manager, n8n |
| `agent.started` | Agent Orchestrator | Monitoring |
| `agent.error` | Agent | Error Handler, Telegram |

## Configuration

```json
{
  "eventBridge": {
    "provider": "redis",
    "channels": ["tasks", "agents", "errors"]
  }
}
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
