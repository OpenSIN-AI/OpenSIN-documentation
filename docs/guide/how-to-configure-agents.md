# How to Configure New Agents

This page describes the current OpenSIN path for introducing new agents without
creating duplicate repos or drifting away from canonical ownership.

> [!IMPORTANT]
> Before creating any new agent surface, read
> [`OpenSIN-overview/docs/CANONICAL-REPOS.md`](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md).
> Many new agent ideas belong inside an existing `Team-SIN-*` monorepo instead
> of a brand-new repository.

## Step 1: Decide Where the Agent Belongs

Use this rule first:

- if the agent belongs to an existing team, add it to that `Team-SIN-*` repo
- if it requires a new standalone agent repo, start from `Template-SIN-Agent`
- if you are unsure, open a repo proposal in `OpenSIN-overview` before coding

## Step 2: Use the Canonical Template

OpenSIN standardizes new standalone agents from:

- [`Template-SIN-Agent`](https://github.com/OpenSIN-AI/Template-SIN-Agent)

This template is the canonical blueprint for new A2A-capable agents.

## Step 3: Register the Agent in Canonical Config

Agent registration and model routing belong in the canonical OpenCode stack:

- `OpenSIN-AI/Infra-SIN-OpenCode-Stack`
- local `~/.config/opencode/*` files when working on a machine-specific setup

Update only the canonical config locations. Do not invent parallel config repos.

## Step 4: Define the Agent Contract

Every production-grade agent needs at minimum:

- `agent.json`
- `.well-known/agent-card.json`
- `AGENTS.md`
- governance metadata required by the template

## Step 5: Verify Ownership and Exposure

Before claiming the agent is ready:

- confirm the owning repo is canonical
- confirm the docs point to the right repo and surface
- confirm any public endpoint is verified before publishing it in docs

## Step 6: Publish Safely

Public docs must not expose internal IPs, internal dashboards, or unverified
production endpoints. If an endpoint is not publicly verified, document it as
internal/unverified instead of presenting it as final truth.

## Related

- [Agent Configuration](/guide/agent-configuration)
- [Building Custom Agents](/tutorials/custom-agents)
- [A2A Protocol](/guide/a2a-protocol)
