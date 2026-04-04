# OpenSIN Documentation

Welcome to the OpenSIN documentation — the world's most comprehensive AI agent system.

## Quick Start

| What you want to do | Where to start |
|---------------------|----------------|
| **New to OpenSIN?** | [Getting Started](/guide/getting-started) |
| **Install OpenSIN** | [Installation Guide](/guide/installation) |
| **Build your first agent** | [Quick Start](/guide/quick-start) |
| **Understand the architecture** | [Architecture Overview](/architecture/overview) |
| **Integrate with messaging apps** | [Integrations](/integrations/telegram) |

## Key Features

- **QueryEngine** — Async generator with ReAct loop, token budget tracking
- **Hook System** — 20+ events, 5 execution modes (shell, HTTP, function, agent, prompt)
- **Tool System** — 8+ built-in tools with deferred loading
- **Permission System** — 6 modes with auto-mode classifier
- **Subagent System** — Fork pattern with cache-identical prefixes
- **MCP Client** — 5 transports (stdio, SSE, HTTP, WS, in-process)
- **Sandbox** — Filesystem/network rules, git escape prevention
- **Memory System** — File-based with SIN.md auto-discovery

## Get Started

```bash
pip install opensin-cli
opensin agent create researcher --model gpt-4
opensin agent test researcher --prompt "What is AI?"
```

## Links

- **GitHub:** https://github.com/OpenSIN-AI/OpenSIN
- **Discord:** https://discord.gg/opensin
