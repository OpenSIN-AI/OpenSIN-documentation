# SIN Agent Frontmatter — Markdown Agent Definitions

> **OpenSIN's Agent Frontmatter** — Geklont aus Claude Code's loadAgentsDir.ts. Agenten als Markdown-Dateien definieren.

## Agent Definition Format

```markdown
---
name: code-reviewer
description: Review code for bugs, security issues, and performance problems
tools: Glob, Grep, Read, Edit, Bash
model: sonnet
color: red
permissionMode: acceptEdits
maxTurns: 10
memory: true
hooks:
  - event: PreToolUse
    matcher: "Edit"
    command: python3 hooks/review_check.py
mcpServers:
  - name: github
    command: npx -y @modelcontextprotocol/server-github
skills:
  - code-review-best-practices
  - security-audit-checklist
isolation: worktree
background: false
effort: high
---

You are a senior code reviewer with 15+ years of experience in Python, TypeScript, and Go.

## Review Guidelines
1. Check for bugs and logic errors
2. Identify security vulnerabilities
3. Suggest performance improvements
4. Verify code style compliance
5. Ensure adequate test coverage

## Output Format
Provide a structured review with:
- Summary of changes
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (nice to have)
- Overall score (1-10)
```

## Frontmatter Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Agent identifier |
| `description` | string | ✅ | What the agent does |
| `tools` | string[] | ✅ | Available tools |
| `model` | string | ❌ | LLM model (default: sonnet) |
| `color` | string | ❌ | UI color for identification |
| `permissionMode` | string | ❌ | default/acceptEdits/bypass/dontAsk/auto |
| `maxTurns` | number | ❌ | Maximum conversation turns |
| `memory` | boolean | ❌ | Enable persistent memory |
| `hooks` | HookDef[] | ❌ | Agent-scoped hooks |
| `mcpServers` | MCPDef[] | ❌ | Agent-specific MCP servers |
| `skills` | string[] | ❌ | Auto-loaded skills |
| `isolation` | string | ❌ | none/worktree |
| `background` | boolean | ❌ | Run as background agent |
| `effort` | string | ❌ | low/medium/high |

## Agent Discovery

```python
from opensin.agents import AgentLoader

loader = AgentLoader(
    paths=[
        ".sin/agents/",           # User agents
        ".sin/plugins/*/agents/", # Plugin agents
        "/etc/sin/agents/",       # System agents
    ]
)

# Load all agents
agents = await loader.load_all()

# Find agent by name
agent = await loader.find("code-reviewer")
```

## Plugin Agents

```markdown
---
name: security-auditor
description: Perform security audits on code changes
tools: Glob, Grep, Read, Bash
model: opus
permissionMode: default
effort: high
---

You are a security auditor specializing in...
```

## Agent Priority Resolution

When multiple agents with same name exist:

1. Built-in agents (highest priority)
2. Plugin agents
3. User agents (`.sin/agents/`)
4. Project agents (`.sin/agents/`)
5. Flag agents (CLI flags)
6. Managed agents (enterprise policy)

## Best Practices

1. **Clear descriptions** — Help users understand what agent does
2. **Minimal tools** — Only include necessary tools
3. **Appropriate model** — Use cheaper models for simple tasks
4. **Permission modes** — Set appropriate permission level
5. **Hook integration** — Use hooks for automation

## Next Steps

- [SIN Fork Subagent](/guide/sin-fork-subagent)
- [SIN Plugin System](/guide/sin-plugins)
