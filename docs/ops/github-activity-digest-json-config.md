# Github Activity Digest — JSON Configuration

> **Workflow:** github-activity-digest | **Category:** n8n Workflow Config | **Status:** Active

## Workflow JSON

```json
{
  "name": "Github Activity Digest",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "hours",
              "hoursInterval": 2
            }
          ]
        }
      },
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.2,
      "position": [250, 300],
      "id": "schedule-trigger"
    },
    {
      "parameters": {
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "resource": "repository",
        "operation": "getAll",
        "owner": "OpenSIN-AI",
        "returnAll": true,
        "options": {}
      },
      "name": "List All Repos",
      "type": "n8n-nodes-base.github",
      "typeVersion": 1,
      "position": [500, 300],
      "id": "list-repos",
      "credentials": {
        "githubApi": {
          "id": "1",
          "name": "GitHub Account"
        }
      }
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.telegram.bot/{{ $env.TELEGRAM_BOT_TOKEN }}/sendMessage",
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={"chat_id": "{{ $env.TELEGRAM_CHAT_ID }}", "text": "📚 Github Activity Digest\nTime: {{ $now.format('yyyy-MM-dd HH:mm') }} "}",
        "options": {}
      },
      "name": "Report to Telegram",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [750, 300],
      "id": "report-telegram"
    }
  ],
  "connections": {
    "Schedule Trigger": {
      "main": [[{"node": "List All Repos", "type": "main", "index": 0}]]
    },
    "List All Repos": {
      "main": [[{"node": "Report to Telegram", "type": "main", "index": 0}]]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "active": true
}
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| TELEGRAM_BOT_TOKEN | Telegram bot token | Yes |
| TELEGRAM_CHAT_ID | Chat ID for notifications | Yes |
| GITHUB_API_KEY | GitHub API key | Yes |

## Import Instructions

1. Copy the JSON configuration above
2. Open n8n UI at http://92.5.60.87:5678
3. Click "Import from File"
4. Paste the JSON
5. Configure credentials
6. Activate the workflow

## Testing

1. Click "Execute Workflow" in n8n UI
2. Monitor execution steps
3. Verify Telegram notification received
4. Check execution logs for errors

---

*Last updated: 2026-04-04 by SIN-Zeus*
