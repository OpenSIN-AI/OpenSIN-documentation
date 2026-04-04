# SIN Implementation Guide — From Claude Code to OpenSIN

Kompletter Implementierungsplan zum Klonen aller Claude Code Features nach OpenSIN.

## Implementation Priority

### Phase 1: Core Engine (Weeks 1-4)

```
Week 1: QueryEngine
├── src/engine/query_engine.py
├── src/engine/react_loop.py
├── src/engine/async_generator.py
└── tests/test_query_engine.py

Week 2: Tool System
├── src/tools/base.py
├── src/tools/factory.py
├── src/tools/assembly.py
├── src/tools/builtin/
│   ├── bash.py
│   ├── file_read.py
│   ├── file_edit.py
│   ├── web_search.py
│   └── ...
└── tests/test_tools.py

Week 3: Permission System
├── src/permissions/modes.py
├── src/permissions/rules.py
├── src/permissions/classifier.py
├── src/permissions/denial_tracker.py
└── tests/test_permissions.py

Week 4: Hook System
├── src/hooks/events.py
├── src/hooks/executor.py
├── src/hooks/session_store.py
├── src/hooks/modes/
│   ├── shell.py
│   ├── http.py
│   ├── function.py
│   └── agent.py
└── tests/test_hooks.py
```

### Phase 2: Agent System (Weeks 5-8)

```
Week 5: Subagent System
├── src/subagent/base.py
├── src/subagent/fork.py
├── src/subagent/background.py
├── src/subagent/worktree.py
└── tests/test_subagent.py

Week 6: Memory System
├── src/memory/index.py
├── src/memory/topics.py
├── src/memory/session.py
├── src/memory/sin_md.py
└── tests/test_memory.py

Week 7: MCP Integration
├── src/mcp/client.py
├── src/mcp/transports/
│   ├── stdio.py
│   ├── sse.py
│   ├── http.py
│   └── ws.py
├── src/mcp/auth.py
└── tests/test_mcp.py

Week 8: Sandbox
├── src/sandbox/adapter.py
├── src/sandbox/filesystem.py
├── src/sandbox/network.py
├── src/sandbox/git_escape.py
└── tests/test_sandbox.py
```

### Phase 3: CLI & UI (Weeks 9-12)

```
Week 9: CLI Framework
├── src/cli/main.py
├── src/cli/commands/
├── src/cli/completion.py
└── tests/test_cli.py

Week 10: TUI
├── src/tui/app.py
├── src/tui/components/
├── src/tui/keybindings.py
└── tests/test_tui.py

Week 11: Plugin System
├── src/plugins/loader.py
├── src/plugins/registry.py
├── src/plugins/builtin/
└── tests/test_plugins.py

Week 12: Integration & Testing
├── tests/integration/
├── tests/e2e/
├── benchmarks/
└── docs/
```

## Code Structure

```
opensin/
├── src/
│   ├── engine/           # QueryEngine, ReAct Loop
│   ├── tools/            # Tool System
│   ├── permissions/      # Permission System
│   ├── hooks/            # Hook System
│   ├── subagent/         # Subagent System
│   ├── memory/           # Memory System
│   ├── mcp/              # MCP Integration
│   ├── sandbox/          # Sandbox
│   ├── cli/              # CLI
│   ├── tui/              # Terminal UI
│   ├── plugins/          # Plugin System
│   └── utils/            # Utilities
├── tests/
├── docs/
├── examples/
└── pyproject.toml
```

## Key Implementation Details

### QueryEngine Async Generator

```python
class QueryEngine:
    async def submit_message(self, content: str) -> AsyncGenerator[Event, None]:
        self.messages.append(UserMessage(content=content))
        async for event in self.react_loop():
            yield event
            if self.should_stop():
                break
```

### Fork Subagent Cache Pattern

```python
class ForkSubagent:
    async def execute(self):
        prefix = self.build_cache_identical_prefix()
        response = await self.api.call(prefix=prefix, suffix=self.task)
        return response
```

### Hook Executor

```python
class HookExecutor:
    async def execute(self, event: str, context: dict):
        hooks = self.store.get(event)
        for hook in hooks:
            result = await hook.run(context)
            if not result.continue_:
                return result
        return HookResult(continue=True)
```

## Testing Strategy

```python
# Unit Tests
pytest tests/unit/ --cov=src --cov-report=html

# Integration Tests
pytest tests/integration/

# E2E Tests
pytest tests/e2e/

# Benchmarks
python benchmarks/run.py
```

## Next Steps

1. Phase 1 starten — QueryEngine implementieren
2. Tool System bauen
3. Permission System implementieren
4. Hook System bauen
5. Testing & Benchmarking
