# Advanced Agent Testing

Comprehensive testing strategies for production AI agents.

## Testing Pyramid

```
         ┌─────────────┐
         │  E2E Tests  │  ← Full agent workflows
        ┌┴─────────────┴┐
       │ Integration Tests│  ← Agent + tools + memory
      ┌┴─────────────────┴┐
     │    Unit Tests       │  ← Individual components
    ┌┴─────────────────────┴┐
   │    Mock Tests          │  ← Isolated function tests
```

## Property-Based Testing

```python
from hypothesis import given, strategies as st

@given(st.text(min_size=1, max_size=1000))
@pytest.mark.asyncio
async def test_agent_handles_any_input(prompt):
    agent = Agent(name="test-agent")
    response = await agent.send(prompt)
    assert response is not None
    assert response.content is not None
```

## Regression Testing

```python
from opensin.testing import RegressionTest

# Save baseline
baseline = RegressionTest(agent, test_prompts)
baseline.save("baseline.json")

# Test against baseline
current = RegressionTest(agent, test_prompts)
diff = current.compare("baseline.json")

if diff.has_regressions:
    print(f"Regressions found: {diff.regressions}")
```

## Chaos Testing

```python
from opensin.testing import ChaosTest

chaos = ChaosTest(
    agent=agent,
    failures=[
        "api_timeout",
        "api_error",
        "rate_limit",
        "network_partition"
    ],
    iterations=100
)

results = await chaos.run()
print(f"Resilience score: {results.resilience_score}/100")
```

## Security Testing

```python
from opensin.testing import SecurityTest

security = SecurityTest(
    agent=agent,
    attacks=[
        "prompt_injection",
        "data_exfiltration",
        "jailbreak",
        "toxic_output"
    ],
    iterations=50
)

results = await security.run()
print(f"Vulnerabilities: {results.vulnerabilities}")
```

## Load Testing

```python
from opensin.testing import LoadTest

load_test = LoadTest(
    agent=agent,
    concurrent_users=50,
    requests_per_user=20,
    ramp_up_seconds=60
)

results = await load_test.run()
print(f"Success rate: {results.success_rate}%")
print(f"Avg latency: {results.avg_latency}ms")
print(f"P99 latency: {results.p99_latency}ms")
print(f"Throughput: {results.throughput} req/s")
```

## Best Practices

1. Mock LLM calls — Don't call real APIs in tests
2. Test edge cases — Empty inputs, errors, timeouts
3. Test tools individually — Then test together
4. Use fixtures — Reusable test setup
5. Test async properly — Use pytest-asyncio

## Next Steps

- [Testing Guide](/guide/testing-guide)
- [Agent Evaluation](/guide/agent-evaluation)
