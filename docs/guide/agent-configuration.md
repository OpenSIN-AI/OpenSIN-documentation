# Agenten-Konfigurationsdateien — Vollstaendige Dokumentation

> **Stand:** 2026-04-14 | **Version:** 2.2.0

Dieses Dokument beschreibt **ALLE** Konfigurationsdateien für die A2A-Agenten-Steuerung im OpenSIN-Oekosystem.

---

## 📋 Uebersicht

Das OpenSIN-System verwaltet **7 Konfigurationsdateien** in 3 Kategorien:

| Kategorie | Dateien | Zweck |
|:---|:---|:---|
| **Haupt-Config** | `opencode.json` | Provider, Modelle, MCPs, Agenten, Commands |
| **Subagenten-Modelle** | `oh-my-openagent.json`, `oh-my-opencode.json` | Modelle für interne Subagenten (explore, librarian, etc.) |
| **Team-Register** | `oh-my-sin.json` | Zentrales Register aller A2A Teams |
| **Team-Configs** | `my-sin-team-*.json` | Spezifische Agenten + Modelle pro Team |

---

## 1. opencode.json — Haupt-Konfiguration

**Pfad:** `~/.config/opencode/opencode.json` (lokal) oder `upgraded-opencode-stack/opencode.json` (Repo)

### Zweck
Die HAUPT-Konfiguration für OpenCode CLI. Definiert alles was der User direkt sieht und nutzt.

### Struktur

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": [...],           // Plugins (Auth, Frameworks)
  "model": "qwen/coder-model", // Default-Modell
  "provider": { ... },       // LLM-Provider und deren Modelle
  "mcp": { ... },            // MCP-Server (Tool-Provider)
  "agent": { ... },          // User-sichtbare Agenten
  "command": { ... },        // Custom Commands
  "permission": "allow"      // Berechtigungen
}
```

### Provider

| Provider | Modelle | Zweck |
|:---|:---|:---|
| **google** (Antigravity) | `antigravity-claude-sonnet-4-6`, `antigravity-claude-opus-4-6-thinking`, `antigravity-gemini-3.1-pro`, `antigravity-gemini-3-flash` | Hauptmodelle via OAuth |
| **openai** | `gpt-5.4`, `gpt-5.4-mini` | Via OCI Proxy (92.5.60.87:4100) |
| **nvidia-nim** | `qwen-3.5-122b`, `qwen-3.5-397b`, `qwen-3.5-flash`, `step-3.5-flash` | NVIDIA NIM API |
| **openrouter** | 8 Free-Modelle (Qwen, DeepSeek, Gemini, Llama, Phi) | OpenRouter Proxy |
| **qwen** | `qwen/coder-model` → `qwen3-coder-plus` | Qwen OAuth (2000/day free) |
| **modal** | `glm-5.1-fp8` | GLM 5.1 via OCI Token Pool |

### Wichtige Agenten

| Agent | Modell | Zweck |
|:---|:---|:---|
| **SIN-Zeus** | `qwen/coder-model` | Fleet Commander |
| **Sisyphus** | `qwen/coder-model` | Ultraworker |
| **Hephaestus** | `qwen/coder-model` | Deep Agent |
| **Atlas** | `qwen/coder-model` | Plan Executor |

---

## 2. oh-my-openagent.json — Subagenten-Modell-Konfiguration

**Pfad:** `~/.config/opencode/oh-my-openagent.json` oder `upgraded-opencode-stack/oh-my-openagent.json`

### Zweck
Definiert welche Modelle die **internen Subagenten** nutzen wenn delegiert wird.

### Unterschied zu opencode.json

| Datei | Sichtbarkeit | Inhalt |
|:---|:---|:---|
| `opencode.json` | **User-sichtbar** | Agenten die du direkt aufrufst |
| `oh-my-openagent.json` | **Intern** | Subagenten die im Hintergrund arbeiten |

### Beispiel: Delegation

```
User: "Finde alle Auth-Implementierungen"
     ↓
SIN-Zeus liest opencode.json → ist der aktive Agent
     ↓
SIN-Zeus delegiert: task(subagent_type="explore")
     ↓
OHO Plugin liest oh-my-openagent.json → explore.model = "nvidia-nim/stepfun-ai/step-3.5-flash"
     ↓
