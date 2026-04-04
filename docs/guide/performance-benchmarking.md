# Performance Benchmarking Guide

Measure and optimize OpenSIN agent performance.

## Benchmark Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Latency (p50) | < 1s | Response time |
| Latency (p99) | < 5s | Response time |
| Throughput | > 100 req/min | Concurrent requests |
| Token Efficiency | < 2000/input | Token counter |
| Cost per Request | < $0.05 | Cost tracker |
| Cache Hit Rate | > 50% | Cache metrics |
| Error Rate | < 0.1% | Error tracking |
| Memory Usage | < 512MB | Process monitoring |

## Running Benchmarks

### Basic Benchmark

```python
from opensin.benchmark import Benchmark

benchmark = Benchmark(
    agent=agent,
    prompts=[
        "What is AI?",
        "Explain quantum computing",
        "Write a Python function to sort a list",
        "Summarize this article: ...",
        "Debug this code: ..."
    ],
    iterations=10
)

results = await benchmark.run()
results.report()
```

### Load Testing

```python
from opensin.benchmark import LoadTest

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

### Stress Testing

```python
from opensin.benchmark import StressTest

stress_test = StressTest(
    agent=agent,
    max_concurrent=200,
    duration_seconds=300,
    fail_threshold=0.05  # 5% error rate
)

results = await stress_test.run()
```

## Optimization Strategies

### Latency Optimization

1. **Use streaming** — First token in < 200ms
2. **Prompt caching** — Reuse cached prompts
3. **Smaller models** — Use haiku for simple tasks
4. **Parallel execution** — Run independent tasks concurrently
5. **Connection pooling** — Reuse HTTP connections

```python
# Streaming for faster first token
async for chunk in agent.stream(prompt):
    display(chunk.text)  # Show as it arrives
```

### Token Optimization

1. **Trim context** — Only include relevant history
2. **Compress prompts** — Remove unnecessary text
3. **Use system prompts** — Reuse across requests
4. **Cache responses** — Don't regenerate identical responses

```python
# Context trimming
context = memory.get_relevant(query, max_tokens=1000)
```

### Cost Optimization

1. **Model tiering** — Right-size models for tasks
2. **Response caching** — Cache common responses
3. **Batch requests** — Combine similar requests
4. **Token budgeting** — Set max tokens per request

```python
# Model tiering
if task.complexity == "simple":
    model = "gpt-3.5-turbo"  # $0.002/1K tokens
elif task.complexity == "complex":
    model = "gpt-4"  # $0.03/1K tokens
```

## Benchmark Reports

### HTML Report

```python
results.save_html("benchmark-report.html")
```

### JSON Report

```python
results.save_json("benchmark-report.json")
```

### CI Integration

```yaml
# .github/workflows/benchmark.yml
- name: Run Benchmarks
  run: python benchmarks/run.py
  
- name: Check Performance
  run: |
    if [ $(cat benchmark.json | jq '.p99_latency') -gt 5000 ]; then
      echo "P99 latency too high!"
      exit 1
    fi
```

## Next Steps

- [Performance Optimization](/guide/performance-optimization)
- [Cost Tracking](/guide/sin-cost-tracking)
- [Monitoring Guide](/guide/monitoring)
