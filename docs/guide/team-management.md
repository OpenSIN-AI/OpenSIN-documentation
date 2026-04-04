# Team Management Best Practices

Build and manage effective multi-agent teams.

## Team Strategies

### Sequential

```python
team = Team(
    name="sequential-team",
    agents=[researcher, writer, reviewer],
    strategy="sequential"  # One after another
)
```

**Use when:** Each step depends on the previous output.

### Parallel

```python
team = Team(
    name="parallel-team",
    agents=[researcher1, researcher2, researcher3],
    strategy="parallel"  # All at once
)
```

**Use when:** Tasks are independent and can run simultaneously.

### Consensus

```python
team = Team(
    name="consensus-team",
    agents=[agent1, agent2, agent3],
    strategy="consensus",  # Vote on outcomes
    quorum=2  # Need 2/3 agreement
)
```

**Use when:** You need multiple perspectives and validation.

### Leader-Follower

```python
team = Team(
    name="leader-team",
    agents=[leader, worker1, worker2, worker3],
    strategy="leader",  # Leader delegates
    leader="leader"
)
```

**Use when:** One agent should coordinate others.

### Pipeline

```python
team = Team(
    name="pipeline-team",
    agents=[ingest, transform, analyze, report],
    strategy="pipeline"  # Assembly line
)
```

**Use when:** Data flows through processing stages.

## Team Size Guidelines

| Team Size | Best For | Max Tasks |
|-----------|----------|-----------|
| 2-3 agents | Simple workflows | 5 |
| 4-6 agents | Complex workflows | 15 |
| 7-10 agents | Enterprise workflows | 30 |
| 10+ agents | Large-scale automation | Unlimited |

## Communication Patterns

### Direct Messages

```python
await team.send_message(
    from_agent="researcher",
    to_agent="writer",
    message="Here are the research findings"
)
```

### Broadcast

```python
await team.broadcast(
    from_agent="coordinator",
    message="Starting new task: research AI trends"
)
```

### Shared Memory

```python
team.shared_memory.set("research_findings", findings)
findings = team.shared_memory.get("research_findings")
```

## Error Handling

### Retry Failed Agents

```python
team = Team(
    name="resilient-team",
    agents=[agent1, agent2],
    retry_policy={
        "max_retries": 3,
        "backoff_factor": 2,
        "retry_on": ["timeout", "api_error"]
    }
)
```

### Fallback Agents

```python
team = Team(
    name="fallback-team",
    agents=[primary_agent],
    fallback=backup_agent  # Used if primary fails
)
```

## Monitoring Teams

```python
# Team metrics
team_metrics = team.get_metrics()
print(f"Tasks completed: {team_metrics.tasks_completed}")
print(f"Success rate: {team_metrics.success_rate}%")
print(f"Avg duration: {team_metrics.avg_duration}s")
print(f"Total cost: ${team_metrics.total_cost}")

# Agent performance
for agent in team.agents:
    print(f"{agent.name}: {agent.get_metrics()}")
```

## Best Practices

1. **Right-size teams** — Don't add agents you don't need
2. **Clear responsibilities** — Each agent should have one role
3. **Define handoffs** — Specify how agents pass work to each other
4. **Monitor costs** — Teams multiply token usage
5. **Set timeouts** — Prevent runaway executions
6. **Test thoroughly** — Test each agent individually and as a team
7. **Log everything** — Essential for debugging team issues

## Next Steps

- [Team Orchestration](/guide/team-orchestration)
- [Advanced Agent Patterns](/guide/advanced-agent-patterns)
- [Performance Optimization](/guide/performance-optimization)
