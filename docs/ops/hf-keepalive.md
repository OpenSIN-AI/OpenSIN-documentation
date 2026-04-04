# 🔄 HF Space Keep-Alive (Redundant)

**⚠️ REGEL: Es darf NIEMALS ein HF Space erstellt werden OHNE Keep-Alive in ALLEN 3 Systemen!**
**⚠️ REGEL: Jedes A2A-SIN Repo MUSS ein Dockerfile haben → sonst KEIN HF Space möglich!**

## Problem

Hugging Face Spaces schlafen nach **48 Stunden Inaktivität** ein. Ein einzelner Keep-Alive-Mechanismus kann ausfallen (Mac aus, n8n down, OCI VM reboot). Deshalb: **3-fache Redundanz.**

## Aktueller Stand: 15 HF Spaces (nicht 19!)

**Kritisch:** Von 68 A2A-SIN Repos haben nur **15** ein HF Space. **53 Repos haben KEIN Dockerfile** und können nicht deployed werden.

### Existierende Spaces (15)

| Space | Status | Keep-Alive |
|-------|--------|------------|
| sin-bugbounty | ✅ Public | ✅ |
| sin-team-orchestrator | ✅ Public | ✅ |
| sin-team-social | ✅ Public | ✅ |
| sin-tiktok | ✅ Public | ✅ |
| sin-tiktok-shop | ✅ Public | ✅ |
| sin-github-issues | ✅ Public | ✅ |
| sin-code-ai | ✅ Public | ✅ |
| sin-code-database | ✅ Public | ✅ |
| sin-code-integration | ✅ Public | ✅ |
| sin-worker-prolific-live | ✅ Public | ✅ |
| sin-worker-prolific-live-v2 | ✅ Public | ✅ |
| backend | ✅ Public | ✅ |
| code-datascience | ✅ Public | ✅ |
| code-devops | ✅ Public | ✅ |
| frontend | ✅ Public | ✅ |

### Fehlende Spaces (53)

→ Siehe [HF Space Crisis](./hf-space-crisis.md) für Root Cause Analysis und Lösungsplan.

## Aktueller Stand: 15 HF Spaces (nicht 19!)

**Kritisch:** Von 68 A2A-SIN Repos haben nur **15** ein HF Space. **53 Repos haben KEIN Dockerfile** und können nicht deployed werden.

### Existierende Spaces (15)

| Space | Status | Keep-Alive |
|-------|--------|------------|
| sin-bugbounty | ✅ Public | ✅ |
| sin-team-orchestrator | ✅ Public | ✅ |
| sin-team-social | ✅ Public | ✅ |
| sin-tiktok | ✅ Public | ✅ |
| sin-tiktok-shop | ✅ Public | ✅ |
| sin-github-issues | ✅ Public | ✅ |
| sin-code-ai | ✅ Public | ✅ |
| sin-code-database | ✅ Public | ✅ |
| sin-code-integration | ✅ Public | ✅ |
| sin-worker-prolific-live | ✅ Public | ✅ |
| sin-worker-prolific-live-v2 | ✅ Public | ✅ |
| backend | ✅ Public | ✅ |
| code-datascience | ✅ Public | ✅ |
| code-devops | ✅ Public | ✅ |
| frontend | ✅ Public | ✅ |

### Fehlende Spaces (53)

→ Siehe [HF Space Crisis](./hf-space-crisis.md) für Root Cause Analysis und Lösungsplan.

## Architektur: 3-Fache Redundanz

```
┌─────────────────────────────────────────────────────────────┐
│              HF Space Keep-Alive (3x Redundant)              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │  PRIMARY:       │  │  SECONDARY:     │  │  TERTIARY:  │ │
│  │  n8n Workflow   │  │  OCI VM Cron    │  │  Mac        │ │
│  │  (alle 5 Min)   │  │  (alle 10 Min)  │  │  LaunchAgent│ │
│  │                 │  │                 │  │  (alle 5 Min)│ │
│  │  ✅ 24/7        │  │  ✅ 24/7        │  │  ⚠️ Mac aus │ │
│  │  ✅ Cloud       │  │  ✅ VM immer an │  │  ⚠️ Fallback │ │
│  └─────────────────┘  └─────────────────┘  └─────────────┘ │
│                                                              │
│  Alle 3 Systeme pingen ALLE 19 Spaces parallel.             │
│  Ausfall von 2 Systemen = Spaces bleiben trotzdem wach.     │
└─────────────────────────────────────────────────────────────┘
```

## 🥇 PRIMARY: n8n Workflow

### Setup auf n8n.opensin.ai

**Workflow erstellen:**

1. **Trigger:** Schedule Node – alle 5 Minuten
2. **HTTP Request:** GET an alle 19 Space-URLs parallel
3. **Error Handling:** Bei Fehler → Telegram/Discord Alert

**n8n Workflow JSON (importieren):**

