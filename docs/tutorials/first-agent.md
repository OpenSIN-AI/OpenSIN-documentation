# Tutorial: Create Your First Agent

This tutorial shows the **current canonical OpenSIN path** for creating a new `A2A-SIN-*` agent.

## Before you scaffold anything

Read these first:

1. [Agent Author Guide](/guide/how-to-configure-agents)
2. [Team Manifest Contract](/api/team)
3. [Canonical Repos](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md)

You need to know whether you are:

- creating a new standalone agent repo,
- adding a capability to an existing team repo,
- or only changing bundle metadata.

## Step 1: Start from the canonical template

Use the canonical creation workflow:

```text
/create-a2a-sin-agent
```

Reference template:

- [OpenSIN-AI/Template-SIN-Agent](https://github.com/OpenSIN-AI/Template-SIN-Agent)

## Step 2: Fill the minimum agent surfaces

Your new agent should expose at least:

- `agent.json`
- `A2A-CARD.md`
- `AGENTS.md`
- `mcp-config.json`
- `.well-known/agent-card.json`
- `.well-known/agent.json`

## Step 3: Register it in the right commercial layer

If the agent belongs to an existing `Team-SIN-*` bundle, update the canonical manifest source in `OpenSIN-overview/templates/teams/` instead of inventing a second registry.

## Step 4: Validate that it is real

Do not call the agent ready until you have proof that:

- it builds,
- its discovery files exist,
- its help or health action responds,
- the correct bundle references the right `A2A-SIN-*` id.

## Next steps

- [Agent Author Guide](/guide/how-to-configure-agents)
- [OpenSIN-Code CLI Reference](/guide/opensin-code)
- [API Reference](/api/index)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **A2A-First** | -200.0 | Reuse the existing fleet and templates before inventing new scaffolds |
| **Annahmen-Verbot** | -5.0 | No "ready" claim without build and runtime proof |
| **Test-Beweis-Pflicht** | 0.0 | Every new agent needs validation evidence |

→ [Alle Mandate](/best-practices/code-quality)
