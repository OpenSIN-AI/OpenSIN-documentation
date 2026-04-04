# Agent Lifecycle Management

Manage agents from creation to retirement.

## Lifecycle Stages

```
Design → Develop → Test → Deploy → Monitor → Update → Retire
```

## Stage 1: Design

```python
# Define agent specification
spec = {
    "name": "customer-support",
    "purpose": "Handle customer support tickets",
    "capabilities": ["classification", "response", "escalation"],
    "model": "gpt-4",
    "tools": ["knowledge_base", "ticket_system", "email"],
    "constraints": {
        "max_tokens": 4000,
        "response_time": "< 5s",
        "accuracy": "> 90%"
    }
}
```

## Stage 2: Develop

```python
from opensin import Agent

agent = Agent(
    name=spec["name"],
    model=spec["model"],
    system_prompt=load_prompt("customer-support.md"),
    tools=spec["tools"],
    config=spec["constraints"]
)
```

## Stage 3: Test

```python
from opensin.testing import TestSuite

tests = TestSuite(agent)
await tests.run_golden_dataset()
await tests.run_load_test()
await tests.run_security_audit()
```

## Stage 4: Deploy

```bash
opensin agent deploy customer-support \
  --environment production \
  --replicas 3 \
  --health-check /health
```

## Stage 5: Monitor

```python
from opensin import AgentMonitor

monitor = AgentMonitor(agent)
monitor.track_metrics([
    "latency",
    "error_rate",
    "cost",
    "user_satisfaction",
    "accuracy"
])
```

## Stage 6: Update

```bash
# Rolling update
opensin agent update customer-support \
  --model gpt-4-turbo \
  --strategy rolling \
  --canary 10
```

## Stage 7: Retire

```bash
# Graceful shutdown
opensin agent retire customer-support \
  --drain-time 300 \
  --redirect-to new-agent
```

## Best Practices

1. **Version agents** — Track agent versions
2. **Canary deployments** — Test with small traffic first
3. **Automated rollback** — Rollback on health check failures
4. **Monitor everything** — Track all key metrics
5. **Document changes** — Keep changelog for each agent

## Next Steps

- [Deployment Automation](/guide/deployment-automation)
- [Testing Guide](/guide/testing-guide)
