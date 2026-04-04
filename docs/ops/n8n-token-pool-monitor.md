# Token Pool Monitor

> **Source:** `n8n-workflows/token-pool-monitor.json` | **Nodes:** 5

## Overview

Token Pool überwachen und bei Bedarf nachfüllen.

## Workflow Structure

| Setting | Value |
|---------|-------|
| **Name** | Token Pool Monitor |
| **Nodes** | 5 |
| **Node Types** | n8n-nodes-base.set, n8n-nodes-base.telegram, n8n-nodes-base.if, n8n-nodes-base.httpRequest, n8n-nodes-base.scheduleTrigger |
| **Active** | ✅ Yes |

## Nodes

### Every 30 Minutes

- **Type:** n8n-nodes-base.scheduleTrigger
- **Version:** 1.2
- **Position:** [220, 300]

### Check Token Pool

- **Type:** n8n-nodes-base.httpRequest
- **Version:** 4.2
- **Position:** [440, 300]

### Pool < 10?

- **Type:** n8n-nodes-base.if
- **Version:** 2
- **Position:** [660, 300]

### Telegram Alert

- **Type:** n8n-nodes-base.telegram
- **Version:** 1.2
- **Position:** [900, 200]

### Pool OK

- **Type:** n8n-nodes-base.set
- **Version:** 3.4
- **Position:** [900, 400]


---

*Last updated: 2026-04-04 by SIN-Zeus*
