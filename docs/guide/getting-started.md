---
title: Getting Started
description: Learn how to get started with OpenSIN
---

# Getting Started

Welcome to OpenSIN — the world's most comprehensive AI agent system.

## What is OpenSIN?

OpenSIN is an open-source platform for building, deploying, and managing AI agents. It supports multi-agent teams, agent-to-agent communication, and integration with various messaging platforms.

## Key Features

- **OpenSIN-Code CLI** — Autonomous coding agent for the terminal
- **Hook System** — 20+ events, 5 execution modes
- **Tool System** — 6+ built-in CLI tools (Bash, Read, Write, Edit, Grep, Glob)
- **Agent Memory** — Letta-style persistent memory system
- **Background Agents** — Async task delegation
- **MCP Client** — 5 transports
- **Sandbox** — Full isolation
- **Memory System** — File-based with SIN.md

## Prerequisites

- Node.js 18+
- Bun — `brew install oven-sh/bun/bun`
- An API key from an LLM provider (configured via opencode CLI)

## Installation

```bash
# Clone the repository
git clone https://github.com/OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code

# Install dependencies
bun install

# Build the project
bun run build
```

## Quick Start

```bash
# Start the OpenSIN-Code CLI
bun start

# Or run directly
cd packages/opensin-sdk
bun run cli
```

## Next Steps

- [Installation Guide](/guide/installation) — Detailed installation instructions
- [Quick Start](/guide/quick-start) — Build your first agent in 5 minutes
- [Agent Basics](/guide/agent-basics) — Learn agent fundamentals
