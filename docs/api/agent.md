---
title: Agent Identity API
description: Specification for OpenSIN Agent Cards and .well-known discovery.
---

<script setup>
const links = [
  { title: 'API Overview', href: '/api/overview', description: 'Architecture and API surface map.' },
  { title: 'A2A Protocol', href: '/api/a2a', description: 'Transport and JSON-RPC methods.' },
  { title: 'Team API', href: '/api/team', description: 'Team orchestration entry points.' },
]
</script>

# Agent Identity API

The Agent Identity API defines how an agent advertises its capabilities, versioning, and security requirements to the fleet.

## Discovery Mechanism

Every OpenSIN-compatible agent **MUST** expose its identity via the standard `.well-known` path:

```text
GET https://<agent-domain>/.well-known/agent-card.json
```

## Agent Card Schema

The `agent-card.json` is the source of truth for the agent's contract.

```json
{
  "name": "Research-Agent",
  "version": "2.4.1",
  "description": "Deep-web research and data extraction specialist.",
  "url": "https://research.opensin.ai",
  "capabilities": {
    "streaming": true,
    "stateful": false,
    "a2a_native": true
  },
  "skills": [
    {
      "id": "search",
      "name": "Web Search",
      "description": "Access real-time information via Google Search"
    }
  ],
  "authentication": {
    "schemes": ["bearer", "mtls"],
    "registry_url": "https://auth.opensin.ai"
  }
}
```

## Fields Definition

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Canonical ID of the agent |
| `version` | string | Yes | SemVer versioning |
| `description` | string | Yes | Human-readable purpose |
| `capabilities` | object | Yes | Technical flags (streaming, stateful) |
| `skills` | array | Yes | List of skill-objects the agent can perform |
| `authentication` | object | Yes | Supported auth methods and endpoints |

## Versioning Policy

OpenSIN agents follow strict **SemVer**:
- **Major:** Breaking changes in JSON-RPC methods or parameters.
- **Minor:** New tools added or non-breaking capability changes.
- **Patch:** Internal fixes and prompt optimizations.

---

## Best Practices

1. **Keep it Static:** The agent-card should be a static file or a fast-cached endpoint.
2. **Detailed Skill Descriptions:** Use clear descriptions for skills; other agents use these to decide when to delegate.
3. **Valid JSON-Schema:** Ensure all tool parameters are documented with valid JSON-Schema for automated validation.

## Quick Entry

<div class="api-link-grid">
  <a v-for="link in links" :key="link.href" class="api-link-card" :href="link.href">
    <strong>{{ link.title }}</strong>
    <span>{{ link.description }}</span>
  </a>
</div>

## Next Steps

- [A2A Protocol Specification](/api/a2a)
- [SDK Tool System](/sdk/tool-system)
- [Domain Registry](/governance/domain-registry)
