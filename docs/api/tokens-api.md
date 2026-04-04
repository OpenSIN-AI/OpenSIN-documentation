# Tokens API API

> **Version:** v1 | **Status:** ✅ Active

## Overview

Tokens API — Token pool management.

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/tokens` | GET | List all |
| `/api/v1/tokens/{id}` | GET | Get by ID |
| `/api/v1/tokens` | POST | Create new |
| `/api/v1/tokens/{id}` | PUT | Update |
| `/api/v1/tokens/{id}` | DELETE | Delete |

## Authentication

All endpoints require Bearer token authentication.

## Rate Limits

- 100 requests per minute
- 10,000 requests per hour

---

*Last updated: 2026-04-04 by SIN-Zesus*
