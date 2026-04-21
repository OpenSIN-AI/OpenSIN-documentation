# OpenSIN-AI Overview

OpenSIN-AI is an ecosystem for autonomous agents, fleet orchestration, and
multi-surface product delivery. This page is a public overview for users and
contributors. It is not the organizational SSOT.

> [!IMPORTANT]
> Canonical ownership, repo mapping, and consolidation state live in
> [`OpenSIN-overview`](https://github.com/OpenSIN-AI/OpenSIN-overview).
> This page summarizes the current model for docs users.

## The Product Model

OpenSIN currently operates across three product-facing layers:

| Surface | Domain | Canonical Repo | Purpose |
|--------|--------|----------------|---------|
| Marketing | `opensin.ai` | `website-opensin.ai` | Open-source landing site and product story |
| Marketplace | `my.opensin.ai` | `website-my.opensin.ai` | Paid-layer marketing, plans, bundles, conversion |
| Dashboard | `chat.opensin.ai` | `OpenSIN-WebApp` | Authenticated fleet control and user application |

The public documentation at `docs.opensin.ai` belongs to
`OpenSIN-documentation` and explains how to use and build with the system.

## Core Repositories

These are the canonical core repos users and contributors should know first:

| Repo | Role |
|------|------|
| [`OpenSIN`](https://github.com/OpenSIN-AI/OpenSIN) | Python kernel and flagship core platform |
| [`OpenSIN-Code`](https://github.com/OpenSIN-AI/OpenSIN-Code) | Autonomous TypeScript coding CLI |
| [`OpenSIN-backend`](https://github.com/OpenSIN-AI/OpenSIN-backend) | A2A fleet control plane |
| [`OpenSIN-WebApp`](https://github.com/OpenSIN-AI/OpenSIN-WebApp) | Authenticated dashboard at `chat.opensin.ai` |
| [`OpenSIN-documentation`](https://github.com/OpenSIN-AI/OpenSIN-documentation) | Public docs website |
| [`OpenSIN-overview`](https://github.com/OpenSIN-AI/OpenSIN-overview) | Organizational SSOT and repo map |

## Supporting Repo Families

OpenSIN uses a clear naming model for supporting repos:

| Prefix | Meaning | Examples |
|--------|---------|----------|
| `Team-SIN-*` | Team monorepos for specialist workers | `Team-SIN-Code-Core` |
| `Infra-SIN-*` | Infrastructure, setup, and config SSOT | `Infra-SIN-Dev-Setup`, `Infra-SIN-OpenCode-Stack` |
| `Biz-SIN-*` | Marketing and business content | `Biz-SIN-Marketing`, `Biz-SIN-Blog-Posts` |
| `Template-SIN-*` | Blueprints and scaffolds | `Template-SIN-Agent` |

## Current Canonical Web Surfaces

| Domain | Surface Type | Notes |
|--------|--------------|-------|
| `opensin.ai` | Public marketing | Open-source landing surface |
| `my.opensin.ai` | Marketplace | Paid layer and conversion surface |
| `chat.opensin.ai` | Authenticated app | Dashboard, fleet interaction, control |
| `docs.opensin.ai` | Documentation | Public end-user docs |
| `blog.opensin.ai` | Blog | Public content and announcements |

## Important Consolidation Rules

- `opensin-ai-code` is no longer a canonical standalone repo. Its absorbed
  reference material lives in `OpenSIN/opensin_agent_platform/`.
- `opensin-ai-cli` and `opensin-ai-platform` are rationalization-pending repos.
  Do not position them as the primary recommended path for new work.
- New OpenCode config links must use the canonical in-org paths:
  `OpenSIN-AI/Infra-SIN-OpenCode-Stack` and
  `OpenSIN-AI/Infra-SIN-Global-Brain`.

## Where To Go Next

- Want to use OpenSIN: [Getting Started](/guide/getting-started)
- Want to understand surfaces: [Domain Registry](/governance/domain-registry)
- Want to build with the engine: [SDK Overview](/sdk/overview)
- Want the org-wide source of truth:
  [`OpenSIN-overview`](https://github.com/OpenSIN-AI/OpenSIN-overview)
