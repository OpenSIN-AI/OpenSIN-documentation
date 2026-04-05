---
title: Installation
description: Install OpenSIN-Code on your system
---

# Installation

## Prerequisites

- Node.js 18 or higher
- npm or pnpm (Node package manager)
- Git (for version control)
- opencode CLI (for LLM provider configuration)

## Install from Source

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code
npm install
npm run build
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
npm run build

# Run tests
npm test

# Start the CLI
npm start
```

## Next Steps

- [Quick Start](/guide/quick-start) — Build your first agent
- [Getting Started](/guide/getting-started) — Overview of OpenSIN
