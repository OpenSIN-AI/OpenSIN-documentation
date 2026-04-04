# SIN Plugin System

> **OpenSIN's Plugin Architecture** — Erweitere OpenSIN mit Commands, Agents, Skills, Hooks und MCP Servern.

## Overview

SIN Plugins sind Verzeichnisse mit einer definierten Struktur. Kein Build, keine Kompilierung — einfach ablegen und es funktioniert.

## Plugin Struktur

```
mein-plugin/
├── .sin-plugin/
│   └── plugin.json          # { name, version, description, author }
├── commands/                # Slash Commands (.md Dateien)
│   ├── commit.md
│   └── review.md
├── agents/                  # Agent Definitionen (.md Dateien)
│   ├── code-reviewer.md
│   └── architect.md
├── skills/                  # Auto-loading Skills
│   ├── python-testing/
│   │   ├── SKILL.md
│   │   └── references/
│   └── react-patterns/
│       ├── SKILL.md
│       └── references/
├── hooks/                   # Event Handler
│   └── hooks.json
├── .mcp.json               # MCP Server Konfiguration
└── README.md               # Dokumentation
```

## plugin.json

```json
{
  "name": "code-review-toolkit",
  "version": "1.0.0",
  "description": "Automated PR review with specialized agents",
  "author": "OpenSIN-AI",
  "license": "MIT"
}
```

## Commands (Slash Commands)

Commands sind Markdown-Dateien mit YAML Frontmatter:

```markdown
---
description: Commit, push, and open a PR
allowed-tools: Bash(git checkout --branch:*), Bash(git add:*)
argument-hint: Optional description
model: sonnet
effort: high
---

## Context
- Current git status: !`git status`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`

## Your task
$ARGUMENTS

Review the changes, create a descriptive commit message, and push to origin.
```

Das `!` Prefix führt Shell-Commands aus und injiziert die Ausgabe.

## Agent Definitionen

```markdown
---
name: code-architect
description: Design feature architectures and review system designs
tools: Glob, Grep, Read, WebFetch, TodoWrite
model: sonnet
color: blue
---

You are a senior software architect with 20+ years of experience.

When designing architectures:
1. Start with requirements analysis
2. Propose multiple approaches
3. Evaluate tradeoffs
4. Recommend the best solution
5. Provide implementation roadmap
```

## Skills (Auto-Loading)

Skills laden sich automatisch basierend auf Trigger-Phrases oder Dateipfaden:

```markdown
---
name: python-testing
description: Best practices for Python testing
trigger: ["test", "pytest", "unittest", "mock", "fixture"]
paths: ["**/test_*.py", "**/*_test.py", "**/tests/**"]
model: haiku
---

# Python Testing Guide

## Framework
- Use pytest exclusively (no unittest)
- Fixtures for setup/teardown
- Parametrize for multiple test cases

## Structure
```python
def test_something():
    # Arrange
    input_data = {...}
    
    # Act
    result = function_under_test(input_data)
    
    # Assert
    assert result == expected
```
```

## Plugin Installation

```bash
# Aus lokalem Verzeichnis
sin plugin install ./mein-plugin

# Aus Git Repository
sin plugin install https://github.com/OpenSIN-AI/sin-code-review

# Aus Marketplace
sin plugin install code-review-toolkit

# Aus Seed Directory
export SIN_PLUGIN_SEED_DIR=~/.sin-plugin-templates
sin plugin install --from-seed
```

## Plugin Quellen

| Quelle | Beispiel | Use Case |
|--------|----------|----------|
| Lokal | `./plugins/my-plugin` | Eigenentwicklung |
| Git | `github.com/org/plugin` | Team-Plugins |
| Marketplace | `sin plugin install name` | Community |
| Seed Dir | `~/.sin-plugin-templates` | Templates |
| Inline | In settings.json | Quick Config |

## Offizielle SIN Plugins

| Plugin | Beschreibung |
|--------|-------------|
| **feature-dev** | 7-Phase guided feature development |
| **code-review** | Automated PR review with parallel agents |
| **security-guidance** | Security reminder PreToolUse hook |
| **commit-commands** | Git workflow automation |
| **sin-loop** | Iterative self-correction loop |
| **hookify** | No-code hook creation |

## Best Practices

1. **Single Responsibility** — Ein Plugin = eine Aufgabe
2. **Dokumentation** — README mit Beispielen
3. **Testing** — Tests für Commands und Hooks
4. **Versionierung** — Semantic Versioning
5. **Keine Secrets** — Niemals API Keys im Plugin

## Next Steps

- [SIN Commands](/guide/sin-commands)
- [SIN Skills](/guide/sin-skills)
- [SIN Hooks](/guide/sin-hooks)
