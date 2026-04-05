---
title: OpenSIN Bridge — Übersicht
description: Die wichtigste Entwicklung der OpenSIN-AI Org — Chrome Extension die Antigravity schlägt
---

# OpenSIN Bridge — Übersicht

> **Die wichtigste Entwicklung der gesamten OpenSIN-AI Organisation.**
> Eine Chrome Extension die Antigravity in ALLEN Kategorien schlägt.

**Version:** 2.5.0  
**Status:** ✅ Active  
**Repo:** [OpenSIN-backend/services/sin-chrome-extension](https://github.com/OpenSIN-AI/OpenSIN-backend/tree/main/services/sin-chrome-extension)  
**HF MCP Server:** https://huggingface.co/spaces/OpenJerro/opensin-bridge-mcp

---

## Warum OpenSIN Bridge die wichtigste Entwicklung ist

OpenSIN Bridge ist das **Bindeglied zwischen AI-Agenten und dem echten Browser**. Ohne diese Extension können AI-Agenten nicht:

- ✅ Auf Webseiten interagieren (Klicken, Tippen, Lesen)
- ✅ Cookies und Sessions verwalten
- ✅ Screenshots und Videos aufnehmen
- ✅ Netzwerk-Requests überwachen
- ✅ Anti-Detection (Stealth Mode) aktivieren
- ✅ 24/7 auf Plattformen wie Prolific, Upwork, Mindrift arbeiten

**Vor OpenSIN Bridge:** AI-Agenten waren auf Text beschränkt.  
**Nach OpenSIN Bridge:** AI-Agenten können den gesamten Browser kontrollieren.

---

## Architektur

```
AI Agent (Claude/GPT)
        │
        ▼ (WebSocket)
HF MCP Server (immer online)
  wss://openjerro-opensin-bridge-mcp.hf.space
        │
        ▼ (WebSocket)
OpenSIN Bridge v2.5.0 (Chrome Extension)
        │
        ▼ (Chrome APIs)
Chrome Browser (deine Sessions, deine Cookies)
```

---

## Schnellstart

### 1. Extension laden
```bash
git clone https://github.com/OpenSIN-AI/OpenSIN-backend.git
cd OpenSIN-backend/services/sin-chrome-extension/extension
# In Chrome: chrome://extensions/ → Load unpacked
```

### 2. Prolific Worker starten
```bash
python3 services/solver-18-survey-worker/opensin_prolific_worker.py
```

### 3. Tools testen
```bash
python3 services/sin-chrome-extension/tests/test_all_tools.py --hf
```
