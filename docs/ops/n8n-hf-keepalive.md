# Hugging Face Keep-Alive Pinger

> **Source:** `n8n-workflows/hf-keepalive.json` | **Nodes:** 3

## Overview

HF Spaces wachhalten durch periodische Pings (alle 6h).

## Workflow Structure

| Setting | Value |
|---------|-------|
| **Name** | Hugging Face Keep-Alive Pinger |
| **Nodes** | 3 |
| **Node Types** | n8n-nodes-base.set, n8n-nodes-base.httpRequest, n8n-nodes-base.scheduleTrigger |
| **Active** | ✅ Yes |

## Nodes

### Every 6 Hours

- **Type:** n8n-nodes-base.scheduleTrigger
- **Version:** 1.2
- **Position:** [100, 300]

### Ping HF Space

- **Type:** n8n-nodes-base.httpRequest
- **Version:** 4.2
- **Position:** [500, 300]

### Agent List

- **Type:** n8n-nodes-base.set
- **Version:** 3.4
- **Position:** [300, 300]


---

*Last updated: 2026-04-04 by SIN-Zeus*