Explore-Agent startet mit Step 3.5 Flash
```

### Agenten-Modelle

| Subagent | Modell | Fallback-Kette |
|:---|:---|:---|
| **explore** | `nvidia-nim/stepfun-ai/step-3.5-flash` | gemini-3-flash → gpt-5.4 → gemini-3.1-pro → claude-sonnet → qwen |
| **librarian** | `nvidia-nim/stepfun-ai/step-3.5-flash` | gemini-3-flash → gpt-5.4 → gemini-3.1-pro → claude-sonnet → qwen |
| **oracle** | `openai/gpt-5.4` | gemini-3.1-pro → claude-opus-thinking → claude-sonnet → qwen |
| **multimodal-looker** | `google/antigravity-gemini-3.1-pro` | gemini-3-flash → gpt-5.4 → claude-sonnet → qwen |
| **momus** | `google/antigravity-gemini-3.1-pro` | gpt-5.4 → claude-opus-thinking → claude-sonnet → qwen |
| **metis** | `google/antigravity-gemini-3.1-pro` | gpt-5.4 → claude-opus-thinking → claude-sonnet → qwen |
| **sisyphus** | `google/antigravity-claude-opus-4-6-thinking` | gemini-3.1-pro → gpt-5.4 → claude-sonnet → qwen |
| **hephaestus** | `google/antigravity-claude-sonnet-4-6` | gemini-3.1-pro → gpt-5.4 → claude-opus-thinking → qwen |
| **atlas** | `google/antigravity-claude-opus-4-6-thinking` | gemini-3.1-pro → gpt-5.4 → claude-sonnet → qwen |
| **prometheus** | `qwen/coder-model` | claude-opus-thinking → gemini-3.1-pro → gpt-5.4 → claude-sonnet |
| **sisyphus-junior** | `google/antigravity-gemini-3.1-pro` | gemini-3-flash → gpt-5.4 → claude-sonnet → qwen |

### Kategorien

| Kategorie | Modell | Zweck |
|:---|:---|:---|
| **quick** | `openai/gpt-5.4` | Schnelle Antworten |
| **deep** | `openai/gpt-5.4` | Tiefe Analysen |
| **artistry** | `openai/gpt-5.4` | Kreative Tasks |
| **ultrabrain** | `google/antigravity-claude-opus-4-6-thinking` | Schwerste Probleme |
| **visual-engineering** | `google/antigravity-gemini-3.1-pro` | UI/UX Tasks |

---

## 3. oh-my-sin.json — Zentrales A2A Team Register

**Pfad:** `upgraded-opencode-stack/oh-my-sin.json`

### Zweck
Das **zentrale Register** ALLER A2A SIN Teams. Klassifiziert Teams, Manager und verweist auf Team-Configs.

### Struktur

```json
{
  "teams": {
    "team-code": {
      "name": "Team Coding",
      "manager": "A2A-SIN-Zeus",
      "config_file": "my-sin-team-code.json",
      "members": ["A2A-SIN-Simone-MCP", ...],
      "primary_model": "...",
      "fallback_models": [...]
    }
  },
  "defaults": {
    "explore_model": "...",
    "librarian_model": "...",
    "fallback_models": [...]
  }
}
```

### Registrierte Teams

| Team | Manager | Config-Datei | Primaer-Modell |
|:---|:---|:---|:---|
| **Team Coding** | A2A-SIN-Zeus | `my-sin-team-code.json` | `claude-sonnet-4-6` |
| **Team Worker** | A2A-SIN-Team-Worker | `my-sin-team-worker.json` | `gemini-3-flash` |
| **Team Infrastructure** | A2A-SIN-Team-Infrastructure | `my-sin-team-infrastructure.json` | `gpt-5.4` |
| **Team Google Apps** | A2A-SIN-Google-Apps | `my-sin-team-google-apps.json` | `gemini-3.1-pro` |
| **Team Apple Apps** | A2A-SIN-Apple-Apps | `my-sin-team-apple-apps.json` | `gpt-5.4` |

---

## 4. my-sin-team-*.json — Team-spezifische Konfiguration

### Zweck
Definiert **spezifische Agenten und Modelle** für jedes Team. Jedes Team hat seine eigene Config-Datei.

### 4.1 my-sin-team-code.json (Team Coding)

**Agenten:**

| Agent | Modell | Rolle |
|:---|:---|:---|
| **sin-zeus** | `claude-opus-4.6-thinking` | Fleet Commander |
| **simone-mcp** | `claude-sonnet-4-6` | Code Worker (LSP) |
| **frontend** | `gemini-3.1-pro` | UI/UX Specialist |
| **backend** | `claude-sonnet-4-6` | API & Services |
| **fullstack** | `gpt-5.4` | Generalist |

**Kategorien:**

| Kategorie | Modell | Zweck |
|:---|:---|:---|
| **architecture** | `claude-opus-4.6-thinking` | Architektur-Design |
| **implementation** | `claude-sonnet-4-6` | Code schreiben |
| **review** | `gemini-3.1-pro` | Code-Review |
| **testing** | `gpt-5.4` | Tests schreiben |
| **refactoring** | `claude-sonnet-4-6` | Refactoring |

### 4.2 my-sin-team-worker.json (Team Worker)

**Agenten:**

| Agent | Modell | Rolle |
|:---|:---|:---|
| **prolific** | `gemini-3-flash` | Survey Automation |
| **freelancer** | `gemini-3.1-pro` | Freelancing Automation |
| **survey** | `gemini-3-flash` | Multi-Platform Surveys |

### 4.3 my-sin-team-infrastructure.json (Team Infrastructure)

**Agenten:**

| Agent | Modell | Rolle |
|:---|:---|:---|
| **deploy** | `gpt-5.4` | Deployment Automation |
| **monitoring** | `gemini-3.1-pro` | System Monitoring |
| **security** | `claude-opus-4.6-thinking` | Security Audits |

---

## 5. PARALLEL-EXPLORATION MANDATE

**Definiert in:** `AGENTS.md` → `PARALLEL-EXPLORATION MANDATE (PRIORITY -4.5)`

### Das Problem
Ein einzelner `task(subagent_type="explore")` liefert bei grossen Codebases nur ~20% Abdeckung.

### Die Loesung
IMMER 5-10 explore + 5-10 librarian-Agenten PARALLEL starten.

### Agenten-Anzahl nach Projekt-Groesse

| Projekt-Groesse | Explore | Librarian | Gesamt |
|:---|:---|:---|:---|
| Klein (< 50 Dateien) | 3 | 2 | 5 |
| Mittel (50-500 Dateien) | 5 | 3 | 8 |
| Gross (500-2000 Dateien) | 7 | 5 | 12 |
| Enterprise (2000+ Dateien) | 10 | 10 | 20 |

### Beispiel

```javascript
// ALLE im SELBEN Block = sie laufen PARALLEL
task(subagent_type="explore", run_in_background=true, load_skills=[],
  description="Find APIs", prompt="[CONTEXT]: Grosse Codebase. [GOAL]: Alle API-Endpunkte...")
