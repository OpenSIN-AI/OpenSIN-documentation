# Advanced Agent Patterns

This guide covers advanced patterns for building sophisticated AI agents with OpenSIN.

## Stateful Agents

Agents can maintain state across multiple interactions:

```python
from opensin import Agent

class StatefulAgent(Agent):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.memory = {}
    
    async def handle_message(self, message):
        # Store context
        self.memory[message.id] = message.content
        
        # Use previous context
        context = self.get_relevant_context(message)
        
        response = await self.generate_response(message, context)
        return response
    
    def get_relevant_context(self, message, max_turns=5):
        recent = list(self.memory.items())[-max_turns:]
        return [content for _, content in recent]
```

## Agent Delegation

Agents can delegate tasks to specialized sub-agents:

```python
from opensin import Agent, Team

class ManagerAgent(Agent):
    def __init__(self):
        super().__init__(name="manager")
        self.researcher = Agent(name="researcher")
        self.writer = Agent(name="writer")
        self.reviewer = Agent(name="reviewer")
    
    async def handle_task(self, task):
        # Research phase
        research = await self.researcher.execute(task)
        
        # Writing phase
        draft = await self.writer.execute({
            "task": task,
            "research": research
        })
        
        # Review phase
        final = await self.reviewer.execute({
            "draft": draft,
            "requirements": task.requirements
        })
        
        return final
```

## Event-Driven Agents

React to events in the system:

```python
from opensin import Agent, Event

class MonitoringAgent(Agent):
    def __init__(self):
        super().__init__(name="monitor")
        self.subscribe("agent.error")
        self.subscribe("system.warning")
    
    async def on_event(self, event: Event):
        if event.type == "agent.error":
            await self.handle_error(event.data)
        elif event.type == "system.warning":
            await self.handle_warning(event.data)
    
    async def handle_error(self, error_data):
        # Log error
        # Notify team
        # Attempt recovery
        pass
```

## Multi-Agent Consensus

Agents can reach consensus through voting:

```python
from opensin import Agent, Team

class ConsensusTeam(Team):
    def __init__(self, agents):
        super().__init__(agents=agents)
        self.quorum = len(agents) // 2 + 1
    
    async def decide(self, proposal):
        votes = []
        for agent in self.agents:
            vote = await agent.evaluate(proposal)
            votes.append(vote)
        
        approve_count = sum(1 for v in votes if v.approve)
        
        if approve_count >= self.quorum:
            return await self.execute_proposal(proposal)
        else:
            return await self.revise_proposal(proposal, votes)
```

## Agent Pipelines

Chain agents in a processing pipeline:

```python
from opensin import Pipeline

pipeline = Pipeline([
    InputValidator(),
    DataEnricher(),
    ContentGenerator(),
    QualityChecker(),
    OutputFormatter()
])

result = await pipeline.execute(input_data)
```

## Resource Management

Manage agent resources efficiently:

```python
from opensin import Agent, ResourceManager

class ResourceAwareAgent(Agent):
    def __init__(self):
        super().__init__(name="resource-aware")
        self.resources = ResourceManager(
            max_tokens=4000,
            max_memory=1000,
            max_api_calls=100
        )
    
    async def handle_request(self, request):
        if not self.resources.has_capacity():
            return await self.queue_request(request)
        
        self.resources.allocate(request)
        try:
            result = await self.process(request)
            return result
        finally:
            self.resources.release(request)
```

## Error Handling Patterns

Robust error handling for production agents:

```python
from opensin import Agent, RetryPolicy

class ResilientAgent(Agent):
    def __init__(self):
        super().__init__(name="resilient")
        self.retry_policy = RetryPolicy(
            max_retries=3,
            backoff_factor=2,
            retry_on=[TimeoutError, ConnectionError]
        )
    
    async def execute_with_retry(self, task):
        return await self.retry_policy.execute(
            lambda: self.process_task(task)
        )
    
    async def process_task(self, task):
        try:
            return await self.run(task)
        except KnownError as e:
            return await self.handle_known_error(e)
        except Exception as e:
            await self.log_error(e)
            raise
```

## Best Practices

1. **Keep agents focused** — Each agent should have a single responsibility
2. **Use delegation** — Delegate complex tasks to specialized agents
3. **Handle errors gracefully** — Always have fallback strategies
4. **Monitor resources** — Track token usage, memory, and API calls
5. **Test thoroughly** — Write unit and integration tests for agents
6. **Document behavior** — Clearly document agent capabilities and limitations
7. **Use events** — Decouple agents using event-driven architecture
8. **Implement retries** — Handle transient failures automatically

## Next Steps

- [Team Orchestration](/guide/team-orchestration) — Coordinate multiple agents
- [A2A Protocol](/guide/a2a-protocol) — Agent-to-Agent communication
- [Performance Best Practices](/best-practices/performance) — Optimize agent performance
