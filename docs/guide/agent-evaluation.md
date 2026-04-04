# Agent Evaluation Guide

Measure and improve agent quality systematically.

## Evaluation Dimensions

| Dimension | What to Measure | How to Measure |
|-----------|----------------|----------------|
| Accuracy | Correctness of responses | Human review, golden datasets |
| Consistency | Same answer for same input | Repeat prompts, compare |
| Latency | Response time | Built-in metrics |
| Cost | Token usage and cost | Cost tracker |
| Safety | Harmful content | Red teaming, safety filters |
| Helpfulness | User satisfaction | Feedback scores |

## Evaluation Methods

### Golden Dataset Testing

```python
from opensin.evaluation import GoldenTest

tests = GoldenTest(
    dataset=[
        {"input": "What is 2+2?", "expected": "4"},
        {"input": "Sort [3,1,2]", "expected": "[1,2,3]"},
        {"input": "Reverse 'hello'", "expected": "olleh"},
    ]
)

results = await tests.run(agent)
print(f"Accuracy: {results.accuracy}%")
print(f"Failed: {results.failed}")
```

### A/B Testing

```python
from opensin.evaluation import ABTest

ab_test = ABTest(
    agent_a=Agent(name="v1", model="gpt-3.5-turbo"),
    agent_b=Agent(name="v2", model="gpt-4"),
    prompts=test_prompts,
    metric="user_satisfaction"
)

results = await ab_test.run()
print(f"Winner: {results.winner}")
print(f"Confidence: {results.confidence}%")
```

### Red Teaming

```python
from opensin.evaluation import RedTeam

red_team = RedTeam(
    attack_types=[
        "prompt_injection",
        "jailbreak",
        "data_exfiltration",
        "toxic_output"
    ],
    iterations=100
)

results = await red_team.run(agent)
print(f"Vulnerabilities found: {results.vulnerabilities}")
```

## Quality Metrics

### Response Quality

```python
from opensin.evaluation import QualityScorer

scorer = QualityScorer(
    criteria={
        "relevance": 0.3,
        "accuracy": 0.3,
        "completeness": 0.2,
        "clarity": 0.2
    }
)

score = await scorer.evaluate(response, reference)
print(f"Quality score: {score}/100")
```

### Safety Score

```python
from opensin.evaluation import SafetyChecker

checker = SafetyChecker(
    checks=["toxicity", "bias", "pii_leak", "harmful_content"]
)

safety = await checker.evaluate(response)
print(f"Safety score: {safety.score}/100")
```

## Continuous Evaluation

### Automated Evaluation Pipeline

```python
from opensin.evaluation import EvaluationPipeline

pipeline = EvaluationPipeline([
    GoldenTest(dataset=golden_dataset),
    QualityScorer(criteria=quality_criteria),
    SafetyChecker(checks=safety_checks),
    PerformanceBenchmark(),
])

# Run after every deployment
results = await pipeline.evaluate(agent)

if results.overall_score < 80:
    raise EvaluationError(f"Score {results.overall_score} below threshold")
```

## Best Practices

1. **Test before deploy** — Always run evaluation before releasing
2. **Monitor in production** — Track quality metrics continuously
3. **Update golden datasets** — Add new test cases regularly
4. **Red team regularly** — Find vulnerabilities before attackers do
5. **Collect user feedback** — Real-world feedback is invaluable

## Next Steps

- [Testing Guide](/guide/testing-guide)
- [Security Audit](/guide/security-audit-checklist)
- [Performance Benchmarking](/guide/performance-benchmarking)
