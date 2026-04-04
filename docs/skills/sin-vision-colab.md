---
name: sin-vision-colab
description: "Screen recording + AI vision analysis via direct Gemini REST API. No browser, no Colab MCP, no CDP. Pure REST with 6-model fallback chain for unlimited vision calls."
license: Apache-2.0
compatibility: opencode
metadata:
  audience: all-agents
  workflow: screen-vision-analysis
  trigger: screen-record, screenshot, vision-analyze, look-screen
  version: v4-gemini-rest-fallback
---

# A2A-SIN-Vision-Colab Skill (v4 SOTA 2026)

Screen recording + AI vision analysis via **direct Gemini REST API** with a **6-model fallback chain**.

## 🔴 WHAT DOES NOT WORK (March 2026)

- ❌ **Browser automation (nodriver, AppleScript) for Colab** — Chrome 146+ blocks DevToolsActivePort
- ❌ **Colab MCP Server** — requires open browser tab, not headless
- ❌ **CDP on default Chrome profile** — blocked since Chrome 146
- ❌ **Leaked Gemini API keys** — old key `AIzaSyA1THIC_...` is revoked

## 🟢 ARCHITECTURE (V4 - Direct Gemini REST API)

```
[Agent] → look-screen CLI → [Gemini REST API] → Vision Analysis
              ↓                    ↑
        screencapture -x      base64 inline_data
              ↓                    ↑
        /tmp/screen.png      6-model fallback chain
```

## 🔑 KEY FEATURES

- ✅ **KEIN Browser!** — Pure REST, no browser at all
- ✅ **KEIN Colab MCP!** — Direct Gemini API, no notebook needed
- ✅ **KEIN CDP!** — No Chrome DevTools Protocol
- ✅ **6-Model Fallback Chain** — Practically unlimited free-tier calls
- ✅ **API Key:** `AIzaSyCnRoGEoQJBAVssEu6BP1ojSBzIwV5r8_o`

## 📋 FALLBACK CHAIN (Unlimited Free Tier)

| Priority | Model | Free Tier Quota | Purpose |
|----------|-------|-----------------|---------|
| 1 | `gemini-2.5-flash` | Unlimited RPM, 1M context | Primary vision |
| 2 | `gemini-3-flash-preview` | 5 RPM, 250K tokens | Backup vision |
| 3 | `gemini-3.1-flash-lite-preview` | 15 RPM, 250K tokens | Lightweight backup |
| 4 | `gemma-3-27b` | 30 RPM, 15K context | Fallback vision |
| 5 | `gemma-3-12b` | 30 RPM, 15K context | Fallback vision |
| 6 | `gemma-3-4b` | 30 RPM, 15K context | Last resort |

## 📋 WANN NUTZEN

| Trigger | Aktion |
|---------|--------|
| "nimm bildschirm auf" | `look-screen --record` |
| "analysiere bildschirm" | `look-screen --screenshot /tmp/screen.png --describe` |
| "was siehst du?" | `look-screen --once --screenshot /tmp/screen.png` |
| "überwache bildschirm" | `look-screen --interval 3` |
| "stop aufnahme" | `look-screen --stop` |

## 🚀 SETUP

### 1. look-screen CLI ist bereits installiert

```bash
# Symlink: ~/.local/bin/look-screen → ~/.open-auth-rotator/tools/look_screen.py
look-screen --version
# Output: look-screen v4.0.0 (Gemini REST API + Fallback Chain)
```

### 2. API Key konfigurieren (optional)

Der API Key ist hardcoded im Script. Überschreiben via Environment Variable:

```bash
export GEMINI_VISION_API_KEY="your-key-here"
```

### 3. Verifizieren

```bash
look-screen --status
# Expected:
# [look-screen] Vision Architecture: v4-gemini-rest-fallback
# [look-screen] Models (6): gemini-2.5-flash, gemini-3-flash-preview, ...
# [look-screen] Browser Automation: NONE (Pure REST)
# [look-screen] Status: Active
```

## 🔧 LOOK-SCREEN CLI

```bash
# Status prüfen
look-screen --status

# Screenshot analysieren
look-screen --screenshot /tmp/screen.png --describe

# Mit custom Prompt
look-screen --screenshot /tmp/screen.png --describe --prompt "Ist ein Fehler sichtbar?"

# Kontinuierliche Überwachung
look-screen --interval 3

# Screenshot + Analyse in einem Befehl
screencapture -x /tmp/screen.png && look-screen --screenshot /tmp/screen.png --describe
```

## 🔄 AGENT WORKFLOW

```python
import subprocess

# 1. Screenshot machen
subprocess.run(["screencapture", "-x", "/tmp/screen.png"])

# 2. Analyse anfordern
result = subprocess.run(
    ["look-screen", "--screenshot", "/tmp/screen.png", "--describe"],
    capture_output=True, text=True
)
analysis = result.stdout
```

## ⚠️ ARCHITECTURAL RULE: NO BROWSER FOR VISION

**NIEMALS** versuchen, Vision-Analyse über Browser, Colab MCP oder CDP zu machen.
Immer `look-screen` CLI nutzen — das ruft direkt die Gemini REST API auf.

## 🔗 RESSOURCEN

- [Gemini Vision API Docs](https://ai.google.dev/gemini-api/docs/vision)
- [Gemini API Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits)
