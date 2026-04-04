# Troubleshooting: Opencode Rate Limited

> **Component:** Opencode | **Severity:** High | **Status:** ✅ Active

## Problem Description

Opencode Rate Limited is occurring in the OpenSIN-AI ecosystem.

## Common Causes

1. **Configuration Issue:** Invalid or missing configuration
2. **Resource Exhaustion:** CPU, memory, or disk full
3. **Network Issue:** Connectivity problems or DNS failures
4. **Authentication Issue:** Expired or invalid credentials
5. **Version Mismatch:** Incompatible versions between components

## Diagnostic Steps

### Step 1: Verify the Issue
```bash
systemctl status opencode
docker ps | grep opencode
```

### Step 2: Check Logs
```bash
journalctl -u opencode -n 100 --no-pager
docker logs opencode --tail 100
```

### Step 3: Check Configuration
```bash
cat /etc/opencode/config.yaml
docker exec opencode cat /app/config.json
```

### Step 4: Check Resources
```bash
top -bn1 | grep opencode
docker stats opencode --no-stream
```

## Solutions

### Solution 1: Restart Component
```bash
systemctl restart opencode
# or
docker restart opencode
```

### Solution 2: Clear Cache
```bash
rm -rf /var/cache/opencode/*
docker exec opencode rm -rf /tmp/*
```

### Solution 3: Update Configuration
```bash
nano /etc/opencode/config.yaml
systemctl restart opencode
```

### Solution 4: Reinstall Component
```bash
apt remove opencode
apt install opencode
systemctl enable opencode
systemctl start opencode
```

## Verification

```bash
systemctl is-active opencode
curl -s http://localhost:5678/health
```

## Prevention

| Measure | Frequency |
|---------|-----------|
| Monitor component health | Continuous |
| Review logs | Daily |
| Update configuration | As needed |
| Test recovery | Monthly |

---

*Last updated: 2026-04-04 by SIN-Zeus*
