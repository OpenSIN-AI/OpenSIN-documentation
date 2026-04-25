---
title: A2A Protocol
description: Canonical entry point for the OpenSIN A2A protocol reference.
---

<script setup>
const links = [
  { title: 'API Overview', href: '/api/overview', description: 'Architecture, auth and surfaces.' },
  { title: 'Agent Identity API', href: '/api/agent', description: 'Agent Cards and discovery.' },
  { title: 'A2A Protocol Specification', href: '/api/a2a', description: 'JSON-RPC transport and methods.' },
  { title: 'Team API', href: '/api/team', description: 'Team orchestration and execution.' },
]
</script>

# A2A Protocol

This page is the direct protocol reference entry point.

## Quick Entry

<div class="api-link-grid">
  <a v-for="link in links" :key="link.href" class="api-link-card" :href="link.href">
    <strong>{{ link.title }}</strong>
    <span>{{ link.description }}</span>
  </a>
</div>

## Primary routes

- [Overview](/api/overview)
- [Agent Identity API](/api/agent)
- [A2A Protocol Specification](/api/a2a)
- [Team API](/api/team)

## Quick note

Use this page when you want the shortest path into the protocol docs.
