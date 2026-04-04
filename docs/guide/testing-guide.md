# Testing Guide

Comprehensive testing strategies for OpenSIN agents and teams.

## Testing Levels

```
┌─────────────────────────────────────┐
│         Testing Pyramid             │
├─────────────────────────────────────┤
│           E2E Tests                 │  ← Few
│        ┌─────────────┐              │
│       Integration Tests             │  ← Some
│      ┌─────────────────┐            │
│     Unit Tests                      │  ← Many
│    ┌─────────────────────┐          │
│   Mock Tests                          │  ← Most
└───┴─────────────────────────────────┴──
```

## Unit Testing

### Test Individual Agents

```python
import pytest
from opensin import Agent
from opensin.testing import MockLLM

@pytest.fixture
def agent():
    return Agent(
        name="test-agent",
        llm=MockLLM(responses=["Hello!", "I can help with that."])
    )

@pytest.mark.asyncio
async def test_agent_responds(agent):
    response = await agent.send("Hi")
    assert response.content == "Hello!"

@pytest.mark.asyncio
async def test_agent_handles_context(agent):
    await agent.send("Remember: my name is Alice")
    response = await agent.send("What's my name?")
    assert "Alice" in response.content
```

### Test Agent Tools

```python
@pytest.fixture
def agent_with_tools():
    agent = Agent(name="tool-agent", llm=MockLLM())
    agent.register_tool("calculator", lambda expr: eval(expr))
    return agent

@pytest.mark.asyncio
async def test_calculator_tool(agent_with_tools):
    result = await agent_with_tools.use_tool("calculator", "2 + 2")
    assert result == 4
```

## Integration Testing

### Test Agent Communication

```python
from opensin import Agent, Team
from opensin.testing import MockLLM, MockA2ABus

@pytest.fixture
def team():
    researcher = Agent(name="researcher", llm=MockLLM(responses=["Research results"]))
    writer = Agent(name="writer", llm=MockLLM(responses=["Written report"]))
    return Team(name="test-team", agents=[researcher, writer])

@pytest.mark.asyncio
async def test_team_execution(team):
    result = await team.execute("Research and write a report")
    assert result is not None
    assert len(result.steps) == 2
```

### Test A2A Protocol

```python
from opensin.a2a import Message, AgentCard
from opensin.testing import MockA2ABus

@pytest.mark.asyncio
async def test_a2a_message():
    bus = MockA2ABus()
    
    message = Message(
        type="request",
        from_agent="sender",
        to_agent="receiver",
        content="Hello"
    )
    
    response = await bus.send(message)
    assert response.type == "response"
    assert response.content is not None
```

## End-to-End Testing

### Full Workflow Test

```python
from opensin import Client, Agent, Team
from opensin.testing import TestEnvironment

@pytest.fixture
def test_env():
    return TestEnvironment(
        api_key="test-key",
        base_url="http://localhost:8000"
    )

@pytest.mark.asyncio
async def test_full_workflow(test_env):
    # Create agent
    agent = await test_env.create_agent(
        name="e2e-agent",
        model="gpt-4"
    )
    
    # Send message
    response = await agent.send("What is 2+2?")
    assert "4" in response.content
    
    # Create team
    team = await test_env.create_team(
        name="e2e-team",
        agents=[agent]
    )
    
    # Execute task
    result = await team.execute("Calculate 2+2")
    assert result is not None
```

## Performance Testing

### Load Testing

```python
import asyncio
import time
from opensin.testing import LoadTester

async def test_concurrent_requests():
    tester = LoadTester(
        agent=agent,
        concurrent_users=10,
        requests_per_user=5
    )
    
    results = await tester.run()
    
    assert results.success_rate > 0.95
    assert results.avg_latency < 2.0  # seconds
    assert results.p99_latency < 5.0   # seconds
```

### Benchmark Testing

```python
from opensin.testing import Benchmark

benchmark = Benchmark()

# Benchmark agent response time
benchmark.measure(
    name="agent_response_time",
    func=lambda: agent.send("Hello"),
    iterations=100
)

# Benchmark team execution
benchmark.measure(
    name="team_execution_time",
    func=lambda: team.execute("Task"),
    iterations=50
)

# Print results
benchmark.report()
```

## Test Configuration

### pytest.ini

```ini
[pytest]
asyncio_mode = auto
testpaths = tests
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    performance: Performance tests
```

### conftest.py

```python
import pytest
from opensin.testing import MockLLM, TestEnvironment

@pytest.fixture(scope="session")
def test_env():
    return TestEnvironment()

@pytest.fixture
def mock_llm():
    return MockLLM()

@pytest.fixture
def agent(mock_llm):
    from opensin import Agent
    return Agent(name="test", llm=mock_llm)
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements-dev.txt
      - run: pytest tests/ -v --cov=opensin
      - run: pytest tests/ -m performance --benchmark-json=benchmark.json
```

## Best Practices

1. **Mock LLM responses** — Don't call real APIs in tests
2. **Test edge cases** — Empty inputs, errors, timeouts
3. **Use fixtures** — Reusable test setup
4. **Test async properly** — Use pytest-asyncio
5. **Measure performance** — Track latency and throughput
6. **Test in CI** — Run tests on every push
7. **Code coverage** — Aim for > 80%

## Next Steps

- [Best Practices](/best-practices/testing)
- [Performance Optimization](/guide/performance-optimization)
- [CI/CD Guide](/ops/n8n-cicd)
