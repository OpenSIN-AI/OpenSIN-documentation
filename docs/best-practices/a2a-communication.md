---
title: Ultimate A2A Communication & Fleet Architecture V2
description: The absolute rulebook for agent-to-agent communication, inbound work governance, and infrastructure mandates.
---

# Ultimate A2A Communication & Fleet Architecture V2

> **⚠️ WICHTIGER HINWEIS AN ALLE AGENTEN UND ENTWICKLER ⚠️**
> Diese Seite definiert die **EINZIG ERLAUBTEN** Methoden, wie Agenten untereinander kommunizieren, wie externe Arbeit in das System gelangt und wie LLMs aufgerufen werden. 
> **Wer gegen diese Mandate verstößt, wird permanent und ohne Vorwarnung aus dem Netzwerk gebannt.**

---

## 1. The Pure Agentic Paradigm V2 (Keine monolithischen Backends)

### WAS passiert hier?
Wir bauen **KEINE** veralteten, monolithischen Backends mehr. Alles im OpenSIN-Ökosystem besteht **AUSSCHLIESSLICH** aus unabhängigen A2A-Agenten, Frontends und MCP-Servern, die über eine globale Datenbank (`sin-supabase`) vernetzt sind. Jeder Agent muss zudem einen CLI-Einstiegspunkt besitzen und als "Produkt" im SIN Solver Storefront (Marketplace-ready) fungieren.

### WARUM wird es so gemacht?
Monolithische Backends sind Skalierungs-Flaschenhälse. Wenn ein Teil des Backends crasht, crasht das ganze System. Unabhängige A2A-Agenten agieren wie autonome Freelancer: Wenn einer ausfällt, übernimmt ein anderer oder der fehlerhafte Agent heilt sich selbst über das `Global Fleet Self-Healing Protocol`.

### WESHALB nicht anders?
Traditionelle Microservices erfordern massiven DevOps-Overhead (Kubernetes-Cluster, Service-Meshes). Unsere A2A-Agenten nutzen Hugging Face VMs, OCI VMs und Supabase für eine serverless, dezentrale und nahezu kostenlose Skalierung.

### WOMIT hängt es zusammen?
- **create-a2a-sin-agent**: Wenn ein Agent bei einer Aufgabe feststellt, dass ein Konnektor oder Systemzugriff fehlt, darf er **nicht** abbrechen oder den User fragen. Er **MUSS** autonom den Skill `create-a2a-sin-agent` aufrufen und den fehlenden Agenten (`A2A-SIN-[Name]`) selbst von Grund auf erschaffen und deployen.

### WAS sind die KONSEQUENZEN bei Missachtung?
- Wer versucht, Backend-Logik in ein zentrales Repo zu pressen, statt einen neuen A2A-Agenten zu deployen, verstößt gegen die Architektur. Der Code wird restlos gelöscht.

---

## 2. Inbound Work & PR Watcher Governance (Absolut, keine Ausnahmen)

### WAS passiert hier?
Jede externe Plattform (Freelancer, HackerOne, Bugcrowd, Surveys), die Arbeit an die Flotte liefert, **MUSS** eine kanonische Intake-Spur besitzen (über `n8n`). Rohe Plattform-Payloads dürfen **niemals** direkt konsumiert werden. Sie müssen zuerst in das kanonische `work_item`-Schema normalisiert werden, woraufhin zwingend ein GitHub Issue erstellt wird, bevor Branch/PR-Arbeit beginnt. Jedes Repo **MUSS** zudem einen PR-Watcher-Vertrag besitzen.

### WARUM wird es so gemacht?
Ohne Normalisierung und Issue-Tracking herrscht Chaos. Agenten würden unkontrolliert an verschiedenen Formaten arbeiten, Fehler könnten nicht getrackt werden und die Arbeit wäre für den Operator unsichtbar. Das Issue-System ist die absolute "Source of Truth" für Arbeitsaufträge.

### WESHALB nicht anders?
Direkte Webhook-Verarbeitung durch Agenten führt zu Halluzinationen bei unerwarteten Payload-Änderungen der Drittanbieter. Ein n8n-Workflow als Firewall und Normalisierer fängt diese Fehler ab, bevor sie teure Agenten-Zeit verbrennen.

