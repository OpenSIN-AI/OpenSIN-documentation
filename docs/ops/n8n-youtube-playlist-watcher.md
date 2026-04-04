# YouTube Playlist → GitHub Issues Watcher

> **Source:** `n8n-workflows/youtube-playlist-watcher.json` | **Nodes:** 5

## Overview

YouTube Playlist überwachen und neue Videos als GitHub Issues erstellen.

## Workflow Structure

| Setting | Value |
|---------|-------|
| **Name** | YouTube Playlist → GitHub Issues Watcher |
| **Nodes** | 5 |
| **Node Types** | n8n-nodes-base.github, n8n-nodes-base.httpRequest, n8n-nodes-base.scheduleTrigger, n8n-nodes-base.code |
| **Active** | ✅ Yes |

## Nodes

### Schedule Trigger

- **Type:** n8n-nodes-base.scheduleTrigger
- **Version:** 1.2
- **Position:** [250, 300]

### Fetch YouTube Playlist

- **Type:** n8n-nodes-base.httpRequest
- **Version:** 4.2
- **Position:** [500, 300]

### Filter New Videos

- **Type:** n8n-nodes-base.code
- **Version:** 2
- **Position:** [750, 300]

### Analyze & Route

- **Type:** n8n-nodes-base.code
- **Version:** 2
- **Position:** [1000, 300]

### Create GitHub Issue

- **Type:** n8n-nodes-base.github
- **Version:** 1
- **Position:** [1250, 300]


---

*Last updated: 2026-04-04 by SIN-Zeus*
