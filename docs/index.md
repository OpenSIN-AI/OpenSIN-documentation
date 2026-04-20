---
layout: home
hero:
  name: "OpenSIN-AI Documentation"
  text: "Canonical docs and verified surface registry for the OpenSIN-AI ecosystem."
  tagline: Guides, architecture, API refs, governance, and AI-ready discovery in one place.
  image:
    src: /logo.svg
    alt: OpenSIN Logo
  actions:
    - theme: brand
      text: Get Started
      link: /guide/getting-started
    - theme: alt
      text: View Registry
      link: /governance/domain-registry
    - theme: alt
      text: View on GitHub
      link: https://github.com/OpenSIN-AI/OpenSIN-documentation
features:
  - title: Canonical Docs
    details: Guides, architecture, API references, tutorials, and best practices in one place.
    link: /guide/getting-started
  - icon:
      src: /logo.svg
    title: A2A Protocol
    details: Agent-to-agent communication that lets specialized workers collaborate without a central bottleneck.
    link: /guide/a2a-protocol
  - title: Surface Registry
    details: Public, gated, and internal/unverified surfaces are tracked with evidence, not guesswork.
    link: /governance/domain-registry
  - title: Security by Design
    details: Auth-broker patterns, approval lanes, and no secrets in code. Critical actions stay reviewable.
    link: /best-practices/security
  - title: AI Discoverability
    details: Root llms.txt files keep humans and agents on the same canonical path.
    link: https://github.com/OpenSIN-AI/OpenSIN-documentation/blob/main/llms.txt
  - title: Open Source
    details: Fully forkable, self-hostable, and extensible. No vendor lock-in, no hidden costs.
    link: https://github.com/OpenSIN-AI/OpenSIN-documentation
---

## Quick Start

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN-documentation.git
cd OpenSIN-documentation
bun install
bun run docs:dev
```

> [!TIP]
> If you only want to read, start with the [surface registry](/governance/domain-registry). If you want to contribute, keep claims evidence-based and update the registry first.

## 🚨 Absolute Mandates (BEFORE you start)

Every agent and developer in the OpenSIN-AI fleet MUST follow these mandates. No exceptions.

| Mandate | Priority | Rule |
|---------|----------|------|
| **A2A-First + Self-Supabase** | -200.0 | SELBST MACHEN via A2A-Agenten — Supabase self-hosted auf OCI VM |
| **Vision-Gate** | -7.0 | KEINE Web-Aktion ohne Screenshot + Vision-Modell-Check |
| **Kommentar-Pflicht** | -6.0 | EXTREM umfangreiche Kommentare in ALLEN Code-Dateien |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne echten Beweis |
| **Immediate Bug Registry** | -4.0 | JEDER Bug SOFORT als GitHub Issue |
| **Technologie-Souveränität** | -2.0 | nodriver + Chrome Profil — Playwright/etc. PERMANENT verboten |
| **LLM via opencode CLI** | -2.5 | `opencode run --format json` — KEINE direkten API-Calls |
| **Bun-Only** | -1.5 | `bun install` / `bun run` — npm/bun PERMANENT verboten |
| **DevTools-First** | -1.0 | JEDER CSS-Selektor via DevTools verifizieren |
| **Antigravity-Only** | -10.0 | KEIN gemini-api Provider — nur `google/antigravity-*` |

→ [Full Mandate Documentation](/best-practices/code-quality)

## Why OpenSIN?

| Feature | OpenSIN | Hermes-Agent | OpenClaw | ChatGPT | Claude |
|---------|---------|-------------|----------|---------|--------|
| Multi-Agent System | ✅ Native | ⚠️ Dispatcher | ⚠️ Limited | ❌ Single | ❌ Single |
| A2A Communication | ✅ Built-in | ⚠️ Basic | ❌ None | ❌ None | ❌ None |
| Self-Hostable | ✅ Yes | ✅ Yes | ✅ Yes | ❌ Cloud | ❌ Cloud |
| Open Source | ✅ Apache 2.0 | ✅ Partial | ✅ Partial | ❌ Proprietary | ❌ Proprietary |
| Model-Agnostic | ✅ 1000+ | ⚠️ Limited | ✅ Multiple | ❌ GPT only | ❌ Claude only |
| Web Automation | ✅ Stealth | ❌ None | ✅ Basic | ❌ None | ❌ None |
| Omni-Channel | ✅ 6+ | ⚠️ Telegram | ⚠️ Telegram | ❌ Web only | ❌ Web only |
| Enterprise Security | ✅ Full | ⚠️ Basic | ❌ None | ✅ Basic | ✅ Basic |
| Cost | ✅ Free | ✅ Free | ✅ Free | 💰 $20/mo | 💰 $20/mo |

## Ecosystem

- **opensin.ai** — [Marketing Site](https://opensin.ai)
- **my.opensin.ai** — [Premium Marketplace](https://my.opensin.ai)
- **docs.opensin.ai** — You are here
- **Domain Registry** — [Verified public / gated / internal map](/governance/domain-registry)
- **GitHub** — [OpenSIN-AI Organization](https://github.com/OpenSIN-AI)
- **Discord** — [Community](https://discord.gg/opensin)
