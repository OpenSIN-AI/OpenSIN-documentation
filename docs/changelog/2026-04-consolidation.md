---
title: April 2026 Consolidation
description: Public summary of the April 2026 OpenSIN organization consolidation.
---

# April 2026 Consolidation

This page is the public-facing summary of the April 2026 consolidation work across the OpenSIN-AI organization.

The full organizational source of truth stays in `OpenSIN-overview`. This page exists so contributors landing on `docs.opensin.ai` get one stable URL that explains the new map quickly.

## Start here first

If you are new to the org, read this sequence in `OpenSIN-overview`:

1. [START-HERE](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/START-HERE.md)
2. [PRODUCT-VISION.md](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/PRODUCT-VISION.md)
3. [STATE-OF-THE-UNION.md](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/STATE-OF-THE-UNION.md)
4. [CANONICAL-REPOS.md](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md)
5. [FOLLOWUPS.md](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/FOLLOWUPS.md)

## What changed

The April consolidation reduced organizational ambiguity in four ways:

1. the product model was fixed into **OSS / Pro / Marketplace**,
2. the web surface was split cleanly into **opensin.ai / my.opensin.ai / chat.opensin.ai / docs.opensin.ai**,
3. canonical repo ownership was documented so contributors know where code belongs,
4. dead or duplicate repos were archived, redirected, or marked for rationalization.

## Canonical map at a glance

These are the product-defining repos contributors should orient around first:

| Repo | Owns |
|---|---|
| [`OpenSIN`](https://github.com/OpenSIN-AI/OpenSIN) | Python kernel and flagship product repo |
| [`OpenSIN-Code`](https://github.com/OpenSIN-AI/OpenSIN-Code) | TypeScript autonomous CLI |
| [`OpenSIN-backend`](https://github.com/OpenSIN-AI/OpenSIN-backend) | fleet control plane |
| [`OpenSIN-WebApp`](https://github.com/OpenSIN-AI/OpenSIN-WebApp) | authenticated app at `chat.opensin.ai` |
| [`website-opensin.ai`](https://github.com/OpenSIN-AI/website-opensin.ai) | OSS marketing site |
| [`website-my.opensin.ai`](https://github.com/OpenSIN-AI/website-my.opensin.ai) | paid marketing + marketplace |
| [`OpenSIN-documentation`](https://github.com/OpenSIN-AI/OpenSIN-documentation) | public docs at `docs.opensin.ai` |

For the authoritative and complete version of that table, use:

- [Canonical Repos](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md)

## Archived repos from the consolidation

The following repos were explicitly moved out of the active path and replaced by canonical homes:

| Archived repo | Canonical replacement |
|---|---|
| `A2A-SIN-Coding-CEO` | `Team-SIN-Code-Core/agents/coding-ceo/` |
| `A2A-SIN-Code-AI` | `Team-SIN-Code-Core/agents/code-ai/` |
| `opensin-ai-code` | `OpenSIN/opensin_agent_platform/` |
| `OpenSIN-onboarding` | `Infra-SIN-Dev-Setup/user-onboarding/` |

There was also follow-on hygiene work for dead and duplicate repos after the initial consolidation wave.

## What is still intentionally open

Consolidation did **not** mean everything was finished. The remaining org-level work is tracked centrally in:

- [FOLLOWUPS.md](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/FOLLOWUPS.md)

Important open themes include:

- CLI rationalization (`opensin-ai-cli` vs `OpenSIN-Code`),
- backend absorption of `Core-SIN-Control-Plane`,
- manifest aggregation and registry generation,
- launch-gate execution across the V1-critical repos.

## Why this matters to docs contributors

If you update `docs.opensin.ai` without following the consolidated map, you will almost certainly document the wrong repo, the wrong product surface, or a repo that should no longer receive changes.

That is why this page exists.

## Related launch work

- [OpenSIN-documentation#134](https://github.com/OpenSIN-AI/OpenSIN-documentation/issues/134)
- [CEO Directive #40](https://github.com/OpenSIN-AI/OpenSIN-overview/issues/40)
