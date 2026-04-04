# SIN Fork Subagent — Cache-Optimierte Parallel Agents

> **OpenSIN's Fork Subagent** — Der innovativste Pattern aus Claude Code. Byte-identische API-Prefixes für maximale Cache Hits.

## Das Problem

Wenn du mehrere Subagents parallel startest, hat jeder einen anderen API-Prefix → kein Prompt Caching → hohe Kosten.

## Die Lösung: Fork Subagent

```python
from opensin.subagent import ForkSubagent

# Impliziter Fork — erbt vollen Kontext vom Parent
fork = ForkSubagent(
    parent=parent_agent,
    task="Analyze this code section",
    cache_prefix=True  # Byte-identischer Prefix!
)

result = await fork.execute()
```

## Cache-Identical Prefix Pattern

```python
class ForkSubagent:
    """Erstellt byte-identische API-Requests für maximale Cache Hits."""
    
    async def execute(self):
        # 1. Placeholder Tool Result verwenden
        placeholder = self.FORK_PLACEHOLDER_RESULT
        
        # 2. Byte-identischen Prefix aufbauen
        prefix = self.build_cache_identical_prefix()
        
        # 3. API Call mit gleichem Prefix wie andere Forks
        response = await self.api.call(
            prefix=prefix,  # Identisch über alle Forks!
            suffix=self.task_suffix
        )
        
        return response
```

## Worktree Isolation

```python
from opensin.subagent import WorktreeIsolation

isolation = WorktreeIsolation(
    repo_path="/path/to/repo",
    branch="feature-branch"
)

# Erstelle isolierten Worktree
worktree = await isolation.create()

# Agent arbeitet im isolierten Worktree
agent = Agent(name="isolated-agent", cwd=worktree.path)
result = await agent.execute(task)

# Auto-Commit Änderungen
if worktree.has_changes:
    await worktree.commit("Agent changes")
else:
    await worktree.cleanup()  # Keine Änderungen → aufräumen
```

## Background-to-Foreground Transition

```python
from opensin.subagent import BackgroundAgent

# Starte als Background Agent
bg_agent = BackgroundAgent(
    name="researcher",
    task="Research AI trends",
    output_file="research_output.md"
)

await bg_agent.start()

# ... warte auf Output ...

# Transition zu Foreground
fg_agent = await bg_agent.transition_to_foreground()
result = await fg_agent.continue_execution()
```

## Agent Definition via Markdown

```markdown
---
name: code-reviewer
description: Review code for bugs and security issues
tools: Glob, Grep, Read, Edit
model: sonnet
color: red
permissionMode: acceptEdits
maxTurns: 10
memory: true
hooks:
  - event: PreToolUse
    command: python3 hooks/security_check.py
mcpServers:
  - name: github
    command: npx -y @modelcontextprotocol/server-github
skills:
  - code-review-best-practices
isolation: worktree
background: false
effort: high
---

You are a senior code reviewer with 15+ years of experience...
```

## Best Practices

1. **Fork für parallele Tasks** — Maximale Cache Hits
2. **Worktree für riskante Änderungen** — Isolierte Ausführung
3. **Background für lange Tasks** — Nicht blockierend
4. **Markdown Definitionen** — Einfach zu warten
5. **Cache-Identical Prefixes** — Spart 50-80% Kosten

## Next Steps

- [SIN Subagents](/guide/sin-subagents)
- [SIN Hooks](/guide/sin-hooks)
