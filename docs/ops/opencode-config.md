# 🔧 Opencode Konfiguration — SSOT

> Stand: 2026-04-04 | Autor: SIN-Zeus

## 📦 Globale Konfiguration

**Pfad:** `~/.config/opencode/opencode.json`

### Default Model
```
openrouter/qwen/qwen3.6-plus:free
```

### Fallback Model
```
openrouter/nvidia/nemotron-3-super-free
```

### Provider Übersicht

| Provider | Modelle | Zweck |
|----------|---------|-------|
| **google** | 4 | Antigravity OAuth (Claude Sonnet 4.6, Claude Opus 4.6, Gemini 3.1 Pro, Gemini 3 Flash) |
| **nvidia-nim** | 2 | Qwen 3.5 122B, Qwen 3.5 397B |
| **gemini-api** | 4 | Direkte Gemini API (3.1 Pro, 3 Flash, 2.5 Pro, 2.5 Flash) |
| **openai** | 1 | GPT-5.4 via OCI Proxy |
| **openrouter** | 9 | Free Models (Qwen, DeepSeek, Gemini, Llama, Phi, Nemotron) |

### Model Context Windows

| Model | Context | Output |
|-------|---------|--------|
| `qwen/qwen3.6-plus:free` | **1.000.000** | 16.384 |
| `antigravity-gemini-3.1-pro` | 1.048.576 | — |
| `antigravity-gemini-3-flash` | 1.048.576 | — |
| `gemini-3.1-pro-preview` | 1.048.576 | — |
| `gemini-3-flash-preview` | 1.048.576 | — |
| `gemini-2.5-pro` | 1.048.576 | — |
| `gemini-2.5-flash` | 1.048.576 | — |
| `qwen-3.5-122b` | 262.144 | — |
| `qwen-3.5-397b` | 262.144 | — |
| `deepseek-chat-v3-0324:free` | 131.072 | 16.384 |
| `deepseek-r1:free` | 131.072 | 16.384 |
| `llama-4-maverick:free` | 131.072 | 16.384 |
| `nemotron-3-super-free` | 131.072 | 16.384 |
| `gpt-5.4` | 128.000 | — |
| `phi-4:free` | 16.384 | 4.096 |

### Agent Konfiguration

Alle 21 Agenten nutzen `openrouter/qwen/qwen3.6-plus:free` als Primary Model mit `openrouter/nvidia/nemotron-3-super-free` als Fallback.

| Agent | Model | Reasoning | Steps |
|-------|-------|-----------|-------|
| Atlas (Plan Executor) | qwen3.6-plus:free | high | 999999 |
| Hephaestus (Deep Agent) | qwen3.6-plus:free | high | 999999 |
| Metis (Plan Consultant) | qwen3.6-plus:free | high | 999999 |
| Momus (Plan Critic) | qwen3.6-plus:free | high | 999999 |
| Prometheus (Plan Builder) | qwen3.6-plus:free | high | 999999 |
| Sisyphus (Ultraworker) | qwen3.6-plus:free | high | 999999 |
| Sisyphus-Junior | qwen3.6-plus:free | medium | 999999 |
| build | qwen3.6-plus:free | high | 999999 |
| explore | qwen3.6-plus:free | low | 999999 |
| general | qwen3.6-plus:free | medium | 999999 |
| librarian | qwen3.6-plus:free | low | 999999 |
| oracle | qwen3.6-plus:free | high | 999999 |
| plan | qwen3.6-plus:free | high | 999999 |
| multimodal-looker | gemini-3.1-pro | low | 999999 |
| sin-zeus | qwen3.6-plus:free | high | 999999 |
| sin-executor-solo | qwen3.6-plus:free | medium | 999999 |
| artistry | qwen3.6-plus:free | high | 999999 |
| compaction | — | low | 999999 |
| summary | — | low | 999999 |
| title | — | low | 999999 |
| omoc | — | high | 999999 |

## 🔧 Bekannte Issues & Fixes

### Fix: JSON Config Corruption (2026-04-04)

**Problem:** Die `opencode.json` war korrupt — Provider-Block zerstört, Modelle falsch verschachtelt.
**Ursache:** Edit-Fehler beim Entfernen eines doppelten Closing-Brace.
**Fix:** Kompletter Provider-Block rekonstruiert (google, nvidia-nim, gemini-api, openai, openrouter).
**Validierung:** `python3 -c "import json; json.load(open('opencode.json'))"` → JSON VALID

### Fix: Context Window qwen3.6-plus:free (2026-04-04)

**Problem:** Context Window war auf 128.000 statt 1.000.000 gesetzt.
**Fix:** `"context": 1000000` in `openrouter` Provider gesetzt.

### Fix: Fallback Model (2026-04-04)

**Problem:** Kein Fallback Model konfiguriert.
**Fix:** `nemotron-3-super-free` als Fallback in Top-Level + allen 21 Agenten.

### Fix: sin-sync Script (2026-04-04)

**Problem:** `declare -A` (bash associative array) funktioniert nicht in zsh.
**Fix:** Zu einfachen Arrays gewechselt (`TARGETS_HOSTS` / `TARGETS_LABELS`).

## 📁 Projekt-Konfiguration

### OpenSIN-backend

**Pfad:** `/Users/jeremy/dev/OpenSIN-backend/.opencode/opencode.json`

- Model: `opencode/qwen3.6-plus-free`
- Fallback: `opencode/nemotron-3-super-free`
- 21 Agenten, alle mit Fallback

### Fleet Config

**Pfad:** `/Users/jeremy/dev/OpenSIN-backend/fleet-config/opencode.json`

- Identisch zu `.opencode/opencode.json`
- Wird an alle HF VMs synchronisiert

## 🚨 Regeln

1. **NIEMALS** `gemini-api` Provider in `opencode.json` eintragen
2. **NIEMALS** direkte API Keys für Google/Anthropic — nur via Antigravity
3. **IMMER** `sin-sync` nach Änderungen an `opencode.json` ausführen
4. **IMMER** JSON Validierung nach edits: `python3 -c "import json; json.load(...)"`
5. **apiKey** gehört unter `options`, NICHT direkt unter Provider
