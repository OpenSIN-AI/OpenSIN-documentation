# Data Flow Architecture

> **Status:** ✅ Active | **Type:** System Design

## Overview

Data flow through the OpenSIN-AI ecosystem.

## Flow

```
User Input → OpenCode → Agent → MCP → External Service
                                    ↓
                              Supabase DB
                                    ↓
                              n8n Workflow
                                    ↓
                              Telegram Alert
```

## Data Storage

| Component | Storage | Type |
|-----------|---------|------|
| OpenCode | Local files | Config |
| n8n | SQLite | Workflows |
| Supabase | PostgreSQL | Business Data |
| HF Spaces | Git | Code |

---

*Last updated: 2026-04-04 by SIN-Zeus*
