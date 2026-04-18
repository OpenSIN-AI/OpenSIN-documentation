---
layout: home
hero:
  name: "OpenSIN-AI Documentation"
  text: "Official docs for the OpenSIN-AI organization."
  tagline: The first Agent-to-Agent network — 100+ autonomous AI agents in 18 specialized teams. Build, deploy, and scale with the OpenSIN design system and A2A protocol.
  image:
    src: /logo.svg
    alt: OpenSIN Logo
  actions:
    - theme: brand
      text: Get Started
      link: /guide/getting-started
    - theme: alt
      text: View on GitHub
      link: https://github.com/OpenSIN-AI/OpenSIN
features:
  - icon:
      src: /logo.svg
    title: A2A Protocol
    details: Agent-to-Agent communication standard enabling 100+ autonomous agents to collaborate, delegate, and deliver results without human intervention.
    link: /guide/a2a-protocol
  - title: 18 Specialized Teams
    details: From Software Engineering to Bug Bounty, Google Apps to DevOps — each team is purpose-built for specific domains with deep expertise.
    link: /guide/team-orchestration
  - title: Model-Agnostic
    details: Works with 1000+ models from OpenAI, Anthropic, Google, Mistral, Groq, Ollama and more. Bring your own API keys or use free tier.
    link: /guide/mcp-integration
  - title: Security by Design
    details: Auth-Broker, Secret-Authority, Approval-Lanes. No secrets in code. Every critical action can be reviewed before execution.
    link: /best-practices/security
  - title: Omni-Channel
    details: WhatsApp, Telegram, Discord, iMessage, Apple Notes — your agents are everywhere you are, responding in your name.
    link: /bridges/chrome-extension
  - title: Open Source
    details: Fully forkable, self-hostable, and extensible. Apache 2.0 licensed. No vendor lock-in, no hidden costs.
    link: https://github.com/OpenSIN-AI/OpenSIN
---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code

# Install (Bun only — npm/bun forbidden)
bun install
bun run build

# Start
bun start
```

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
- **GitHub** — [OpenSIN-AI Organization](https://github.com/OpenSIN-AI)
- **Discord** — [Community](https://discord.gg/opensin)
