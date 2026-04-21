# Domain Registry — OpenSIN-AI

> Evidence-based registry of public, gated, and internal/unverified surfaces.

> [!IMPORTANT]
> Public means publicly reachable without auth. Gated means the surface exists but login is required. Internal/unverified means the surface is referenced in docs or code but is not confirmed public in the current checks.

## Registry

| Surface | Status | Owner / repo | Evidence | Notes |
|:---|:---|:---|:---|:---|
| `docs.opensin.ai` | Public | `OpenSIN-documentation` | Live public docs site | This repository |
| `chat.opensin.ai` | Gated | `OpenSIN-WebApp` | HTTP 200 (Dashboard) | Official user interface |
| `opensin.ai` | Public | `website-opensin.ai` | Live marketing surface | Product landing |

## Internal Assets (Unverified)
*The following are currently internal or in-transition:*
- `api.opensin.ai` (Neural-Bus Hub)
- `registry.opensin.ai` (Skill Discovery)

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
