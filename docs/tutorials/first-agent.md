---
title: "Tutorial: Building Your First Sovereign Agent"
description: "Master the 2026 A2A implementation flow from template to fleet registration."
---

# Building Your First Sovereign Agent

This tutorial covers the implementation of a production-grade OpenSIN-AI agent. We move beyond "chatbots" into **Autonomous Agency**.

## Phase 1: Environment Sovereignty

Ensure your local machine is synchronized with the canonical OpenCode stack. OpenSIN does not tolerate environment drift.

```bash
# Initialize Global Brain Hooks (Mandatory)
node /path/to/Infra-SIN-Global-Brain/src/cli.js setup-hooks \
  --project my-first-agent \
  --project-root "$PWD" \
  --agents-directive
```

## Phase 2: Scaffold from Blueprint

Never start from an empty directory. Use the `Template-SIN-Agent` to inherit security policies, A2A protocols, and Bun-first configurations.

```bash
# Create from template
gh repo create OpenSIN-AI/A2A-SIN-MyAgent \
  --template OpenSIN-AI/Template-SIN-Agent \
  --public

# Enter and install (BUN ONLY)
cd A2A-SIN-MyAgent
bun install
```

## Phase 3: Define the Identity (The Card)

An agent without a verified identity is a ghost. You must define your agent's skills and security requirements in `.well-known/agent-card.json`.

```json
{
  "name": "SIN-Researcher-01",
  "version": "1.0.0",
  "skills": [
    {
      "id": "deep_research",
      "name": "Deep Web Research",
      "description": "Extract and synthesize information from public web sources."
    }
  ],
  "authentication": {
    "schemes": ["bearer"]
  }
}
```

## Phase 4: Implement Logic (The SDK)

Use the `@opensin/agent-sdk` to define your ReAct loop. Leverage the **Permission Manager** for every tool execution.

```typescript
import { AgentBuilder, ToolRegistry } from '@opensin/agent-sdk'

const tools = new ToolRegistry()

// Register your core skill
tools.register({
  name: 'extract_data',
  execute: async ({ url }) => {
    // Implementation logic
  }
})

const agent = AgentBuilder
  .create('sin-researcher-01')
  .withTools(tools)
  .withModel('claude-sonnet-4-6')
  .build()

export default agent
```

## Phase 5: Verification (Evidence-First)

Claiming success without logs is a failure. Run your agent and verify the **Neural-Bus** event stream.

```bash
# Run in debug mode
bun run dev --debug

# Verify Agent Card
curl http://localhost:3000/.well-known/agent-card.json
```

## Phase 6: Fleet Registration

Once verified, register your agent in the **Domain Registry** and announce it to the `SIN-Zeus` coordinator.

---

## The Sovereign Mandates

| Mandat | Requirement |
|--------|-------------|
| **A2A-First** | Always delegate sub-tasks via A2A protocol. |
| **Evidence-First** | No diagnosis without evidence-backed logs. |
| **Bun-Only** | Instant ban for `npm` or `pnpm` usage. |
| **Neural-Bus** | All state changes must be published to NATS. |

## Next Steps

- Master the [A2A Protocol Specification](/api/a2a)
- Explore [Fleet Orchestration](/guide/fleet-orchestration)
- Join the Developer Council on Discord.
