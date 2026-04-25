---
title: MCP Integration
description: Connect OpenSIN agents to external tools
---

<script setup>
const links = [
  { title: 'Agent Basics', href: '/guide/agent-basics', description: 'Fundamentals of agents and tools.' },
  { title: 'Team Orchestration', href: '/guide/team-orchestration', description: 'How multiple agents collaborate.' },
  { title: 'Getting Started', href: '/guide/getting-started', description: 'Setup and first steps.' },
  { title: 'OpenSIN Code', href: '/guide/opensin-code', description: 'The autonomous coding surface.' },
]
</script>

# MCP Integration

The Model Context Protocol (MCP) enables OpenSIN agents to connect to external tools and data sources.

## Quick Entry

<div class="api-link-grid">
  <a v-for="link in links" :key="link.href" class="api-link-card" :href="link.href">
    <strong>{{ link.title }}</strong>
    <span>{{ link.description }}</span>
  </a>
</div>

## Overview

MCP provides a standardized way for agents to:
- Discover available tools
- Execute tool calls
- Receive tool results
- Manage tool permissions

## Supported Transports

| Transport | Description |
|-----------|-------------|
| stdio | Local process communication |
| SSE | Server-sent events |
| HTTP | REST API communication |
| WebSocket | Real-time bidirectional |
| in-process | Direct function calls (fastest) |

## Next Steps

- [A2A Protocol](/guide/a2a-protocol)
- [Agent Basics](/guide/agent-basics)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **LLM via opencode CLI** | -2.5 | `opencode run --format json` — KEINE direkten API-Calls |
| **A2A-Agenten-Pflicht** | -200.0 | SELBST MACHEN via `create-a2a-sin-agent` |
| **Kommentar-Pflicht** | -6.0 | EXTREM umfangreiche Kommentare |

→ [Alle Mandate](/best-practices/a2a-communication)
