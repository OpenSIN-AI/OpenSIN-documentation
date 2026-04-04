# Auth API API

> **Version:** v1 | **Status:** ✅ Active

## Overview

Auth API — Authentication endpoints.

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/auth` | GET | List all |
| `/api/v1/auth/{id}` | GET | Get by ID |
| `/api/v1/auth` | POST | Create new |
| `/api/v1/auth/{id}` | PUT | Update |
| `/api/v1/auth/{id}` | DELETE | Delete |

## Authentication

All endpoints require Bearer token authentication.

## Rate Limits

- 100 requests per minute
- 10,000 requests per hour

---

*Last updated: 2026-04-04 by SIN-Zesus*
