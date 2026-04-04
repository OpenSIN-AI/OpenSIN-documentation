# Workflows API API

> **Version:** v1 | **Status:** ✅ Active

## Overview

Workflows API — Manage n8n workflows.

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/workflows` | GET | List all |
| `/api/v1/workflows/{id}` | GET | Get by ID |
| `/api/v1/workflows` | POST | Create new |
| `/api/v1/workflows/{id}` | PUT | Update |
| `/api/v1/workflows/{id}` | DELETE | Delete |

## Authentication

All endpoints require Bearer token authentication.

## Rate Limits

- 100 requests per minute
- 10,000 requests per hour

---

*Last updated: 2026-04-04 by SIN-Zesus*
