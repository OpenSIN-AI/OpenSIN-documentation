---
title: Quick Start
description: Build your first OpenSIN agent flow
---

<script setup>
const links = [
  { title: 'Getting Started', href: '/guide/getting-started', description: 'Overview and prerequisites.' },
  { title: 'Agent Basics', href: '/guide/agent-basics', description: 'Agent fundamentals and config.' },
  { title: 'OpenSIN Code', href: '/guide/opensin-code', description: 'Autonomous coding surface.' },
  { title: 'API Overview', href: '/api/overview', description: 'Reference the underlying API surfaces.' },
]
</script>

# Quick Start

## Quick Entry

<div class="api-link-grid">
  <a v-for="link in links" :key="link.href" class="api-link-card" :href="link.href">
    <strong>{{ link.title }}</strong>
    <span>{{ link.description }}</span>
  </a>
</div>

## Minimal path

1. Install Bun.
2. Clone the repo.
3. Run `bun install`.
4. Start building an agent loop.
