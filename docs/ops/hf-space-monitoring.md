# 🛡️ HF Space Self-Healing & Monitoring

**⚠️ REGEL: Jedes A2A-SIN Repo MUSS ein Dockerfile haben → sonst KEIN HF Space möglich!**
**⚠️ REGEL: Kein HF Space ohne Keep-Alive in ALLEN 3 Systemen!**
**⚠️ REGEL: Kein HF Space ohne Monitoring-Alert!**

## Problem: Spaces können verschwinden

Spaces können gelöscht werden durch:
- HF Account Cleanup (inaktive Spaces)
- Manuelles Löschen
- API Rate Limits bei Erstellung
- Token-Ablauf

## Lösung: Self-Healing Monitoring

### Architektur

```
┌─────────────────────────────────────────────────────────────┐
│           HF Space Self-Healing System                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │  MONITOR        │  │  RECOVERY       │  │  ALERT      │ │
│  │  (alle 5 Min)   │  │  (automatisch)  │  │  (sofort)   │ │
│  │                 │  │                 │  │             │ │
│  │ 1. Space        │  │ 1. Space        │  │ 1. Telegram │ │
│  │    existiert?   │  │    erstellen    │  │    Alert    │ │
│  │ 2. Space        │  │ 2. Docker       │  │ 2. Discord  │ │
│  │    erreichbar?  │  │    Image push   │  │    Alert    │ │
│  │ 3. Health       │  │ 3. Space        │  │ 3. GitHub   │ │
│  │    Endpoint?    │  │    starten      │  │    Issue    │ │
│  │ 4. Agent Card   │  │ 4. Keep-Alive   │  │             │ │
│  │    vorhanden?   │  │    eintragen    │  │             │ │
│  └─────────────────┘  └─────────────────┘  └─────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 🥇 PRIMARY: n8n Monitoring Workflow

### Setup auf n8n.opensin.ai

**Workflow erstellen:**

1. **Trigger:** Schedule Node – alle 5 Minuten
2. **HTTP Request:** GET an alle Space-URLs mit HF Token
3. **IF Node:** Prüfe ob Space 200 zurückgibt
4. **Code Node:** Wenn 404 → Space existiert nicht mehr
5. **Telegram Alert:** Sofortige Benachrichtigung
6. **HTTP Request:** Space neu erstellen (wenn Rate Limit es erlaubt)

**n8n Workflow JSON:**

```json
{
  "name": "HF Space Self-Healing Monitor",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [{"field": "minutes", "minutesInterval": 5}]
        }
      },
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.1,
      "position": [250, 300]
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
        "method": "GET",
        "url": "https://delqhi-{{ $json.space }}.hf.space/health",
        "options": { "timeout": 10000 },
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [{ "name": "Authorization", "value": "Bearer {{ $env.HF_TOKEN }}" }]
        }
      },
      "name": "Health Check",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [650, 300],
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "conditions": {
          "conditions": [{
            "leftValue": "={{ $json.statusCode }}",
            "rightValue": 200,
            "operator": { "type": "number", "operation": "notEquals" }
          }]
        }
      },
      "name": "IF Down",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [850, 300]
    },
    {
      "parameters": {
        "method": "GET",
        "url": "https://huggingface.co/api/spaces/delqhi/{{ $json.space }}",
        "options": { "timeout": 10000 },
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [{ "name": "Authorization", "value": "Bearer {{ $env.HF_TOKEN }}" }]
        }
      },
      "name": "Check Space Exists",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [1050, 200],
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "chatId": "=-100xxxx",
        "text": "=🚨 HF Space DOWN: {{ $json.space }}\nStatus: {{ $json.statusCode }}\nURL: https://delqhi-{{ $json.space }}.hf.space/\n\nPrüfe ob Space existiert..."
      },
      "name": "Telegram Alert",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [1050, 400]
    },
    {
      "parameters": {
        "jsCode": "const space = $('Check Space Exists').first().json;\nif (space.error && space.error.includes('Repository not found')) {\n  return [{ space: $('Space List').first().json.space, action: 'RECREATE' }];\n} else if (space.runtime && space.runtime.stage === 'RUNNING') {\n  return [{ space: $('Space List').first().json.space, action: 'RESTART' }];\n} else {\n  return [{ space: $('Space List').first().json.space, action: 'INVESTIGATE' }];\n}"
      },
      "name": "Determine Action",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [1250, 200]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://huggingface.co/api/spaces/delqhi/{{ $json.space }}/restart",
        "options": { "timeout": 30000 },
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [{ "name": "Authorization", "value": "Bearer {{ $env.HF_TOKEN }}" }]
        }
      },
      "name": "Restart Space",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [1450, 100]
    }
  ],
  "connections": {
    "Schedule Trigger": { "main": [[{ "node": "Space List", "type": "main", "index": 0 }]] },
    "Space List": { "main": [[{ "node": "Health Check", "type": "main", "index": 0 }]] },
    "Health Check": { "main": [[{ "node": "IF Down", "type": "main", "index": 0 }]] },
    "IF Down": {
      "main": [
        [{ "node": "Check Space Exists", "type": "main", "index": 0 }],
        []
      ]
    },
    "Check Space Exists": { "main": [[{ "node": "Determine Action", "type": "main", "index": 0 }]] },
    "IF Down": { "main": [[], [{ "node": "Telegram Alert", "type": "main", "index": 0 }]] },
    "Determine Action": { "main": [[{ "node": "Restart Space", "type": "main", "index": 0 }]] }
  }
}
```

### Environment Variables in n8n setzen

```
HF_TOKEN=[REDACTED]
TELEGRAM_BOT_TOKEN=<dein-telegram-bot-token>
TELEGRAM_CHAT_ID=<deine-chat-id>
```

---

## 🥈 SECONDARY: OCI VM Monitoring Script

### Setup auf der OCI Ubuntu VM

```bash
sudo cat > /usr/local/bin/hf-space-monitor.sh << 'SCRIPT'
#!/bin/bash
# HF Space Self-Healing Monitor für OCI VM
# Läuft alle 5 Minuten via Cron