```json
{
  "name": "HF Space Keep-Alive",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "minutes",
              "minutesInterval": 5
            }
          ]
        }
      },
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "method": "GET",
        "url": "https://delqhi-{{ $json.space }}.hf.space/",
        "options": {
          "timeout": 10000
        },
        "sendHeaders": false
      },
      "name": "Ping HF Space",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [650, 300],
      "retryOnFail": true,
      "maxTries": 3,
      "waitBetweenTries": 2000
    },
    {
      "parameters": {
        "jsCode": "return [\n  { space: 'sin-bugbounty' },\n  { space: 'sin-team-orchestrator' },\n  { space: 'sin-team-social' },\n  { space: 'sin-tiktok' },\n  { space: 'sin-tiktok-shop' },\n  { space: 'sin-github-issues' },\n  { space: 'sin-code-ai' },\n  { space: 'sin-code-database' },\n  { space: 'sin-code-integration' },\n  { space: 'sin-worker-prolific-live' },\n  { space: 'sin-worker-prolific-live-v2' },\n  { space: 'backend' },\n  { space: 'code-datascience' },\n  { space: 'code-devops' },\n  { space: 'frontend' }\n];"
      },
      "name": "Space List",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict"
          },
          "conditions": [
            {
              "id": "error-check",
              "leftValue": "={{ $json.statusCode }}",
              "rightValue": 200,
              "operator": {
                "type": "number",
                "operation": "notEquals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "name": "IF Error",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [850, 300]
    },
    {
      "parameters": {
        "chatId": "=-100xxxx",
        "text": "=⚠️ HF Space DOWN: {{ $json.space }}\nStatus: {{ $json.statusCode }}\nURL: https://delqhi-{{ $json.space }}.hf.space/",
        "additionalFields": {}
      },
      "name": "Telegram Alert",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [1050, 400]
    }
  ],
  "connections": {
    "Schedule Trigger": { "main": [[{ "node": "Space List", "type": "main", "index": 0 }]] },
    "Space List": { "main": [[{ "node": "Ping HF Space", "type": "main", "index": 0 }]] },
    "Ping HF Space": { "main": [[{ "node": "IF Error", "type": "main", "index": 0 }]] },
    "IF Error": { "main": [[{ "node": "Telegram Alert", "type": "main", "index": 0 }]] }
  }
}
```

### n8n Workflow aktivieren

1. n8n.opensin.ai öffnen
2. Workflows → New → JSON importieren
3. Telegram Bot Token und Chat ID eintragen
4. **Workflow aktivieren** (Toggle auf ON)

---

## 🥈 SECONDARY: OCI VM Cron Job

### Setup auf der OCI Ubuntu VM

```bash
# SSH auf die OCI VM
ssh ubuntu@<oci-vm-ip>

# Script erstellen
sudo cat > /usr/local/bin/hf-keepalive.sh << 'SCRIPT'
#!/bin/bash
SPACES=(
  "sin-bugbounty" "sin-team-orchestrator" "sin-team-social"
  "sin-tiktok" "sin-tiktok-shop" "sin-github-issues"
  "sin-code-ai" "sin-code-database" "sin-code-integration"
  "sin-worker-prolific-live" "sin-worker-prolific-live-v2"
  "backend" "code-datascience" "code-devops" "frontend"
)
LOG="/var/log/sin-hf-keepalive.log"
for space in "${SPACES[@]}"; do
  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "https://delqhi-${space}.hf.space/" 2>/dev/null)
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ${space}: ${code}" >> "$LOG"
done
# Log rotieren – max 5000 Zeilen
tail -n 5000 "$LOG" > "${LOG}.tmp" && mv "${LOG}.tmp" "$LOG"
SCRIPT
sudo chmod +x /usr/local/bin/hf-keepalive.sh

# Cron Job erstellen (alle 10 Minuten)
(crontab -l 2>/dev/null; echo "*/10 * * * * /usr/local/bin/hf-keepalive.sh") | crontab -

# Testen
/usr/local/bin/hf-keepalive.sh
tail -20 /var/log/sin-hf-keepalive.log
```

### Cron Job verwalten

```bash
# Status prüfen
crontab -l | grep hf-keepalive

# Logs ansehen
tail -f /var/log/sin-hf-keepalive.log

# Manuelles Ausführen
/usr/local/bin/hf-keepalive.sh

# Deaktivieren (NIEMALS!)
crontab -e  # Zeile mit hf-keepalive auskommentieren
```

---

## 🥉 TERTIARY: Mac LaunchAgent (Fallback)

### Setup auf dem Mac

```bash
# Script
~/.opensin/scripts/hf-keepalive.sh

# LaunchAgent
~/Library/LaunchAgents/com.opensin.hf-keepalive.plist

# Intervall: Alle 5 Minuten
```

→ Vollständige Anleitung: [HF Keep-Alive Mac](./hf-keepalive.md)

