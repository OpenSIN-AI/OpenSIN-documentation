# GitHub @opnsin-code Mention → Auto-Delegate

> **Source:** `n8n-workflows/github-mention-auto-delegation.json` | **Nodes:** 6

## Overview

Auto-Delegation bei GitHub @opnsin-code Mentions.

## Workflow Structure

| Setting | Value |
|---------|-------|
| **Name** | GitHub @opnsin-code Mention → Auto-Delegate |
| **Nodes** | 6 |
| **Node Types** | n8n-nodes-base.github, n8n-nodes-base.code, n8n-nodes-base.githubTrigger |
| **Active** | ✅ Yes |

## Nodes

### GitHub Webhook

- **Type:** n8n-nodes-base.githubTrigger
- **Version:** 1
- **Position:** [250, 300]

### Check @opnsin-code Mention

- **Type:** n8n-nodes-base.code
- **Version:** 2
- **Position:** [500, 300]

### Extract Tasks From Comment

- **Type:** n8n-nodes-base.code
- **Version:** 2
- **Position:** [750, 300]

### Route To SIN Agents

- **Type:** n8n-nodes-base.code
- **Version:** 2
- **Position:** [1000, 300]

### Reply With Delegation

- **Type:** n8n-nodes-base.github
- **Version:** 1
- **Position:** [1250, 300]

### Create Sub-Issue Per Agent

- **Type:** n8n-nodes-base.github
- **Version:** 1
- **Position:** [1500, 300]


---

*Last updated: 2026-04-04 by SIN-Zeus*
