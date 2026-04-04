# A2A Fleet Architecture

> **Status:** ✅ Active | **Type:** System Design

## Overview

The A2A fleet consists of 130+ agents organized into teams.

## Team Structure

```
Fleet Orchestrator
├── Team Marketing (8 agents)
├── Team Coding (6 agents)
├── Team Infrastructure (8 agents)
├── Team Apple Apps (9 agents)
├── Team Google Apps (6 agents)
├── Team Security (12 agents)
└── Team Worker (3 agents)
```

## Communication

Agents communicate via:
- A2A Protocol (direct)
- n8n Workflows (async)
- Telegram (notifications)

---

*Last updated: 2026-04-04 by SIN-Zeus*
