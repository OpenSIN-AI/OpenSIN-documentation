# OpenSIN-AI Issue Watcher + Auto-Delegation

> **Source:** `n8n-workflows/issue-watcher-auto-delegation.json` | **Nodes:** 6

## Overview

GitHub Issues überwachen und automatisch an A2A Agents delegieren.

## Workflow Structure

| Setting | Value |
|---------|-------|
| **Name** | OpenSIN-AI Issue Watcher + Auto-Delegation |
| **Nodes** | 6 |
| **Node Types** | n8n-nodes-base.github, n8n-nodes-base.scheduleTrigger, n8n-nodes-base.code |
| **Active** | ✅ Yes |

## Nodes

### Every 10 Minutes

- **Type:** n8n-nodes-base.scheduleTrigger
- **Version:** 1.2
- **Position:** [250, 300]

### Get All OpenSIN-AI Repos

- **Type:** n8n-nodes-base.code
- **Version:** 2
- **Position:** [500, 300]

### Fetch Open Issues Per Repo

- **Type:** n8n-nodes-base.github
- **Version:** 1
- **Position:** [750, 300]

### Route Issues To Agents

- **Type:** n8n-nodes-base.code
- **Version:** 2
- **Position:** [1000, 300]

### Add Comment: Agent Assigned

- **Type:** n8n-nodes-base.github
- **Version:** 1
- **Position:** [1250, 300]

### Add Labels

- **Type:** n8n-nodes-base.github
- **Version:** 1
- **Position:** [1500, 300]


---

*Last updated: 2026-04-04 by SIN-Zeus*