HF_TOKEN="[REDACTED]"
LOG="/var/log/sin-hf-monitor.log"
ALERT_LOG="/var/log/sin-hf-alerts.log"

SPACES=(
  "sin-bugbounty" "sin-team-orchestrator" "sin-team-social"
  "sin-tiktok" "sin-tiktok-shop" "sin-github-issues"
  "sin-code-ai" "sin-code-database" "sin-code-integration"
  "sin-worker-prolific-live" "sin-worker-prolific-live-v2"
  "backend" "code-datascience" "code-devops" "frontend"
)

for space in "${SPACES[@]}"; do
  # Health Check
  health_code=$(curl -s -o /dev/null -w "%{http_code}" \
    -H "Authorization: Bearer ${HF_TOKEN}" \
    --max-time 10 "https://delqhi-${space}.hf.space/health" 2>/dev/null)
  
  if [ "$health_code" = "200" ]; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ${space}: OK" >> "$LOG"
    continue
  fi
  
  # Space existiert noch?
  api_response=$(curl -s -H "Authorization: Bearer ${HF_TOKEN}" \
    --max-time 10 "https://huggingface.co/api/spaces/delqhi/${space}" 2>/dev/null)
  
  if echo "$api_response" | grep -q "Repository not found"; then
    # Space wurde gelöscht → RECREATE
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ${space}: DELETED - needs recreation" >> "$ALERT_LOG"
    
    # Versuche Space neu zu erstellen
    create_response=$(curl -s -X POST \
      -H "Authorization: Bearer ${HF_TOKEN}" \
      -H "Content-Type: application/json" \
      "https://huggingface.co/api/repos/create" \
      -d "{\"name\":\"delqhi/${space}\",\"type\":\"space\",\"sdk\":\"docker\"}" 2>/dev/null)
    
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ${space}: Create response: ${create_response}" >> "$ALERT_LOG"
    
  elif echo "$api_response" | grep -q "paused"; then
    # Space ist paused → RESTART
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ${space}: PAUSED - restarting" >> "$ALERT_LOG"
    
    restart_response=$(curl -s -X POST \
      -H "Authorization: Bearer ${HF_TOKEN}" \
      "https://huggingface.co/api/spaces/delqhi/${space}/restart" 2>/dev/null)
    
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ${space}: Restart response: ${restart_response}" >> "$ALERT_LOG"
    
  else
    # Space existiert aber health=404 → INVESTIGATE
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ${space}: DOWN (health=${health_code}) - investigate" >> "$ALERT_LOG"
  fi
