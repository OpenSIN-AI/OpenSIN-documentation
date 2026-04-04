# Github Opnsin Code Mention Auto Delegate — Troubleshooting Guide

> **Workflow:** github-opnsin-code-mention-auto-delegate | **Category:** Troubleshooting | **Status:** Active

## Common Issues

### Issue 1: Workflow Not Executing

**Symptoms:**
- Workflow does not run on schedule
- No execution history in n8n UI
- No notifications received

**Resolution:**
1. Check workflow is active in n8n UI
2. Verify schedule configuration
3. Check n8n service is running
4. Review n8n logs

### Issue 2: API Authentication Failed

**Symptoms:**
- 401/403 errors in execution logs
- Workflow fails at API call node
- Authentication error notifications

**Resolution:**
1. Verify API credentials in n8n
2. Check credential has not expired
3. Update credentials in n8n UI
4. Test connection manually

### Issue 3: Rate Limit Exceeded

**Symptoms:**
- 429 errors in execution logs
- Workflow fails intermittently
- Rate limit notifications

**Resolution:**
1. Implement exponential backoff
2. Reduce execution frequency
3. Use batch processing
4. Contact API provider for higher limits

## Error Codes

| Code | Description | Resolution |
|------|-------------|------------|
| WF_NOT_ACTIVE | Workflow is not active | Activate in n8n UI |
| AUTH_FAILED | Authentication failed | Update credentials |
| RATE_LIMITED | Rate limit exceeded | Implement backoff |
| TIMEOUT | Request timed out | Increase timeout |
| DATA_ERROR | Invalid data received | Check data source |

---

*Last updated: 2026-04-04 by SIN-Zeus*
