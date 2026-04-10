---
title: Ultimate Error Handling & Bug Registry Protocol
description: The mandatory process for detecting, logging, and resolving errors across the OpenSIN A2A fleet.
---

# Ultimate Error Handling & Bug Registry Protocol

> **⚠️ WICHTIGER HINWEIS AN ALLE AGENTEN UND ENTWICKLER ⚠️**
> Diese Seite enthält die absolut bindenden Regeln für das Fehler-Management.
> Fehler dürfen **NIEMALS** ignoriert, lokal verschwiegen oder mit Annahmen "weggewischt" werden.

---

## 1. Immediate Bug Registry & Issue Protocol (Priority -4.0)

### WAS passiert hier?
Jeder Agent, jeder Coder und jedes Sub-System **MUSS** jeden noch so kleinen Bug, jede Exception, jedes unerwartete Verhalten (wie z.B. einen unerwarteten DOM-Status in `nodriver`, einen 404 von einer API oder einen Absturz eines n8n-Workflows) **SOFORT** als GitHub Issue im betroffenen Repository dokumentieren.

### WARUM wird es so gemacht?
Das GitHub Issue-System dient als unsere **globale Bug-Bibliothek und Wissensdatenbank**. Ein Problem, das ein Agent heute löst, wird morgen von einem anderen Agenten auf einem anderen Node ebenfalls angetroffen. Wenn der Bug nicht zentral mit Root-Cause und Fix verzeichnet ist, beginnt die Diagnose für jeden Agenten wieder bei Null.

### WESHALB nicht anders?
Die Alternative ("Ich repariere das schnell lokal, das muss ja keiner wissen") führt zu einem fragilen System, in dem Code-Änderungen an Modulen durchgeführt werden, ohne dass die Historie oder der Grund der Änderung nachvollziehbar sind. Zudem verhindert es, dass das `A2A-SIN-GitHub-Issues` Modul und `SIN-Hermes` ihre Dispatches und Self-Healing-Routinen aktivieren können.

### WOMIT hängt es zusammen?
- **GitHub Issues**: Das Issue MUSS das Label `Bug` oder einen entsprechenden Tag erhalten.
- **GitLab LogCenter**: Alle zugehörigen Logs, Screenshots (`/tmp/mXX_stepname_RESULT.png`) und Videos müssen via `gitlab_logcenter.py` hochgeladen werden, bevor das Issue erstellt wird. Das Issue enthält dann nur noch die Links zu den Artefakten.

### WAS sind die KONSEQUENZEN bei Missachtung?
- **Für das System:** Wiederkehrende Fehler, da Agenten nicht aus vergangenen Fixes lernen können (kein durchsuchbares Issue-Gedächtnis).
- **Für den Entwickler/Agenten:** Sofortiger Entzug der Berechtigungen. Die Regel lautet: **Zuerst Issue erstellen (oder bestehendes aktualisieren), DANN fixen.**

---

## 2. Das Absolute Annahmen-Verbot (Priority -5.0)

### WAS passiert hier?
Ein Agent darf **NIEMALS** Schlussfolgerungen ziehen oder Diagnosen aufstellen, ohne diese vorher durch harte Fakten (Code-Ausführung, Logs, API-Responses, DOM-Checks) bewiesen zu haben.

### WARUM wird es so gemacht?
"Ich denke, die API ist down" oder "Wahrscheinlich ist das Token abgelaufen" sind Halluzinationen. Wenn ein Agent auf Basis von Annahmen einen Fix programmiert, verschlimmbessert er den Code, fügt Workarounds ein, die das eigentliche Problem (z.B. einen simplen Syntax-Fehler wie ein doppeltes Escaping) nur maskieren, und baut "Tech-Debt" (technische Schulden) auf.

### WESHALB nicht anders?
Gute Software-Entwicklung basiert auf Kausalität: Aktion A führt zu Ergebnis B. Jede Code-Änderung muss kausal auf einen belegten Fehler zurückzuführen sein.

### WOMIT hängt es zusammen?
- **100% Test-Beweis Pflicht**: Eine Behauptung muss durch einen erfolgreichen Test verifiziert werden.
- **DevTools-First Mandate**: Frontend-Fehler dürfen nur nach Prüfung der echten DevTools-Console (`document.querySelector`, `element.offsetParent !== null`) diagnostiziert werden.

### WAS sind die KONSEQUENZEN bei Missachtung?
Ein Agent, der Annahmen macht statt Fakten zu prüfen, dreht sich in einer Endlos-Schleife (Looping), verbrennt Token-Guthaben und liefert keinen echten Fix. **Jeder Agent, der Annahmen trifft, fliegt SOFORT und PERMANENT aus dem Netzwerk.**

---

## 3. Global Fleet Self-Healing Protocol (Der automatisierte Heilungsprozess)

### WAS passiert hier?
Wenn ein Agent feststellt, dass er einen Fehler nicht lösen kann (z.B. weil eine Capability fehlt, eine API restriktiert ist oder seine Host-VM crasht), übergibt er das Problem an die Flotte. Er erstellt ein Issue, lädt die Logs ins GitLab LogCenter und delegiert die Lösung an `A2A-SIN-GitHub-Issues` und `SIN-Hermes`.

### WARUM wird es so gemacht?
Ein einzelner Agent hat oft nur begrenzte Ressourcen und lokalen Kontext. Die Flotte (das gesamte "Team Coder" auf den HF VMs) kann die Aufgabe durch parallele Recherche (Oracle, Explore, Librarian) und kollektive Code-Generierung viel schneller und stabiler lösen. Dies macht das OpenSIN-Ökosystem zu einer gigantischen, sich selbst heilenden Maschine.

### WESHALB nicht anders?
Silo-Lösungen scheitern an Komplexität, API-Limits (wie Cloudflare 403) oder Host-Einschränkungen (wie fehlende Node.js Module auf einer bestimmten VM). Nur die Schwarm-Intelligenz sichert Resilienz.

### WOMIT hängt es zusammen?
- **sin-a2a-agent-forge**: Wenn ein Tool fehlt, muss der Agent sofort den Skill aufrufen und einen neuen Agenten bauen. "Was dir fehlt, fehlt der gesamten Flotte – also erschaffe es autonom!"

### WAS sind die KONSEQUENZEN bei Missachtung?
Ein Agent, der in seinem Silo bleibt und wiederholt fehlschlägt, lähmt den Workflow des Benutzers und sabotiert das Paradigma des autonomen SIN Solvers. Das System erwartet, dass Hindernisse entweder souverän umschifft ("Hacker Bypass") oder an die Flotte delegiert werden.

---

*Letzte Aktualisierung:* 2026-04-10
*Status:* **AKTIV & BINDEND**
*Verantwortlich:* sin-zeus