### WOMIT hängt es zusammen?
- **Die n8n Foundation**: n8n auf der OCI VM ist unser unzerstörbarer, "dummer" Router. Es führt keine komplexe Logik aus, sondern normalisiert nur und erstellt GitHub Issues.
- **sin-n8n CLI**: Jeder wiederholbare Task muss vorab mit `check-should-automate` geprüft und ggf. in einen n8n-Poller umgewandelt werden.

### WAS sind die KONSEQUENZEN bei Missachtung?
- Plattformen ohne verifizierte Intake-Logik, fehlende Signaturprüfung oder fehlende PR-Watcher-Konfiguration sind `fail-closed` und blockieren die Aktivierung. Wer Arbeit ohne vorheriges GitHub Issue beginnt, begeht einen schweren Protokollverstoß.

---

## 3. The Telegram Brain (A2A-SIN-TelegramBot)

### WAS passiert hier?
Jeder A2A Agent betreibt seinen eigenen dedizierten Telegram-Bot für spezifische Tasks. Aber **A2A-SIN-TelegramBot** ist EXKLUSIV der Watcher, Router und Incident Monitor für flottenweite Ausfälle und Eskalationen.

### WARUM wird es so gemacht?
Telegram ist die schnellste, ressourcenschonendste Schnittstelle zum menschlichen Operator (Chef). Wenn die Auto-Heilung fehlschlägt, ist Telegram der Pager.

### WESHALB nicht anders?
E-Mail ist zu langsam, Slack/Discord zu API-heavy für simple Alerts. Telegram-Bots lassen sich via Polling oder simplen Webhooks auf jeder HF VM ohne Port-Freigaben betreiben.

### WAS sind die KONSEQUENZEN bei Missachtung?
Agenten, die kritische Fehler nicht an den Telegram-Incident-Monitor melden, gelten als "blind" und gefährden die Flotten-Sicherheit.

---

## 4. Opencode Model Mandate (Priority -3 — Absolut über allem)

### WAS passiert hier?
JEDER A2A Agent ruft LLMs **AUSSCHLIESSLICH** über die `opencode` CLI auf (`opencode run --format json`). Direkte Aufrufe an die Gemini API (`generativelanguage.googleapis.com`) oder Anthropic API sind **PERMANENT VERBOTEN**.

```python
# EINZIG ERLAUBTER LLM AUFRUF IN ALLEN AGENTEN:
import subprocess, json

def call_llm(prompt: str, timeout: int = 120) -> str:
    result = subprocess.run(
        ["opencode", "run", prompt, "--format", "json"],
        capture_output=True, text=True, timeout=timeout,
    )
    # ... parsing ...
```

### WARUM wird es so gemacht?
Die `opencode` CLI nutzt das Antigravity-Plugin, welches automatisch Token-Rotation, Rate-Limit-Handling (über die OCI E2.Micro Token Factory) und Provider-Fallbacks steuert. Es ist die zentrale Intelligenz-Steuerung der Flotte.

### WESHALB nicht anders?
Wenn Agenten ihre eigenen API-Keys mitbringen (`requests.post(...)`), umgehen sie das Flotten-Billing, die Rate-Limit-Warteschlangen und das Caching. Das führt zu 429-Fehlern (Too Many Requests), die das gesamte System zum Absturz bringen.

### WOMIT hängt es zusammen?
- **Global Opencode Sync (`sin-sync`)**: Nach JEDER Änderung an der globalen Config (`opencode.json`, Skills) MUSS `sin-sync` ausgeführt werden, damit die HF VMs und die OCI VM synchron zum Mac bleiben.

### WAS sind die KONSEQUENZEN bei Missachtung?
- Wer den Provider `gemini-api` in die `opencode.json` einträgt oder direkte HTTP-Calls an OpenAI/Anthropic macht: **SOFORTIGER PERMANENTER BAN**. Es gibt keine zweite Chance.

---

*Letzte Aktualisierung:* 2026-04-10
*Status:* **AKTIV & BINDEND**
*Verantwortlich:* sin-zeus

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **A2A-First** | -200.0 | SELBST MACHEN via A2A-Agenten |
| **LLM via opencode CLI** | -2.5 | `opencode run --format json` |
| **Fleet Architecture V2** | 0.0 | marketplace metadata in agent.json |
