# Inbound Intake — Operations Guide

## Overview

The **Inbound Intake** system normalizes all incoming work (GitHub webhooks, Telegram messages, scheduled polls) into a standard `work_item` schema before processing. This ensures every platform is treated uniformly regardless of its native format.

## Architecture

```
[External Platform] → [Webhook/Poller] → [Normalize] → [Create GitHub Issue] → [SIN-Hermes Dispatch]
```

## Prerequisites

- n8n running on OCI VM (`http://92.5.60.87:5678`)
- GitHub Personal Access Token with repo scope
- `inbound-intake` workflow activated in n8n

## Workflow: `inbound-intake`

### Trigger

Webhook POST to `http://92.5.60.87:5678/webhook/inbound-work`

### Body Schema

```json
{
  "source": "prolific|hackerone|upwork|telegram|github|pr-review",
  "type": "bug|enhancement|survey|research",
  "title": "Work item title",
  "description": "Detailed description",
  "priority": "low|medium|high|critical",
  "metadata": {}
}
```

### Steps

1. **Webhook** receives incoming payload
2. **Normalize Work Item** → transforms to canonical schema
3. **Create GitHub Issue** → opens issue in target repo with type label
4. **Log to Supabase** → records work item for tracking

## PR-Watcher: `watch-pr-feedback.sh`

Runs as a cron job every 5 minutes:

```bash
*/5 * * * * /Users/jeremy/dev/OpenSIN-documentation/scripts/watch-pr-feedback.sh
```

Monitors:

- New PRs in `OpenSIN-AI/*` org
- PR reviews and comments
- Issue updates

## File Locations

| File              | Path                                |
| ----------------- | ----------------------------------- |
| n8n workflow      | `n8n-workflows/inbound-intake.json` |
| Governance config | `governance/repo-governance.json`   |
| PR watcher script | `scripts/watch-pr-feedback.sh`      |
| Operations doc    | `docs/03_ops/inbound-intake.md`     |

## Troubleshooting

### n8n workflow not triggering

- Check workflow is **activated** in n8n
- Verify webhook URL is correct in platform config
- Check n8n logs: `http://92.5.60.87:5678/execution`

### GitHub issue not created

- Verify PAT has `repo` scope
- Check workflow execution in n8n
- Ensure `owner`/`repo` fields are set in workflow

### PR watcher not running

```bash
# Check cron status
crontab -l

# Manual run
bash /Users/jeremy/dev/OpenSIN-documentation/scripts/watch-pr-feedback.sh
```

## Activation

To activate for a new repo:

1. Copy `governance/repo-governance.json` to the repo's `governance/` directory
2. Import `n8n-workflows/inbound-intake.json` into n8n
3. Configure webhook URL in the source platform
4. Set up cron: `*/5 * * * * /path/to/watch-pr-feedback.sh`

## Agent

`assistant/api` (this session)
Generated: 2026-04-17
