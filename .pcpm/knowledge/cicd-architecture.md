# CRITICAL: OpenSIN CI/CD Architecture

**Datum:** 2026-04-13
**Priorität:** KRITISCH - MUSS VON ALLEN AGENTEN BEACHTET WERDEN

## WICHTIGSTE REGEL

**WIR NUTZEN KEINE DIREKTEN GITHUB ACTIONS!**

Statt direkter GitHub Actions nutzen wir unser **eigenes CI/CD-System**:

```
GitHub Webhook → A2A-SIN-GitHub-Action → n8n Workflow → OCI VM Runner
```

### Architektur

1. **A2A-SIN-GitHub-Action** (`github.com/OpenSIN-AI/A2A-SIN-GitHub-Action`)
   - Minimaler GitHub Action Wrapper
   - Sendet Webhook an n8n bei jedem Push/PR
   - Keine Build-Logik in der Action selbst!

2. **n8n Workflows** (OCI VM `92.5.60.87:5678`)
   - Empfängt Webhooks von GitHub
   - Orchestriert Builds, Tests, Deployments
   - Nutzt OCI VM Runner für schwere Arbeiten

3. **OCI VM Runner**
   - Führt tatsächliche Builds/Tests aus
   - Berichtet Ergebnisse zurück an n8n
   - n8n updated GitHub Status Checks

### WARUM dieses System?

- **Keine GitHub Actions Minuten verschwendet** → Kosten sparen
- **Zentrale Steuerung** → Alle Pipelines in n8n sichtbar
- **Flexible Runner** → OCI VM, HF Spaces, lokale Maschinen
- **Einheitliches Logging** → Alles in n8n Execution Logs

### REGELN FÜR ALLE AGENTEN

1. **NIEMALS** `.github/workflows/*.yml` direkt erstellen für Build/Test/Deploy
2. **IMMER** `A2A-SIN-GitHub-Action` als minimalen Webhook-Trigger nutzen
3. **IMMER** n8n Workflows für die eigentliche Pipeline-Logik nutzen
4. Bei neuen Repos: Nur minimalen Webhook-Trigger einrichten, Rest in n8n

### Ausnahmen

Die einzigen erlaubten `.github/workflows/` Dateien sind:

- `webhook-trigger.yml` — Sendet Payload an n8n Webhook
- KEINE Build-Test-Deploy Workflows direkt in GitHub!

### Referenzen

- **A2A-SIN-GitHub-Action:** `github.com/OpenSIN-AI/A2A-SIN-GitHub-Action`
- **n8n Dashboard:** `http://92.5.60.87:5678`
- **OCI VM:** `ubuntu@92.5.60.87`
- **sin-n8n CLI:** `~/.local/bin/sin-n8n`

---

**DIESE INFORMATION IST KRITISCH FÜR ALLE NEUEN REPOS UND AGENTEN!**
**JEDES NEUE REPO BRAUCHT NUR DEN MINIMALEN WEBHOOK-TRIGGER!**
