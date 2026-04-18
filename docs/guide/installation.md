---
title: Installation
description: Install OpenSIN-Code on your system
---

# Installation

## Prerequisites

- Node.js 18 or higher
- Bun (package manager) — `brew install oven-sh/bun/bun`
- Git (for version control)
- opencode CLI (for LLM provider configuration)

## Install from Source

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code
bun install
bun run build
```

## Configure Environment

Create a `.env` file in your project directory:

```bash
# LLM Provider API Keys (configured via opencode CLI)
# Run: opencode auth login
# OpenSIN-Code uses opencode for all LLM calls automatically

# OpenSIN Configuration
OPENSIN_LOG_LEVEL=INFO
```

## Verify Installation

```bash
# Check the build
bun run build

# Run tests
bun test

# Start the CLI
bun start
```

## Next Steps

- [Quick Start](/guide/quick-start) — Build your first agent
- [Getting Started](/guide/getting-started) — Overview of OpenSIN

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` — npm/bun sind verboten |
| **Antigravity-Only** | -10.0 | KEIN gemini-api Provider — nur `google/antigravity-*` |
| **Kommentar-Pflicht** | -6.0 | EXTREM umfangreiche Kommentare in ALLEN Code-Dateien |

→ [Alle Mandate](/best-practices/code-quality)
