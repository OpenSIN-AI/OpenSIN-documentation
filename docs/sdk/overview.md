---
title: "SDK Overview"
---

# OpenSIN SDK

The `@opensin/sdk` (TypeScript) and `opensin-ouroboros` (Python) packages provide the core building blocks for the OpenSIN-AI ecosystem.

## Vision

The SDK is designed to be **Engine-Agnostic**. It provides a high-level orchestration layer that can swap between the **TypeScript Runtime** (Standard) and the **Rust Engine** (High-Performance) seamlessly.

## Key Packages

| Package | Language | Role |
|---------|----------|------|
| `@opensin/sdk` | TypeScript | Primary orchestration and plugin layer |
| `@opensin/agent-sdk` | TypeScript | Specialized tools for building A2A agents |
| `opensin-ouroboros` | Python | Data processing and Python-based worker logic |

## Installation

```bash
# Node.js / Bun
bun add @opensin/sdk

# Python
pip install opensin-ouroboros
```

## Core Modules

### ⚡ [Agent Loop](/sdk/agent-loop)
The heart of every agent. Handles the ReAct cycle, token counting, and tool execution.

### 🛠️ [Tool System](/sdk/tool-system)
A unified interface for local (MCP) and remote (A2A) tools.

### 🧠 [Memory & Context](/sdk/memory)
Advanced context pruning and persistent memory storage.

## The 2026 Sovereign Standard

Every SDK interaction follows the **A2A-First Mandate**:
- Never hardcode API keys; use the [Passwordmanager](/guide/passwordmanager) hooks.
- Never use direct LLM calls; use the `opencode run` abstraction.
- Always provide **Evidence-First** logs for debugging.

---

## Next Steps

- [Agent Loop Deep-Dive](/sdk/agent-loop)
- [Building Custom Tools](/sdk/tool-system)
- [Lifecycle Hooks](/sdk/hooks)
