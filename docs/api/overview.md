---
title: API Overview
description: Technical architecture of the OpenSIN-AI API ecosystem.
---

<script setup>
const links = [
  { title: 'Agent Identity API', href: '/api/agent', description: 'Discovery, Agent Cards, versioning, and auth requirements.' },
  { title: 'A2A Protocol', href: '/api/a2a', description: 'JSON-RPC transport, methods, and security headers.' },
  { title: 'Team API', href: '/api/team', description: 'Team creation, execution, and orchestration flow.' },
  { title: 'A2A Protocol Hub', href: '/api/a2a-protocol', description: 'Shortest path into the protocol reference.' },
]
</script>

# API Overview

The OpenSIN-AI ecosystem exposes two primary API layers: the **Local SDK Layer** for internal agent logic and the **Remote A2A Layer** for cross-agent communication via the Neural-Bus.

## Core Protocols

| Protocol | Purpose | Implementation |
|----------|---------|----------------|
| **MCP** | Local tool discovery and execution | [Model Context Protocol](https://modelcontextprotocol.io) |
| **A2A** | Decentralized agent-to-agent communication | JSON-RPC 2.0 over HTTPS/NATS |
| **Neural-Bus** | Real-time event mesh and state sync | NATS JetStream |

## API Surfaces

### 1. Agent Identity API
Used for discovery and capability advertising. Every agent must expose a `.well-known/agent-card.json`.

- **Primary Entry:** `GET /.well-known/agent-card.json`
- **Purpose:** Public contract metadata (skills, tools, auth schemes).

### 2. A2A Communication API
The primary interface for agents to exchange tasks and observations.

- **Standard:** JSON-RPC 2.0
- **Base Route:** `/a2a/v1`
- **Key Methods:** `tools/call`, `agent/spawn`, `observation/push`

### 3. Team Orchestration API
Managed by `Team-SIN-*` agents to coordinate multi-agent workflows.

- **Purpose:** Parallel task distribution and result aggregation.
- **Backbone:** SIN-Hermes Router.

## Quick Entry

<div class="api-link-grid">
  <a v-for="link in links" :key="link.href" class="api-link-card" :href="link.href">
    <strong>{{ link.title }}</strong>
    <span>{{ link.description }}</span>
  </a>
</div>

## Authentication

OpenSIN uses a tiered authentication model managed by the [Passwordmanager](/guide/passwordmanager):

1. **Bearer Token (JWT):** Standard for public A2A endpoints.
2. **Mutual TLS (mTLS):** Required for Neural-Bus core infrastructure.
3. **Skill-Based Scopes:** Granular permissions per tool execution.

## Rate Limiting & Safety

All API calls are subject to the **Permission Manager** gate. Destructive actions or high-cost model calls are paused for human approval unless pre-authorized.

## Related

- [Agent Identity API](/api/agent)
- [A2A Protocol](/api/a2a)
- [Team API](/api/team)

---

## Next Steps

- [A2A Protocol Specification](/api/a2a)
- [Agent Identity API](/api/agent)
- [Neural-Bus Overview](/architecture/global-brain-neural-bus)
