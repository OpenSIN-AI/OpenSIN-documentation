---
title: "Installation Guide"
description: "High-performance setup for the OpenSIN-AI ecosystem."
---

# Installation & Optimization

Setting up OpenSIN-AI requires a commitment to the **Billion-Dollar Standard**. We do not use "easy" installers. We build for performance and security.

## 1. Runtime Layer

OpenSIN-AI is optimized for **Bun**. We have permanently banned `npm` and `bunx` for production environments.

```bash
# Install Bun (The only authorized runtime)
curl -fsSL https://bun.sh/install | bash
```

## 2. Global Brain Sync

Every machine in the OpenSIN fleet must be coupled with the **Global Brain (PCPM)**.

```bash
# Sync Global Brain
git clone https://github.com/Delqhi/global-brain.git ~/dev/global-brain
cd ~/dev/global-brain && bun install
```

## 3. Neural-Bus Infrastructure

For local development of A2A agents, you need a local **NATS JetStream** instance.

```bash
# Launch Neural-Bus (Dockerized)
docker run -d --name neural-bus -p 4222:4222 nats:latest -js
```

## 4. OpenCode CLI

The primary interface for developers.

```bash
# Global install
bun add -g @opensin/opencode-cli
```

---

## ⚖️ Verification Mandate

After installation, run the **Enterprise Health Check**:

```bash
opencode run --action '{"action":"system.health"}'
```

If the response latency is >200ms, your environment is non-compliant. Optimize your network routing or consult the [Performance Guide](/best-practices/performance).

---

## Related

- [First Agent Tutorial](/tutorials/first-agent)
- [SDK Overview](/sdk/overview)
- [Agent Configuration](/guide/agent-configuration)
---
title: Installation
description: Install and verify OpenSIN locally
---

<script setup>
const links = [
  { title: 'Getting Started', href: '/guide/getting-started', description: 'Overview and prerequisites.' },
  { title: 'Quick Start', href: '/guide/quick-start', description: 'The fastest path to a working setup.' },
  { title: 'Troubleshooting', href: '/guide/troubleshooting', description: 'Common issues and fixes.' },
  { title: 'OpenSIN Code', href: '/guide/opensin-code', description: 'Autonomous coding surface.' },
]
</script>

# Installation

## Quick Entry

<div class="api-link-grid">
  <a v-for="link in links" :key="link.href" class="api-link-card" :href="link.href">
    <strong>{{ link.title }}</strong>
    <span>{{ link.description }}</span>
  </a>
</div>

## Install

```bash
bun install
```
