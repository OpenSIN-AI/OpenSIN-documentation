# Advanced Agent Configuration

Master every configuration option for OpenSIN agents.

## Agent Configuration Options

```python
from opensin import Agent, AgentConfig

config = AgentConfig(
    # Core Settings
    name="my-agent",
    model="gpt-4",
    system_prompt="You are a helpful assistant.",
    temperature=0.7,
    max_tokens=4000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    
    # Memory Settings
    memory_enabled=True,
    memory_max_tokens=8000,
    memory_strategy="sliding_window",  # or "summary", "vector"
    memory_ttl=3600,  # 1 hour
    
    # Tool Settings
    tools=["web_search", "code_interpreter", "calculator"],
    tool_choice="auto",  # or "required", "none"
    tool_timeout=30,  # seconds
    
    # Performance Settings
    streaming=True,
    prompt_caching=True,
    response_format="text",  # or "json_object"
    
    # Security Settings
    sandbox_enabled=True,
    max_api_calls_per_minute=60,
    max_tokens_per_request=4000,
    
    # Retry Settings
    max_retries=3,
    retry_delay=1.0,
    retry_on=["timeout", "rate_limit"],
    
    # Logging Settings
    log_level="INFO",
    log_requests=True,
    log_responses=True,
    log_tokens=True,
)

agent = Agent(config=config)
```

## Model Selection Guide

| Model | Best For | Cost | Speed |
|-------|----------|------|-------|
| gpt-4 | Complex reasoning, code | $$$ | Medium |
| gpt-3.5-turbo | Simple tasks, chat | $ | Fast |
| claude-sonnet | Analysis, writing | $$ | Medium |
| claude-haiku | Classification, extraction | $ | Fast |
| gemini-pro | Multimodal tasks | $$ | Medium |
| local-llama | Privacy, offline | Free | Varies |

## Temperature Guide

| Temperature | Behavior | Use Case |
|-------------|----------|----------|
| 0.0 | Deterministic, consistent | Data extraction, classification |
| 0.2-0.4 | Focused, reliable | Code generation, analysis |
| 0.5-0.7 | Balanced, creative | General tasks, writing |
| 0.8-1.0 | Creative, varied | Brainstorming, ideation |
| 1.0-2.0 | Wild, unpredictable | Creative writing, art |

## Memory Strategies

### Sliding Window

```python
config.memory_strategy = "sliding_window"
config.memory_max_tokens = 8000
# Keeps most recent messages, drops oldest
```

### Summary

```python
config.memory_strategy = "summary"
config.memory_max_tokens = 4000
# Summarizes old messages to save tokens
```

### Vector

```python
config.memory_strategy = "vector"
config.memory_max_tokens = 16000
# Stores embeddings, retrieves by relevance
```

## Tool Configuration

```python
# Define custom tools
from opensin.tools import Tool

calculator = Tool(
    name="calculator",
    description="Perform mathematical calculations",
    parameters={
        "expression": {
            "type": "string",
            "description": "Math expression to evaluate"
        }
    },
    handler=lambda expr: eval(expr)
)

agent.register_tool(calculator)
```

## Best Practices

1. **Start simple** — Begin with basic config, add complexity as needed
2. **Monitor costs** — Track token usage and adjust max_tokens
3. **Use streaming** — Better UX with faster first token
4. **Cache prompts** — Save 50-80% on repeated prompts
5. **Set timeouts** — Prevent hanging requests
6. **Test models** — Benchmark different models for your use case
7. **Log everything** — Essential for debugging and optimization

## Next Steps

- [Agent Basics](/guide/agent-basics)
- [Performance Optimization](/guide/performance-optimization)
- [Cost Tracking](/guide/sin-cost-tracking)
