# Plugin Development Guide

Extend OpenSIN with custom plugins and tools.

## Overview

OpenSIN plugins allow you to add custom capabilities to agents without modifying the core system.

## Plugin Types

| Type | Purpose | Example |
|------|---------|---------|
| Tool Plugin | Add new tools to agents | Web scraper, calculator |
| Memory Plugin | Custom memory storage | Vector DB, Redis cache |
| Transport Plugin | Custom communication | Custom messaging protocol |
| Auth Plugin | Custom authentication | OAuth provider, SSO |
| Middleware Plugin | Request/response processing | Logging, rate limiting |

## Creating a Tool Plugin

### Basic Plugin

```python
from opensin.plugins import ToolPlugin, ToolDefinition

class WeatherPlugin(ToolPlugin):
    """Get weather information for a location."""
    
    name = "weather"
    version = "1.0.0"
    description = "Get current weather and forecasts"
    
    tools = [
        ToolDefinition(
            name="get_weather",
            description="Get current weather for a location",
            parameters={
                "location": {"type": "string", "required": True},
                "units": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            }
        )
    ]
    
    async def execute(self, tool_name: str, params: dict) -> dict:
        if tool_name == "get_weather":
            return await self._get_weather(params["location"], params.get("units", "celsius"))
        raise ValueError(f"Unknown tool: {tool_name}")
    
    async def _get_weather(self, location: str, units: str) -> dict:
        # Implementation
        return {"temperature": 22, "condition": "sunny", "units": units}
```

### Register Plugin

```python
from opensin import Agent

agent = Agent(name="weather-assistant", model="gpt-4")
agent.register_plugin(WeatherPlugin())

# Agent can now use weather tool
response = await agent.send("What's the weather in Berlin?")
```

## Creating a Memory Plugin

```python
from opensin.plugins import MemoryPlugin

class RedisMemoryPlugin(MemoryPlugin):
    """Store agent memory in Redis."""
    
    name = "redis-memory"
    version = "1.0.0"
    
    def __init__(self, redis_url: str):
        self.redis_url = redis_url
    
    async def store(self, key: str, value: dict) -> None:
        # Store in Redis
        pass
    
    async def retrieve(self, key: str) -> dict:
        # Retrieve from Redis
        pass
    
    async def search(self, query: str, limit: int = 10) -> list:
        # Search in Redis
        pass
    
    async def delete(self, key: str) -> None:
        # Delete from Redis
        pass
```

## Creating a Middleware Plugin

```python
from opensin.plugins import MiddlewarePlugin

class LoggingMiddleware(MiddlewarePlugin):
    """Log all agent requests and responses."""
    
    name = "logging"
    version = "1.0.0"
    
    async def on_request(self, request: dict) -> dict:
        print(f"Request: {request}")
        return request
    
    async def on_response(self, response: dict) -> dict:
        print(f"Response: {response}")
        return response
    
    async def on_error(self, error: Exception) -> None:
        print(f"Error: {error}")
```

## Plugin Configuration

### config.yaml

```yaml
plugins:
  - name: weather
    enabled: true
    config:
      api_key: "${WEATHER_API_KEY}"
      default_units: "celsius"
  
  - name: redis-memory
    enabled: true
    config:
      redis_url: "redis://localhost:6379"
      ttl: 3600
  
  - name: logging
    enabled: true
    config:
      level: "INFO"
      output: "file"
      path: "/var/log/opensin/plugins.log"
```

## Plugin Lifecycle

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Create  │───>│ Register │───>│  Execute │───>│  Destroy │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
                    │
                    v
              ┌──────────┐
              │ Configure│
              └──────────┘
```

## Publishing Plugins

### Package Structure

```
my-plugin/
├── pyproject.toml
├── README.md
├── src/
│   └── my_plugin/
│       ├── __init__.py
│       ├── plugin.py
│       └── tools/
│           └── my_tool.py
└── tests/
    └── test_plugin.py
```

### pyproject.toml

```toml
[project]
name = "opensin-my-plugin"
version = "1.0.0"
description = "My OpenSIN plugin"
requires-python = ">=3.10"
dependencies = ["opensin-sdk>=1.0"]

[project.entry-points."opensin.plugins"]
my-plugin = "my_plugin.plugin:MyPlugin"
```

### Publish

```bash
# Build
python -m build

# Publish to PyPI
python -m twine upload dist/*

# Or publish to OpenSIN Marketplace
opensin marketplace publish ./dist/opensin-my-plugin-1.0.0.tar.gz
```

## Best Practices

1. **Single responsibility** — Each plugin should do one thing well
2. **Error handling** — Handle all edge cases gracefully
3. **Configuration** — Make plugins configurable via environment variables
4. **Testing** — Write comprehensive tests
5. **Documentation** — Document all tools and parameters
6. **Versioning** — Follow semantic versioning
7. **Security** — Never expose secrets in plugin code

## Next Steps

- [Custom Agents](/tutorials/custom-agents)
- [MCP Integration](/guide/mcp-integration)
- [Best Practices](/best-practices/agent-design)
