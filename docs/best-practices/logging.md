# Logging Best Practices

> **Status:** ✅ Active | **Type:** Observability

## Overview

Logging guidelines for OpenSIN-AI projects.

## Log Levels

| Level | Usage |
|-------|-------|
| ERROR | Service failures |
| WARN | Degraded performance |
| INFO | Important events |
| DEBUG | Development details |

## Format

```json
{
  "timestamp": "2026-04-04T10:00:00Z",
  "level": "INFO",
  "service": "n8n",
  "message": "Workflow executed",
  "context": {"workflowId": "abc123"}
}
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
