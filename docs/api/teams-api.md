# Teams API API

> **Version:** v1 | **Status:** ✅ Active

## Overview

Teams API — Team management.

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/teams` | GET | List all |
| `/api/v1/teams/{id}` | GET | Get by ID |
| `/api/v1/teams` | POST | Create new |
| `/api/v1/teams/{id}` | PUT | Update |
| `/api/v1/teams/{id}` | DELETE | Delete |

## Authentication

All endpoints require Bearer token authentication.

## Rate Limits

- 100 requests per minute
- 10,000 requests per hour

---

*Last updated: 2026-04-04 by SIN-Zesus*
