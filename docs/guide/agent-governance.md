# Agent Governance

Manage agents responsibly across your organization.

## Governance Framework

### Agent Lifecycle Governance

| Stage | Requirements | Approval |
|-------|-------------|----------|
| Design | Spec document, risk assessment | Team lead |
| Development | Code review, security scan | Tech lead |
| Testing | Test suite, golden dataset | QA team |
| Deployment | Health checks, monitoring | Ops team |
| Production | SLA compliance, audit trail | CTO |
| Retirement | Data migration, deprecation plan | Product owner |

### Policy Management

```yaml
# agent-policies.yaml
policies:
  model_usage:
    allowed_models:
      - gpt-4
      - gpt-3.5-turbo
      - claude-sonnet
    restricted_models:
      - claude-opus  # Requires approval
    banned_models: []

  data_access:
    pii_handling: required
    data_retention: 90_days
    encryption: required

  cost_management:
    daily_budget: 100.00
    monthly_budget: 3000.00
    alert_thresholds: [0.5, 0.75, 0.9]

  security:
    prompt_injection_protection: required
    input_validation: required
    output_sanitization: required
    audit_logging: required
```

### Compliance Monitoring

```python
from opensin.governance import ComplianceMonitor

monitor = ComplianceMonitor(
    policies=policies,
    check_interval=300,  # 5 minutes
    alert_channels=["slack", "email"]
)

# Start monitoring
await monitor.start()

# Get compliance report
report = await monitor.get_report()
print(f"Compliance score: {report.score}%")
print(f"Violations: {report.violations}")
```

### Audit Trail

```python
from opensin.governance import AuditTrail

audit = AuditTrail(
    storage="immutable",
    retention_days=365,
    log_events=[
        "agent.created",
        "agent.deployed",
        "agent.updated",
        "agent.retired",
        "policy.violated",
        "budget.exceeded"
    ]
)

# Query audit trail
entries = await audit.query(
    event="agent.deployed",
    start_date="2026-01-01",
    end_date="2026-04-04"
)
```

### Role-Based Access

| Role | Permissions |
|------|------------|
| Admin | Full access to all agents |
| Developer | Create, update, test agents |
| Operator | Deploy, monitor, scale agents |
| Viewer | Read-only access |
| Auditor | Access to audit logs only |

## Best Practices

1. **Define policies upfront** — Before creating agents
2. **Enforce automatically** — Don't rely on manual checks
3. **Audit regularly** — Review compliance monthly
4. **Train team** — Everyone should understand governance
5. **Update policies** — Evolve with the organization

## Next Steps

- [Compliance Guide](/guide/compliance)
- [Security Audit](/guide/security-audit-checklist)
