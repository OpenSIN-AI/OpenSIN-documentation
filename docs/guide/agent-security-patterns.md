# Agent Security Patterns

Secure design patterns for production AI agents.

## Pattern 1: Input Validation Gate

```python
from opensin.security import InputValidator

validator = InputValidator(
    max_length=4000,
    block_patterns=["<script>", "DROP TABLE", "eval(", "rm -rf"],
    sanitize_html=True,
    validate_encoding=True
)

async def handle_input(raw_input):
    validated = await validator.validate(raw_input)
    if not validated.is_valid:
        raise SecurityError(validated.violations)
    return validated.data
```

## Pattern 2: Output Sanitization

```python
from opensin.security import OutputSanitizer

sanitizer = OutputSanitizer(
    redact_pii=True,
    block_secrets=True,
    validate_json=True,
    max_length=8000
)

async def handle_output(raw_output):
    sanitized = await sanitizer.sanitize(raw_output)
    return sanitized
```

## Pattern 3: Tool Permission Scoping

```python
from opensin.security import ToolPermissions

permissions = ToolPermissions(
    rules={
        "Bash": {"allow": ["git *", "ls *", "cat *"], "deny": ["rm *", "sudo *"]},
        "FileRead": {"allow": ["**/*.py", "**/*.md"], "deny": ["**/.env*", "**/secrets*"]},
        "FileWrite": {"allow": ["./output/**"], "deny": ["/**"]}
    }
)

agent.set_permissions(permissions)
```

## Pattern 4: Prompt Injection Defense

```python
from opensin.security import PromptShield

shield = PromptShield(
    detection_mode="strict",
    block_injection=True,
    sanitize_user_input=True,
    separate_system_context=True
)

async def process_message(system_prompt, user_message):
    if shield.detect_injection(user_message):
        return "Your request has been blocked for security reasons."
    
    safe_message = shield.sanitize(user_message)
    return await agent.generate(system_prompt, safe_message)
```

## Pattern 5: Rate Limiting & Throttling

```python
from opensin.security import RateLimiter

limiter = RateLimiter(
    requests_per_minute=60,
    requests_per_hour=1000,
    tokens_per_day=100000,
    cost_per_day=50.00
)

@limiter.limit
async def handle_request(request):
    return await agent.process(request)
```

## Pattern 6: Audit Trail

```python
from opensin.security import AuditLogger

audit = AuditLogger(
    storage="database",
    retention_days=90,
    log_events=["request", "response", "tool_use", "error"]
)

async def process_request(request):
    audit.log("request", {
        "agent": agent.name,
        "input_length": len(request),
        "timestamp": datetime.utcnow()
    })
    
    response = await agent.process(request)
    
    audit.log("response", {
        "agent": agent.name,
        "output_length": len(response),
        "tokens_used": response.tokens,
        "cost": response.cost
    })
    
    return response
```

## Security Checklist

- [ ] Input validation on all user inputs
- [ ] Output sanitization on all agent outputs
- [ ] Tool permissions follow least-privilege
- [ ] Prompt injection protection enabled
- [ ] Rate limiting configured
- [ ] Audit logging enabled
- [ ] Secrets never logged
- [ ] Regular security reviews

## Next Steps

- [Security Hardening](/guide/security-hardening)
- [Security Audit Checklist](/guide/security-audit-checklist)
