# SIN-Fleet Incident Watcher (Telegram -> Hermes)

> **Source:** `n8n-workflows/telegram-incident-watcher.json` | **Nodes:** 3

## Overview

Incident-Weiterleitung von Telegram an Hermes Dispatcher.

## Workflow Structure

| Setting | Value |
|---------|-------|
| **Name** | SIN-Fleet Incident Watcher (Telegram -> Hermes) |
| **Nodes** | 3 |
| **Node Types** | n8n-nodes-base.webhook, n8n-nodes-base.github, n8n-nodes-base.supabase |
| **Active** | ✅ Yes |

## Nodes

### Webhook

- **Type:** n8n-nodes-base.webhook
- **Version:** 1
- **Position:** [250, 300]

### Create GitHub Issue

- **Type:** n8n-nodes-base.github
- **Version:** 1
- **Position:** [450, 300]

### Insert into Supabase (Hermes Pool)

- **Type:** n8n-nodes-base.supabase
- **Version:** 1
- **Position:** [650, 300]


---

*Last updated: 2026-04-04 by SIN-Zeus*
