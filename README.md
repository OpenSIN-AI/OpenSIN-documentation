<a name="readme-top"></a>

<p align="center">
  <img src="https://docs.opensin.ai/logo.svg" alt="OpenSIN-AI Logo" width="120" />
</p>

<h1 align="center">OpenSIN-AI Documentation</h1>

<p align="center">
  <i>The canonical knowledge layer for the OpenSIN-AI ecosystem — docs.opensin.ai</i>
</p>

<p align="center">
  <a href="https://github.com/OpenSIN-AI/OpenSIN-documentation/actions/workflows/deploy.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/OpenSIN-AI/OpenSIN-documentation/deploy.yml?label=deploy&logo=github&style=flat-square" alt="Deploy Status" />
  </a>
  <a href="https://docs.opensin.ai">
    <img src="https://img.shields.io/badge/docs-live-008060?style=flat-square&logo=gitbook&logoColor=white" alt="Docs Live" />
  </a>
  <a href="https://github.com/OpenSIN-AI/OpenSIN-documentation/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="License" />
  </a>
  <a href="https://bun.sh">
    <img src="https://img.shields.io/badge/runtime-bun-black?style=flat-square&logo=bun" alt="Bun" />
  </a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> ·
  <a href="#structure">Structure</a> ·
  <a href="#governance">Governance</a> ·
  <a href="#contributing">Contributing</a>
</p>

---

> [!IMPORTANT]
> This repository is the **Single Source of Truth (SSOT)** for all OpenSIN-AI documentation, API references, and architecture blueprints. It is managed by the OpenSIN-AI Governance Board.
>
> The visual design language shown on `docs.opensin.ai` is now the canonical OpenSIN web design baseline for all other surfaces.
> Keep `developers.opensin.ai` and `member.opensin.ai` aligned to this look, but preserve their separate runtimes and repos.

## 🚀 Quick Start

This project uses **VitePress** and **Bun**.

```bash
# Install dependencies (BUN ONLY)
bun install

# Run development server
bun run dev

# Build for production
bun ./scripts/build-docs.mjs
```

> [!NOTE]
> Keep companion repos and local worktrees outside this repository root.
> Use sibling directories such as `~/dev/<repo>` so `OpenSIN-documentation/` stays clean during sync, checkout, and review.

## 📂 Structure

```text
OpenSIN-documentation/
├── docs/               # Documentation Content (VitePress)
│   ├── guide/          # Getting Started & User Guides
│   ├── api/            # API Reference
│   ├── architecture/   # Deep Dive into the Engine
│   ├── fleet/          # A2A Agent Fleet Registry
│   └── governance/     # Protocols, Rules & Ethics
├── scripts/            # Build & Maintenance tools
├── package.json        # Project metadata
└── AGENTS.md           # Mandatory Agent directives
```

## ⚖️ Governance

All documentation follows the **OpenSIN 2026 Standards**:
- **A2A-First:** Every agent interaction is documented via the A2A protocol.
- **Global Brain:** Syncs with `https://github.com/Delqhi/global-brain`.
- **Surface Plan:** Aligned with `OpenSIN-Web-Surface-Plan`.

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

1. Fork the repo.
2. Create a feature branch.
3. Commit changes (Agent-led commits preferred).
4. Open a Pull Request.

---

<p align="center">
  <a href="https://opensin.ai">
    <img src="https://img.shields.io/badge/🤖_Powered_by-OpenSIN--AI-7B3FE4?style=for-the-badge&logo=github&logoColor=white" alt="Powered by OpenSIN-AI" />
  </a>
</p>

<p align="center">
  <sub>Developed by the <a href="https://opensin.ai"><strong>OpenSIN-AI</strong></a> Ecosystem — Enterprise AI Agents working autonomously.</sub><br/>
  <sub>🌐 <a href="https://opensin.ai">opensin.ai</a> · 💬 <a href="https://opensin.ai/agents">Agents</a> · 🚀 <a href="https://opensin.ai/dashboard">Dashboard</a></sub>
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
