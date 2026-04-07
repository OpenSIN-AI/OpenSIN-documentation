---
title: "CI/CD mit n8n + sin-github-action"
---

# CI/CD mit n8n + sin-github-action

> **🚨 ABSOLUTES VERBOT: Normale GitHub Actions Runner von GitHub DÜRFEN NIEMALS genutzt werden!**
>
> GitHub Actions Billing ist ein bekanntes Blocking-Problem in der OpenSIN-AI Organisation. Jede CI/CD-Pipeline MUSS über **n8n auf der OCI VM** + **sin-github-action** laufen.

---

## Warum kein normales GitHub Actions?

| Problem | Details |
|---------|---------|
| 💸 **Billing blockiert** | GitHub Actions Billing schlägt fehl → Jobs starten nicht |
| 🐢 **Zu langsam** | Paid Runner: 10+ Minuten Startup + Build |
| 🔒 **Vendor Lock-in** | Abhängigkeit von GitHub Infrastruktur |
| 💰 **Kosten** | Bezahlte Runner = direkte Kosten pro Minute |

**Unsere Lösung:** GitHub Runner läuft nur ~2 Sekunden (curl-only), der eigentliche Build läuft auf unserem **kostenlosen OCI VM (Oracle Cloud Always-Free)**. Zero Billing.

---

## Architektur

```
GitHub Push/PR
     │
     ▼
sin-github-action (composite, nur curl — ~2s, fast kostenlos)
     │ POST /webhook/opensin-ci
     ▼
n8n @ http://92.5.60.87:5678  (n8n.delqhi.com)
     │ HTTP Request Node → 172.18.0.1:3456/run
     ▼
opensin-ci-runner.py (systemd service auf OCI VM)
     │ git clone → npm ci → npm run build → npm test
     ▼
GitHub Commit Status API ✅ / ❌
```

### Komponenten

