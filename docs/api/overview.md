---
title: API Overview
description: Overview of the current V1 API surfaces in the OpenSIN product stack.
---

# API Overview

OpenSIN V1 has **three different API layers** that matter to users and integrators:

1. the **OpenSIN backend control plane**,
2. the **A2A agent protocol**,
3. the **team manifest contract** that powers the marketplace.

This page maps those layers before you dive into endpoint detail.

## 1. Backend control plane

Canonical runtime owner:

- [OpenSIN-AI/OpenSIN-backend](https://github.com/OpenSIN-AI/OpenSIN-backend)

What it owns:

- health and readiness endpoints,
- auth flows used by `chat.opensin.ai`,
- billing and Stripe webhook handling,
- task / worker orchestration surfaces,
- service registry and runtime coordination.

Start here:

- [Backend V1 API](/api/backend-v1)

## 2. A2A protocol

This is the inter-agent layer used when OpenSIN agents talk to each other.

Use this when you need:

- agent cards,
- A2A message envelopes,
- agent-to-agent routing semantics.

Start here:

- [A2A Protocol API](/api/a2a)

## 3. Marketplace / team manifest contract

OpenSIN V1 does **not** model Team-SIN bundles as arbitrary prose pages.
It models them as structured manifests.

That contract lives in:

- `schemas/team.schema.json` in `OpenSIN-overview`
- per-team `team.json` manifests
- aggregated `oh-my-sin.json` data for the marketplace UI

Start here:

- [Team Manifest Contract](/api/team)

## Current V1 status

| Surface | Status | Notes |
|---|---|---|
| Backend reference | documented baseline | current docs are curated from `OpenSIN-backend/API.md` and route files |
| A2A reference | present | protocol-level docs exist, but final launch examples can still expand |
| Team manifest contract | now canonical | backed by the Wave 4 schema and template manifests |
| Auto-generated OpenAPI | not launch-blocking | explicitly out of scope for docs V1 |

## Recommended reading order

1. This overview
2. [Backend V1 API](/api/backend-v1)
3. [A2A Protocol API](/api/a2a)
4. [Team Manifest Contract](/api/team)

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Annahmen-Verbot** | -5.0 | API docs must point back to real repos, route files, or tracked issues |
| **Test-Beweis-Pflicht** | 0.0 | Do not mark launch docs complete without a successful docs build |

→ [Alle Mandate](/best-practices/code-quality)