---

## 📊 Überwachte Spaces (19)

| Space | URL | n8n | OCI Cron | Mac |
|-------|-----|:---:|:--------:|:---:|
| sin-server | `delqhi-sin-server.hf.space` | ✅ | ✅ | ✅ |
| sin-team-social | `delqhi-sin-team-social.hf.space` | ✅ | ✅ | ✅ |
| sin-team-orchestrator | `delqhi-sin-team-orchestrator.hf.space` | ✅ | ✅ | ✅ |
| sin-team-google-apps | `delqhi-sin-team-google-apps.hf.space` | ✅ | ✅ | ✅ |
| sin-team-shop | `delqhi-sin-team-shop.hf.space` | ✅ | ✅ | ✅ |
| sin-team-company | `delqhi-sin-team-company.hf.space` | ✅ | ✅ | ✅ |
| sin-team-worker | `delqhi-sin-team-worker.hf.space` | ✅ | ✅ | ✅ |
| sin-team-creator | `delqhi-sin-team-creator.hf.space` | ✅ | ✅ | ✅ |
| sin-team-marketing | `delqhi-sin-team-marketing.hf.space` | ✅ | ✅ | ✅ |
| sin-cloudflare | `delqhi-sin-cloudflare.hf.space` | ✅ | ✅ | ✅ |
| sin-supabase | `delqhi-sin-supabase.hf.space` | ✅ | ✅ | ✅ |
| sin-storage | `delqhi-sin-storage.hf.space` | ✅ | ✅ | ✅ |
| sin-authenticator | `delqhi-sin-authenticator.hf.space` | ✅ | ✅ | ✅ |
| sin-passwordmanager | `delqhi-sin-passwordmanager.hf.space` | ✅ | ✅ | ✅ |
| sin-research | `delqhi-sin-research.hf.space` | ✅ | ✅ | ✅ |
| sin-tiktok | `delqhi-sin-tiktok.hf.space` | ✅ | ✅ | ✅ |
| sin-tiktok-shop | `delqhi-sin-tiktok-shop.hf.space` | ✅ | ✅ | ✅ |
| sin-mindrift | `delqhi-sin-mindrift.hf.space` | ✅ | ✅ | ✅ |
| sin-imessage | `delqhi-sin-imessage.hf.space` | ✅ | ✅ | ✅ |

---

## 🚨 Deployment-Checkliste für NEUE HF Spaces

**BEVOR ein neuer Space deployed wird:**

- [ ] Space Visibility auf **PUBLIC** setzen (NIEMALS private!)
- [ ] Dockerfile mit HEALTHCHECK vorhanden
- [ ] `/.well-known/agent-card.json` Endpoint funktioniert
- [ ] `/health` Endpoint gibt 200 zurück
- [ ] **n8n Workflow: Space-Name zur Space List hinzufügen**
- [ ] **OCI VM: Space-Name zu `/usr/local/bin/hf-keepalive.sh` hinzufügen**
- [ ] **Mac: Space-Name zu `~/.opensin/scripts/hf-keepalive.sh` hinzufügen**
- [ ] Space-URL manuell testen: `https://delqhi-<space>.hf.space/`
- [ ] Fleet-Validation: `npm run test:a2a:fleet`
- [ ] Live-Audit: `npm run test:a2a:live -- --agent <slug>`

---

## 🔧 Troubleshooting

### Space gibt 404 zurück
1. **Private?** → Auf Public setzen: `huggingface-cli repo settings delqhi/<space> --visibility public`
2. **Deleted?** → Space neu erstellen via `npm run deploy:hf`
3. **Asleep?** → Alle 3 Keep-Alive-Systeme prüfen

### n8n Workflow läuft nicht
```bash
# n8n Status prüfen
curl -s "https://n8n.opensin.ai/healthz"

# Workflow manuell triggern
# n8n UI → Workflow → Execute Workflow
```

### OCI VM Cron läuft nicht
```bash
# Cron Status prüfen
systemctl status cron

# Script manuell testen
/usr/local/bin/hf-keepalive.sh

# Logs prüfen
tail -50 /var/log/sin-hf-keepalive.log
```

### Mac LaunchAgent läuft nicht
```bash
launchctl list | grep opensin
~/.opensin/scripts/hf-keepalive.sh
cat /tmp/sin-hf-keepalive.err
```

### Space bleibt nach Public-Setzen 404
- Space braucht **Rebuild**: HF Dashboard → Settings → Factory Rebuild
- Oder: `huggingface-cli repo restart delqhi/<space>`

## 🔗 Verknüpfte Dokumentation

- [A2A Fleet](./a2a-fleet.md) – Agent-Übersicht
- [Best Practices](./best-practices.md) – HF Deployment Standards
- [n8n CI/CD](./n8n-cicd.md) – Pipeline-Dokumentation
