---
title: "Building Custom Agents"
---

# Building Custom Agents

Build custom OpenSIN agents from the current canonical stack, not from legacy
or duplicate repos.

## Before You Start

Read these first:

- [`OpenSIN-overview/docs/CANONICAL-REPOS.md`](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md)
- [How to Configure New Agents](/guide/how-to-configure-agents)
- [A2A Protocol](/guide/a2a-protocol)

## Prerequisites

- Node.js 20+
- Bun
- GitHub account
- OpenCode CLI available

## Fastest Path

If you need a new standalone agent repo, start from the canonical template:

```bash
gh repo create OpenSIN-AI/my-new-agent \
  --template OpenSIN-AI/Template-SIN-Agent \
  --public

cd my-new-agent
bun install
```

> [!IMPORTANT]
> Many new agent ideas should not become standalone repos. First verify whether
> the work belongs inside an existing `Team-SIN-*` monorepo.

## Required Files

Every production-grade agent should expose a clean public contract:

- `agent.json`
- `.well-known/agent-card.json`
- `AGENTS.md`
- governance files required by the template

## Validation Checklist

Before publishing an agent:

- `bun run build` succeeds
- the agent card is valid and reachable
- the repo ownership is canonical
- docs link to the correct surface
- no internal-only endpoints are exposed in public docs

## Related

- [Template-SIN-Agent](https://github.com/OpenSIN-AI/Template-SIN-Agent)
- [Agent Configuration](/guide/agent-configuration)
- [A2A Protocol](/guide/a2a-protocol)
