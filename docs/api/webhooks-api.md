# Webhooks API API

> **Version:** v1 | **Status:** ✅ Active

## Overview

Webhooks API — Webhook management.

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/webhooks` | GET | List all |
| `/api/v1/webhooks/{id}` | GET | Get by ID |
| `/api/v1/webhooks` | POST | Create new |
| `/api/v1/webhooks/{id}` | PUT | Update |
| `/api/v1/webhooks/{id}` | DELETE | Delete |

## Authentication

All endpoints require Bearer token authentication.

## Rate Limits

- 100 requests per minute
- 10,000 requests per hour

---

*Last updated: 2026-04-04 by SIN-Zesus*
