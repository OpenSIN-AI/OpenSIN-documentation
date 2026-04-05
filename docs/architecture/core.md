---
title: Core Architecture
description: OpenSIN core architecture overview
---

# Core Architecture

OpenSIN is built on a modular, extensible architecture.

## Components

### QueryEngine

The heart of OpenSIN — manages the complete conversation lifecycle with async generators, ReAct loops, and token budget tracking.

### Hook System

Event-driven automation with 20+ events and 5 execution modes (shell, HTTP, function, agent, prompt).

### Tool System

Rich tool interface with 8+ built-in tools, deferred loading, and permission-aware filtering.

### Permission System

Multi-source permission rules with 6 modes and auto-mode classifier.

### Subagent System

Fork pattern with cache-identical prefixes for maximum cache hits.

### MCP Client

Multi-transport support (stdio, SSE, HTTP, WS, in-process).

### Sandbox

Filesystem and network rules with git escape prevention.

### Memory System

File-based memory with SIN.md auto-discovery and session extraction.

## Next Steps

- [A2A Protocol](/architecture/a2a)
- [Security](/architecture/security)
