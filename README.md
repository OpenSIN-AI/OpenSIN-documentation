# OpenSIN Documentation

> **OpenSIN-AI** — The world's most comprehensive autonomous AI agent ecosystem.

---

## 🏢 Organization Overview

OpenSIN-AI is a GitHub organization building a fully autonomous, multi-agent AI platform. The architecture combines a CLI core, A2A (Agent-to-Agent) protocol, Chrome Bridge extension, and a fleet of specialized agents — all orchestrated through n8n workflows on dedicated infrastructure.

**GitHub:** https://github.com/OpenSIN-AI
**Website:** https://opensin.ai
**Dashboard:** https://a2a.delqhi.com
**Discord:** https://discord.gg/opensin

---

## 📦 Repository Landscape

### Core Repositories

| Repository | Purpose | URL |
|------------|---------|-----|
| **OpenSIN** | Free-tier CLI agent — ReAct loop, tools, hooks, MCP | [github.com/OpenSIN-AI/OpenSIN](https://github.com/OpenSIN-AI/OpenSIN) |
| **OpenSIN-Code** | SIN Code CLI — TypeScript-based opencode fork with plugins | [github.com/OpenSIN-AI/OpenSIN-Code](https://github.com/OpenSIN-AI/OpenSIN-Code) |
| **OpenSIN-backend** | Subscription backend — API services, Chrome extension, sinInChrome | [github.com/OpenSIN-AI/OpenSIN-backend](https://github.com/OpenSIN-AI/OpenSIN-backend) |

### Websites

| Repository | Purpose | URL |
|------------|---------|-----|
| **website-opensin.ai** | Public marketing site — features, pricing, docs | [github.com/OpenSIN-AI/website-opensin.ai](https://github.com/OpenSIN-AI/website-opensin.ai) |
| **website-my.opensin.ai** | User dashboard — account management, agent fleet overview | [github.com/OpenSIN-AI/website-my.opensin.ai](https://github.com/OpenSIN-AI/website-my.opensin.ai) |

### Infrastructure & Templates

| Repository | Purpose | URL |
|------------|---------|-----|
| **OpenSIN-documentation** | VitePress documentation site — this repo | [github.com/OpenSIN-AI/OpenSIN-documentation](https://github.com/OpenSIN-AI/OpenSIN-documentation) |
| **Template-A2A-SIN-Agent** | Agent template — scaffold for new A2A agents | [github.com/OpenSIN-AI/Template-A2A-SIN-Agent](https://github.com/OpenSIN-AI/Template-A2A-SIN-Agent) |
| **dev-setup** | Quick-start development environment setup | [github.com/OpenSIN-AI/dev-setup](https://github.com/OpenSIN-AI/dev-setup) |

### Marketing

| Repository | Purpose | URL |
|------------|---------|-----|
| **OpenSIN-Marketing-Release-Strategie** | Release planning, blog posts, marketing materials | [github.com/OpenSIN-AI/OpenSIN-Marketing-Release-Strategie](https://github.com/OpenSIN-AI/OpenSIN-Marketing-Release-Strategie) |
| **OpenSIN-Blog-Posts** | Published blog content | [github.com/OpenSIN-AI/OpenSIN-Blog-Posts](https://github.com/OpenSIN-AI/OpenSIN-Blog-Posts) |

---

## 🧠 Architecture at a Glance

```
┌─────────────────────────────────────────────────────────┐
│                    OpenSIN Ecosystem                     │
├──────────────┬──────────────┬───────────────────────────┤
│   CLI Core   │   A2A Fleet  │    Infrastructure         │
│              │              │                           │
│ OpenSIN      │ 20+ A2A      │ n8n (OCI VM)              │
│ (Free)       │ Agents       │ Supabase (OCI VM 200GB)   │
│              │              │                           │
│ OpenSIN-Code │ SIN-Zeus     │ HF Spaces (free VMs)      │
│ (Pro)        │ (Orchestrator)│ Cloudflare Pages         │
│              │              │                           │
│              │ SIN-Hermes   │ Chrome Extension          │
│              │ (Dispatcher) │ (39 MCP Tools)            │
│              │              │                           │
│              │ SIN-Solver   │ OpenSIN Bridge            │
│              │ (Web App)    │ (WebSocket MCP Server)    │
└──────────────┴──────────────┴───────────────────────────┘
```

### Key Components

1. **CLI Core** — Two implementations: Python-based `OpenSIN` (free) and TypeScript-based `OpenSIN-Code` (pro/subscription). Both feature ReAct loops, tool systems, MCP clients, hook systems, and subagent delegation.

2. **A2A Protocol** — Agent-to-Agent communication standard. Each agent has its own MCP server, Telegram bot, and can delegate tasks to other agents.

3. **OpenSIN Bridge** — Chrome extension with 39 MCP tools. Provides video recording, stealth mode, cookie management, webRequest logging, and WebSocket-based MCP server on HuggingFace.

4. **n8n Orchestration** — Workflow engine on OCI VM (`92.5.60.87`) handling inbound work items, PR watching, token rotation, and fleet coordination.

5. **Supabase Database** — Central PostgreSQL database on OCI VM (200GB) serving as the persistent data layer for all agents.

---

## 🚀 Quick Start

### Install OpenSIN CLI (Free)

```bash
pip install opensin-cli
opensin agent create researcher --model gpt-4
opensin agent test researcher --prompt "What is AI?"
```

### Install SIN Code CLI (Pro)

```bash
# Clone the repository
git clone https://github.com/OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code
npm install
npm run build
```

### Run OpenSIN Bridge (Chrome Extension)

1. Clone OpenSIN-backend: `git clone https://github.com/OpenSIN-AI/OpenSIN-backend.git`
2. Load `services/sin-chrome-extension` as unpacked extension in Chrome
3. Connect to HF MCP Server at https://huggingface.co/spaces/OpenJerro/opensin-bridge-mcp

### Deploy Documentation

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN-documentation.git
cd OpenSIN-documentation
npm install
npm run docs:dev
```

---

## 📚 Documentation Index

| Topic | Link |
|-------|------|
| Getting Started | [Guide](/guide/getting-started) |
| Installation | [Guide](/guide/installation) |
| Quick Start | [Guide](/guide/quick-start) |
| Agent Basics | [Guide](/guide/agent-basics) |
| MCP Integration | [Guide](/guide/mcp-integration) |
| A2A Protocol | [Guide](/guide/a2a-protocol) |
| Team Orchestration | [Guide](/guide/team-orchestration) |
| Deployment | [Guide](/guide/deployment) |
| Monitoring | [Guide](/guide/monitoring) |
| Scaling | [Guide](/guide/scaling) |
| Troubleshooting | [Guide](/guide/troubleshooting) |
| Changelog | [Guide](/guide/changelog) |
| OpenSIN Bridge | [Docs](/bridges/chrome-extension) |
| API Reference | [API](/api/) |
| Architecture | [Architecture](/architecture/) |

---

## 🌉 OpenSIN Bridge — Chrome Extension

**The most significant development in the entire OpenSIN-AI organization.**

OpenSIN Bridge is a Chrome Extension with **39 MCP Tools** that outperforms Antigravity in every category:

- **39 Tools** (vs Antigravity's ~15)
- **Video Recording** (chrome.tabCapture)
- **Stealth Mode** (Anti-Detection)
- **Cookie CRUD** (Full Chrome Cookie API)
- **webRequest Logging** (500 entries)
- **HF MCP Server** (always online via WebSocket)
- **Open Source, free, no vendor lock-in**

### Links
- 🔗 [Extension Repo](https://github.com/OpenSIN-AI/OpenSIN-backend/tree/main/services/sin-chrome-extension)
- 🌐 [HF MCP Server](https://huggingface.co/spaces/OpenJerro/opensin-bridge-mcp)
- 📖 [Tool Reference](./docs/bridges/chrome-extension.md)
- 📝 [Blog Post](https://github.com/OpenSIN-AI/OpenSIN-Marketing-Release-Strategie/blob/main/blog-posts/20-opensin-bridge-chrome-extension.md)

---

## 🔗 External Services

| Service | Purpose |
|---------|---------|
| **OCI VM** (`92.5.60.87`) | n8n workflow engine, Supabase database |
| **HuggingFace Spaces** | Free VM hosting for A2A agents and MCP servers |
| **Cloudflare Pages** | Documentation and website hosting |
| **Supabase** | Central PostgreSQL database (200GB on OCI) |
| **Telegram** | Agent communication and operator chat |
