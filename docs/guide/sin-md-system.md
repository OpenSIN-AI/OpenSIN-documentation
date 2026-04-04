# SIN.md System — Project Context Files

> **OpenSIN's answer to CLAUDE.md** — Hier definierst du, wie sich OpenSIN in deinem Projekt verhalten soll.

## Overview

`SIN.md` Dateien sind die DNA deines Projekts. Sie definieren Regeln, Patterns, Architektur und Verhalten für alle OpenSIN Agenten.

## Auto-Discovery

OpenSIN lädt automatisch alle `SIN.md` Dateien in deinem Projekt:

```
my-project/
├── SIN.md                    # Global (gilt für alles)
├── src/
│   ├── SIN.md               # Gilt für src/ und Subdirs
│   ├── api/
│   │   └── SIN.md           # Gilt für api/
│   └── frontend/
│       └── SIN.md           # Gilt für frontend/
├── tests/
│   └── SIN.md               # Gilt für tests/
└── docs/
    └── SIN.md               # Gilt für docs/
```

## SIN.md Format

```markdown
# Project Name

## Tech Stack
- Python 3.11, FastAPI, PostgreSQL
- React, TypeScript, TailwindCSS

## Code Style
- 4 spaces indentation
- Type hints required
- Docstrings für alle public functions
- Max 500 lines pro Datei

## Architecture Rules
- API Layer darf NICHT direkt auf DB zugreifen
- Services sind die einzige Schicht zwischen API und DB
- Keine zirkulären Imports

## Commands
- `make test` — Tests ausführen
- `make lint` — Linting
- `make build` — Build

## Important Patterns
- Repository Pattern für DB Zugriff
- Dependency Injection überall
- Event-driven für async Tasks

## Don't Touch
- `legacy/` — Nicht anfassen, wird abgelöst
- `config/secrets.py` — Niemals ändern
```

## Nested SIN.md Dateien

OpenSIN kombiniert alle relevanten `SIN.md` Dateien basierend auf dem aktuellen Arbeitsverzeichnis:

```
# Wenn du in src/api/ arbeitest:
1. SIN.md (root)      → wird geladen
2. src/SIN.md         → wird geladen
3. src/api/SIN.md     → wird geladen
```

## Git Status Injection

OpenSIN injiziert automatisch Git-Status in den Kontext:

```markdown
## Current Git State
- Branch: feature/user-auth
- Status: 3 modified, 2 untracked
- Last commit: feat: add login endpoint (2 hours ago)
```

## SIN.md vs AGENTS.md

| Datei | Zweck | Scope |
|-------|-------|-------|
| `SIN.md` | Projekt-Kontext, Regeln, Patterns | Globales Projekt-Wissen |
| `AGENTS.md` | Agent-spezifische Instruktionen | Spezifisches Agent-Verhalten |
| `SIN-MEMORY.md` | Session-übergreifendes Gedächtnis | Persistente Projekt-Erinnerungen |

## Best Practices

1. **Kurz halten** — Max 200 Zeilen pro SIN.md
2. **Aktuell halten** — Veraltete Infos sind schlimmer als keine
3. **Spezifisch sein** — "Schreib guten Code" hilft nicht
4. **Beispiele geben** — Zeig, wie es gemacht wird
5. **Negativ-Beispiele** — Zeig auch, wie es NICHT gemacht wird

## Beispiel: Python Projekt

```markdown
# Python API Service

## Stack
- Python 3.11, FastAPI, SQLAlchemy 2.0, PostgreSQL 15
- Pytest, Ruff, MyPy

## Struktur
```
app/
├── api/          # Routes (dünn!)
├── services/     # Business Logic
├── models/       # SQLAlchemy Models
├── schemas/      # Pydantic Schemas
└── repositories/ # DB Zugriff
```

## Regeln
- API Routes: max 10 lines, nur Request/Response
- Services: enthalten ALLE Business Logic
- Repositories: einzige Stelle mit SQLAlchemy Queries
- Keine f-strings in Logs — nutze structlog
- Async überall außer bei reinen CPU-Tasks

## Testing
- Unit Tests neben dem Code: `test_<file>.py`
- Integration Tests in `tests/integration/`
- Mock externe Services IMMER
- Coverage minimum: 85%
```

## Beispiel: Frontend Projekt

```markdown
# React Frontend

## Stack
- React 18, TypeScript, Vite, TailwindCSS
- React Query, Zustand, React Router v6

## Komponenten-Regeln
- Functional Components ONLY
- Custom Hooks für Logic-Extraktion
- Max 200 lines pro Komponente
- Props immer als Interface definieren

## State Management
- Server State → React Query
- UI State → useState/useReducer
- Global State → Zustand stores
- KEIN Redux

## Testing
- Vitest + React Testing Library
- Component Tests für alle UI-Komponenten
- Integration Tests für User Flows
```

## Deaktivieren

```bash
# SIN.md Auto-Loading deaktivieren
export SIN_CODE_DISABLE_SIN_MDS=1

# Oder im Agent Config
agent.config.sin_md_enabled = False
```

## Next Steps

- [AGENTS.md Guide](/guide/agent-basics)
- [Plugin System](/guide/plugin-development)
- [Hook System](/guide/sin-hooks)
