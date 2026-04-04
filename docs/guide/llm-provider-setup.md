# LLM Provider Setup Guide

Configure and optimize LLM providers for OpenSIN agents.

## Supported Providers

| Provider | Models | Setup |
|----------|--------|-------|
| OpenAI | GPT-4, GPT-3.5, o1 | API key |
| Anthropic | Claude Sonnet, Opus, Haiku | API key |
| Google | Gemini Pro, Flash | OAuth/API key |
| Mistral | Mistral Large, Medium, Small | API key |
| Groq | Llama, Mixtral (ultra-fast) | API key |
| Ollama | Local models (Llama, Mistral) | Local install |
| TogetherAI | 50+ open source models | API key |
| Cerebras | Llama (ultra-low latency) | API key |

## OpenAI Setup

```bash
export OPENAI_API_KEY=sk-...
```

```python
from opensin import Agent

agent = Agent(
    name="assistant",
    model="gpt-4",  # or gpt-3.5-turbo, o1
    provider="openai"
)
```

## Anthropic Setup

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

```python
agent = Agent(
    name="assistant",
    model="claude-sonnet-4-6",  # or claude-opus, claude-haiku
    provider="anthropic"
)
```

## Google Setup

```bash
export GOOGLE_API_KEY=AIza...
```

```python
agent = Agent(
    name="assistant",
    model="gemini-pro",  # or gemini-flash
    provider="google"
)
```

## Ollama (Local) Setup

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull model
ollama pull llama3.1:70b

# Configure
export OLLAMA_BASE_URL=http://localhost:11434
```

```python
agent = Agent(
    name="assistant",
    model="llama3.1:70b",
    provider="ollama"
)
```

## Model Comparison

| Model | Context | Speed | Cost/1K | Best For |
|-------|---------|-------|---------|----------|
| GPT-4 | 128K | Medium | $0.03 | Complex reasoning |
| GPT-3.5 | 16K | Fast | $0.002 | Simple tasks |
| Claude Sonnet | 200K | Medium | $0.015 | Analysis, writing |
| Claude Haiku | 200K | Fast | $0.001 | Classification |
| Gemini Pro | 32K | Medium | $0.005 | Multimodal |
| Llama 3.1 70B | 128K | Varies | Free | Local, private |

## Best Practices

1. **Start with GPT-4** — Best balance of quality and cost
2. **Use Haiku for simple tasks** — 90% cheaper than Sonnet
3. **Cache prompts** — Save 50-80% on repeated prompts
4. **Monitor costs** — Set budget limits
5. **Test locally** — Use Ollama for development

## Next Steps

- [Agent Configuration](/guide/agent-configuration)
- [Cost Tracking](/guide/sin-cost-tracking)
