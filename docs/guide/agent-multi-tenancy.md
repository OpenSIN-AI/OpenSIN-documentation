# Agent Multi-Tenancy

Run agents for multiple tenants securely.

## Architecture

```
┌─────────────────────────────────────────┐
│          Multi-Tenant Gateway           │
├─────────────────────────────────────────┤
│  Tenant A    │  Tenant B    │  Tenant C │
│  ┌────────┐  │  ┌────────┐  │  ┌──────┐ │
│  │Agent A1│  │  │Agent B1│  │  │Agent │ │
│  │Agent A2│  │  │Agent B2│  │  │C1    │ │
│  └────────┘  │  └────────┘  │  └──────┘ │
├─────────────────────────────────────────┤
│          Shared Infrastructure          │
└─────────────────────────────────────────┘
```

## Tenant Isolation

### Data Isolation

```python
from opensin.tenancy import TenantIsolator

isolator = TenantIsolator(
    strategy="schema",  # or "database", "row-level"
    tenant_id_header="X-Tenant-ID"
)

# All data is automatically scoped
data = await isolator.query(tenant_id, query)
```

### Resource Isolation

```python
from opensin.tenancy import ResourceManager

resources = ResourceManager(
    limits={
        "tenant_a": {"max_agents": 10, "max_tokens": 100000},
        "tenant_b": {"max_agents": 5, "max_tokens": 50000},
        "tenant_c": {"max_agents": 20, "max_tokens": 200000}
    }
)
```

## Tenant Configuration

```yaml
# tenants.yml
tenants:
  tenant_a:
    name: "Acme Corp"
    plan: "enterprise"
    agents:
      - researcher
      - writer
      - reviewer
    limits:
      max_agents: 10
      max_tokens_per_day: 100000
      max_requests_per_minute: 60
    billing:
      rate_per_request: 0.01
      rate_per_token: 0.00001
      
  tenant_b:
    name: "Startup Inc"
    plan: "pro"
    agents:
      - researcher
      - writer
    limits:
      max_agents: 5
      max_tokens_per_day: 50000
      max_requests_per_minute: 30
```

## Tenant Management

```python
from opensin.tenancy import TenantManager

manager = TenantManager()

# Create tenant
await manager.create_tenant("tenant_a", config=tenant_config)

# Update tenant
await manager.update_tenant("tenant_a", limits={"max_agents": 15})

# Delete tenant
await manager.delete_tenant("tenant_a")

# List tenants
tenants = await manager.list_tenants()
```

## Billing

```python
from opensin.tenancy import BillingManager

billing = BillingManager(
    rate_per_request=0.01,
    rate_per_token=0.00001,
    billing_cycle="monthly"
)

# Generate invoice
invoice = await billing.generate_invoice("tenant_a", period="2026-04")
```

## Best Practices

1. **Isolate data** — Never mix tenant data
2. **Enforce limits** — Prevent resource abuse
3. **Monitor per-tenant** — Track metrics per tenant
4. **Bill accurately** — Track usage precisely
5. **Scale independently** — Scale tenants independently

## Next Steps

- [Agent Scaling](/guide/agent-scaling)
- [Security Hardening](/guide/security-hardening)
