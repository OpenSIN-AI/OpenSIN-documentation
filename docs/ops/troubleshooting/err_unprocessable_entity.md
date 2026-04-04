# ERR_UNPROCESSABLE_ENTITY: Unprocessable Entity

> **Severity:** High | **Category:** Error Code

## Description

Error `ERR_UNPROCESSABLE_ENTITY` indicates that unprocessable entity has occurred.

## Symptoms

- Operation fails with `ERR_UNPROCESSABLE_ENTITY` status
- Logs show "Error: ERR_UNPROCESSABLE_ENTITY"
- Service becomes unresponsive

## Causes

1. Configuration mismatch
2. Network connectivity issues
3. Resource exhaustion
4. Authentication failure

## Resolution

### Step 1: Check Logs
```bash
tail -f /var/log/opensin/error.log | grep ERR_UNPROCESSABLE_ENTITY
```

### Step 2: Verify Configuration
Check `config.json` for valid settings.

### Step 3: Restart Service
```bash
systemctl restart opensin-agent
```

### Step 4: Contact Support
If issue persists, contact the Ops team.

---

*Last updated: 2026-04-04 by SIN-Zeus*
