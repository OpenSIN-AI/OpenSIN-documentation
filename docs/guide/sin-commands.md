# SIN Commands — Slash Commands

> **OpenSIN's Command System** — Erweitere OpenSIN mit eigenen Slash Commands.

## Overview

SIN Commands sind Markdown-Dateien die sich zu System Prompts erweitern. Keine Programmierung nötig.

## Command Typen

| Typ | Beschreibung | Beispiel |
|-----|-------------|----------|
| `prompt` | Expandiert zu System Prompt | `/commit`, `/review` |
| `action` | Führt externe Aktion aus | `/deploy`, `/test` |

## Command erstellen

Erstelle eine `.md` Datei in `.sin/commands/`:

```markdown
---
description: Review the current PR
allowed-tools: Bash(git diff*), Read, Grep
argument-hint: [filename]
---

Review the changes in this project. Focus on:
1. Bug detection
2. Security issues
3. Performance problems
4. Code style

$ARGUMENTS
```

## Shell Command Injection

Das `!` Prefix führt Commands aus:

```markdown
## Current State
- Branch: !`git branch --show-current`
- Changed files: !`git diff --name-only`
- Test status: !`pytest --co -q 2>&1 | tail -1`
```

## Built-in Commands

| Command | Beschreibung |
|---------|-------------|
| `/config` | Konfiguration anzeigen/ändern |
| `/model` | Modell wechseln |
| `/permissions` | Permission Rules anzeigen |
| `/plan` | Planungsmodus |
| `/compact` | Context komprimieren |
| `/cost` | Kosten anzeigen |
| `/stats` | Session Statistiken |
| `/memory` | Memory Management |
| `/skills` | Verfügbare Skills |
| `/hooks` | Hook Status |
| `/plugins` | Plugin Management |
| `/doctor` | System Health Check |
| `/help` | Hilfe anzeigen |
| `/review` | Code Review |
| `/commit` | Commit erstellen |
| `/test` | Tests ausführen |
| `/deploy` | Deployment starten |

## Next Steps

- [Plugin System](/guide/sin-plugins)
- [SIN Skills](/guide/sin-skills)
