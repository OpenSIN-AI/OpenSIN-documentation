# Global Fleet Self-Healing Protocol

> **Source:** `n8n-workflows/fleet-self-healing.json` | **Nodes:** 4

## Overview

Automatisches Self-Healing der A2A Flotte bei Fehlern und Incidents.

## Workflow Structure

| Setting | Value |
|---------|-------|
| **Name** | Global Fleet Self-Healing Protocol |
| **Nodes** | 4 |
| **Node Types** | n8n-nodes-base.webhook, n8n-nodes-base.supabase, n8n-nodes-base.httpRequest |
| **Active** | ✅ Yes |

## Nodes

### Webhook - Error Receiver

- **Type:** n8n-nodes-base.webhook
- **Version:** ?
- **Position:** [100, 300]

### Publish Error Logs to Gist

- **Type:** n8n-nodes-base.httpRequest
- **Version:** ?
- **Position:** [300, 300]

### Create Issue via SIN-GitHub-Issues

- **Type:** n8n-nodes-base.httpRequest
- **Version:** ?
- **Position:** [500, 300]

### Insert into Hermes Dispatch Pool

- **Type:** n8n-nodes-base.supabase
- **Version:** ?
- **Position:** [700, 300]


---

*Last updated: 2026-04-04 by SIN-Zeus*
