# OpenSIN-AI Platform — Plugin Ecosystem & GitHub Automation

OpenSIN-AI Platform ist das Plugin- und Automatisierungs-Ökosystem der OpenSIN-AI Organisation. 14 Plugins, GitHub Workflows und DevContainer-Setup.

> **Repository:** [OpenSIN-AI/opensin-ai-platform](https://github.com/OpenSIN-AI/opensin-ai-platform)
>
> **Umfang:** 182 Dateien | 87.247 Zeilen | 14 Plugins

## OpenSIN-AI Agent Roadmap

- Feature spec: [OpenSIN-overview/docs/opensin-ai-agent-feature-spec.md](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/opensin-ai-agent-feature-spec.md)
- Comparison guide: [OpenSIN-AI Agent Features](opensin-ai-agent-features.md)
- This repo documents the automation and plugin surfaces that support the OpenSIN-AI Agent stack.

---

## Plugin Ecosystem

| Plugin                                        | Beschreibung                         | Dateien |
| --------------------------------------------- | ------------------------------------ | ------- |
| [opensin-feature-dev](#feature-dev)           | 7-Phase Feature Development Workflow | 6       |
| [opensin-model-migration](#model-migration)   | Modell-Migration (Sonnet → Opus)     | 5       |
| [opensin-agent-sdk-dev](#agent-sdk-dev)       | Agent SDK Development Toolkit        | 5       |
| [opensin-code-review](#code-review)           | Multi-Agent Code Review              | 3       |
| [opensin-commit-commands](#commit-commands)   | Git Workflow Commands                | 5       |
| [opensin-explanatory-mode](#explanatory-mode) | Erklär-Modus via Hooks               | 4       |
| [opensin-frontend-design](#frontend-design)   | Production-Grade Frontend Generation | 3       |
| [opensin-hookify](#hookify)                   | Hook Creation from Conversations     | 20      |
| [opensin-learning-mode](#learning-mode)       | Interactive Learning Mode            | 3       |
| [opensin-plugin-dev](#plugin-dev)             | Plugin Development Toolkit           | 30+     |
| [opensin-pr-review](#pr-review)               | PR Review Toolkit                    | 9       |
| [opensin-loop](#loop)                         | Self-Referential Development Loops   | 7       |
| [opensin-security](#security)                 | Security Guidance Hooks              | 3       |

---

## Feature Dev

7-Phase guided workflow für Feature-Entwicklung:

1. **Discovery** — Requirements gathering
2. **Exploration** — Codebase analysis
3. **Questions** — Clarification phase
4. **Architecture** — Design blueprint
5. **Implementation** — Code generation
6. **Review** — Quality assurance
7. **Summary** — Documentation

### Agents

- **Code Reviewer** — Reviews code with confidence scoring (threshold 80)
- **Code Explorer** — Traces execution paths, maps architecture
- **Code Architect** — Designs implementation blueprints

---

## Hookify

Hook-Erstellung aus Conversations:

```bash
/hookify — Create hooks from conversation analysis
/hookify:list — List all configured rules
/hookify:configure — Interactive enable/disable
/hookify:help — Usage guide
```

### Hook Types

- **PreToolUse** — Validate before tool execution
- **PostToolUse** — Audit after tool execution
- **Stop** — Control session termination
- **UserPromptSubmit** — Filter user prompts

---

## Plugin Dev Toolkit

Umfassende Toolkit für Plugin-Entwicklung:

```bash
/plugin-dev:create-plugin — 8-Phase guided plugin creation
```

### Skills

- **Plugin Structure** — Directory layout, manifest, auto-discovery
- **Command Development** — Slash commands with YAML frontmatter
- **Hook Development** — Prompt-based and command hooks
- **Skill Development** — Skills with progressive disclosure
- **Agent Development** — Agent creation with frontmatter
- **MCP Integration** — Server configuration (stdio, SSE, HTTP, WebSocket)

---

## GitHub Automation

| Workflow                          | Zweck                         |
| --------------------------------- | ----------------------------- |
| `opensin.yml`                     | Haupt CI/CD Pipeline          |
| `opensin-issue-triage.yml`        | Auto-Triage neuer Issues      |
| `opensin-dedupe-issues.yml`       | Duplicate-Erkennung           |
| `sweep.yml`                       | Täglicher Stale-Issue Cleanup |
| `auto-close-duplicates.yml`       | Auto-Close von Duplicates     |
| `issue-lifecycle-comment.yml`     | Lifecycle Labels & Comments   |
| `lock-closed-issues.yml`          | Lock alter Issues             |
| `log-issue-events.yml`            | Analytics                     |
| `non-write-users-check.yml`       | Security Check                |
| `remove-autoclose-label.yml`      | Label Management              |
| `backfill-duplicate-comments.yml` | Backfill alter Issues         |
| `issue-opened-dispatch.yml`       | Dispatch zu externem Repo     |

---

## DevContainer

Sandboxed development environment:

- **Base:** Node.js 20
- **Firewall:** iptables — blocks all outbound except approved endpoints
- **Tools:** git, gh, delta, zsh, vim, nano, fzf
- **VS Code Extensions:** ESLint, Prettier, Remote Containers, GitLens

---

## Schnellstart

```bash
# Repository klonen
git clone https://github.com/OpenSIN-AI/opensin-ai-platform.git
cd opensin-ai-platform

# DevContainer starten
# In VS Code: F1 > Dev Containers: Reopen in Container

# Oder manuell
docker build -t opensin-ai-platform .devcontainer/
docker run -it opensin-ai-platform
```

---

_Zuletzt aktualisiert: 2026-04-07 | OpenSIN-AI_

---

## Relevante Mandate

| Mandat                   | Priority | Doku                                                    |
| ------------------------ | -------- | ------------------------------------------------------- |
| **Bun-Only**             | -1.5     | `bun install` / `bun run` statt npm                     |
| **LLM via opencode CLI** | -2.5     | `opencode run --format json` — KEINE direkten API-Calls |
| **A2A-Agenten-Pflicht**  | -200.0   | SELBST MACHEN via `create-a2a-sin-agent`                |
| **Kommentar-Pflicht**    | -6.0     | EXTREM umfangreiche Kommentare                          |

→ [Alle Mandate](/best-practices/a2a-communication)
