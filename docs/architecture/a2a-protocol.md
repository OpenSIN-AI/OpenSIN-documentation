# A2A Protocol Architecture

> **Status:** ✅ Active | **Type:** Protocol Design

## Overview

Agent-to-Agent (A2A) protocol enables communication between OpenSIN agents.

## Protocol Flow

```
Agent A → A2A Message → Agent B
              ↓
        Message Router
              ↓
        Task Queue
```

## Message Format

```json
{
  "from": "agent-a",
  "to": "agent-b",
  "type": "task",
  "payload": {"action": "execute", "params": {}},
  "timestamp": "2026-04-04T10:00:00Z"
}
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
