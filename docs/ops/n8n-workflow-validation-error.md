# N8N Workflow Validation Error — Troubleshooting Guide

> **Category:** Troubleshooting | **Severity:** High | **Version:** 1.0 | **Status:** Active

## Symptoms

- N8N Workflow Validation Error errors in logs
- Service degradation or outage
- Alert notifications triggered
- User reports of issues

## Impact

| Aspect | Impact Level | Description |
|--------|-------------|-------------|
| Availability | High | Service may be partially or fully unavailable |
| Performance | High | Response times may be significantly degraded |
| Data | Medium | Potential data inconsistency or loss |
| Users | High | Users may be unable to perform operations |

## Root Causes

1. **Configuration Issue:** Invalid or missing configuration settings
2. **Resource Exhaustion:** CPU, memory, disk, or network limits reached
3. **Network Issue:** Connectivity problems, DNS failures, or firewall blocks
4. **Authentication Issue:** Expired or invalid credentials
5. **Dependency Issue:** Downstream service failure or version mismatch

## Diagnostic Steps

### Step 1: Verify the Issue
```bash
# Check service status
systemctl status n8n
docker ps | grep n8n

# Check recent logs
journalctl -u n8n -n 100 --no-pager
docker logs n8n --tail 100
```

### Step 2: Check Resources
```bash
# Check CPU and memory
top -bn1 | head -20
free -h

# Check disk space
df -h

# Check network
ping -c 3 n8n.local
```

### Step 3: Check Configuration
```bash
# Verify configuration
cat /etc/n8n/config.yaml
docker exec n8n cat /app/config.json
```

### Step 4: Check Dependencies
```bash
# Check dependent services
systemctl status dependent-service
curl -s http://localhost:port/health
```

## Resolution

### Solution 1: Restart Service
```bash
systemctl restart n8n
# or
docker restart n8n
```

### Solution 2: Clear Cache
```bash
rm -rf /var/cache/n8n/*
docker exec n8n rm -rf /tmp/*
```

### Solution 3: Update Configuration
```bash
# Edit configuration
nano /etc/n8n/config.yaml
# Restart to apply changes
systemctl restart n8n
```

### Solution 4: Scale Resources
```bash
# Increase resource limits
docker update --memory=4g n8n
docker update --cpus=2 n8n
```

### Solution 5: Rollback
```bash
# Rollback to previous version
docker stop n8n
docker rm n8n
docker run -d --name n8n previous-image
```

## Prevention

| Measure | Frequency | Owner |
|---------|-----------|-------|
| Monitor resource usage | Continuous | Ops Team |
| Review logs | Daily | Ops Team |
| Update dependencies | Weekly | Dev Team |
| Test recovery | Monthly | Ops Team |
| Review configuration | Quarterly | Architecture Team |

## Escalation Path

| Level | Contact | Response Time |
|-------|---------|---------------|
| L1 | On-call Engineer | 5 minutes |
| L2 | Team Lead | 15 minutes |
| L3 | SIN-Zeus | 30 minutes |
| L4 | Management | 1 hour |

## Related Guides

- [Troubleshooting Overview](./troubleshooting-overview.md)
- [Incident Response](../incident-response/incident-response-overview.md)
- [Monitoring](../../guide/monitoring/monitoring-overview.md)

---

*Last updated: 2026-04-04 by SIN-Zeus*
