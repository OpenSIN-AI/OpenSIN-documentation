---
title: Team API
description: API reference for OpenSIN teams
---

<script setup>
const links = [
  { title: 'API Overview', href: '/api/overview', description: 'Architecture and shared API layers.' },
  { title: 'Agent Identity API', href: '/api/agent', description: 'Discovery and identity contract.' },
  { title: 'A2A Protocol', href: '/api/a2a', description: 'Transport and JSON-RPC methods.' },
  { title: 'A2A Hub', href: '/api/a2a-protocol', description: 'Shortest path into the protocol docs.' },
]
</script>

# Team API

Create and manage OpenSIN teams.

## Quick Entry

<div class="api-link-grid">
  <a v-for="link in links" :key="link.href" class="api-link-card" :href="link.href">
    <strong>{{ link.title }}</strong>
    <span>{{ link.description }}</span>
  </a>
</div>

## Endpoints

### Create Team

```http
POST /v1/teams
```

**Request:**
```json
{
  "name": "research-team",
  "agents": ["agent_123", "agent_456"],
  "strategy": "sequential",
  "max_iterations": 10
}
```

### List Teams

```http
GET /v1/teams
```

### Execute Team Task

```http
POST /v1/teams/{team_id}/execute
```

**Request:**
```json
{
  "task": "Research AI trends and write a report",
  "context": {"focus": "enterprise applications"}
}
```

## Next Steps

- [Agent API](/api/agent)
- [A2A Protocol](/api/a2a)

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
