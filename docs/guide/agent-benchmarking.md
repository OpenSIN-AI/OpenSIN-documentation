# Agent Benchmarking Framework

Systematic benchmarking for AI agent performance.

## Benchmark Dimensions

| Dimension | Metrics | Tools |
|-----------|---------|-------|
| Accuracy | Correctness, F1 score | Golden datasets |
| Latency | P50, P95, P99 | Built-in profiler |
| Cost | Cost per request, per token | Cost tracker |
| Reliability | Error rate, uptime | Health checks |
| Safety | Injection resistance, toxicity | Red team suite |
| Consistency | Response variance | Repeat testing |

## Benchmark Suite

```python
from opensin.benchmark import BenchmarkSuite

suite = BenchmarkSuite(
    name="agent-evaluation",
    benchmarks=[
        "accuracy",
        "latency",
        "cost",
        "reliability",
        "safety",
        "consistency"
    ]
)

results = await suite.run(agent)
print(f"Overall score: {results.overall_score}/100")
print(f"Weak areas: {results.weak_areas}")
print(f"Strong areas: {results.strong_areas}")
```

## Accuracy Benchmark

```python
from opensin.benchmark import AccuracyBenchmark

benchmark = AccuracyBenchmark(
    dataset="golden_dataset.json",
    metrics=["exact_match", "f1_score", "bleu", "rouge"]
)

results = await benchmark.run(agent)
print(f"Exact match: {results.exact_match}%")
print(f"F1 score: {results.f1_score}")
```

## Latency Benchmark

```python
from opensin.benchmark import LatencyBenchmark

benchmark = LatencyBenchmark(
    prompts=test_prompts,
    iterations=100,
    percentiles=[50, 95, 99]
)

results = await benchmark.run(agent)
print(f"P50: {results.p50}ms")
print(f"P95: {results.p95}ms")
print(f"P99: {results.p99}ms")
```

## Cost Benchmark

```python
from opensin.benchmark import CostBenchmark

benchmark = CostBenchmark(
    prompts=test_prompts,
    iterations=50
)

results = await benchmark.run(agent)
print(f"Average cost: ${results.avg_cost}")
print(f"Cost per 1K requests: ${results.cost_per_1k}")
```

## Safety Benchmark

```python
from opensin.benchmark import SafetyBenchmark

benchmark = SafetyBenchmark(
    attack_types=[
        "prompt_injection",
        "jailbreak",
        "data_exfiltration",
        "toxic_output"
    ],
    iterations=100
)

results = await benchmark.run(agent)
print(f"Vulnerabilities: {results.vulnerabilities}")
print(f"Safety score: {results.safety_score}/100")
```

## Consistency Benchmark

```python
from opensin.benchmark import ConsistencyBenchmark

benchmark = ConsistencyBenchmark(
    prompts=test_prompts,
    iterations=20,
    similarity_threshold=0.8
)

results = await benchmark.run(agent)
print(f"Consistency score: {results.consistency_score}%")
print(f"Variance: {results.variance}")
```

## Benchmark Reports

```python
# Generate comprehensive report
report = results.generate_report(format="markdown")
print(report)

# Export
results.export_json("benchmark-results.json")
results.export_html("benchmark-results.html")
results.export_pdf("benchmark-results.pdf")
```

## Continuous Benchmarking

```python
from opensin.benchmark import ContinuousBenchmark

cb = ContinuousBenchmark(
    benchmarks=benchmark_suite,
    schedule="daily",
    alert_thresholds={
        "accuracy": {"min": 0.9},
        "latency_p99": {"max": 5000},
        "cost_per_request": {"max": 0.10}
    }
)

await cb.start()
```

## Best Practices

1. **Benchmark before deploy** — Never deploy without benchmarks
2. **Track trends** — Monitor performance over time
3. **Compare versions** — A/B test agent versions
4. **Set thresholds** — Define minimum acceptable scores
5. **Automate** — Run benchmarks in CI/CD pipeline

## Next Steps

- [Agent Evaluation](/guide/agent-evaluation)
- [Performance Benchmarking](/guide/performance-benchmarking)
