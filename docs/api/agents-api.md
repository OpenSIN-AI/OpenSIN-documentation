# Agents API API

> **Version:** v1 | **Status:** ✅ Active

## Overview

Agents API — List, create, update, delete agents.

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/agents` | GET | List all |
| `/api/v1/agents/{id}` | GET | Get by ID |
| `/api/v1/agents` | POST | Create new |
| `/api/v1/agents/{id}` | PUT | Update |
| `/api/v1/agents/{id}` | DELETE | Delete |

## Authentication

All endpoints require Bearer token authentication.

## Rate Limits

- 100 requests per minute
- 10,000 requests per hour

---

*Last updated: 2026-04-04 by SIN-Zesus*
