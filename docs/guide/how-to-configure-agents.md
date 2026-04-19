---
title: Agent Author Guide
description: How to scaffold and register a new A2A-SIN agent using the canonical OpenSIN workflow.
---

# Agent Author Guide

This guide is for maintainers who need to create or extend an `A2A-SIN-*` agent.

The most important rule is simple:

> **Start from the canonical template and the canonical repo map. Do not invent a parallel scaffold.**

## 1. Decide whether you need a new repo at all

Before you scaffold anything, read:

- [START-HERE](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/START-HERE.md)
- [Canonical Repos](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md)

Use this decision rule:

| Situation | Correct action |
|---|---|
| The capability belongs inside an existing team monorepo | Add a folder there |
| The capability is a new standalone A2A agent | Start from `Template-SIN-Agent` |
| The capability only changes a commercial bundle | Edit the owning `team.json`, not the agent repo |

## 2. Start from `Template-SIN-Agent`

Canonical template:

- [OpenSIN-AI/Template-SIN-Agent](https://github.com/OpenSIN-AI/Template-SIN-Agent)

Canonical creation workflow:

```text
/create-a2a-sin-agent
```

That workflow exists specifically so new agents do not drift away from the org standard.

## 3. Minimum files every new agent needs

At minimum, a new agent repo should expose these surfaces:

| File / surface | Why it exists |
|---|---|
| `agent.json` | machine-readable agent identity |
| `A2A-CARD.md` | human-readable capability summary |
| `AGENTS.md` | repo-local development rules |
| `mcp-config.json` | MCP exposure |
| `clients/opencode-mcp.json` | OpenCode client wiring |
| `clients/codex-config.toml` | editor / client integration |
| `.well-known/agent-card.json` | public agent discovery |
| `.well-known/agent.json` | public machine-readable metadata |
| `.well-known/oauth-client.json` | auth metadata if the agent exposes OAuth |

## 4. Register the agent in the right commercial layer

OpenSIN V1 treats `Team-SIN-*` repositories as **team manifests**, not as the runtime home of the agent code.

That means:

- runtime logic lives in the `A2A-SIN-*` repo,
- bundle composition lives in the team manifest,
- the marketplace renders from aggregated manifest data.

### Source of truth

- Schema: [team.schema.json](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/schemas/team.schema.json)
- Templates: [OpenSIN-overview/templates/teams](https://github.com/OpenSIN-AI/OpenSIN-overview/tree/main/templates/teams)

**Do not edit downstream `team.json` mirrors by hand if the overview repo is the canonical source.**

## 5. Validation checklist before you call the agent ready

Use the smallest honest checklist that proves the agent is real:

- build succeeds,
- the agent card renders,
- a health or help action responds,
- the `.well-known/` discovery endpoints exist,
- the bundle / team manifest references the correct agent id.

## 6. Where docs for the new agent belong

Different docs belong in different places:

| Content | Correct home |
|---|---|
| Runtime code and repo-local instructions | the agent repo |
| Public user documentation | `OpenSIN-documentation` |
| Org topology / canonical ownership | `OpenSIN-overview` |
| Marketplace composition and pricing | `team.json` + marketplace docs |

## 7. Common mistakes to avoid

- Creating a new repo when an existing team repo or template already owns the concern.
- Editing commercial bundle metadata in the wrong place.
- Documenting an agent as live before its discovery or health surfaces are reachable.
- Writing docs that disagree with [Canonical Repos](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md).

## Next steps

- [Team manifest contract](/api/team)
- [OpenSIN-Code CLI reference](/guide/opensin-code)
- [April 2026 consolidation](/changelog/2026-04-consolidation)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **A2A-First** | -200.0 | New capabilities should route through the existing agent fleet first |
| **Annahmen-Verbot** | -5.0 | Do not claim an agent is ready until health and discovery are verified |
| **Test-Beweis-Pflicht** | 0.0 | Every new agent needs build and runtime proof |

→ [Alle Mandate](/best-practices/code-quality)
