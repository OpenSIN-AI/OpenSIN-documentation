---
title: Agent Design Best Practices
description: Best practices for designing OpenSIN agents
---

# Agent Design Best Practices

## 1. Single Responsibility

Each agent should have one clear purpose.

```bash
# Good: Specialized agents
opensin agent create researcher --model gpt-4
opensin agent create writer --model gpt-4
opensin agent create reviewer --model gpt-4

# Bad: One agent doing everything
opensin agent create generalist --model gpt-4
```

## 2. Use Appropriate Models

Match model capability to task complexity.

| Task | Recommended Model |
|------|-------------------|
| Simple classification | gpt-3.5-turbo |
| Content generation | gpt-4 |
| Complex reasoning | gpt-4 |
| Code generation | gpt-4 |

## 3. Optimize System Prompts

Be specific and provide clear instructions.

```bash
# Good: Specific system prompt
opensin agent update researcher \
  --system-prompt "You are an expert researcher specializing in AI trends. Provide detailed, well-sourced reports with citations."

# Bad: Vague system prompt
opensin agent update researcher \
  --system-prompt "You are a helpful assistant."
```

## 4. Use Tools Wisely

Only enable tools that the agent needs.

```bash
# Good: Minimal tool set
opensin agent create researcher \
  --tools web_search,summarizer

# Bad: Too many tools
opensin agent create researcher \
  --tools web_search,summarizer,code_interpreter,file_read,file_write,web_fetch,bash
```

## 5. Monitor and Optimize

Track agent performance and costs.

```bash
# Check agent metrics
opensin agent metrics researcher

# View agent logs
opensin agent logs researcher

# Check costs
opensin cost --agent researcher
```

## Next Steps

- [Security Best Practices](/best-practices/security)
- [Performance Best Practices](/best-practices/performance)
