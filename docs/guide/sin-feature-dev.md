# SIN Feature Development Workflow

> **OpenSIN's 7-Phase Feature Development** — Strukturierte Methodik statt einfachem Chat.

## Overview

Der Feature Development Workflow führt dich durch 7 Phasen von der Idee bis zur Implementation.

## Die 7 Phasen

```
Phase 1: Discovery         → Was soll gebaut werden?
    ↓
Phase 2: Codebase Exploration → Wie ist der aktuelle Stand?
    ↓
Phase 3: Clarifying Questions → Was fehlt noch?
    ↓
Phase 4: Architecture Design  → Wie wird es gebaut?
    ↓
Phase 5: Implementation       → Code schreiben
    ↓
Phase 6: Quality Review       → Code prüfen
    ↓
Phase 7: Summary              → Zusammenfassung
```

## Phase 1: Discovery

```bash
/sin feature-dev "Add user authentication"
```

Der Agent analysiert:
- User Requirements
- Existing Auth System
- Security Requirements
- Dependencies

## Phase 2: Codebase Exploration

Parallele Agenten explorieren die Codebase:

```python
# Parallel: 3 Explorer Agents
explorers = [
    Subagent(name="auth-explorer", task="Find auth-related code"),
    Subagent(name="api-explorer", task="Find API endpoints"),
    Subagent(name="db-explorer", task="Find database models"),
]

results = await SubagentPool().execute(explorers)
```

## Phase 3: Clarifying Questions

Der Agent stellt gezielte Fragen:

```
❓ Soll OAuth2 oder JWT verwendet werden?
❓ Welche externen Provider (Google, GitHub)?
❓ Session Duration?
❓ Rate Limiting erforderlich?
```

## Phase 4: Architecture Design

```markdown
# Architecture: User Authentication

## Components
- Auth Service (new)
- JWT Token Manager
- OAuth2 Provider Integration
- Session Store (Redis)

## Flow
1. User login → Auth Service
2. Validate credentials → JWT issued
3. Token stored in Redis
4. Subsequent requests validated via JWT

## Files to Create
- src/auth/service.py
- src/auth/jwt_manager.py
- src/auth/oauth2.py
- src/auth/models.py
```

## Phase 5: Implementation

Parallele Implementation mit Subagents:

```python
implementation_agents = [
    Subagent(name="auth-service", task="Implement auth service"),
    Subagent(name="jwt-manager", task="Implement JWT manager"),
    Subagent(name="oauth2", task="Implement OAuth2 integration"),
]

await SubagentPool().execute(implementation_agents)
```

## Phase 6: Quality Review

Parallel Review mit spezialisierten Agenten:

```python
review_agents = [
    Subagent(name="security-reviewer", model="gpt-4", task="Security audit"),
    Subagent(name="bug-finder", model="gpt-4", task="Find bugs"),
    Subagent(name="style-checker", model="gpt-3.5", task="Code style"),
]

reviews = await SubagentPool().execute(review_agents)
```

## Phase 7: Summary

```markdown
# Feature Complete: User Authentication

## Created Files
- src/auth/service.py (245 lines)
- src/auth/jwt_manager.py (180 lines)
- src/auth/oauth2.py (320 lines)
- src/auth/models.py (95 lines)

## Tests
- 24 unit tests added
- 3 integration tests added
- Coverage: 92%

## Security
- ✅ No hardcoded secrets
- ✅ Rate limiting enabled
- ✅ Input validation complete
```

## Next Steps

- [SIN Subagents](/guide/sin-subagents)
- [Code Review Plugin](/guide/sin-code-review)