done

# Log rotation
tail -n 5000 "$LOG" > "${LOG}.tmp" && mv "${LOG}.tmp" "$LOG"
tail -n 2000 "$ALERT_LOG" > "${ALERT_LOG}.tmp" && mv "${ALERT_LOG}.tmp" "$ALERT_LOG"
SCRIPT
sudo chmod +x /usr/local/bin/hf-space-monitor.sh

# Cron Job (alle 5 Minuten)
(crontab -l 2>/dev/null; echo "*/5 * * * * /usr/local/bin/hf-space-monitor.sh") | crontab -

echo "✅ Monitor installiert"
```

---

## 🥉 TERTIARY: Mac LaunchAgent Monitoring

### Setup auf dem Mac

```bash
cat > ~/.opensin/scripts/hf-space-monitor.sh << 'SCRIPT'
#!/bin/bash
# HF Space Self-Healing Monitor für Mac
# Läuft alle 5 Minuten via LaunchAgent

HF_TOKEN="[REDACTED]"
LOG="/tmp/sin-hf-monitor.log"
ALERT_LOG="/tmp/sin-hf-alerts.log"

SPACES=(
  "sin-bugbounty" "sin-team-orchestrator" "sin-team-social"
  "sin-tiktok" "sin-tiktok-shop" "sin-github-issues"
  "sin-code-ai" "sin-code-database" "sin-code-integration"
  "sin-worker-prolific-live" "sin-worker-prolific-live-v2"
  "backend" "code-datascience" "code-devops" "frontend"
)

for space in "${SPACES[@]}"; do
  health_code=$(curl -s -o /dev/null -w "%{http_code}" \
    -H "Authorization: Bearer ${HF_TOKEN}" \
    --max-time 10 "https://delqhi-${space}.hf.space/health" 2>/dev/null)
  
  if [ "$health_code" = "200" ]; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ${space}: OK" >> "$LOG"
    continue
  fi
  
  api_response=$(curl -s -H "Authorization: Bearer ${HF_TOKEN}" \
    --max-time 10 "https://huggingface.co/api/spaces/delqhi/${space}" 2>/dev/null)
  
  if echo "$api_response" | grep -q "Repository not found"; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) 🚨 ${space}: DELETED - needs recreation" >> "$ALERT_LOG"
    # macOS Notification
    osascript -e "display notification \"Space ${space} wurde gelöscht!\" with title \"🚨 HF Space Alert\""
  elif echo "$api_response" | grep -q "paused"; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ⚠️ ${space}: PAUSED - restarting" >> "$ALERT_LOG"
    curl -s -X POST -H "Authorization: Bearer ${HF_TOKEN}" \
      "https://huggingface.co/api/spaces/delqhi/${space}/restart" 2>/dev/null
  else
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ❌ ${space}: DOWN (health=${health_code})" >> "$ALERT_LOG"
    osascript -e "display notification \"Space ${space} ist down!\" with title \"❌ HF Space Alert\""
  fi
done

tail -n 1000 "$LOG" > "${LOG}.tmp" && mv "${LOG}.tmp" "$LOG"
tail -n 500 "$ALERT_LOG" > "${ALERT_LOG}.tmp" && mv "${ALERT_LOG}.tmp" "$ALERT_LOG"
SCRIPT
chmod +x ~/.opensin/scripts/hf-space-monitor.sh

