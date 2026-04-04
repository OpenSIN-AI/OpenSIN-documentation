# Security Hardening Guide

Comprehensive security guide for production OpenSIN deployments.

## Overview

Security is critical when deploying AI agents that handle sensitive data and interact with external systems. This guide covers all aspects of securing your OpenSIN deployment.

## Authentication

### API Key Management

Never hardcode API keys. Use environment variables or a secrets manager:

```python
# BAD - hardcoded keys
api_key = "sk-1234567890abcdef"

# GOOD - environment variables
import os
api_key = os.environ.get("OPENAI_API_KEY")

# BETTER - secrets manager
from opensin.security import SecretsManager
secrets = SecretsManager()
api_key = secrets.get("openai/api-key")
```

### Token Rotation

Implement automatic token rotation:

```python
from opensin.security import TokenRotator

rotator = TokenRotator(
    keys=["key1", "key2", "key3"],
    rotation_interval=3600,
    strategy="round-robin"
)

api_key = rotator.get_current_key()
```

## Network Security

### TLS/SSL

Always use encrypted connections:

```python
agent = Agent(
    name="secure-agent",
    tls_enabled=True,
    tls_cert="/path/to/cert.pem",
    tls_key="/path/to/key.pem"
)
```

### Rate Limiting

Protect against abuse:

```python
from opensin.security import RateLimiter

limiter = RateLimiter(
    requests_per_minute=60,
    requests_per_hour=1000,
    burst_limit=10
)
```

## Data Protection

### Encryption at Rest

```python
from opensin.security import Encryption

encryption = Encryption(algorithm="AES-256-GCM", key=encryption_key)
encrypted = encryption.encrypt(sensitive_data)
decrypted = encryption.decrypt(encrypted)
```

### PII Handling

```python
from opensin.security import PIIRedactor

redactor = PIIRedactor(
    patterns=["email", "phone", "ssn", "credit_card"],
    replacement="[REDACTED]"
)

safe_message = redactor.redact(user_message)
```

## Agent Security

### Input Validation

```python
from opensin.security import InputValidator

validator = InputValidator(
    max_length=4000,
    allowed_types=["text", "json"],
    block_patterns=["<script>", "DROP TABLE", "eval("]
)
```

### Prompt Injection Protection

```python
from opensin.security import PromptGuard

guard = PromptGuard(
    detection_mode="strict",
    block_injection=True,
    sanitize_input=True
)

if guard.detect_injection(message):
    return "Input rejected for security reasons."
```

## Monitoring & Auditing

### Security Logging

```python
from opensin.security import SecurityLogger

logger = SecurityLogger(
    log_level="INFO",
    log_file="/var/log/opensin/security.log",
    include=["auth", "access", "injection", "rate_limit"]
)
```

### Audit Trail

```python
from opensin.security import AuditTrail

audit = AuditTrail(
    storage="database",
    retention_days=90,
    immutable=True
)
```

## Security Checklist

### Pre-Deployment

- [ ] All API keys rotated
- [ ] TLS/SSL enabled
- [ ] Rate limiting configured
- [ ] Input validation enabled
- [ ] Prompt injection protection active
- [ ] Security logging configured
- [ ] Audit trail enabled
- [ ] PII redaction active
- [ ] Firewall rules applied
- [ ] MFA enabled for admin

### Post-Deployment

- [ ] Monitor security logs
- [ ] Review access patterns
- [ ] Test incident response
- [ ] Update dependencies
- [ ] Rotate keys on schedule
- [ ] Review audit trail
- [ ] Check anomaly alerts

## Incident Response

1. **Contain** - Isolate affected systems
2. **Assess** - Determine scope and impact
3. **Remediate** - Fix the vulnerability
4. **Recover** - Restore normal operations
5. **Review** - Learn and improve

## Next Steps

- [Security Architecture](/architecture/security)
- [Best Practices](/best-practices/security)
- [Governance](/governance/SECURITY)
