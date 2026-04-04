# n8n Workflow Example

> **Category:** Automation | **Difficulty:** Beginner

## Overview

Example n8n workflow that monitors GitHub issues and sends Telegram notifications.

## Workflow JSON

```json
{
  "name": "Issue Monitor",
  "nodes": [
    {
      "name": "Schedule",
      "type": "n8n-nodes-base.scheduleTrigger",
      "parameters": {"rule": {"interval": [{"field": "minutes", "minutesInterval": 15}]}}
    },
    {
      "name": "Get Issues",
      "type": "n8n-nodes-base.github",
      "parameters": {"resource": "issue", "operation": "getAll"}
    },
    {
      "name": "Notify",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {"method": "POST", "url": "https://api.telegram.org/bot..."}
    }
  ]
}
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
