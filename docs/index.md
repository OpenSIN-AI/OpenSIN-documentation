---
layout: home
hero:
  name: "OpenSIN Docs"
  text: "The World's Most Comprehensive AI Agent System"
  tagline: Build, deploy, and manage AI agents at scale with multi-agent collaboration
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
  - icon: 🧠
    title: QueryEngine
    details: Async generator with ReAct loop, token budget tracking, and automatic context compaction
  - icon: 🔗
    title: Hook System
    details: 20+ events with 5 execution modes — shell, HTTP, function, agent, and prompt hooks
  - icon: 🛠️
    title: Tool System
    details: 8+ built-in tools with deferred loading and permission-aware filtering
  - icon: 🔒
    title: Permission System
    details: 6 modes with auto-mode classifier and bypass-immune safety checks
  - icon: 🤝
    title: Subagent System
    details: Fork pattern with cache-identical prefixes for maximum cache hits
  - icon: 🌐
    title: MCP Client
    details: 5 transports — stdio, SSE, HTTP, WebSocket, and in-process
  - icon: 🏖️
    title: Sandbox
    details: Filesystem and network rules with git escape prevention
  - icon: 🧠
    title: Memory System
    details: File-based memory with SIN.md auto-discovery and session extraction
---

## Quick Start

```bash
# Install the CLI
pip install opensin-cli

# Create your first agent
opensin agent create researcher --model gpt-4

# Test your agent
opensin agent test researcher --prompt "What is AI?"
```

## Why OpenSIN?

| Feature | OpenSIN | Others |
|---------|---------|--------|
| Multi-Agent Teams | ✅ Native | ❌ Manual |
| A2A Protocol | ✅ Built-in | ❌ None |
| Platform Integrations | ✅ 27+ | ❌ None |
| Production Ready | ✅ Yes | ⚠️ Partial |
| Open Source | ✅ Apache 2.0 | ❌ Proprietary |
| Provider Agnostic | ✅ 100+ | ❌ Locked |

## Links

- **GitHub:** https://github.com/OpenSIN-AI/OpenSIN
- **Discord:** https://discord.gg/opensin
- **API Reference:** /api/overview
