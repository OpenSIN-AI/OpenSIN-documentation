---
title: "Vercel Deployment"
---

# Vercel Deployment

This page documents the Vercel-hosted OpenSIN surfaces that are part of the
current public product model. It is intentionally scoped to public-safe,
verified information only.

> [!IMPORTANT]
> Source of truth for repo ownership and deployed surfaces is
> [`OpenSIN-overview/docs/CANONICAL-REPOS.md`](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md).
> If this page and that file disagree, `OpenSIN-overview` wins.

## Verified Surface Mapping

| Domain | Canonical Repo | Role | Platform |
|--------|----------------|------|----------|
| `chat.opensin.ai` | [`OpenSIN-WebApp`](https://github.com/OpenSIN-AI/OpenSIN-WebApp) | Authenticated dashboard, fleet control, chat | Vercel |
| `my.opensin.ai` | [`website-my.opensin.ai`](https://github.com/OpenSIN-AI/website-my.opensin.ai) | Paid-layer marketing and marketplace | Vercel |

> [!NOTE]
> `docs.opensin.ai` is not deployed on Vercel. The documentation site is hosted
> separately and documented in the
> [Domain Registry](/governance/domain-registry).

## What Belongs On Vercel

OpenSIN uses Vercel for web properties that need fast frontend delivery and, in
the case of `chat.opensin.ai`, authenticated application routing.

### `chat.opensin.ai`

- Repo: [`OpenSIN-WebApp`](https://github.com/OpenSIN-AI/OpenSIN-WebApp)
- Package name: `opensin-chat`
- Stack: Next.js 16 + Supabase
- Purpose: logged-in user surface for dashboard, fleet control, billing-adjacent
  actions, and agent interaction

### `my.opensin.ai`

- Repo: [`website-my.opensin.ai`](https://github.com/OpenSIN-AI/website-my.opensin.ai)
- Stack: static marketing / marketplace surface
- Purpose: plans, bundles, conversion funnel, and premium-layer positioning

## What Does Not Belong Here

This page does not track:

- unrelated Vercel projects from other businesses or old personal orgs
- internal project IDs that are not required for public operation
- speculative domains or in-progress experiments without canonical ownership

If you need internal deployment runbooks, credentials, or project-level secret
handling, that information belongs in the private infrastructure repos, not in
public docs.

## Deployment Model

For the public-facing Vercel surfaces, the expected production flow is:

```text
git push -> Vercel build -> deployment preview -> production promotion
```

The exact CI/CD contract for the org is tracked in `OpenSIN-overview`, which
documents that self-hosted automation is the canonical CI layer and that public
surface repos consume those contracts instead of inventing their own.

## Environment Notes

Public docs should only reference environment variables that matter to the
surface contract. For example, `chat.opensin.ai` depends on backend/auth
endpoints exposed by the backend control plane, but this page intentionally does
not duplicate secret or internal-only deployment values.

## Related

- [Domain Registry](/governance/domain-registry)
- [OpenSIN-AI Overview](/guide/opensin-ai-overview)
- [Deployment Guide](/guide/deployment)
