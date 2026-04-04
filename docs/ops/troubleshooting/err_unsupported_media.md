# ERR_UNSUPPORTED_MEDIA: Unsupported Media

> **Severity:** High | **Category:** Error Code

## Description

Error `ERR_UNSUPPORTED_MEDIA` indicates that unsupported media has occurred.

## Symptoms

- Operation fails with `ERR_UNSUPPORTED_MEDIA` status
- Logs show "Error: ERR_UNSUPPORTED_MEDIA"
- Service becomes unresponsive

## Causes

1. Configuration mismatch
2. Network connectivity issues
3. Resource exhaustion
4. Authentication failure

## Resolution

### Step 1: Check Logs
```bash
tail -f /var/log/opensin/error.log | grep ERR_UNSUPPORTED_MEDIA
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
