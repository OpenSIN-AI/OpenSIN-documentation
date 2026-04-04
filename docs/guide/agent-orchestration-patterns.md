# Agent Orchestration Patterns

Advanced patterns for coordinating multiple agents.

## Pattern 1: Router

```python
from opensin import Router

router = Router(
    routes=[
        {"condition": "code", "agent": coding_agent},
        {"condition": "research", "agent": research_agent},
        {"condition": "writing", "agent": writing_agent},
        {"condition": "analysis", "agent": analysis_agent},
    ],
    default=fallback_agent
)

result = await router.route(user_input)
```

## Pattern 2: Map-Reduce

```python
from opensin import MapReduce

mr = MapReduce(
    mapper=Agent(name="mapper", model="gpt-3.5-turbo"),
    reducer=Agent(name="reducer", model="gpt-4")
)

result = await mr.execute(
    input=data_chunks,
    map_prompt="Summarize this chunk",
    reduce_prompt="Combine all summaries into one report"
)
```

## Pattern 3: Debate

```python
from opensin import Debate

debate = Debate(
    agents=[agent_pro, agent_con],
    rounds=3,
    moderator=Agent(name="moderator", model="gpt-4")
)

result = await debate.execute(
    topic="Should we use microservices?"
)
```

## Pattern 4: Chain of Verification

```python
from opensin import VerificationChain

chain = VerificationChain([
    GeneratorAgent(),    # Generate answer
    VerifierAgent(),     # Verify facts
    CorrectorAgent(),    # Fix errors
    FinalizerAgent()     # Format output
])

result = await chain.execute("What is the capital of France?")
```

## Pattern 5: Hierarchical

```python
from opensin import HierarchicalTeam

team = HierarchicalTeam(
    manager=Agent(name="manager", model="gpt-4"),
    workers=[
        Agent(name="worker1", model="gpt-3.5-turbo"),
        Agent(name="worker2", model="gpt-3.5-turbo"),
        Agent(name="worker3", model="gpt-3.5-turbo"),
    ],
    reviewer=Agent(name="reviewer", model="gpt-4")
)
```

## Pattern 6: Swarm

```python
from opensin import Swarm

swarm = Swarm(
    agents=[agent1, agent2, agent3, agent4, agent5],
    coordination="stigmergy",  # Indirect coordination
    communication="broadcast"
)

result = await swarm.execute(task)
```

## Pattern Selection Guide

| Pattern | Best For | Cost | Speed |
|---------|----------|------|-------|
| Router | Multi-domain | Low | Fast |
| Map-Reduce | Large data | Medium | Medium |
| Debate | Complex decisions | High | Slow |
| Chain of Verification | Accuracy critical | High | Slow |
| Hierarchical | Complex workflows | Medium | Medium |
| Swarm | Exploration | High | Fast |

## Next Steps

- [Team Management](/guide/team-management)
- [Advanced Agent Patterns](/guide/advanced-agent-patterns)