task(subagent_type="explore", run_in_background=true, load_skills=[],
  description="Find Services", prompt="[CONTEXT]: Grosse Codebase. [GOAL]: Alle Services...")
task(subagent_type="explore", run_in_background=true, load_skills=[],
  description="Find Models", prompt="[CONTEXT]: Grosse Codebase. [GOAL]: Alle Daten-Modelle...")
task(subagent_type="librarian", run_in_background=true, load_skills=[],
  description="Framework Docs", prompt="[GOAL]: Offizielle Doku des Frameworks...")
task(subagent_type="librarian", run_in_background=true, load_skills=[],
  description="Best Practices", prompt="[GOAL]: Best Practices für die Technologie...")
```

---

## 6. Dateipfade im Oekosystem

| Repo | Pfad | Datei |
|:---|:---|:---|
| **upgraded-opencode-stack** | `/` | `opencode.json`, `oh-my-sin.json`, `oh-my-openagent.json`, `my-sin-team-*.json` |
| **~/.config/opencode/** | `/` | Alle oben genannten (via `sin-sync` synchronisiert) |
| **OCI VM** | `~/.config/opencode/` | Synchronisiert via `sin-sync` |
| **HF VMs** | `~/.config/opencode/` | Synchronisiert via `sin-sync` |

---

## 7. Sync-Prozess

Nach jeder Aenderung an einer Config-Datei:

```bash
# 1. Aenderung im Repo committen
cd ~/dev/upgraded-opencode-stack
git add -A && git commit -m "update: agent config changes" && git push origin main

