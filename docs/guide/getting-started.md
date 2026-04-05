---
title: Getting Started
description: Learn how to get started with OpenSIN
---

# Getting Started

Welcome to OpenSIN — the world's most comprehensive AI agent system.

## What is OpenSIN?

OpenSIN is an open-source platform for building, deploying, and managing AI agents. It supports multi-agent teams, agent-to-agent communication, and integration with various messaging platforms.

## Key Features

- **QueryEngine** — Async generator with ReAct loop
- **Hook System** — 20+ events, 5 execution modes
- **Tool System** — 8+ built-in tools
- **Permission System** — 6 modes with safety checks
- **Subagent System** — Fork pattern with cache-identical prefixes
- **MCP Client** — 5 transports
- **Sandbox** — Full isolation
- **Memory System** — File-based with SIN.md

## Prerequisites

- Python 3.11+
- pip (Python package manager)
- An API key from an LLM provider (OpenAI, Anthropic, etc.)

## Installation

```bash
pip install opensin-cli
```

## Quick Start

```bash
# Create your first agent
opensin agent create researcher --model gpt-4

# Test your agent
opensin agent test researcher --prompt "What is AI?"
```

## Next Steps

- [Installation Guide](/guide/installation) — Detailed installation instructions
- [Quick Start](/guide/quick-start) — Build your first agent in 5 minutes
- [Agent Basics](/guide/agent-basics) — Learn agent fundamentals
