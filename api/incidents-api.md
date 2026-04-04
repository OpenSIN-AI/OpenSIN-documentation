# Incidents API API

> **Version:** v1 | **Status:** ✅ Active

## Overview

Incidents API — Incident tracking.

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/incidents` | GET | List all |
| `/api/v1/incidents/{id}` | GET | Get by ID |
| `/api/v1/incidents` | POST | Create new |
| `/api/v1/incidents/{id}` | PUT | Update |
| `/api/v1/incidents/{id}` | DELETE | Delete |

## Authentication

All endpoints require Bearer token authentication.

## Rate Limits

- 100 requests per minute
- 10,000 requests per hour

---

*Last updated: 2026-04-04 by SIN-Zesus*
