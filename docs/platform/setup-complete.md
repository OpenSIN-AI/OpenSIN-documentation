# 🚀 OpenSIN Complete Setup Guide

## 1. OCI VM ✅ DONE

Keep-Alive + Monitoring sind auf der OCI VM (`ubuntu@92.5.116.158`) installiert:

```bash
# Verify
ssh ubuntu@92.5.116.158 "crontab -l | grep hf"
ssh ubuntu@92.5.116.158 "tail -5 /var/log/sin-hf-keepalive.log"
ssh ubuntu@92.5.116.158 "tail -5 /var/log/sin-hf-monitor.log"
```

## 2. Mac ✅ DONE

Keep-Alive + Monitoring LaunchAgents laufen:

```bash
launchctl list | grep opensin
# com.opensin.hf-keepalive
# com.opensin.hf-monitor
```

## 3. n8n Workflow Import

### Schritt-für-Schritt

1. **n8n.opensin.ai öffnen**
2. **Workflows → New → Import from JSON**
3. **JSON einfügen** (siehe unten)
4. **Environment Variables setzen:**
   - `HF_TOKEN` = `[REDACTED]`
   - `TELEGRAM_BOT_TOKEN` = (aus sin-passwordmanager holen)
   - `TELEGRAM_CHAT_ID` = (aus sin-passwordmanager holen)
5. **Workflow aktivieren** (Toggle auf ON)

### n8n Workflow JSON

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
        "url": "https://huggingface.co/api/spaces/delqhi/{{ $('Space List').first().json.space }}",
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
        "chatId": "={{ $env.TELEGRAM_CHAT_ID }}",
        "text": "=🚨 HF Space DOWN: {{ $('Space List').first().json.space }}\nStatus: {{ $json.statusCode }}\nURL: https://delqhi-{{ $('Space List').first().json.space }}.hf.space/"
      },
      "name": "Telegram Alert",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [1050, 400]
    }
  ],
  "connections": {
    "Schedule Trigger": { "main": [[{ "node": "Space List", "type": "main", "index": 0 }]] },
    "Space List": { "main": [[{ "node": "Health Check", "type": "main", "index": 0 }]] },
    "Health Check": { "main": [[{ "node": "IF Down", "type": "main", "index": 0 }]] },
    "IF Down": {
      "main": [
        [{ "node": "Check Space Exists", "type": "main", "index": 0 }],
        [{ "node": "Telegram Alert", "type": "main", "index": 0 }]
      ]
    }
  }
}
```

## 4. backend Space agent-card.json

**Problem:** HF Token hat keine Schreibrechte auf `delqhi/backend` Space.

**Lösung:** Manuell via HF UI oder mit Owner-Account:

```bash
# Option A: HF Web UI
# 1. https://huggingface.co/spaces/delq/backend öffnen
# 2. Files → Add file → Create new file
# 3. Pfad: .well-known/agent-card.json
# 4. Content: (siehe unten)
# 5. Commit

# Option B: Git Clone mit Owner-Account
cd /tmp && rm -rf backend-hf
git clone https://<OWNER_USERNAME>:<OWNER_TOKEN>@huggingface.co/spaces/delqhi/backend backend-hf
cd backend-hf
mkdir -p .well-known
# agent-card.json erstellen (siehe unten)
git add .well-known/agent-card.json
git commit -m "Add agent-card.json for A2A discovery"
git push
```

### agent-card.json Content

```json
{
  "protocol": "A2A",
  "protocol_version": "0.2.5",
  "name": "SIN-Backend",
  "description": "OpenSIN Backend - Supabase DB, Auth, Fleet-Management",
  "url": "https://delqhi-backend.hf.space/a2a/v1",
  "provider": {
    "organization": "OpenSIN-AI",
    "url": "https://github.com/OpenSIN-AI/OpenSIN-backend"
  },
  "capabilities": {
    "streaming": true,
    "push_notifications": false,
    "state_transition_history": true
  },
  "security": { "schemes": {} },
  "default_input_modes": ["text"],
  "default_output_modes": ["text"],
  "skills": [
    { "id": "fleet-management", "name": "Fleet Management", "description": "Manage A2A agent fleet" },
    { "id": "auth", "name": "Authentication", "description": "Handle user authentication via Supabase" },
    { "id": "database", "name": "Database Operations", "description": "Supabase database operations" }
  ]
}
```

## 5. 5 gelöschte Spaces neu erstellen

**Status:** HF Rate Limit (20 Spaces/Tag) erschöpft. Warten bis ~13:00 UTC.

### Auto-Create Script (nach Rate Limit)

```bash
HF_TOKEN=$(cat ~/.cache/huggingface/token)
SPACES=("sin-team-orchestrator" "sin-team-social" "sin-tiktok" "sin-tiktok-shop")

