# 🚀 n8n Setup & Betrieb — SSOT

> Stand: 2026-04-04 | Autor: SIN-Zeus

## 📐 Architektur

```
┌──────────────────────────────────────────────────────────────┐
│                    n8n CI/CD Platform                         │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  OCI VM (92.5.60.87:5678)                                    │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │  Docker: n8n-n8n-1 (n8n v2.12.3)                        │ │
│  │  Volume: n8n_data → /home/node/.n8n                     │ │
│  │  Env: N8N_API_KEY_ENABLED=true                          │ │
│  │       N8N_SECURE_COOKIE=false                           │ │
│  │       N8N_USER_MANAGEMENT_DISABLED=true                 │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  Workflows: 7 active                                         │
│  API Key: JWT-based (expiresAt: 0 = never)                   │
│  Owner: zukunftsorientierte.energie@gmail.com                │
└──────────────────────────────────────────────────────────────┘
```

## 🔑 API Key Management

### Aktueller API Key

Der API Key liegt in `~/.config/opencode/n8n.env`:
```
N8N_API_KEY=eyJhbGciOiJIUzI1NiIs...
```

### API Key erstellen (falls nötig)

```bash
# 1. Login
curl -s -c /tmp/n8n_cookie.txt -X POST http://92.5.60.87:5678/rest/login \
  -H 'Content-Type: application/json' \
  -d '{"emailOrLdapLoginId":"zukunftsorientierte.energie@gmail.com","password":"ZOE.jerry2024"}'

# 2. API Key erstellen
curl -s -b /tmp/n8n_cookie.txt -X POST http://92.5.60.87:5678/rest/api-keys \
  -H 'Content-Type: application/json' \
  -d '{"label":"SIN-Zeus Fleet","scopes":["workflow:create","workflow:read","workflow:update","workflow:delete","workflow:activate","workflow:deactivate","workflow:list","execution:read","execution:list","credential:create","credential:read","credential:update","credential:delete","credential:list","variable:create","variable:read","variable:update","variable:delete","variable:list"],"expiresAt":0}'

# 3. rawApiKey aus der Response extrahieren und in n8n.env speichern
```

## 📋 Aktive Workflows

| # | Name | Trigger | Zweck |
|---|------|---------|-------|
| 1 | Global Fleet Self-Healing Protocol | Webhook | Automatisches Self-Healing der A2A Flotte |
| 2 | GitHub @opnsin-code Mention → Auto-Delegate | GitHub Webhook | Auto-Delegation bei GitHub Mentions |
| 3 | Hugging Face Keep-Alive Pinger | Schedule (6h) | HF Spaces wachhalten |
| 4 | OpenSIN-AI Issue Watcher + Auto-Delegation | Schedule (10min) | GitHub Issues überwachen & delegieren |
| 5 | SIN-Fleet Incident Watcher (Telegram → Hermes) | Webhook | Incident-Weiterleitung via Telegram |
| 6 | Token Pool Monitor | Schedule (30min) | Token Pool überwachen |
| 7 | YouTube Playlist → GitHub Issues Watcher | Schedule | YouTube Playlist → GitHub Issues |

## 🔧 n8n Container Management

### Status prüfen
```bash
ssh ubuntu@92.5.60.87 "docker ps | grep n8n"
```

### Logs prüfen
```bash
ssh ubuntu@92.5.60.87 "docker logs n8n-n8n-1 --tail 50"
```

### Neustart
```bash
ssh ubuntu@92.5.60.87 "docker restart n8n-n8n-1"
```

### Workflows importieren
```bash
# Dateien auf OCI VM kopieren
scp n8n-workflows/*.json ubuntu@92.5.60.87:/tmp/n8n-import/

# In Container kopieren
ssh ubuntu@92.5.60.87 "docker exec n8n-n8n-1 mkdir -p /tmp/n8n-import"
for wf in *.json; do
  ssh ubuntu@92.5.60.87 "docker cp /tmp/n8n-import/$wf n8n-n8n-1:/tmp/n8n-import/$wf"
done

# Importieren
ssh ubuntu@92.5.60.87 "docker exec n8n-n8n-1 n8n import:workflow --separate --input=/tmp/n8n-import/"
```

### Workflows aktivieren (via DB)
```bash
# DB aus Container kopieren
ssh ubuntu@92.5.60.87 "docker cp n8n-n8n-1:/home/node/.n8n/database.sqlite /tmp/n8n.db"
scp ubuntu@92.5.60.87:/tmp/n8n.db /tmp/n8n.db

# Aktivieren
python3 -c "
import sqlite3
db = sqlite3.connect('/tmp/n8n.db')
db.execute('UPDATE workflow_entity SET active=1')
db.commit()
db.close()
"

# Zurückkopieren
scp /tmp/n8n.db ubuntu@92.5.60.87:/tmp/n8n.db
ssh ubuntu@92.5.60.87 "docker cp /tmp/n8n.db n8n-n8n-1:/home/node/.n8n/database.sqlite"

# Container neustarten
ssh ubuntu@92.5.60.87 "docker restart n8n-n8n-1"
```

## ⚠️ Bekannte Probleme & Lösungen

### Problem: API Key funktioniert nicht nach Neustart
**Ursache:** n8n v2.x ignoriert `N8N_API_KEY` env var ohne `N8N_API_KEY_ENABLED=true`
**Lösung:** Container mit `-e N8N_API_KEY_ENABLED=true` starten

### Problem: Workflows nach Import nicht sichtbar
**Ursache:** CLI Import erstellt Workflows ohne User-Zuordnung
**Lösung:** Workflows über REST API erstellen (`POST /api/v1/workflows`)

### Problem: SQLite CORRUPT nach Restart
**Ursache:** WAL-Datei nicht korrekt gemerged
**Lösung:** `PRAGMA wal_checkpoint(TRUNCATE)` vor Neustart ausführen

### Problem: SQLITE_READONLY nach docker cp
**Ursache:** Falsche Dateiberechtigungen (1001:1001 statt 1000:1000)
**Lösung:** `chown 1000:1000` und `chmod 644` auf database.sqlite

## 📁 Workflow JSON Dateien

Alle Workflows liegen in:
```
/Users/jeremy/dev/OpenSIN-backend/n8n-workflows/
├── fleet-self-healing.json
├── github-mention-auto-delegation.json
├── hf-keepalive.json
├── issue-watcher-auto-delegation.json
├── telegram-incident-watcher.json
├── token-pool-monitor.json
└── youtube-playlist-watcher.json
```

## 🔗 Verknüpfte Dokumentation

- [n8n CI/CD Pipeline](../n8n-cicd.md)
- [A2A Fleet](../a2a-fleet.md)
- [HF Keep-Alive](../hf-keepalive.md)
