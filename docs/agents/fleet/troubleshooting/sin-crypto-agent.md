# Sin Crypto Agent — Troubleshooting Guide

> **Agent:** sin-crypto-agent | **Category:** Troubleshooting

## Common Issues

### Issue 1: Agent Not Responding

**Symptoms:**
- Agent doesn't respond to commands
- Status shows "offline"

**Resolution:**
1. Check agent status: `sin-n8n get sin-crypto-agent`
2. Restart agent: `opencode run --agent "sin-crypto-agent" "ping"`
3. Check logs: `tail -f /var/log/opensin/sin-crypto-agent.log`

### Issue 2: High Error Rate

**Symptoms:**
- Error rate > 5%
- Frequent task failures

**Resolution:**
1. Check model availability
2. Verify API credentials
3. Reduce maxSteps if timing out

### Issue 3: Slow Response Times

**Symptoms:**
- Response time > 30s
- Tasks taking longer than expected

**Resolution:**
1. Check network latency
2. Verify model endpoint
3. Consider using fallback model

## Error Codes

| Code | Description | Resolution |
|------|-------------|------------|
| AGENT_OFFLINE | Agent is not responding | Restart agent |
| MODEL_UNAVAILABLE | LLM model is down | Switch to fallback |
| RATE_LIMITED | API rate limit exceeded | Wait and retry |
| TIMEOUT | Request timed out | Increase timeout |

## Contact Support

If issues persist, contact the Ops team via Telegram.

---

*Last updated: 2026-04-04 by SIN-Zeus*