| Komponente | Ort | Zweck |
|-----------|-----|-------|
| `sin-github-action` | [github.com/OpenSIN-AI/sin-github-action](https://github.com/OpenSIN-AI/sin-github-action) | Composite GitHub Action (nur curl, ~2s) |
| n8n Workflow `cx2UwQYwBPKucckV` | OCI VM 92.5.60.87:5678 | Webhook → CI Runner Dispatcher |
| `opensin-ci-runner.py` | `/home/ubuntu/opensin-ci-runner.py` (OCI) | Python HTTP Server, führt Build/Test aus |
| systemd service | `opensin-ci-runner.service` (OCI) | Hält den CI Runner am Leben |

---

## Setup für ein neues Repo

### 1. Secret setzen

```bash
gh secret set N8N_CI_WEBHOOK_URL \
  --repo OpenSIN-AI/<DEIN-REPO> \
  --body "http://92.5.60.87:5678/webhook/opensin-ci"
```

### 2. `.github/workflows/ci.yml` anlegen

```yaml
name: CI → n8n OCI Runner

# ╔══════════════════════════════════════════════════════════════════╗
# ║  ZERO BILLING CI — delegates all work to n8n on OCI VM          ║
# ║  Runner cost: ~2s (curl only) instead of 10+ min paid runners   ║
# ║  Build/test/lint runs on: OCI VM via n8n @ n8n.delqhi.com       ║
# ╚══════════════════════════════════════════════════════════════════╝

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  dispatch:
    runs-on: ubuntu-latest
    timeout-minutes: 2
    steps:
      - name: Dispatch CI to n8n OCI Runner
        uses: OpenSIN-AI/sin-github-action@main
        with:
          n8n_webhook_url: ${{ secrets.N8N_CI_WEBHOOK_URL }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          pipeline: all
```

### 3. Fertig

Der Push triggert automatisch:
1. GitHub Action startet (ubuntu-latest, ~2s)
2. `sin-github-action` setzt Commit-Status auf `pending`
3. POST an n8n Webhook `http://92.5.60.87:5678/webhook/opensin-ci`
4. n8n leitet weiter an CI Runner (Port 3456 auf OCI Host)
5. CI Runner klont Repo, führt `npm run build` + `npm test` aus
6. GitHub Commit-Status wird auf `success` ✅ oder `failure` ❌ gesetzt

---

## Verfügbare Pipeline-Modi

Der `pipeline` Input in der Action steuert, was gebaut wird:

| Wert | Was läuft |
|------|-----------|
| `all` | build + test (Standard) |
| `build` | Nur `npm run build` |
| `test` | Nur `npm test` |
| `lint` | Nur `npm run lint` |

---

## n8n Workflow Details

### Workflow: `OpenSIN CI Webhook`
- **ID:** `cx2UwQYwBPKucckV`
- **Webhook Path:** `opensin-ci`
- **Webhook URL:** `http://92.5.60.87:5678/webhook/opensin-ci`
- **Öffentliche URL:** `https://n8n.delqhi.com/webhook/opensin-ci`

### n8n API Key (für Verwaltung)

```bash
N8N_KEY="n8n_api_69175bcabef4b10d619b43598cd557a92ee38aac5ae4b1ca"
N8N_URL="http://92.5.60.87:5678"

# Workflow Status prüfen
curl -H "X-N8N-API-KEY: $N8N_KEY" "$N8N_URL/api/v1/workflows/cx2UwQYwBPKucckV" | python3 -c "import json,sys; d=json.load(sys.stdin); print('active:', d.get('active'))"

# Workflow aktivieren (nach Neustart nötig)
curl -X POST -H "X-N8N-API-KEY: $N8N_KEY" "$N8N_URL/api/v1/workflows/cx2UwQYwBPKucckV/activate"
```

### ⚠️ Wichtig: n8n Webhook Registrierung

In n8n 2.12 (SQLite) werden Webhooks **nur beim Startup** aus der DB geladen. Wenn der Workflow nach dem Start über die API aktiviert wird, muss der Container neugestartet werden:

```bash
ssh ubuntu@92.5.60.87 "docker restart n8n-n8n-1 && sleep 15"
```

Nach dem Neustart prüfen:
```bash
ssh ubuntu@92.5.60.87 "docker logs n8n-n8n-1 2>&1 | grep 'OpenSIN CI'"
# Erwartete Ausgabe: Activated workflow "OpenSIN CI Webhook" (ID: cx2UwQYwBPKucckV)
```

---

## CI Runner Details

Der CI Runner ist ein Python HTTP Server auf dem OCI VM.

### Service verwalten

```bash
# Status
ssh ubuntu@92.5.60.87 "sudo systemctl status opensin-ci-runner"

# Logs
ssh ubuntu@92.5.60.87 "sudo journalctl -u opensin-ci-runner -f"

# Neustart
ssh ubuntu@92.5.60.87 "sudo systemctl restart opensin-ci-runner"
```

### Manueller Test

```bash
ssh ubuntu@92.5.60.87 'curl -s -X POST \
  -H "Content-Type: application/json" \
  http://127.0.0.1:3456/run \
  -d "{\"secret\":\"opensin-ci-2026\",\"repo\":\"OpenSIN-AI/OpenSIN-Code\",\"sha\":\"abc\",\"ref\":\"main\",\"pipeline\":\"all\",\"github_token\":\"DEIN_TOKEN\"}"'
```

### Service-Datei

```
/etc/systemd/system/opensin-ci-runner.service
/home/ubuntu/opensin-ci-runner.py
```

### Netzwerk-Konfiguration

Der CI Runner bindet auf `0.0.0.0:3456`. Der n8n Docker Container (Netzwerk `n8n_default`, Bridge `172.18.0.0/16`) erreicht den Host über `172.18.0.1:3456`.

**iptables Regel (persistent):**
```bash
sudo iptables -I INPUT 1 -s 172.18.0.0/16 -p tcp --dport 3456 -j ACCEPT
sudo iptables -I DOCKER-USER -s 172.18.0.0/16 -p tcp --dport 3456 -j ACCEPT
# Gespeichert in /etc/iptables/rules.v4
```

---

## Troubleshooting

### Problem: GitHub Action schlägt fehl mit Billing-Fehler

```
The job was not started because recent account payments have failed
```

**Fix:** Das ist normal für direkte GitHub-hosted Runner. Der CI Dispatch Job braucht trotzdem einen Runner. Lösung: `runs-on: ubuntu-latest` mit `timeout-minutes: 2` — der Job startet, sendet den Webhook, und endet in <2s.

Falls auch das blockiert → lokalen self-hosted Runner auf OCI registrieren:

```bash
# Auf OCI VM:
mkdir -p ~/actions-runner && cd ~/actions-runner
curl -o actions-runner-linux-arm64-2.x.tar.gz -L https://github.com/actions/runner/releases/download/v2.x/actions-runner-linux-arm64-2.x.tar.gz
tar xzf ./actions-runner-linux-arm64-2.x.tar.gz
./config.sh --url https://github.com/OpenSIN-AI --token <RUNNER_TOKEN>
sudo ./svc.sh install && sudo ./svc.sh start
```

Dann in `ci.yml`: `runs-on: self-hosted`

### Problem: Webhook 404 nach n8n Neustart

Der Workflow ist nicht mehr active. Re-aktivieren und neu starten:

```bash
N8N_KEY="n8n_api_69175bcabef4b10d619b43598cd557a92ee38aac5ae4b1ca"
curl -X POST -H "X-N8N-API-KEY: $N8N_KEY" \
  http://92.5.60.87:5678/api/v1/workflows/cx2UwQYwBPKucckV/activate
ssh ubuntu@92.5.60.87 "docker restart n8n-n8n-1"
sleep 15
# Test:
curl -s -o/dev/null -w "HTTP:%{http_code}" -X POST \
  -H "Content-Type: application/json" \
  http://92.5.60.87:5678/webhook/opensin-ci \
  -d '{"repo":"test","sha":"abc","ref":"main","pipeline":"all","github_token":"x"}'
```

### Problem: CI Runner nicht erreichbar aus n8n Container

```bash
# Netzwerk prüfen
ssh ubuntu@92.5.60.87 "docker exec n8n-n8n-1 ip route show"
# Docker host IP aus Container herausfinden (Gateway)
# Dann iptables regeln für diese IP prüfen:
ssh ubuntu@92.5.60.87 "sudo iptables -L INPUT -n | grep 3456"
```

### Problem: `docker-compose up` → Container Conflict

```bash
ssh ubuntu@92.5.60.87 "docker rm -f n8n-n8n-1 && cd /opt/n8n && docker compose up -d"
```

---

## Verwandte Ressourcen

- [sin-github-action Repo](https://github.com/OpenSIN-AI/sin-github-action)
- [n8n OCI Admin](http://92.5.60.87:5678) (VPN/SSH-Tunnel nötig)
- [n8n Public UI](https://n8n.delqhi.com)
- [OCI VM SSH](ssh://ubuntu@92.5.60.87)
- [A2A-SIN-CI-CD Agent](https://github.com/OpenSIN-AI/A2A-SIN-CI-CD)
