# n8n Architecture

> **Status:** ✅ Active | **Type:** Workflow Engine

## Overview

n8n serves as the workflow automation engine for OpenSIN-AI.

## Architecture

```
Trigger → Workflow → Actions → Notifications
    ↓
  n8n Server (OCI VM)
    ↓
  SQLite Database
```

## Current Workflows

22 active workflows covering:
- GitHub monitoring
- Issue processing
- Security scanning
- Infrastructure health
- Token pool management

---

*Last updated: 2026-04-04 by SIN-Zeus*
