# Performance Optimization Guide

Optimize your OpenSIN agents for speed, cost, and reliability.

## Token Optimization

### Reduce Context Window

```python
# BAD - sending full conversation history
context = full_conversation_history

# GOOD - sending only relevant context
context = get_relevant_context(message, max_tokens=2000)
```

### Use Streaming

```python
async def stream_response(agent, prompt):
    async for chunk in agent.stream(prompt):
        yield chunk.text
```

## Caching Strategies

### Response Caching

```python
from opensin.cache import ResponseCache

cache = ResponseCache(
    ttl=3600,  # 1 hour
    max_size=1000,
    strategy="lru"
)

async def get_response(prompt):
    cached = cache.get(prompt)
    if cached:
        return cached
    
    response = await agent.generate(prompt)
    cache.set(prompt, response)
    return response
```

### Semantic Caching

```python
from opensin.cache import SemanticCache

cache = SemanticCache(
    similarity_threshold=0.95,
    max_size=5000
)

async def get_semantic_response(prompt):
    similar = cache.find_similar(prompt)
    if similar:
        return similar.response
    
    response = await agent.generate(prompt)
    cache.store(prompt, response)
    return response
```

## Batch Processing

### Parallel Execution

```python
import asyncio

async def process_batch(agent, items):
    tasks = [agent.process(item) for item in items]
    results = await asyncio.gather(*tasks)
    return results
```

### Chunking Large Tasks

```python
async def process_large_task(agent, data, chunk_size=100):
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    results = []
    for chunk in chunks:
        result = await agent.process(chunk)
        results.append(result)
    return combine_results(results)
```

## Model Selection

### Tiered Model Strategy

```python
class TieredAgent:
    def __init__(self):
        self.fast_model = Agent(model="gpt-3.5-turbo")
        self.smart_model = Agent(model="gpt-4")
        self.expert_model = Agent(model="gpt-4-turbo")
    
    async def process(self, task):
        if task.complexity == "low":
            return await self.fast_model.execute(task)
        elif task.complexity == "medium":
            return await self.smart_model.execute(task)
        else:
            return await self.expert_model.execute(task)
```

## Memory Management

### Efficient Memory Usage

```python
from opensin.memory import MemoryManager

memory = MemoryManager(
    max_tokens=4000,
    compression_ratio=0.5,
    eviction_policy="lru"
)

# Compress old memories
memory.compress()

# Evict least relevant memories
memory.evict(threshold=0.3)
```

## Monitoring Performance

### Key Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Latency | < 2s | Response time |
| Token Usage | < 2000/input | Token counter |
| Cost | < $0.01/request | Cost tracker |
| Success Rate | > 99% | Error tracking |
| Cache Hit Rate | > 50% | Cache metrics |

### Performance Dashboard

```python
from opensin.monitoring import PerformanceMonitor

monitor = PerformanceMonitor(
    metrics=["latency", "tokens", "cost", "errors"],
    dashboard_url="http://localhost:3000"
)

# Track performance
monitor.track_request(start_time, tokens_used, cost)
```

## Cost Optimization

### Budget Controls

```python
from opensin.cost import BudgetManager

budget = BudgetManager(
    daily_limit=50.00,
    monthly_limit=1000.00,
    alert_threshold=0.8
)

if budget.would_exceed_limit(estimated_cost):
    return "Budget limit reached."
```

### Cost Tracking

```python
from opensin.cost import CostTracker

tracker = CostTracker()

# Track per-agent costs
tracker.track(agent_name, tokens, cost)

# Get cost report
report = tracker.get_report(period="monthly")
```

## Next Steps

- [Scaling Guide](/guide/scaling) - Scale to production
- [Monitoring Guide](/guide/monitoring) - Monitor performance
- [Best Practices](/best-practices/performance) - Performance best practices
