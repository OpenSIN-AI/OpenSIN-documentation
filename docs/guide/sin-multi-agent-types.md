# SIN Multi-Agent Types — 7 Agent Types

> **OpenSIN's Agent Types** — Geklont aus Claude Code's Task.ts. 7 verschiedene Agent-Typen für verschiedene Use Cases.

## Agent Types

| Type | Description | Use Case |
|------|-------------|----------|
| `local_bash` | Shell command execution | Simple bash tasks |
| `local_agent` | Subprocess agent | Isolated agent execution |
| `remote_agent` | Remote agent (CCR) | Cloud-based agents |
| `in_process_teammate` | In-process parallel agent | Fast parallel work |
| `local_workflow` | Workflow agent | Multi-step workflows |
| `monitor_mcp` | MCP monitoring agent | MCP server monitoring |
| `dream` | Auto-dream consolidation | Memory consolidation |

## Local Bash Agent

```python
from opensin.agents import BashAgent

agent = BashAgent(
    name="bash-helper",
    working_directory="/path/to/project",
    timeout=30
)

result = await agent.execute("git status")
```

## Local Agent (Subprocess)

```python
from opensin.agents import LocalAgent

agent = LocalAgent(
    name="researcher",
    model="gpt-4",
    system_prompt="You are an expert researcher.",
    tools=["web_search", "summarizer"],
    timeout=120
)

result = await agent.execute("Research AI trends for 2026")
```

## Remote Agent (CCR)

```python
from opensin.agents import RemoteAgent

agent = RemoteAgent(
    name="cloud-researcher",
    endpoint="https://api.opensin.ai/v1/agents/researcher",
    auth_token="your-token",
    timeout=300
)

result = await agent.execute("Deep research on quantum computing")
```

## In-Process Teammate

```python
from opensin.agents import InProcessTeammate

teammate = InProcessTeammate(
    name="parallel-analyst",
    model="gpt-3.5-turbo",
    system_prompt="Analyze this data.",
    tools=["data_analysis"]
)

# Runs in same process — no subprocess overhead
result = await teammate.execute(data)
```

## Local Workflow Agent

```python
from opensin.agents import WorkflowAgent

agent = WorkflowAgent(
    name="data-pipeline",
    steps=[
        {"agent": "ingest", "action": "load_data"},
        {"agent": "clean", "action": "clean_data"},
        {"agent": "analyze", "action": "analyze_data"},
        {"agent": "report", "action": "generate_report"}
    ]
)

result = await agent.execute()
```

## Monitor MCP Agent

```python
from opensin.agents import MonitorMCPAgent

agent = MonitorMCPAgent(
    name="mcp-monitor",
    mcp_servers=["github", "slack", "jira"],
    check_interval=60
)

# Monitor MCP server health
status = await agent.check_health()
```

## Dream Agent (Memory Consolidation)

```python
from opensin.agents import DreamAgent

agent = DreamAgent(
    name="dreamer",
    memory_path=".sin/memory",
    consolidation_interval=86400  # Daily
)

# Consolidate daily logs into topic files
await agent.consolidate()
```

## Agent Type Selection Guide

| Task Complexity | Recommended Type | Model |
|----------------|------------------|-------|
| Simple bash | `local_bash` | N/A |
| Single task | `local_agent` | sonnet |
| Complex research | `remote_agent` | opus |
| Parallel analysis | `in_process_teammate` | haiku |
| Multi-step workflow | `local_workflow` | sonnet |
| MCP monitoring | `monitor_mcp` | haiku |
| Memory consolidation | `dream` | sonnet |

## Best Practices

1. **Right type for task** — Don't over-engineer simple tasks
2. **In-process for speed** — Use teammates for parallel work
3. **Remote for heavy tasks** — Offload complex work to cloud
4. **Monitor MCP servers** — Use monitor agent for health checks
5. **Dream regularly** — Consolidate memory daily

## Next Steps

- [SIN Fork Subagent](/guide/sin-fork-subagent)
- [SIN Subagents](/guide/sin-subagents)