for space in "${SPACES[@]}"; do
  echo "Erstelle ${space}..."
  result=$(curl -s -X POST \
    -H "Authorization: Bearer ${HF_TOKEN}" \
    -H "Content-Type: application/json" \
    "https://huggingface.co/api/repos/create" \
    -d "{\"name\":\"delqhi/${space}\",\"type\":\"space\",\"sdk\":\"docker\"}")
  
  if echo "$result" | grep -q "url"; then
    echo "  ✅ ${space} erstellt"
    # Dockerfile + server.js + agent-card.json pushen
    # Siehe: /ops/hf-space-monitoring → Recovery-Prozedur
  else
    echo "  ❌ ${space}: ${result:0:100}"
  fi
done
```

## 📊 Aktueller Status

| Space | Health | Card | Keep-Alive | Monitor |
|-------|--------|------|------------|---------|
| sin-bugbounty | ✅ 200 | ✅ 200 | ✅ Mac + OCI | ✅ Mac + OCI |
| sin-github-issues | ✅ 200 | ✅ 200 | ✅ Mac + OCI | ✅ Mac + OCI |
| sin-code-ai | ✅ 200 | ✅ 200 | ✅ Mac + OCI | ✅ Mac + OCI |
| sin-code-database | ✅ 200 | ✅ 200 | ✅ Mac + OCI | ✅ Mac + OCI |
| sin-code-integration | ✅ 200 | ✅ 200 | ✅ Mac + OCI | ✅ Mac + OCI |
| sin-worker-prolific-live | ✅ 200 | ✅ 200 | ✅ Mac + OCI | ✅ Mac + OCI |
| sin-worker-prolific-live-v2 | ✅ 200 | ✅ 200 | ✅ Mac + OCI | ✅ Mac + OCI |
| code-datascience | ✅ 200 | ✅ 200 | ✅ Mac + OCI | ✅ Mac + OCI |
| code-devops | ✅ 200 | ✅ 200 | ✅ Mac + OCI | ✅ Mac + OCI |
| frontend | ✅ 200 | ✅ 200 | ✅ Mac + OCI | ✅ Mac + OCI |
| **backend** | ✅ 200 | ❌ 404 | ✅ Mac + OCI | ✅ Mac + OCI |
| sin-team-orchestrator | ❌ 404 | ❌ 404 | ✅ Mac + OCI | ✅ Mac + OCI |
| sin-team-social | ❌ 404 | ❌ 404 | ✅ Mac + OCI | ✅ Mac + OCI |
| sin-tiktok | ❌ 404 | ❌ 404 | ✅ Mac + OCI | ✅ Mac + OCI |
| sin-tiktok-shop | ❌ 404 | ❌ 404 | ✅ Mac + OCI | ✅ Mac + OCI |

## 🔗 Verknüpfte Dokumentation

- [HF Space Keep-Alive](./hf-keepalive.md) – 3-fache Redundanz
- [HF Space Monitoring](./hf-space-monitoring.md) – Self-Healing System
- [HF Space Crisis](./hf-space-crisis.md) – Root Cause Analysis
- [Best Practices](./best-practices.md) – GOLDENE REGELN
