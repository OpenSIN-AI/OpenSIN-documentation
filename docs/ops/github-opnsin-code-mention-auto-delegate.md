# Github Opnsin Code Mention Auto Delegate — Operational Runbook

> **Workflow:** github-opnsin-code-mention-auto-delegate | **Category:** n8n Operations | **Version:** 1.0 | **Status:** Active

## Purpose

This runbook provides step-by-step operational procedures for the github opnsin code mention auto delegate workflow.

## Workflow Overview

- **Trigger:** Schedule / Webhook
- **Frequency:** Configurable (Default: Every 2h)
- **Owner:** DevOps Team
- **Priority:** High

## Pre-Flight Checks

Before executing or modifying this workflow, verify:
- [ ] n8n instance is healthy (`curl http://92.5.60.87:5678/healthz`)
- [ ] GitHub credentials are valid
- [ ] Telegram bot is responsive
- [ ] Supabase connection is active

## Execution Procedure

### Step 1: Manual Trigger
1. Open n8n UI at http://92.5.60.87:5678
2. Navigate to Workflows > Github Opnsin Code Mention Auto Delegate
3. Click "Execute Workflow"
4. Monitor execution steps in real-time

### Step 2: Monitoring
- Check execution logs for errors
- Verify Telegram notification received
- Confirm data updates in target systems

### Step 3: Post-Execution Verification
- Check workflow success rate in dashboard
- Verify no orphaned processes
- Confirm resource usage is within limits

## Error Handling

| Error | Severity | Action |
|-------|----------|--------|
| API Rate Limit | Medium | Wait and retry (exponential backoff) |
| Authentication Failure | High | Rotate credentials immediately |
| Timeout | Medium | Increase timeout, check network |
| Data Validation Error | Low | Log and skip invalid items |

## Recovery Procedures

### Scenario 1: Workflow Stuck
1. Cancel the execution in n8n UI
2. Check for locked resources
3. Restart the workflow manually

### Scenario 2: Credential Expiry
1. Rotate the expired credential
2. Update n8n credential store
3. Re-run the failed execution

## Monitoring & Alerting

| Metric | Threshold | Alert Channel |
|--------|-----------|---------------|
| Error Rate | > 5% | Telegram + GitHub Issue |
| Execution Time | > 120s | Telegram |
| Success Rate | < 95% | Daily Report |

## Troubleshooting

| Symptom | Cause | Resolution |
|---------|-------|------------|
| No notifications | Telegram bot down | Restart bot service |
| Missing data | API change | Update workflow nodes |
| High latency | Network issue | Check OCI VM network |

## Related Documents

- [Workflow Config](../workflows/github-opnsin-code-mention-auto-delegate-json-config.md)
- [Execution Log](../workflows/github-opnsin-code-mention-auto-delegate-execution-log.md)
- [Optimization Guide](../workflow-optimization/error-handling-best-practices.md)

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-04 | SIN-Zeus | Initial release |

---

*Last updated: 2026-04-04 by SIN-Zeus*
