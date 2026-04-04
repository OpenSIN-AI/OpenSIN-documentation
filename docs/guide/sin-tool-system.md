# SIN Tool System — Rich Tool Interface

> **OpenSIN's Tool System** — Das umfassendste Tool-System für AI Agenten. 43+ Built-in Tools mit sicherer Factory.

## Tool Interface

```python
from opensin.tools import Tool, build_tool

@build_tool
class WebSearchTool(Tool):
    name = "web_search"
    description = "Search the web for information"
    
    input_schema = {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Search query"},
            "num_results": {"type": "integer", "default": 5}
        },
        "required": ["query"]
    }
    
    async def execute(self, query: str, num_results: int = 5) -> dict:
        """Führe die Websuche aus."""
        results = await self.search_engine.search(query, limit=num_results)
        return {"results": results, "total": len(results)}
    
    def check_permissions(self, input: dict) -> PermissionDecision:
        """Tool-spezifische Permission-Logik."""
        return PermissionDecision.ALLOW
    
    def is_read_only(self) -> bool:
        return True
    
    def is_concurrency_safe(self) -> bool:
        return True
    
    def to_auto_classifier_input(self, input: dict) -> dict:
        """Input für den Auto-Mode Classifier."""
        return {
            "tool": self.name,
            "action": f"Search web for: {input['query']}",
            "risk_level": "low"
        }
```

## Tool Assembly mit Cache Stability

```python
from opensin.tools import assemble_tool_pool

# Tools werden nach Namen sortiert für byte-identische Definitionen
tool_pool = assemble_tool_pool(
    built_in_tools=built_in_tools,
    mcp_tools=mcp_tools,
    permission_context=permission_context
)

# Sortierung garantiert gleiche Tool-Definitionen über Sessions
# → Maximale Prompt Cache Hits!
```

## ToolSearch Deferred Loading

```python
from opensin.tools import ToolSearchTool

# Tools mit shouldDefer=True erscheinen nicht im initialen Prompt
# Das Modell entdeckt sie bei Bedarf über ToolSearchTool

class ExpensiveTool(Tool):
    name = "expensive_tool"
    should_defer = True  # Nicht im initialen Prompt
    always_load = False  # Nur bei Bedarf laden
    
    async def execute(self, **kwargs):
        # Teure Operation
        pass
```

## Permission-Aware Tool Filtering

```python
from opensin.tools import filter_tools_by_deny_rules

# MCP Server-Prefix Rules
# mcp__github filtert ALLE Tools von diesem Server
# BEFORE das Modell sie sieht — nicht erst beim Aufruf!

filtered_tools = filter_tools_by_deny_rules(
    tools=all_tools,
    deny_rules=["mcp__github", "Bash(rm -rf *)"]
)
```

## Built-in Tools (43+)

| Tool | Beschreibung | Read-Only |
|------|-------------|-----------|
| `BashTool` | Shell Commands ausführen | ❌ |
| `FileReadTool` | Dateien lesen | ✅ |
| `FileEditTool` | Dateien bearbeiten | ❌ |
| `FileWriteTool` | Dateien schreiben | ❌ |
| `GlobTool` | Datei-Pattern Matching | ✅ |
| `GrepTool` | Content Search | ✅ |
| `WebFetchTool` | Webseiten laden | ✅ |
| `WebSearchTool` | Websuche | ✅ |
| `AgentTool` | Subagents spawnen | ❌ |
| `SkillTool` | Skills aufrufen | ✅ |
| `TodoWriteTool` | Tasks tracken | ✅ |
| `MCPTool` | MCP Tools proxy | ❌ |
| `ToolSearchTool` | Deferred Tool Loading | ✅ |

## Best Practices

1. **`build_tool()` Factory** — Sichere Defaults für alle Tools
2. **Sortierte Tool Assembly** — Byte-identische Definitionen
3. **ToolSearch Deferred Loading** — Vermeidet überfüllte Prompts
4. **Permission-Aware Filtering** — Filtert vor dem API Call
5. **Rich Metadata** — `is_read_only`, `is_concurrency_safe`, etc.

## Next Steps

- [Plugin Development](/guide/plugin-development)
- [SIN Permissions](/guide/sin-permissions)
