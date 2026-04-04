# 🐛 OMOC Swarm Bugs — Registry

> Stand: 2026-04-04 | Autor: SIN-Zeus
> **REGEL:** Bugs dokumentieren, KEINE FIXES!

## Bug-Übersicht

| # | Issue | Titel | Severity | Status |
|---|-------|-------|----------|--------|
| 1 | [#17](https://github.com/OpenSIN-AI/opensin-swarm/issues/17) | In-Memory State Lost | HIGH | 🔴 OFFEN |
| 2 | [#20](https://github.com/OpenSIN-AI/opensin-swarm/issues/20) | swarm.loop Missing | MEDIUM | 🔴 OFFEN |
| 3 | [#22](https://github.com/OpenSIN-AI/opensin-swarm/issues/22) | swarm.forget Property Bug | HIGH | 🔴 OFFEN |
| 4 | [#23](https://github.com/OpenSIN-AI/opensin-swarm/issues/23) | Jam Race Condition | HIGH | 🔴 OFFEN |
| 5 | [#25](https://github.com/OpenSIN-AI/opensin-swarm/issues/25) | JSON Parser Fragile | MEDIUM | 🔴 OFFEN |
| 6 | [#27](https://github.com/OpenSIN-AI/opensin-swarm/issues/27) | Silent Failure | MEDIUM | 🔴 OFFEN |
| 7 | [#29](https://github.com/OpenSIN-AI/opensin-swarm/issues/29) | No Timeout | HIGH | 🔴 OFFEN |
| 8 | [#31](https://github.com/OpenSIN-AI/opensin-swarm/issues/31) | Worktree Leak | LOW | 🔴 OFFEN |

## Detail-Beschreibungen

### BUG-001: In-Memory State Only (swarms Map)
- **Issue:** [#17](https://github.com/OpenSIN-AI/opensin-swarm/issues/17)
- **Severity:** HIGH
- **Symptom:** Swarm-State lebt NUR im Plugin-Prozess. Bei Plugin-Reload/Restart ist ALLES verloren.
- **Ursache:** Zeile 31: `const swarms = new Map()` — reine In-Memory Map ohne Persistenzschicht.
- **Betroffene Datei:** `plugins/omoc-swarm.ts`
- **Impact:** Jeder OpenCode-Neustart zerstört alle aktiven Swarms.

### BUG-002: swarm.loop Dokumentiert aber Nicht Implementiert
- **Issue:** [#20](https://github.com/OpenSIN-AI/opensin-swarm/issues/20)
- **Severity:** MEDIUM
- **Symptom:** README und Tool-Liste erwähnen `swarm.loop` als Queue Runner, Tool existiert nicht.
- **Ursache:** Feature dokumentiert aber nie implementiert.
- **Betroffene Dateien:** `README.md`, `plugins/omoc-swarm.ts`

### BUG-003: swarm.forget Property Bug
- **Issue:** [#22](https://github.com/OpenSIN-AI/opensin-swarm/issues/22)
- **Severity:** HIGH
- **Symptom:** `swarm.forget` liest `result.swarmId` was `undefined` ist.
- **Ursache:** Zeile 801: falscher Property-Zugriff auf resolveSwarm Return-Value.
- **Betroffene Datei:** `plugins/omoc-swarm.ts` Zeile 801
- **Impact:** `swarms.delete(undefined)` ist ein No-Op — Swarm wird nie gelöscht.

### BUG-004: swarm.jam Same-Worktree Race Condition
- **Issue:** [#23](https://github.com/OpenSIN-AI/opensin-swarm/issues/23)
- **Severity:** HIGH
- **Symptom:** Members im JAM teilen sich Worktree ohne File-Locking.
- **Ursache:** Zeilen 699-728: Kein Koordination-Mechanismus für gleichzeitige Edits.
- **Impact:** Git-Konflikte, überschriebene Changes, korrupte Worktrees.

### BUG-005: swarm.max JSON Parser Fragile
- **Issue:** [#25](https://github.com/OpenSIN-AI/opensin-swarm/issues/25)
- **Severity:** MEDIUM
- **Symptom:** JSON.parse schlägt wenn LLM Markdown-Blöcke um JSON packt.
- **Ursache:** Zeile 533: Kein Strip von Markdown-Fences vor Parse.
- **Betroffene Datei:** `plugins/omoc-swarm.ts` Zeilen 533-540

### BUG-006: discoverSwarmForSession Silent Failure
- **Issue:** [#27](https://github.com/OpenSIN-AI/opensin-swarm/issues/27)
- **Severity:** MEDIUM
- **Symptom:** Alle Errors werden geschluckt. Keine Diagnose möglich.
- **Ursache:** Zeile 253: `catch { return undefined }` — blanketer catch-all.
- **Impact:** Debugging unmöglich bei Discovery-Fehlern.

### BUG-007: No Timeout on session.prompt
- **Issue:** [#29](https://github.com/OpenSIN-AI/opensin-swarm/issues/29)
- **Severity:** HIGH
- **Symptom:** `client.session.prompt` hat KEIN Timeout. Kann unbegrenzt hängen.
- **Ursache:** Kein Timeout in swarm.max, swarm.jam, swarm.parallel, swarm.send.
- **Impact:** Swarm-Operationen hängen forever bei LLM Rate Limit / Network Issues.

### BUG-008: worktree Cleanup Default False
- **Issue:** [#31](https://github.com/OpenSIN-AI/opensin-swarm/issues/31)
- **Severity:** LOW
- **Symptom:** `.omoc-worktrees` Verzeichnisse sammeln sich an.
- **Ursache:** Zeile 418: `cleanup = args.cleanup ?? false` — Cleanup per Default AUS.
- **Impact:** Wachsender Disk-Verbrauch, aufgeblähte git Repos.

## n8n API Auth Bug

| # | Issue | Titel | Severity | Status |
|---|-------|-------|----------|--------|
| 9 | [#1](https://github.com/OpenSIN-AI/A2A-SIN-CI-CD/issues/1) | n8n API Key Auth Fails on v2.12.3 | HIGH | ✅ GEFIXT |

### BUG-009: n8n API Key Authentication Fails
- **Issue:** [#1](https://github.com/OpenSIN-AI/A2A-SIN-CI-CD/issues/1)
- **Severity:** HIGH
- **Status:** ✅ GEFIXT (2026-04-04)
- **Symptom:** Alle API Calls returned 401 trotz korrektem X-N8N-API-KEY Header.
- **Ursache:** 3-fach Problem: (1) Owner Account fehlte, (2) API Key ungültig, (3) DB Permissions falsch
- **Fix:** Owner Setup via REST, neuer JWT API Key, DB Permissions korrigiert, Workflows über REST API erstellt
- **Betroffen:** OCI VM 92.5.60.87:5678, n8n v2.12.3
