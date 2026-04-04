# Agent Cost Optimization

Reduce agent costs while maintaining quality.

## Cost Breakdown

### Per-Request Cost

| Component | Cost | Optimization |
|-----------|------|-------------|
| Input tokens | $0.01/1K | Reduce context, cache prompts |
| Output tokens | $0.03/1K | Limit max_tokens, stream |
| Tool calls | $0.001/call | Batch calls, cache results |
| Memory operations | $0.0001/op | Use vector search, prune |

## Optimization Strategies

### 1. Model Tiering

```python
def select_model(task):
    if task.complexity < 0.3:
        return "gpt-3.5-turbo"    # $0.002/1K
    elif task.complexity < 0.7:
        return "claude-sonnet"     # $0.015/1K
    else:
        return "gpt-4"             # $0.03/1K
```

**Savings: 40-60%**

### 2. Prompt Caching

```python
from opensin.cache import PromptCache

cache = PromptCache(ttl=3600, max_size=10000)

async def get_response(prompt):
    cached = cache.get(prompt)
    if cached:
        return cached  # $0 cost
    response = await agent.generate(prompt)
    cache.set(prompt, response)
    return response
```

**Savings: 50-80% on repeated prompts**

### 3. Response Streaming

```python
async for chunk in agent.stream(prompt):
    if is_complete(chunk.text):
        break  # Save remaining tokens
```

**Savings: 20-40% on output tokens**

### 4. Batch Processing

```python
# Process multiple inputs in one request
batch_prompt = "\n---\n".join([f"Task {i}: {task}" for i, task in enumerate(tasks)])
response = await agent.send(batch_prompt)
results = parse_batch_response(response)
```

**Savings: 30-50% on overhead tokens**

## Budget Management

```python
from opensin import BudgetManager

budget = BudgetManager(
    daily_limit=50.00,
    monthly_limit=1000.00,
    alert_thresholds=[0.5, 0.75, 0.9],
    hard_stop=True
)
```

## Monthly Cost Estimates

| Usage Level | Requests/Month | Est. Cost |
|-------------|---------------|-----------|
| Hobby | 1,000 | $5-15 |
| Small Team | 10,000 | $50-150 |
| Business | 100,000 | $500-1,500 |
| Enterprise | 1,000,000 | $5,000-15,000 |

## Best Practices

1. **Right-size models** — Don't use GPT-4 for simple tasks
2. **Cache aggressively** — Reuse responses when possible
3. **Stream responses** — Stop early when you have enough
4. **Batch requests** — Combine similar requests
5. **Monitor costs** — Track spending in real-time
6. **Set budgets** — Hard limits prevent surprises

## Next Steps

- [Cost Tracking](/guide/sin-cost-tracking)
- [Agent Economics](/guide/agent-economics)