# LaunchAgent erstellen
cat > ~/Library/LaunchAgents/com.opensin.hf-monitor.plist << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.opensin.hf-monitor</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/Users/jeremy/.opensin/scripts/hf-space-monitor.sh</string>
    </array>
    <key>StartInterval</key>
    <integer>300</integer>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/sin-hf-monitor.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/sin-hf-monitor.err</string>
</dict>
</plist>
PLIST
launchctl load ~/Library/LaunchAgents/com.opensin.hf-monitor.plist
```

---

## 🚨 Recovery-Prozedur: Space wurde gelöscht

### Manuelles Neuanlegen

```bash
HF_TOKEN="[REDACTED]"
SPACE="sin-team-orchestrator"

# 1. Space erstellen
curl -X POST \
  -H "Authorization: Bearer ${HF_TOKEN}" \
  -H "Content-Type: application/json" \
  "https://huggingface.co/api/repos/create" \
  -d "{\"name\":\"delqhi/${SPACE}\",\"type\":\"space\",\"sdk\":\"docker\"}"

# 2. Repo klonen
git clone https://huggingface.co/spaces/delqhi/${SPACE} /tmp/${SPACE}
cd /tmp/${SPACE}

# 3. Dockerfile aus Repo holen
gh api repos/OpenSIN-AI/A2A-SIN-${SPACE}/contents/Dockerfile \
  --jq '.content' | base64 -d > Dockerfile

# 4. server.js aus Repo holen
gh api repos/OpenSIN-AI/A2A-SIN-${SPACE}/contents/server.js \
  --jq '.content' | base64 -d > server.js

# 5. .well-known/agent-card.json aus Repo holen
gh api repos/OpenSIN-AI/A2A-SIN-${SPACE}/contents/.well-known/agent-card.json \
  --jq '.content' | base64 -d > .well-known/agent-card.json

# 6. Commit und push
git add -A
git commit -m "Initial HF Space deployment"
git push

# 7. Space startet automatisch → warten bis RUNNING
# 8. Keep-Alive eintragen
# 9. Health Check: curl https://delqhi-${SPACE}.hf.space/health
```

---

## 📊 Monitoring Dashboard

### Space Status Tabelle

| Space | Health | Card | Status | Last Check |
|-------|--------|------|--------|------------|
| sin-bugbounty | ✅ 200 | ✅ 200 | OK | - |
| sin-team-orchestrator | ❌ 404 | ❌ 404 | **DELETED** | - |
| sin-team-social | ❌ 404 | ❌ 404 | **DELETED** | - |
| sin-tiktok | ❌ 404 | ❌ 404 | **DELETED** | - |
| sin-tiktok-shop | ❌ 404 | ❌ 404 | **DELETED** | - |
| sin-github-issues | ✅ 200 | ✅ 200 | OK | - |
| sin-code-ai | ✅ 200 | ✅ 200 | OK | - |
| sin-code-database | ✅ 200 | ✅ 200 | OK | - |
| sin-code-integration | ✅ 200 | ✅ 200 | OK | - |
| sin-worker-prolific-live | ✅ 200 | ✅ 200 | OK | - |
| sin-worker-prolific-live-v2 | ✅ 200 | ✅ 200 | OK | - |
| backend | ✅ 200 | ❌ 404 | DEGRADED | - |
| code-datascience | ✅ 200 | ✅ 200 | OK | - |
| code-devops | ✅ 200 | ✅ 200 | OK | - |
| frontend | ✅ 200 | ✅ 200 | OK | - |

---

## 🔗 Verknüpfte Dokumentation

- [HF Space Keep-Alive](./hf-keepalive.md) – 3-fache Redundanz
- [HF Space Crisis](./hf-space-crisis.md) – Root Cause Analysis
- [Best Practices](./best-practices.md) – GOLDENE REGELN
- [A2A Fleet](./a2a-fleet.md) – Agent-Übersicht
