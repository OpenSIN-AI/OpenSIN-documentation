# Domain Registry — OpenSIN-AI

> Evidence-based registry of public, gated, and internal/unverified surfaces.

> [!IMPORTANT]
> Public means publicly reachable without auth. Gated means the surface exists but login is required. Internal/unverified means the surface is referenced in docs or code but is not confirmed public in the current checks.

## Registry

| Surface | Status | Owner / repo | Evidence | Notes |
|:---|:---|:---|:---|:---|
| `opensin.ai` | Public | `website-opensin.ai` | Live public marketing site | Canonical landing page |
| `my.opensin.ai` | Public | `website-my.opensin.ai` | Live public marketplace | Subscription / commerce surface |
| `blog.opensin.ai` | Public | `opensin-blog.pages.dev` | Live public blog | Content and updates |
| `docs.opensin.ai` | Public | `OpenSIN-documentation` | Live public docs site | This repository |
| `chat.opensin.ai` | Gated | `OpenSIN-WebApp` | Login required | Dashboard / user workspace |
| `api.opensin.ai` | Internal / unverified | `OpenSIN-backend` | Not publicly resolvable from this environment | Do not advertise as public until verified |
| `opensin.ai/agents` | Internal / unverified | Unclear | Public route returns 404 | Treat as non-public |
| `hermes.opensin.ai` | Internal / unverified | Unclear | Not publicly resolvable from this environment | Reference only |
| `code-analyzer.opensin.ai` | Internal / unverified | Unclear | Not publicly resolvable from this environment | Reference only |

## Change policy

1. Verify with a live check or owning repo evidence.
2. Update this registry before updating README or marketing copy.
3. Update `llms.txt` / `llms-full.txt` whenever a surface status changes.
4. Downgrade to internal/unverified if evidence disappears.

## Related docs

- [OpenSIN-AI Overview](/guide/opensin-ai-overview)
- [Vercel Deployment](/guide/vercel-deployment)
- [A2A Protocol API](/api/a2a)
- [Governance Overview](/governance/overview)
