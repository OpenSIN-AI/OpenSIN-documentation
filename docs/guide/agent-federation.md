# Agent Federation

Connect agents across organizations and platforms.

## Federation Architecture

```
Organization A                    Federation Hub                    Organization B
┌─────────────┐                  ┌─────────────┐                  ┌─────────────┐
│  Agent A1   │◄────────────────►│   Router    │◄────────────────►│  Agent B1   │
│  Agent A2   │◄────────────────►│  Registry   │◄────────────────►│  Agent B2   │
│  Agent A3   │◄────────────────►│  Gateway    │◄────────────────►│  Agent B3   │
└─────────────┘                  └─────────────┘                  └─────────────┘
```

## Setting Up Federation

### 1. Register Agent

```python
from opensin.federation import FederationRegistry

registry = FederationRegistry(
    hub_url="https://federation.opensin.ai",
    auth_token="your-token"
)

# Register agent
await registry.register(agent, metadata={
    "organization": "Acme Corp",
    "capabilities": ["research", "analysis"],
    "availability": "24/7",
    "rate_limit": 100
})
```

### 2. Discover Agents

```python
# Search federation
agents = await registry.search(
    capability="research",
    organization="*",
    availability="24/7"
)

# Get agent details
agent = await registry.get("researcher@acme-corp")
```

### 3. Send Cross-Organization Messages

```python
from opensin.federation import FederationClient

client = FederationClient(
    hub_url="https://federation.opensin.ai",
    auth_token="your-token"
)

# Send message to external agent
response = await client.send(
    to="researcher@acme-corp",
    message="Research AI trends for 2026"
)
```

## Federation Security

### Authentication

```python
# OAuth2 authentication
from opensin.federation import OAuth2Auth

auth = OAuth2Auth(
    client_id="your-client-id",
    client_secret="your-client-secret",
    token_url="https://federation.opensin.ai/oauth/token"
)
```

### Authorization

```python
# Define access policies
policies = {
    "allow": [
        {"organization": "partner-org", "capability": "research"},
        {"organization": "trusted-org", "capability": "analysis"},
    ],
    "deny": [
        {"organization": "blocked-org"},
    ]
}
```

## Federation Governance

### SLA Management

```python
from opensin.federation import SLAManager

sla = SLAManager(
    response_time=5000,  # 5 seconds
    availability=0.999,  # 99.9%
    accuracy=0.95,       # 95%
    cost_per_request=0.05
)

# Monitor SLA compliance
compliance = await sla.check_compliance(agent)
print(f"SLA compliance: {compliance.score}%")
```

### Billing

```python
from opensin.federation import BillingManager

billing = BillingManager(
    rate_per_request=0.05,
    rate_per_token=0.00001,
    billing_cycle="monthly"
)

# Generate invoice
invoice = await billing.generate_invoice(agent, period="2026-04")
```

## Best Practices

1. **Define clear SLAs** — Set expectations upfront
2. **Monitor compliance** — Track performance continuously
3. **Secure communication** — Use encrypted channels
4. **Handle failures** — Graceful degradation
5. **Audit regularly** — Review federation activity

## Next Steps

- [Agent Registry](/guide/agent-registry)
- [A2A Protocol](/guide/a2a-protocol)
