# Agent Testing Strategies

Comprehensive testing approaches for AI agents.

## Testing Pyramid for Agents

```
         ┌─────────────┐
         │  E2E Tests  │  ← Full agent workflows
        ┌┴─────────────┴┐
       │ Integration Tests│  ← Agent + tools + memory
      ┌┴─────────────────┴┐
     │    Unit Tests       │  ← Individual components
    ┌┴─────────────────────┴┐
   │    Mock Tests          │  ← Isolated function tests
```

## Unit Testing Agents

### Test Agent Responses

```python
import pytest
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
```

### Test Tools

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

### Test Agent + Memory

```python
@pytest.mark.asyncio
async def test_agent_memory():
    agent = Agent(name="memory-agent", memory_enabled=True)
    
    await agent.send("My name is Alice")
    response = await agent.send("What's my name?")
    
    assert "Alice" in response.content
```

### Test Agent + Tools

```python
@pytest.mark.asyncio
async def test_agent_with_web_search():
    agent = Agent(name="researcher", tools=["web_search"])
    
    response = await agent.send("What is the capital of France?")
    
    assert "Paris" in response.content
```

## E2E Testing

### Full Workflow Test

```python
@pytest.mark.asyncio
async def test_support_workflow():
    # Create team
    team = Team(
        name="support",
        agents=[triage_agent, response_agent, escalation_agent]
    )
    
    # Execute workflow
    result = await team.execute({
        "ticket": "I can't login to my account",
        "customer": "user@example.com"
    })
    
    # Verify results
    assert result.classification == "account"
    assert result.priority == "P1"
    assert result.response is not None
```

## Property-Based Testing

```python
from hypothesis import given, strategies as st

@given(st.text(min_size=1, max_size=1000))
@pytest.mark.asyncio
async def test_agent_handles_any_input(prompt):
    agent = Agent(name="test-agent")
    response = await agent.send(prompt)
    assert response is not None
    assert response.content is not None
```

## Regression Testing

```python
from opensin.testing import RegressionTest

# Save baseline
baseline = RegressionTest(agent, test_prompts)
baseline.save("baseline.json")

# Test against baseline
current = RegressionTest(agent, test_prompts)
diff = current.compare("baseline.json")

if diff.has_regressions:
    print(f"Regressions found: {diff.regressions}")
```

## Best Practices

1. **Mock LLM calls** — Don't call real APIs in tests
2. **Test edge cases** — Empty inputs, errors, timeouts
3. **Test tools individually** — Then test together
4. **Use fixtures** — Reusable test setup
5. **Test async properly** — Use pytest-asyncio

## Next Steps

- [Testing Guide](/guide/testing-guide)
- [Agent Evaluation](/guide/agent-evaluation)
