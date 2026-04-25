# Troubleshooting

Common issues and their solutions.

## Agent Not Responding

1. Check agent status: `Check the OpenSIN-Code CLI output and logs`
2. Verify API connectivity
3. Check logs: `Review logs in the terminal output`

## High Error Rate

1. Review error patterns
2. Check rate limits (For Google accounts and OpenAI pools, see [Dual Auth Rotators](/examples/dual-auth-rotators))
3. Verify input format

## High Latency

1. Reduce context window
2. Use streaming responses
3. Implement caching

## Next Steps

- [Monitoring](/guide/monitoring)
- [Getting Started](/guide/getting-started)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
---
title: Troubleshooting
description: Diagnose common OpenSIN issues
---

<script setup>
const links = [
  { title: 'Getting Started', href: '/guide/getting-started', description: 'Check prerequisites and setup.' },
  { title: 'Installation', href: '/guide/installation', description: 'Verify Bun and dependency setup.' },
  { title: 'Quick Start', href: '/guide/quick-start', description: 'Fast path to a working agent loop.' },
  { title: 'API Overview', href: '/api/overview', description: 'Cross-check the reference surfaces.' },
]
</script>

# Troubleshooting

## Quick Entry

<div class="api-link-grid">
  <a v-for="link in links" :key="link.href" class="api-link-card" :href="link.href">
    <strong>{{ link.title }}</strong>
    <span>{{ link.description }}</span>
  </a>
</div>

## Common checks

- Confirm Bun is installed.
- Confirm the repo built successfully.
- Confirm the route you are opening exists.
