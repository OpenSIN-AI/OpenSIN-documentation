# Runbook: N8N Node Crash

> **Priority:** P1 | **Service:** N8N | **Status:** ✅ Active

## Symptoms

- Service becomes unresponsive
- Error logs show related failures
- Monitoring alerts triggered
- Users report issues

## Impact

| Aspect | Impact |
|--------|--------|
| **Availability** | Service degraded or down |
| **Data** | Potential data loss or corruption |
| **Users** | Unable to perform operations |
| **Downstream** | Dependent services affected |

## Diagnosis

### Step 1: Check Service Status
```bash
docker ps | grep n8n
systemctl status n8n
```

### Step 2: Check Logs
```bash
docker logs n8n --tail 100
journalctl -u n8n -n 100
```

### Step 3: Check Resources
```bash
top -bn1 | head -20
free -h
df -h
```

### Step 4: Check Connectivity
```bash
curl -s http://localhost:5678/health
ping -c 3 n8n.local
```

## Resolution

### Immediate Actions
1. **Restart the service:** `systemctl restart n8n`
2. **Clear cache:** `rm -rf /var/cache/n8n/*`
3. **Check dependencies:** Verify all dependent services are running

### If Issue Persists
1. **Check disk space:** `df -h`
2. **Check memory:** `free -h`
3. **Check logs for errors:** `grep -i error /var/log/n8n.log`
4. **Restart dependent services**

### Escalation
If issue cannot be resolved within 30 minutes:
1. Notify team via Telegram
2. Create GitHub issue with logs
3. Escalate to on-call engineer

## Prevention

| Measure | Frequency | Owner |
|---------|-----------|-------|
| Monitor resource usage | Continuous | Ops Team |
| Review logs | Daily | Ops Team |
| Update dependencies | Weekly | Dev Team |
| Test recovery | Monthly | Ops Team |

---

*Last updated: 2026-04-04 by SIN-Zeus*
