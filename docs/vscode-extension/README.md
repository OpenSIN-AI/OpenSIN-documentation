# OpenSIN VS Code Extension — Developer Documentation

> **Agentic AI Coding Assistant for OpenSIN** — Powered by Kilo Code & Claude Code concepts

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![License](https://img.shields.io/badge/license-Proprietary-green)
![VS Code](https://img.shields.io/badge/VS%20Code-%3E%3D1.85.0-blue)

---

## Overview

The OpenSIN VS Code Extension (published as **SIN Code**) transforms Visual Studio Code into an **agentic AI coding workspace**. It bridges the `opencode` CLI with a rich sidebar chat, inline completions, code actions, a swarm coordinator for multi-agent dispatch, a gamified buddy system, automatic memory consolidation, and a built-in Agent Marketplace.

Built in **3 phases**, SIN Code covers the full spectrum from basic AI chat to autonomous multi-agent orchestration.

## Quick Links

| Resource | URL |
|----------|-----|
| **Marketplace** | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=opensin.opensin-vscode) |
| **GitHub Repo** | [OpenSIN-AI/OpenSIN-Code](https://github.com/OpenSIN-AI/OpenSIN-Code) (directory: `kairos-vscode/`) |
| **Issues** | [GitHub Issues](https://github.com/OpenSIN-AI/OpenSIN-Code/issues) |

## Documentation Structure

| Document | Description |
|----------|-------------|
| [Architecture Overview](./architecture/overview.md) | System architecture, data flow diagrams, extension points |
| [Setup & Installation](./setup/installation.md) | Installation from .vsix, development mode, requirements |
| [Feature Documentation](./features/index.md) | Phase 1-3 feature deep-dives |
| [API Reference](./api/index.md) | CLI Bridge, LSP Provider, internal APIs |
| [Contributing Guide](./contributing/guide.md) | How to contribute, coding standards, PR workflow |
| [Changelog](./changelog.md) | Release history and version notes |
| [Troubleshooting](./troubleshooting/guide.md) | Common issues, debugging, FAQ |

## Feature Summary

### Phase 1: Core AI Assistant
- **5 Agent Modes** — Architect, Code, Debug, Ask, Proactive
- **Sidebar Chat** — Streaming responses, mode badge, cancel button
- **Memory Consolidation** — AGENTS.md, SIN-MEMORY.md, CLAUDE.md auto-loading
- **LSP Integration** — Diagnostics, symbol extraction, cursor-aware context
- **Model Selector** — Auto-discovered from `~/.config/opencode/`

### Phase 2: Intelligence Layer
- **Swarm Coordinator** — Parallel dispatch to Explore, Librarian, Oracle, Artistry
- **BUDDY Gamification** — XP, levels, moods, commit detection
- **Auto Test Runner** — Runs tests on `.test.` / `.spec.` file saves
- **File Context Management** — Add files to conversation context

### Phase 3: Advanced Capabilities
- **Inline Completions** — Ghost-text code completions (`Cmd+Shift+I`)
- **AI Code Actions** — Fix Error, Refactor, Explain, Generate Tests
- **Agent Marketplace** — Browse, install, and manage specialized agents

## License

Copyright 2024-2026 SIN-Solver Team. All rights reserved.

This is a proprietary extension, part of the SIN Code CLI product line.
