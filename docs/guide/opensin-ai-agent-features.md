# OpenSIN-AI Capabilities

OpenSIN-AI is a fleet-first agent system built for autonomous work, not a
single chatbot. This page summarizes the current user-visible capabilities and
where they live in the product surface.

> [!IMPORTANT]
> Canonical ownership and repo mapping live in
> [`OpenSIN-overview/docs/CANONICAL-REPOS.md`](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md).
> This page explains the current product experience, not org governance.

## What OpenSIN Users Can Do

| Capability | What it gives you | Where it lives |
|------------|-------------------|----------------|
| **Autonomous fleet control** | Run a team of specialized agents instead of a single prompt loop | `chat.opensin.ai` |
| **Public documentation** | Learn the current system without reading raw source code | `docs.opensin.ai` |
| **Marketing surface** | Understand the product and the value proposition | `opensin.ai` |
| **Marketplace / paid layer** | Browse plans, bundles, and premium access paths | `my.opensin.ai` |
| **Agent orchestration** | Dispatch work across teams and worker agents | `OpenSIN-backend` |
| **A2A communication** | Let agents coordinate directly instead of bottlenecking through one process | OpenSIN core stack |

## Current Strengths

### 1. Fleet-First Design
OpenSIN is built around teams and workers, not one monolithic assistant.
That means work can be specialized, parallelized, and audited.

### 2. Multiple Surfaces for Different Audiences

- users start at the docs and marketing surfaces
- authenticated operators use `chat.opensin.ai`
- contributors use the documentation and canonical repo map
- maintainers use the org SSOT and infrastructure repos

### 3. Strong Canonical Ownership
The platform is now structured around a small number of canonical repos.
This reduces drift and makes it easier to know where a change belongs.

## Surface Map

| Domain | Purpose | Audience |
|--------|---------|----------|
| `opensin.ai` | Marketing / product story | New users, developers |
| `my.opensin.ai` | Marketplace / paid layer | Buyers, subscribers |
| `chat.opensin.ai` | Authenticated dashboard | Operators, power users |
| `docs.opensin.ai` | Canonical docs | Everyone |
| `blog.opensin.ai` | Updates and launches | Community |

## Roadmap Direction

OpenSIN is moving toward:

- clearer user journeys across surfaces
- less duplicate repo ownership
- more consistent docs and navigation
- better separation between public docs and private infra notes
- stronger canonical links to the owning repo of each feature

## Related

- [OpenSIN-AI Overview](/guide/opensin-ai-overview)
- [Domain Registry](/governance/domain-registry)
- [A2A Protocol](/guide/a2a-protocol)
- [OpenSIN-Code](/guide/opensin-code)
