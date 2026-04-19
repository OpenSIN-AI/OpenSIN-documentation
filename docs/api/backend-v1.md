---
title: OpenSIN Backend V1 API
description: Baseline control-plane API reference for the V1 launch scope.
---

# OpenSIN Backend V1 API

This page documents the **current baseline API surface** for `OpenSIN-backend`.

Source inputs:

- [`OpenSIN-backend/API.md`](https://github.com/OpenSIN-AI/OpenSIN-backend/blob/main/API.md)
- [`app/api/routes/health.py`](https://github.com/OpenSIN-AI/OpenSIN-backend/blob/main/app/api/routes/health.py)
- [`app/api/routes/auth.py`](https://github.com/OpenSIN-AI/OpenSIN-backend/blob/main/app/api/routes/auth.py)
- [`app/routes/billing.py`](https://github.com/OpenSIN-AI/OpenSIN-backend/blob/main/app/routes/billing.py)

## Scope note

This is a **curated V1 reference**, not a generated OpenAPI dump.

That matches the docs launch gate: public API guidance is required for V1, while full OpenAPI generation is explicitly a later improvement.

## Health, readiness, and metrics

The backend documents the following service-level contracts:

| Endpoint | Purpose |
|---|---|
| `GET /health` | overall service health |
| `GET /ready` | readiness for automation / deployment checks |
| `GET /version` | build or release version surface |
| `GET /metrics` | Prometheus-style or machine-readable metrics surface |

The current `health.py` route also exposes a room snapshot under `GET /rooms` for the coordinator's dependent services.

## Auth surface

Documented legacy auth routes:

| Endpoint | Purpose |
|---|---|
| `POST /api/v1/auth/login` | authenticate and start a session |
| `POST /api/v1/auth/logout` | invalidate the session |

At the moment, the checked-in `auth.py` route returns a maintenance response for `login`:

```json
{
  "message": "Auth system in maintenance"
}
```

That is important for docs users: the route exists, but the implementation is still in-flight and tied to the broader `chat.opensin.ai` launch work.

## Billing and Stripe surface

Current route module:

- `app/routes/billing.py`

Documented endpoints:

| Endpoint | Purpose |
|---|---|
| `GET /api/billing/plans` | list plan definitions |
| `POST /api/billing/subscribe` | request a subscription flow |
| `POST /api/billing/webhook` | receive Stripe webhook events |
| `GET /api/billing/usage` | inspect usage counters and limits |

The current billing route exposes three baseline plans in code:

- `free`
- `pro`
- `enterprise`

Launch-gate note:

The **real commercial catalog** for V1 is still tracked separately in [OpenSIN-backend#1173](https://github.com/OpenSIN-AI/OpenSIN-backend/issues/1173), because the marketplace needs Stripe product ids that align with the current `team.json` schema.

## Room-13 coordinator contracts

`API.md` also documents the coordinator-style task and worker surfaces.

### Task contracts

| Endpoint | Purpose |
|---|---|
| `POST /api/tasks` | create a task |
| `GET /api/tasks` | list tasks |
| `GET /api/tasks/{task_id}` | inspect one task |
| `POST /api/tasks/claim-next` | claim next available task |
| `PUT /api/tasks/{task_id}/assign` | assign a task |
| `PUT /api/tasks/{task_id}/start` | mark execution start |
| `PUT /api/tasks/{task_id}/complete` | mark execution complete |
| `DELETE /api/tasks/{task_id}` | delete a task |

### Worker contracts

| Endpoint | Purpose |
|---|---|
| `POST /api/workers` | register a worker |
| `GET /api/workers` | list workers |
| `GET /api/workers/{worker_id}` | inspect one worker |
| `PUT /api/workers/{worker_id}` | update worker metadata |
| `POST /api/workers/{worker_id}/heartbeat` | send heartbeat |
| `POST /api/workers/{worker_id}/claim` | claim work |
| `POST /api/workers/{worker_id}/checkpoint` | persist progress |
| `POST /api/workers/{worker_id}/resume` | resume work |
| `POST /api/workers/{worker_id}/release` | release claimed work |
| `POST /api/workers/{worker_id}/task/complete` | complete assigned task |
| `DELETE /api/workers/{worker_id}` | delete a worker |

### Additional coordinator groups

`API.md` also calls out the following grouped surfaces:

- `/api/services`
- `/api/credentials`
- `/api/gateway`
- `/api/captcha`
- `/api/webhooks`
- `/api/workflows`
- `/api/n8n`
- `/api/steel`

## Response expectations

The current backend docs define a few behavioral rules that matter to integrators:

- `health` should represent degraded state honestly,
- `ready` should be safe for automation,
- `metrics` should stay machine-consumable,
- task and worker payloads should remain additive so older consumers do not break.

## What is intentionally not covered here yet

- generated OpenAPI,
- exhaustive schema dumps for every route,
- private dashboard-only BFF endpoints.

Those are useful, but not required to make `docs.opensin.ai` launch-ready for V1.

## Next steps

- [API Overview](/api/overview)
- [A2A Protocol API](/api/a2a)
- [Team Manifest Contract](/api/team)
