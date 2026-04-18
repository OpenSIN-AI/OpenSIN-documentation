# SIN-Hermes — Task Dispatcher

**Role:** Global Task Dispatcher & Fleet Health Monitor
**Model:** `qwen/coder-model`
**Status:** Active
**URL:** `https://hermes.opensin.ai`

---

## Overview

SIN-Hermes is the global dispatcher and router for the OpenSIN-AI fleet. It receives tasks from SIN-Zeus or external triggers, routes them to the appropriate Team Manager or agent, and monitors fleet health across all nodes.

---

## Responsibilities

### 1. Task Routing
- Receives payloads from Zeus, webhooks, or external platforms
- Maps tasks to Team Managers based on capability registry
- Ensures idempotent delivery (no duplicate task execution)
- Tracks task lifecycle from submission to completion

### 2. Fleet Health Monitoring
- Monitors agent heartbeat across all fleet nodes
- Detects crashed or unresponsive agents
- Triggers self-healing via GitHub Issues
- Escalates critical failures to Telegram

### 3. Platform Intake
- Receives work from external platforms (Prolific, HackerOne, Upwork, etc.)
- Normalizes payloads into `work_item` schema
- Creates or updates GitHub Issues for tracking
- Dispatches to appropriate team via PR-Watcher

### 4. Self-Healing Loop
```
Error detected
  → Create GitHub Issue (SIN-GitHub-Issues)
    → SIN-Hermes dispatches to Team Coder
      → Team Coder plans and fixes
        → PR created and reviewed
          → Issue closed with root cause documented
```

---

## MCP Configuration

```json
{
  "sin-hermes": {
    "command": "node",
    "args": ["dist/src/cli.js", "serve-mcp"],
    "env": {
      "HERMES_URL": "https://hermes.opensin.ai"
    }
  }
}
```

---

## Agent Card

```json
{
  "name": "SIN-Hermes",
  "version": "1.0.0",
  "description": "Task dispatcher and router for the SIN fleet",
  "url": "https://hermes.opensin.ai",
  "capabilities": ["dispatch", "routing", "health-monitoring", "intake"]
}
```

---

## Platform Integration

| Platform | Intake Method | Normalization |
|----------|--------------|---------------|
| GitHub Webhooks | Push/PR events | → `work_item` schema |
| n8n Workflows | HTTP webhook | → `work_item` schema |
| Telegram Bot | Command/message | → `work_item` schema |
| External APIs | Poller/webhook | → `work_item` schema |

---

## Commands

| Command | Description |
|---------|-------------|
| `hermes.dispatch` | Route task to appropriate team/agent |
| `hermes.health` | Fleet health status check |
| `hermes.intake` | Process incoming platform payload |
| `hermes.self-heal` | Trigger self-healing loop for detected errors |

---

## Related

- [Zeus — Fleet Commander](/governance/zeus)
- [Governance Overview](/governance/overview)
- [A2A Architecture](/architecture/a2a)
- [Inbound Intake Architecture](https://github.com/OpenSIN-AI/OpenSIN-documentation/blob/main/INBOUND_WORK_ARCHITECTURE.md)

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Immediate Bug Registry** | -4.0 | JEDER Bug SOFORT als GitHub Issue |
| **PR-Watcher** | 0.0 | Alle Repos brauchen PR-Watcher |
| **Zeus/Hermes** | 0.0 | Fleet-Kommando via SIN-Zeus |

→ [Alle Mandate](/best-practices/error-handling)
