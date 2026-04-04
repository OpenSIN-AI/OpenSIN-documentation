# Agent Error Handling

Robust error handling patterns for production agents.

## Error Types

| Error Type | Cause | Recovery |
|------------|-------|----------|
| APIError | LLM provider down | Retry with backoff |
| TimeoutError | Request too slow | Increase timeout or retry |
| RateLimitError | Too many requests | Wait and retry |
| ContextLengthError | Input too long | Truncate or summarize |
| ToolExecutionError | Tool failed | Retry or fallback |
| ValidationError | Invalid input/output | Fix and retry |
| AuthenticationError | Invalid credentials | Refresh credentials |

## Retry Patterns

### Exponential Backoff

```python
from opensin.error import RetryWithBackoff

@RetryWithBackoff(
    max_retries=3,
    base_delay=1,
    max_delay=60,
    retry_on=[APIError, TimeoutError]
)
async def call_agent(prompt):
    return await agent.generate(prompt)
```

### Circuit Breaker

```python
from opensin.error import CircuitBreaker

breaker = CircuitBreaker(
    failure_threshold=5,
    recovery_timeout=60,
    half_open_max_calls=1
)

async def safe_call(prompt):
    async with breaker:
        return await agent.generate(prompt)
```

### Fallback

```python
from opensin.error import Fallback

fallback = Fallback(
    primary=Agent(name="primary", model="gpt-4"),
    secondary=Agent(name="fallback", model="gpt-3.5-turbo"),
    final=Agent(name="last-resort", model="gpt-3.5-turbo")
)

result = await fallback.execute(prompt)
```

## Error Handling Best Practices

### 1. Graceful Degradation

```python
async def handle_request(prompt):
    try:
        return await agent.generate(prompt)
    except ContextLengthError:
        # Summarize and retry
        summarized = await summarize(prompt)
        return await agent.generate(summarized)
    except RateLimitError:
        # Wait and retry
        await asyncio.sleep(60)
        return await agent.generate(prompt)
    except APIError:
        # Use fallback model
        return await fallback_agent.generate(prompt)
```

### 2. Structured Errors

```python
from opensin.error import OpenSINError

class AgentError(OpenSINError):
    def __init__(self, message, code, details=None):
        super().__init__(message)
        self.code = code
        self.details = details or {}
        self.timestamp = datetime.utcnow()
        self.agent_id = self.agent.name
```

### 3. Error Logging

```python
from opensin.error import ErrorLogger

logger = ErrorLogger(
    storage="database",
    retention_days=90,
    alert_on=["critical", "repeated"]
)

async def handle_error(error):
    await logger.log(error)
    
    if error.is_repeated:
        await alert_team(error)
    
    if error.is_critical:
        await escalate(error)
```

### 4. Error Monitoring

```python
from opensin.error import ErrorMonitor

monitor = ErrorMonitor(
    window=300,  # 5 minutes
    threshold=0.05,  # 5% error rate
    alert_channels=["slack", "email"]
)

await monitor.start()
```

## Common Error Scenarios

### Token Limit Exceeded

```python
try:
    response = await agent.generate(long_prompt)
except ContextLengthError:
    # Option 1: Truncate
    truncated = truncate_prompt(long_prompt, max_tokens=4000)
    response = await agent.generate(truncated)
    
    # Option 2: Summarize
    summarized = await summarizer.summarize(long_prompt)
    response = await agent.generate(summarized)
    
    # Option 3: Split
    chunks = split_prompt(long_prompt, max_tokens=4000)
    responses = [await agent.generate(chunk) for chunk in chunks]
    response = combine_responses(responses)
```

### Rate Limiting

```python
from opensin.error import RateLimiter

limiter = RateLimiter(
    requests_per_minute=60,
    tokens_per_hour=100000
)

async def rate_limited_call(prompt):
    await limiter.acquire()
    return await agent.generate(prompt)
```

## Best Practices

1. **Always handle errors** — Never let errors propagate unhandled
2. **Use retries** — Transient errors are common
3. **Set timeouts** — Prevent hanging requests
4. **Log everything** — Essential for debugging
5. **Monitor error rates** — Alert on anomalies
6. **Have fallbacks** — Always have a backup plan
7. **Test error paths** — Test error handling thoroughly

## Next Steps

- [Troubleshooting](/guide/troubleshooting)
- [Monitoring Guide](/guide/monitoring)