# 2. Auf alle Maschinen syncen
sin-sync
```

**Wichtig:** Auth-Dateien (`auth.json`, `token.json`, etc.) werden AUTOMATISCH ausgeschlossen.

---

## 7. /create-a2a-sin-agent — ULTIMATER Creation Skill

**Dieser Skill ersetzt drei alte Skills:**
- ❌ `/create-a2a` → deprecated
- ❌ `/create-a2a-team` → deprecated
- ❌ `/create-a2a-sin-coder` → deprecated
- ✅ `/create-a2a-sin-agent` → **ULTIMATIVER Skill** (alle Funktionen in einem)

### Was der ultimative Skill kann

| Erstelle | Zweck | Template |
|:---|:---|:---|
| **SIN Agent** | Einzelner A2A Agent (z.B. `A2A-SIN-Google-Docs`) | Template-SIN-Agent (unified) |
| **SIN Team** | Team Manager (z.B. `Team-SIN-Survey`) | Template-SIN-Team |
| **SIN Coder** | Entwickler-Agent (z.B. `A2A-SIN-Frontend`) | Template-SIN-Agent + Coder-Mandate |

### Unified Template

**Drei Templates wurden zu EINEM fusioniert:**
- `Template-SIN-Agent` (Basis)
- `Template-SIN-Agent-Worker` (Worker)
- `Template-SIN-Worker` (Minimal)

**→ Jetzt: `Template-SIN-Agent` (all-in-one)**

Jeder neue Agent nutzt dieses eine Template und konfiguriert sich via `agent.json`:
- `type: "agent"` — Standard Agent
- `type: "worker"` — Worker Agent (minimal)
- `type: "coder"` — Coder Agent (mit LangGraph + Security)
- `type: "team-manager"` — Team Manager (mit Hermes Dispatch)

### PARALLEL-EXPLORATION MANDATE

Bei grossen Codebases (100k+ Zeilen, 1000+ Dateien) MUESSEN Agenten **5-10 parallele explore + 5-10 librarian-Agenten** starten:

```
task(subagent_type="explore", run_in_background=true, load_skills=[], description="Find APIs", prompt="[CONTEXT]: Grosse Codebase. [GOAL]: Alle API-Endpunkte...")
task(subagent_type="explore", run_in_background=true, load_skills=[], description="Find Services", prompt="[CONTEXT]: Grosse Codebase. [GOAL]: Alle Services...")
// ... 5-10 weitere parallele Agenten
```

---

## 8. Changelog

### v2.3.0 (2026-04-14)
- `/create-a2a-sin-agent` — ULTIMATER Skill (mergt create-a2a + create-a2a-team + create-a2a-sin-coder)
- Template-Fusion: 3 Templates → 1 (Template-SIN-Agent all-in-one)
- Alte Skills als deprecated markiert

### v2.2.0 (2026-04-14)
- `oh-my-sin.json` — Zentrales Team Register eingefuehrt
- `my-sin-team-code.json` — Team Coding Config
- `my-sin-team-worker.json` — Team Worker Config
- `my-sin-team-infrastructure.json` — Team Infra Config
- `explore`/`librarian` → `nvidia-nim/stepfun-ai/step-3.5-flash`
- PARALLEL-EXPLORATION MANDATE in AGENTS.md
- Volle Fallback-Ketten restored (6 Modelle pro Agent)

### v2.1.0 (2026-04-13)
- GitLab Storage Skill (deprecated in v2.4.0, replaced by A2A-SIN-Box-Storage)
- OCI VM Architecture Docs
- Vision model entfernt, reasoningEffort entfernt

### v2.4.0 (2026-04-15)
- **Box Storage Migration**: `A2A-SIN-Box-Storage` ersetzt GitLab LogCenter als Standard-Cloud-Storage
- Migration-Guide: `docs/storage/box-cloud-storage.md`
- Aktualisierte Mandate in `AGENTS.md` (BOX STORAGE MANDATE PRIORITY 00)
- Kompatibilitätsschicht: `box_storage.py` (ersetzt `gitlab_logcenter.py`)
- Deprecated: `gitlab-storage` Plugin, `room-07-gitlab-storage` Service
- Deadline: Vollständige Migration bis 2026-05-01

### v2.0.0 (2026-04-12)
- Qwen OAuth Plugin fix

### v1.0.0 (2026-04-11)
- Initial Release

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **LLM via opencode CLI** | -2.5 | `opencode run --format json` — KEINE direkten API-Calls |
| **A2A-Agenten-Pflicht** | -200.0 | SELBST MACHEN via `create-a2a-sin-agent` |
| **Kommentar-Pflicht** | -6.0 | EXTREM umfangreiche Kommentare |

→ [Alle Mandate](/best-practices/a2a-communication)
