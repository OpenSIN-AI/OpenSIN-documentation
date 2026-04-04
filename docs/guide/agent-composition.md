# Agent Composition

Combine agents to build complex systems.

## Composition Operators

### Sequential Composition

```python
from opensin import compose

# f ∘ g: apply g first, then f
combined = compose(analyzer, summarizer)
result = await combined.execute(data)
```

### Parallel Composition

```python
from opensin import parallel

# Run agents in parallel
combined = parallel(researcher1, researcher2, researcher3)
results = await combined.execute(query)
```

### Conditional Composition

```python
from opensin import conditional

# Run agent based on condition
combined = conditional(
    condition=lambda x: x.complexity > 0.5,
    true_agent=expert_agent,
    false_agent=basic_agent
)
result = await combined.execute(input)
```

### Iterative Composition

```python
from opensin import iterate

# Repeat until condition met
combined = iterate(
    agent=refinement_agent,
    until=lambda x: x.quality > 0.9,
    max_iterations=10
)
result = await combined.execute(draft)
```

## Composition Patterns

### Pipeline Pattern

```python
pipeline = (
    ingest
    >> clean
    >> analyze
    >> visualize
    >> report
)
```

### Fan-Out/Fan-In

```python
from opensin import fan_out, fan_in

# Fan-out to multiple agents
results = await fan_out(
    agent=processor,
    inputs=data_chunks
)

# Fan-in to combine results
combined = await fan_in(
    aggregator=summary_agent,
    inputs=results
)
```

### Circuit Breaker

```python
from opensin import circuit_breaker

protected = circuit_breaker(
    agent=external_api_agent,
    failure_threshold=5,
    recovery_timeout=60
)
```

## Best Practices

1. **Keep agents small** — Single responsibility
2. **Compose, don't inherit** — Build complexity through composition
3. **Test compositions** — Test combined behavior
4. **Monitor compositions** — Track composition metrics
5. **Document flows** — Document data flow through compositions

## Next Steps

- [Advanced Agent Patterns](/guide/advanced-agent-patterns)
- [Team Management](/guide/team-management)
