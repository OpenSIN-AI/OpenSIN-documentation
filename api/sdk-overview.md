# SDK Overview

OpenSIN provides SDKs for multiple languages to integrate AI agents into your applications.

## Available SDKs

| Language | Package | Status |
|----------|---------|--------|
| Python | `opensin-sdk` | ✅ Stable |
| JavaScript/TypeScript | `@opensin/sdk` | ✅ Stable |
| Go | `github.com/opensin-ai/go-sdk` | 🔄 Beta |
| Rust | `opensin-sdk` (crates.io) | 🔄 Beta |
| Swift | `OpenSIN` (SPM) | 📋 Planned |

## Python SDK

### Installation

```bash
pip install opensin-sdk
```

### Quick Start

```python
from opensin import Client, Agent, Team

# Initialize client
client = Client(api_key="your-api-key")

# Create an agent
agent = Agent(
    name="assistant",
    model="gpt-4",
    system_prompt="You are a helpful assistant."
)

# Send a message
response = await agent.send("Hello, what can you do?")
print(response.content)

# Create a team
team = Team(
    name="research-team",
    agents=[researcher, writer, reviewer]
)

# Execute a task
result = await team.execute("Research AI trends and write a report")
```

### Core Classes

#### Client

```python
client = Client(
    api_key="your-api-key",
    base_url="https://api.opensin.ai",
    timeout=30,
    retries=3
)
```

#### Agent

```python
agent = Agent(
    name="my-agent",
    model="gpt-4",
    system_prompt="You are a helpful assistant.",
    temperature=0.7,
    max_tokens=4000,
    memory_enabled=True,
    tools=["search", "code_interpreter"]
)
```

#### Team

```python
team = Team(
    name="my-team",
    agents=[agent1, agent2, agent3],
    strategy="consensus",  # or "leader", "vote", "pipeline"
    max_iterations=10
)
```

### A2A Protocol

```python
from opensin.a2a import Message, AgentCard

# Get agent card
card = await client.get_agent_card("researcher")

# Send A2A message
message = Message(
    type="request",
    from_agent="writer",
    to_agent="researcher",
    content="Research AI trends for 2026"
)

response = await client.send_message(message)
```

## JavaScript/TypeScript SDK

### Installation

```bash
npm install @opensin/sdk
```

### Quick Start

```typescript
import { Client, Agent, Team } from '@opensin/sdk';

const client = new Client({ apiKey: 'your-api-key' });

const agent = new Agent({
  name: 'assistant',
  model: 'gpt-4',
  systemPrompt: 'You are a helpful assistant.'
});

const response = await agent.send('Hello!');
console.log(response.content);
```

## Error Handling

```python
from opensin import OpenSINError, RateLimitError, AuthenticationError

try:
    response = await agent.send(prompt)
except RateLimitError:
    # Wait and retry
    await asyncio.sleep(60)
    response = await agent.send(prompt)
except AuthenticationError:
    # Check API key
    print("Invalid API key")
except OpenSINError as e:
    print(f"Error: {e}")
```

## Next Steps

- [Python SDK Reference](/api/sdk-python)
- [JavaScript SDK Reference](/api/sdk-javascript)
- [A2A Protocol](/api/a2a)
- [Agent API](/api/agent)
