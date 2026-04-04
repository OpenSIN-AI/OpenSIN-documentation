# Agent Collaboration Patterns

How agents work together to solve complex problems.

## Collaboration Models

### 1. Master-Worker

```python
from opensin import MasterWorker

mw = MasterWorker(
    master=Agent(name="manager", model="gpt-4"),
    workers=[
        Agent(name="worker-1", model="gpt-3.5-turbo"),
        Agent(name="worker-2", model="gpt-3.5-turbo"),
        Agent(name="worker-3", model="gpt-3.5-turbo"),
    ],
    distribution="round_robin"
)

result = await mw.execute(task)
```

### 2. Peer-to-Peer

```python
from opensin import PeerNetwork

network = PeerNetwork(
    agents=[agent1, agent2, agent3],
    communication="direct",
    consensus="majority"
)

result = await network.execute(task)
```

### 3. Specialist Network

```python
from opensin import SpecialistNetwork

network = SpecialistNetwork(
    specialists={
        "code": coding_agent,
        "research": research_agent,
        "writing": writing_agent,
        "analysis": analysis_agent,
    },
    router=Agent(name="router", model="gpt-4")
)

result = await network.route_and_execute(task)
```

### 4. Assembly Line

```python
from opensin import AssemblyLine

line = AssemblyLine([
    {"agent": intake_agent, "task": "classify and prioritize"},
    {"agent": research_agent, "task": "gather information"},
    {"agent": analysis_agent, "task": "analyze findings"},
    {"agent": writing_agent, "task": "generate response"},
    {"agent": review_agent, "task": "quality check"},
])

result = await line.process(ticket)
```

## Communication Protocols

### Direct Messages

```python
await agent1.send_to(agent2, "Here's the data you requested")
```

### Broadcast

```python
await coordinator.broadcast("Starting new task: research Q1 data")
```

### Shared Workspace

```python
workspace = SharedWorkspace()
await workspace.put("research_findings", findings)
findings = await workspace.get("research_findings")
```

## Conflict Resolution

```python
from opensin import ConflictResolver

resolver = ConflictResolver(
    strategy="vote",  # or "expert", "consensus", "mediator"
    mediator=Agent(name="mediator", model="gpt-4")
)

result = await resolver.resolve(
    opinions=[agent1.opinion, agent2.opinion, agent3.opinion]
)
```

## Best Practices

1. **Clear roles** — Each agent should have one responsibility
2. **Defined interfaces** — Specify input/output formats
3. **Error handling** — Handle agent failures gracefully
4. **Monitoring** — Track collaboration metrics
5. **Timeouts** — Prevent deadlocks

## Next Steps

- [Team Management](/guide/team-management)
- [Orchestration Patterns](/guide/agent-orchestration-patterns)
