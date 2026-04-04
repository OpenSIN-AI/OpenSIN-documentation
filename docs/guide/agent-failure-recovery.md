# Agent Failure Recovery

Recover from agent failures gracefully.

## Failure Types

| Type | Cause | Recovery |
|------|-------|----------|
| API Failure | LLM provider down | Retry with backoff |
| Timeout | Request too slow | Increase timeout or retry |
| Rate Limit | Too many requests | Wait and retry |
| Context Overflow | Input too long | Truncate or summarize |
| Tool Failure | Tool execution error | Retry or fallback |
| Memory Overflow | Too much context | Compact memory |
| Network Failure | Connection lost | Reconnect and retry |

## Recovery Strategies

### 1. Retry with Backoff

```python
from opensin.recovery import RetryWithBackoff

@RetryWithBackoff(
    max_retries=3,
    base_delay=1,
    max_delay=60,
    retry_on=[APIError, TimeoutError]
)
async def call_agent(prompt):
    return await agent.generate(prompt)
```

### 2. Circuit Breaker

```python
from opensin.recovery import CircuitBreaker

breaker = CircuitBreaker(
    failure_threshold=5,
    recovery_timeout=60,
    half_open_max_calls=1
)

async def safe_call(prompt):
    async with breaker:
        return await agent.generate(prompt)
```

### 3. Fallback Agent

```python
from opensin.recovery import FallbackAgent

fallback = FallbackAgent(
    primary=Agent(name="primary", model="gpt-4"),
    secondary=Agent(name="fallback", model="gpt-3.5-turbo"),
    final=Agent(name="last-resort", model="gpt-3.5-turbo")
)

result = await fallback.execute(prompt)
```

### 4. Graceful Degradation

```python
async def handle_request(prompt):
    try:
        return await agent.generate(prompt)
    except ContextLengthError:
        summarized = await summarize(prompt)
        return await agent.generate(summarized)
    except RateLimitError:
        await asyncio.sleep(60)
        return await agent.generate(prompt)
    except APIError:
        return await fallback_agent.generate(prompt)
```

## Recovery Monitoring

```python
from opensin.recovery import RecoveryMonitor

monitor = RecoveryMonitor(
    window=300,  # 5 minutes
    threshold=0.05,  # 5% failure rate
    alert_channels=["slack", "email"]
)

await monitor.start()
```

## Best Practices

1. Always handle errors — Never let errors propagate unhandled
2. Use retries — Transient errors are common
3. Set timeouts — Prevent hanging requests
4. Log everything — Essential for debugging
5. Monitor failure rates — Alert on anomalies
6. Have fallbacks — Always have a backup plan
7. Test failure paths — Test error handling thoroughly

## Next Steps

- [Error Handling](/guide/agent-error-handling)
- [Troubleshooting](/guide/troubleshooting)
