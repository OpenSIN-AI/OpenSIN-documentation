# Sin Docs Agent — Troubleshooting Guide

> **Agent:** sin-docs-agent | **Category:** Troubleshooting | **Status:** ✅ Active

## Common Issues

### Issue 1: Agent Not Responding

**Symptoms:**
- Agent doesn't respond to commands
- Status shows "offline" in dashboard
- No recent activity in logs

**Resolution:**
1. Check agent status: `sin-n8n get sin-docs-agent`
2. Restart agent: `opencode run --agent "sin-docs-agent" "ping"`
3. Check logs: `tail -f /var/log/opensin/sin-docs-agent.log`
4. Verify model availability: `opencode run --model openrouter/qwen/qwen3.6-plus:free "test"`

### Issue 2: High Error Rate

**Symptoms:**
- Error rate > 5%
- Frequent task failures
- Multiple retries exhausted

**Resolution:**
1. Check model availability and rate limits
2. Verify API credentials are valid
3. Reduce maxSteps if timing out
4. Switch to fallback model if primary is down

### Issue 3: Slow Response Times

**Symptoms:**
- Response time > 30s
- Tasks taking longer than expected
- Queue backlog growing

**Resolution:**
1. Check network latency to model endpoint
2. Verify model endpoint is responsive
3. Consider using fallback model for faster response
4. Check for resource contention on host

### Issue 4: Token Pool Exhaustion

**Symptoms:**
- "Token pool empty" errors
- Agent unable to make LLM calls
- Fallback model also unavailable

**Resolution:**
1. Check token pool status: `curl http://92.5.60.87:5678/api/v1/tokens/pool-status`
2. Trigger token rotation: `curl -X POST http://92.5.60.87:5678/api/v1/tokens/rotate`
3. Wait for new tokens to be provisioned
4. Escalate to Ops team if pool remains empty

## Error Codes

| Code | Description | Resolution |
|------|-------------|------------|
| AGENT_OFFLINE | Agent is not responding | Restart agent service |
| MODEL_UNAVAILABLE | LLM model is down | Switch to fallback model |
| RATE_LIMITED | API rate limit exceeded | Wait and retry with backoff |
| TIMEOUT | Request timed out | Increase timeout or reduce complexity |
| TOKEN_EXPIRED | Authentication token expired | Rotate credentials |
| CONFIG_INVALID | Invalid configuration | Review and fix config file |
| MCP_FAILED | MCP call failed | Check MCP server status |
| OOM_KILLED | Out of memory | Reduce maxSteps or increase memory |

## Contact Support

If issues persist after following these guides:
1. Collect logs: `journalctl -u sin-docs-agent --no-pager > /tmp/sin-docs-agent-logs.txt`
2. Collect config: `cat /etc/opensin/sin-docs-agent/config.yaml > /tmp/sin-docs-agent-config.txt`
3. Create GitHub issue with attached logs
4. Notify Ops team via Telegram

---

*Last updated: 2026-04-04 by SIN-Zeus*
