# Team Creator — Team Playbook

> **Team:** Team Creator | **Category:** A2A Agent Teams | **Version:** 1.0 | **Status:** Active

## Team Overview

The Team Creator team is responsible for autonomous execution of tasks within their domain.

## Team Structure

| Role | Agents | Responsibilities |
|------|--------|------------------|
| Lead | Orchestrator | Task distribution, monitoring |
| Senior | 3-5 Agents | Complex task execution |
| Junior | 2-3 Agents | Routine task execution |
| Support | 1-2 Agents | Specialized support tasks |

## Communication Protocol

- **Internal:** A2A Protocol (direct agent-to-agent)
- **External:** n8n Workflows (async)
- **Alerts:** Telegram Bot (real-time)
- **Reports:** Daily summary via email/Telegram

## Escalation Path

| Level | Contact | Response Time |
|-------|---------|---------------|
| L1 | Team Lead Agent | Immediate |
| L2 | SIN-Zeus | 15 minutes |
| L3 | Ops Team | 30 minutes |
| L4 | Management | 1 hour |

## Performance Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Task Success Rate | > 95% | > 98% |
| Response Time | < 30s | < 15s |
| Error Rate | < 1% | < 0.1% |
| Uptime | > 99.9% | > 99.99% |

## SOPs

1. **Task Intake:** Receive task via n8n or A2A message
2. **Analysis:** Evaluate task complexity and requirements
3. **Assignment:** Assign to appropriate agent based on skills
4. **Execution:** Agent executes task with monitoring
5. **Verification:** Verify results against acceptance criteria
6. **Reporting:** Report results to orchestrator
7. **Archival:** Archive task and results for audit

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Agent offline | Restart agent, check model availability |
| Task timeout | Increase timeout, switch to fallback model |
| High error rate | Verify credentials, check rate limits |
| Communication failure | Check A2A protocol, n8n connectivity |

## Related Documents

- [Agent Reference Cards](../reference-cards/)
- [Integration Guides](../../integrations/agents/)
- [Team Configuration](../fleet/configs/)

---

*Last updated: 2026-04-04 by SIN-Zeus*
