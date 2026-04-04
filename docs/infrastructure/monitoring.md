# Monitoring Setup

> **Status:** ✅ Active | **Type:** Observability

## Overview

OpenSIN monitoring setup for infrastructure and application observability.

## Components

| Component | Purpose |
|-----------|---------|
| n8n Health Monitor | Workflow health |
| Supabase Health Monitor | Database health |
| OCI VM Disk Monitor | Disk usage |
| Token Pool Monitor | Token availability |

## Alerts

Alerts are sent via Telegram to the operations team:
- Service down
- High disk usage (>90%)
- Token pool empty
- Workflow failures

---

*Last updated: 2026-04-04 by SIN-Zeus*
