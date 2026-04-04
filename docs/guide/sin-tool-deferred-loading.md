# SIN Tool Deferred Loading — ToolSearch Pattern

> **OpenSIN's ToolSearch** — Geklont aus Claude Code. Tools werden erst bei Bedarf geladen → kleinere Prompts → weniger Kosten.

## Das Problem

43+ Tools im Prompt = viele Tokens = hohe Kosten. Die meisten Tools werden pro Request nicht gebraucht.

## Die Lösung: Deferred Loading

```python
from opensin.tools import Tool

class ExpensiveTool(Tool):
    name = "expensive_operation"
    should_defer = True  # Nicht im initialen Prompt
    always_load = False  # Nur bei Bedarf
    
    async def execute(self, **kwargs):
        # Teure Operation
        pass
```

## ToolSearch Tool

```python
from opensin.tools import ToolSearchTool

class ToolSearchTool(Tool):
    """Ermöglicht dem Modell, Tools bei Bedarf zu entdecken."""
    
    name = "tool_search"
    description = "Search for available tools by name or description"
    
    async def execute(self, query: str) -> list[Tool]:
        """Suche Tools die zur Query passen."""
        matching_tools = []
        for tool in self.all_tools:
            if tool.should_defer and tool.matches(query):
                matching_tools.append(tool)
        return matching_tools
```

## Workflow

```
1. Initialer Prompt: Nur Basis-Tools (wenige Tokens)
2. Modell braucht spezielles Tool
3. Modell ruft ToolSearch auf
4. ToolSearch findet passendes Tool
5. Tool wird zum Prompt hinzugefügt
6. Modell nutzt das Tool
```

## Performance Impact

| Scenario | Initial Tokens | Cost per 1000 Requests |
|----------|---------------|----------------------|
| Alle Tools | 8000 | $30.00 |
| Deferred | 3000 | $11.25 |
| **Ersparnis** | **62% weniger** | **$18.75** |

## Implementation

```python
class ToolAssembly:
    def __init__(self):
        self.always_load_tools = []
        self.deferred_tools = []
        self.loaded_tools = set()
    
    def get_initial_tools(self) -> list[Tool]:
        """Nur always_load Tools im initialen Prompt."""
        return self.always_load_tools
    
    def search_tools(self, query: str) -> list[Tool]:
        """Suche deferred Tools die zur Query passen."""
        return [
            tool for tool in self.deferred_tools
            if tool.matches(query) and tool.name not in self.loaded_tools
        ]
    
    def load_tool(self, tool: Tool):
        """Lade ein Tool in den aktuellen Prompt."""
        self.loaded_tools.add(tool.name)
```

## Best Practices

1. **Basis-Tools immer laden** — Read, Grep, Glob
2. **Spezial-Tools deferen** — Expensive, selten genutzte Tools
3. **ToolSearch beschreiben** — Gute Beschreibungen für bessere Suche
4. **Monitor Usage** — Tracke welche Tools wie oft geladen werden

## Next Steps

- [SIN Tool System](/guide/sin-tool-system)
- [Cost Optimization](/guide/agent-cost-optimization)
