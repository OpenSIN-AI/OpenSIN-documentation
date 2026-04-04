# REST API Bridge

> **Status:** ✅ Active | **Type:** HTTP Communication

## Overview

REST API bridge provides standard HTTP endpoints for external service integration.

## Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/v1/agents` | GET | List all agents |
| `/api/v1/agents/{id}` | GET | Get agent details |
| `/api/v1/tasks` | POST | Create task |
| `/api/v1/tasks/{id}` | GET | Get task status |

## Authentication

All endpoints require Bearer token authentication.

---

*Last updated: 2026-04-04 by SIN-Zeus*
