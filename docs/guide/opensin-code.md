# OpenSIN Code

OpenSIN-Code ist das autonome CLI- und SDK-System der OpenSIN-AI Organisation. Es ist der Kern des agentic AI Coding Assistant Ökosystems.

> **Repository:** [OpenSIN-AI/OpenSIN-Code](https://github.com/OpenSIN-AI/OpenSIN-Code)
>
> **Umfang:** 2.394 Dateien | 637.024 Zeilen Code | TypeScript + Rust

---

## Architektur

OpenSIN-Code ist als Monorepo mit Turborepo organisiert:

```
packages/
├── opensin-cli/          # CLI Entry Point, Commander.js, REPL
├── opensin-server/       # Express HTTP Server
├── opensin-sdk/          # Core SDK (Agent Loop, Tools, MCP, Memory)
│   ├── src/core/         # 1.902 Dateien migrierter Core-Code
│   ├── src/utils/plugins/ # Plugin-Architektur (44 Dateien)
│   └── src/bare_mode/    # Bare Mode (4 Dateien)
│   └── src/buddy/        # Buddy Companion (4 Dateien)
│   └── src/copy_command/ # Copy Command (4 Dateien)
│   └── src/plugin_state/ # Plugin State Management (5 Dateien)
│   └── src/prompt_interrupt/ # Prompt Interrupt (4 Dateien)
│   └── src/skill_commands/ # Skill Commands (6 Dateien)
│   └── src/subtask_tree/ # Subtask Tree (5 Dateien)
│   └── src/supercomplete/ # Supercomplete (5 Dateien)
│   └── src/terminal_notifications/ # Terminal Notifications (4 Dateien)
├── opensin-engine/       # Rust Engine (71 Dateien, 37.7K Zeilen)
│   ├── crates/api/       # API Layer (Provider Client, Types, SSE)
│   ├── crates/runtime/   # Runtime (Conversation, Config, Compact)
│   ├── crates/tools/     # 19 Built-in Tools
│   ├── crates/sin-cli/   # Rust CLI (REPL, Render, Input)
│   ├── crates/plugins/   # Rust Plugin System
│   ├── crates/commands/  # 27+ Slash Commands
│   ├── crates/lsp/       # LSP Integration
│   └── crates/server/    # Axum HTTP Server
├── cli-tools/            # 6 Core CLI Tools (Bash, Read, Edit, Write, Glob, Grep)
├── plugin-sdk/           # Plugin SDK
└── plugin-runtime/       # Plugin Loader & Registry

plugins/                  # 14 migrierte Plugins
├── sin-code-review/      # Code Review (6 Dateien)
├── sin-commit-commands/  # Git Workflow (10 Dateien)
├── sin-feature-dev/      # Feature Dev (12 Dateien)
├── sin-frontend-design/  # Frontend Design (6 Dateien)
├── sin-security-guidance/ # Security (6 Dateien)
├── sin-hookify/          # Hook Engine (48 Dateien)
├── sin-explanatory-mode/ # Erklär-Modus (8 Dateien)
├── sin-learning-mode/    # Lern-Modus (8 Dateien)
├── sin-model-migration/  # Modell-Migration (10 Dateien)
├── sin-agent-sdk-dev/    # Agent SDK (10 Dateien)
├── sin-plugin-dev/       # Plugin Dev Toolkit (116 Dateien)
├── sin-pr-review/        # PR Review (18 Dateien)
├── sin-loop/             # Self-Referential Loops (16 Dateien)
└── sin-ralph/            # Ralph Loop (7 Dateien)

opensin-code-vscode/      # VS Code Extension (18 Dateien)
.github/workflows/        # 12 GitHub Actions Workflows
scripts/                  # 8 Automation Scripts
examples/                 # Beispiel-Konfigurationen
```

---

## Core Engine

### TypeScript SDK (`packages/opensin-sdk/`)

Das TypeScript SDK bildet das Herzstück von OpenSIN-Code:

- **Query Loop** — API Streaming, Tool Execution, Auto-Compact
- **Tool System** — 40+ Tools (Bash, Read, Edit, Write, Glob, Grep, WebFetch, etc.)
- **Command Registry** — 70+ Slash Commands
- **Plugin System** — Installation, Validation, Marketplace
- **MCP Client** — Multi-Server MCP Integration
- **Memory System** — Session Memory, Auto-Memory, Team Memory
- **Permissions** — Permission Modes (Default, Accept Edits, Dangerously)
- **Auth** — OAuth, API Keys, Bedrock, Vertex
- **Config** — Global/Project Settings, `.sin/` Directory

### Rust Engine (`packages/opensin-engine/`)

Die Rust Engine bietet ein performantes Backend:

- **API Layer** — Provider Client Abstraction, SSE Parser, Model Registry
- **Runtime** — Core Agent Loop, Config Loading, Session Compaction
- **Tools** — 19 Built-in Tools in Rust
- **CLI** — REPL, Terminal Renderer, Vim-mode Line Editor
- **Commands** — 27+ Slash Commands
- **Plugins** — Full Plugin System mit Hook Execution
- **LSP** — Language Server Protocol Integration
- **Server** — Axum HTTP API mit SSE Streaming

---

## Plugin-System

OpenSIN-Code kommt mit 14 vorinstallierten Plugins. Siehe [Plugin-Dokumentation](/docs/plugins/opensin-code-plugins) für Details.

### Eigene Plugins entwickeln

```bash
# Plugin erstellen
/plugin-dev:create-plugin

# Oder manuell
mkdir -p plugins/sin-mein-plugin/.sin-plugin
mkdir -p plugins/sin-mein-plugin/commands
mkdir -p plugins/sin-mein-plugin/agents
mkdir -p plugins/sin-mein-plugin/skills
mkdir -p plugins/sin-mein-plugin/hooks
```

Siehe [Plugin Development Tutorial](/docs/tutorials/plugin-development) für eine Schritt-für-Schritt-Anleitung.

---

## VS Code Extension

Die `opensin-code-vscode` Extension integriert OpenSIN-Code direkt in VS Code:

- **Task Dispatch** — Agenten-Tasks direkt aus dem Editor starten
- **Swarm Coordination** — Agent-Schwärme koordinieren
- **Buddy Companion** — AI-Begleiter im Editor
- **Memory Consolidation** — Session-Speicher verwalten
- **Agent Modes** — Zwischen Agent-Modi wechseln
- **LSP Integration** — Language Server Protocol

---

## GitHub Automation

### Workflows

| Workflow | Zweck |
|----------|-------|
| `opensin.yml` | Haupt CI/CD Pipeline |
| `opensin-issue-triage.yml` | Auto-Triage neuer Issues |
| `opensin-dedupe-issues.yml` | Duplicate-Erkennung |
| `sweep.yml` | Täglicher Stale-Issue Cleanup |
| `auto-close-duplicates.yml` | Auto-Close von Duplicates |
| `issue-lifecycle-comment.yml` | Lifecycle Labels & Comments |
| `lock-closed-issues.yml` | Lock alter Issues |
| `log-issue-events.yml` | Analytics |
| `non-write-users-check.yml` | Security Check |
| `remove-autoclose-label.yml` | Label Management |
| `backfill-duplicate-comments.yml` | Backfill alter Issues |
| `issue-opened-dispatch.yml` | Dispatch zu externem Repo |

---

## Schnellstart

```bash
# Repository klonen
git clone https://github.com/OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code

# Dependencies installieren
npm install

# Bauen
npm run build

# Tests ausführen
npm run test

# Typecheck
npm run typecheck
```

---

## Migration

Die gesamte Codebasis wurde von sin-claude nach OpenSIN-AI migriert:

- **2.394 Dateien** migriert
- **637.024 Zeilen** Code
- **100% OpenSIN-Branding** — keine externen Referenzen
- **14 Plugins** vollständig portiert
- **Rust Engine** als performantes Backend
- **12 GitHub Actions** Workflows
- **8 Automation Scripts**

---

*Zuletzt aktualisiert: 2026-04-07 | OpenSIN-AI*
