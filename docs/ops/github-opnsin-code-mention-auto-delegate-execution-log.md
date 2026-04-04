# Github Opnsin Code Mention Auto Delegate — Execution Log Template

> **Workflow:** github-opnsin-code-mention-auto-delegate | **Category:** Execution Log | **Status:** Active

## Execution Log Format

Each execution of the github opnsin code mention auto delegate workflow generates a log entry with the following format:

```json
{
  "executionId": "unique-execution-id",
  "workflowId": "github-opnsin-code-mention-auto-delegate",
  "workflowName": "Github Opnsin Code Mention Auto Delegate",
  "startTime": "2026-04-04T10:00:00Z",
  "endTime": "2026-04-04T10:00:30Z",
  "duration": 30000,
  "status": "success",
  "nodes": {
    "Schedule Trigger": {
      "status": "success",
      "duration": 100,
      "output": {}
    },
    "List All Repos": {
      "status": "success",
      "duration": 5000,
      "output": {
        "repos": 156
      }
    },
    "Report to Telegram": {
      "status": "success",
      "duration": 2000,
      "output": {
        "messageId": 12345
      }
    }
  },
  "errors": [],
  "warnings": []
}
```

## Log Analysis

### Success Criteria
- All nodes executed successfully
- Duration within expected range (< 60s)
- No errors in execution log
- Telegram notification sent successfully

### Failure Criteria
- Any node failed execution
- Duration exceeded threshold (> 120s)
- Errors present in execution log
- Telegram notification failed

### Warning Criteria
- Duration approaching threshold (45-60s)
- Deprecated API calls detected
- Rate limit approaching
- Non-critical errors handled gracefully

## Retention Policy

| Log Type | Retention Period | Storage |
|----------|-----------------|---------|
| Execution Logs | 90 days | n8n database |
| Error Logs | 1 year | n8n database + S3 |
| Audit Logs | 7 years | S3 + Glacier |

## Alerting Rules

| Condition | Severity | Channel | Response Time |
|-----------|----------|---------|---------------|
| Execution failure | P1 | Telegram + GitHub | 5 minutes |
| Duration > 120s | P2 | Telegram | 15 minutes |
| Error rate > 5% | P1 | Telegram + GitHub | 5 minutes |
| Warning rate > 10% | P3 | Daily report | 24 hours |

---

*Last updated: 2026-04-04 by SIN-Zeus*
