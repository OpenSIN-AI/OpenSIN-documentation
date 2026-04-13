# OpenSIN Code Plugins

OpenSIN-Code kommt mit einem umfassenden Plugin-System. Alle Plugins sind im Verzeichnis `plugins/` des OpenSIN-Code Repositories gespeichert.

## Installierte Plugins

| Plugin | Beschreibung | Dateien |
|--------|-------------|---------|
| [sin-code-review](#sin-code-review) | Automatisierte Code-Reviews mit Multi-Agent-System | 6 |
| [sin-commit-commands](#sin-commit-commands) | Git-Workflow-Befehle für Commits, Push und PRs | 10 |
| [sin-feature-dev](#sin-feature-dev) | Feature-Entwicklung mit spezialisierten Agenten | 12 |
| [sin-frontend-design](#sin-frontend-design) | UI/UX-Implementierung und Design-Skill | 6 |
| [sin-security-guidance](#sin-security-guidance) | Security-Reminder-Hook für sichere Code-Praktiken | 6 |
| [sin-hookify](#sin-hookify) | Regelbasierte Hook-Erstellung zur Verhaltenskontrolle | 48 |
| [sin-explanatory-mode](#sin-explanatory-mode) | Erklärt Implementierungsentscheidungen und Muster | 8 |
| [sin-learning-mode](#sin-learning-mode) | Interaktiver Lernmodus für Code-Entscheidungen | 8 |
| [sin-model-migration](#sin-model-migration) | Migration zwischen verschiedenen Sin-Modellen | 10 |
| [sin-agent-sdk-dev](#sin-agent-sdk-dev) | SDK-Entwicklung für Sin-Agenten | 10 |
| [sin-plugin-dev](#sin-plugin-dev) | Plugin-Entwicklungs-Toolkit mit 7 Skills | 116 |
| [sin-pr-review](#sin-pr-review) | PR-Review-Toolkit mit 6 spezialisierten Agenten | 18 |
| [sin-loop](#sin-loop) | Selbst-referenzielle Entwicklungsloops | 16 |
| [sin-ralph](#sin-ralph) | Ralph-Loop-Technik für iterative Entwicklung | 7 |

---

## sin-code-review

Automatisierte Code-Reviews für Pull Requests mit mehreren spezialisierten Agenten und Confidence-basiertem Scoring.

### Verwendung

```bash
/code-review
```

### Features

- Multi-Agent Review mit Confidence Scoring
- Automatische Issue-Erstellung für gefundene Probleme
- Unterstützt verschiedene Review-Typen: Security, Performance, Style

---

## sin-commit-commands

Streamline deinen Git-Workflow mit einfachen Befehlen für Committing, Pushing und Pull Request Erstellung.

### Befehle

- `/commit` — Intelligentes Committen mit generierter Nachricht
- `/commit-push-pr` — Commit, Push und PR in einem Schritt
- `/clean-gone` — Entfernte Branches und Stale Files aufräumen

---

## sin-feature-dev

Feature-Entwicklung mit spezialisierten Agenten für Architektur, Exploration und Review.

### Agenten

- **Code Architect** — Plant die Architektur neuer Features
- **Code Explorer** — Analysiert die bestehende Codebasis
- **Code Reviewer** — Reviewt den implementierten Code

### Verwendung

```bash
/feature-dev "Beschreibung des Features"
```

---

## sin-frontend-design

Frontend Design Skill für UI/UX-Implementierung. Hilft bei der Erstellung von benutzerfreundlichen Interfaces mit bewährten Design-Patterns.

---

## sin-security-guidance

Security Reminder Hook, der vor potenziellen Sicherheitsproblemen warnt, wenn Dateien bearbeitet werden — einschließlich Command Injection, XSS und unsicheren Code-Mustern.

### Hook

- **PreToolUse** — Prüft Dateiänderungen auf Sicherheitslücken

---

## sin-hookify

Erstelle Hooks um unerwünschte Verhaltensweisen zu verhindern, indem Konversationsmuster analysiert werden. Das mächtigste Plugin im OpenSIN-Ökosystem.

### Features

- Regelbasierte Hook-Erstellung via Markdown-Konfiguration
- Events: `bash`, `file`, `stop`, `prompt`, `all`
- Aktionen: `warn` und `block`
- YAML-Frontmatter mit Regex-Pattern-Matching

### Befehle

- `/hookify` — Erstelle neue Hooks aus Konversationsanalyse
- `/hookify-list` — Liste aller konfigurierten Hooks
- `/hookify-help` — Hilfe und Dokumentation
- `/hookify-configure` — Hooks interaktiv aktivieren/deaktivieren

### Beispiele

```markdown
---
name: "dangerous-rm"
enabled: true
event: "bash"
pattern: "rm\\s+(-rf?|--recursive)"
action: "block"
---

Blockiert `rm -rf` Befehle.
```

---

## sin-explanatory-mode

Fügt pädagogische Einblicke über Implementierungsentscheidungen und Codebase-Muster hinzu.

### Hook

- **SessionStart** — Lädt erklärende Kontextinformationen

---

## sin-learning-mode

Interaktiver Lernmodus, der bei Entscheidungspunkten nach sinnvollen Code-Beiträgen fragt.

### Hook

- **SessionStart** — Aktiviert den Lernmodus bei Session-Beginn

---

## sin-model-migration

Migration von Code und Prompts zwischen verschiedenen Sin-Modellen (Sonnet 4.x, Opus 4.1 → Opus 4.5).

### Skill

- **sin-opus-4-5-migration** — Schritt-für-Schritt Migrationsanleitung

---

## sin-agent-sdk-dev

SDK-Entwicklung für Sin-Agenten mit Verifikations-Agenten für Python und TypeScript.

### Agenten

- **Agent SDK Verifier (Python)** — Validiert Python SDK-Implementierungen
- **Agent SDK Verifier (TypeScript)** — Validiert TypeScript SDK-Implementierungen

---

## sin-plugin-dev

Das umfassendste Plugin-Entwicklungs-Toolkit mit 7 Skills und über 100 Referenzdokumenten.

### Skills

| Skill | Beschreibung |
|-------|-------------|
| **Plugin Structure** | Verzeichnisstruktur, Manifest, Komponenten-Organisation |
| **Hook Development** | Hook-Typen, Konfiguration, Events, Best Practices |
| **Command Development** | Befehlsformat, Frontmatter, dynamische Argumente |
| **MCP Integration** | Server-Typen, Auth, Lifecycle, Debugging |
| **Plugin Settings** | `.sin/plugin-name.local.md` Pattern für Projektkonfiguration |
| **Agent Development** | Agent-Dateistruktur, System-Prompt-Design, Validierung |
| **Skill Development** | Skill-Anatomie, Progressive Disclosure, Validierung |

### Befehle

- `/plugin-dev:create-plugin` — Geführte Plugin-Erstellung in 8 Phasen

### Agenten

- **Agent Creator** — Erstellt neue Agenten
- **Plugin Validator** — Validiert Plugin-Struktur und Sicherheit
- **Skill Reviewer** — Reviewt Skill-Qualität

---

## sin-pr-review

Umfassendes PR-Review-Toolkit mit 6 spezialisierten Review-Agenten.

### Agenten

| Agent | Spezialisierung |
|-------|----------------|
| **Comment Analyzer** | Prüft Code-Kommentare auf Genauigkeit und Vollständigkeit |
| **PR Test Analyzer** | Testabdeckungsanalyse für PRs |
| **Silent Failure Hunter** | Error-Handling-Auditor mit Null-Toleranz für stille Fehler |
| **Type Design Analyzer** | Type-Design-Experte (Encapsulation, Invarianten) |
| **Code Reviewer** | Projekt-Richtlinien, Bug-Detection, Code-Qualität |
| **Code Simplifier** | Vereinfacht Code bei Erhalt der Funktionalität |

### Befehle

```bash
/review-pr [number] [--aspects comments,tests,errors,types,code,simplify,all]
```

---

## sin-loop

Implementierung der Sin-Loop-Technik — kontinuierliche selbst-referenzielle AI-Loops für interaktive iterative Entwicklung.

### Befehle

- `/sin-loop` — Startet den Loop mit einem Prompt
- `/cancel-sin-loop` — Bricht den aktiven Loop ab
- `/sin-loop-help` — Hilfe und Dokumentation

### Hook

- **Stop** — Fängt Exit-Versuche ab und feddert den Prompt zurück

---

## sin-ralph

Ralph-Loop-Technik für iterative Entwicklung. Ähnlich wie sin-loop, aber mit eigenem Hook-System.

---

## Plugin-Entwicklung

Siehe [Plugin Development Tutorial](/docs/tutorials/plugin-development) für eine Schritt-für-Schritt-Anleitung.

### Flow-Builder Skill

`create-flow` gehört nicht zu den OpenSIN-Code-Plugins, ist aber das kanonische OpenCode-Skill für Flow-Arbeit:

- Step-by-step Screenshots direkt im Flow-Workspace
- Vision-Analyse im selben Schritt
- strukturierte Artefakte pro Schritt: `screenshot.png`, `vision.txt`, `analysis.json`, `analysis.md`
- die kanonische Runtime-Quelle ist `OpenSIN-AI/SIN-InkogniFlow`; alternative Flow-Runtimes sollen nicht daneben weiterentwickelt werden

### Plugin-Struktur

```
plugins/sin-mein-plugin/
├── .sin-plugin/
│   └── plugin.json          # Manifest
├── commands/                 # Slash Commands
│   └── mein-befehl.md
├── agents/                   # Spezialisierte Agenten
│   └── mein-agent.md
├── skills/                   # Skills
│   └── mein-skill/
│       └── SKILL.md
├── hooks/                    # Hooks
│   └── hooks.json
└── README.md
```

### plugin.json

```json
{
  "name": "sin-mein-plugin",
  "version": "1.0.0",
  "description": "Beschreibung des Plugins",
  "author": {
    "name": "Dein Name",
    "email": "developer@opensin.ai"
  }
}
```
