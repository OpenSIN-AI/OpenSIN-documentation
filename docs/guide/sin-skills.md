# SIN Skills — Auto-Loading Capabilities

> **OpenSIN's Skill System** — Wissen das sich automatisch lädt wenn es gebraucht wird.

## Overview

Skills sind Wissens-Dokumente die sich basierend auf Trigger-Phrases oder Dateipfaden automatisch laden.

## Progressive Disclosure

Skills nutzen 3 Level um Context minimal zu halten:

```
Level 1: Metadata (IMMER geladen)
  → name, description, trigger phrases
  ↓ Trigger match?
Level 2: SKILL.md (Hauptdokument)
  → Kern-Wissen, Beispiele
  ↓ Referenz benötigt?
Level 3: references/ (Support-Dokumente)
  → API Docs, Patterns, Best Practices
```

## Skill erstellen

```
skills/python-testing/
├── SKILL.md              # Hauptdokument
└── references/
    ├── pytest-fixtures.md
    ├── mocking-guide.md
    └── async-testing.md
```

### SKILL.md

```markdown
---
name: python-testing
description: Python testing best practices
trigger: ["test", "pytest", "mock", "fixture", "coverage"]
paths: ["**/test_*.py", "**/tests/**"]
---

# Python Testing

## Rules
- pytest ONLY
- Arrange-Act-Assert pattern
- Mock externe Services
- Coverage >= 85%
```

## Skill Trigger

Skills laden sich wenn:
1. **Trigger Phrase** im User Prompt vorkommt
2. **Dateipfad**匹配 dem `paths:` Pattern
3. **Tool Usage** einen Skill erfordert

## Next Steps

- [Plugin System](/guide/sin-plugins)
- [SIN Commands](/guide/sin-commands)
