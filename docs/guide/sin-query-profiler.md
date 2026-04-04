# SIN Query Profiler — Performance Measurement

> **OpenSIN's Query Profiler** — Geklont aus Claude Code's queryProfiler.ts. Query-Performance messen und optimieren.

## Profiler Implementation

```python
from opensin.profiler import QueryProfiler

profiler = QueryProfiler(
    checkpoints=["init", "api_call", "tool_exec", "compact", "complete"]
)

# Checkpoints setzen
profiler.checkpoint("init")
# ... Query startet ...
profiler.checkpoint("api_call")
# ... API Call ...
profiler.checkpoint("tool_exec")
# ... Tool Execution ...
profiler.checkpoint("complete")

# Report generieren
report = profiler.generate_report()
print(f"Total duration: {report.total_duration}ms")
print(f"API call: {report.api_call_duration}ms")
print(f"Tool exec: {report.tool_exec_duration}ms")
```

## Checkpoint System

```python
class QueryProfiler:
    def __init__(self):
        self.checkpoints = {}
        self.start_time = time.time()
    
    def checkpoint(self, name: str):
        """Setzt einen Checkpoint."""
        self.checkpoints[name] = {
            "timestamp": time.time(),
            "elapsed_ms": (time.time() - self.start_time) * 1000
        }
    
    def get_duration(self, start: str, end: str) -> float:
        """Berechnet Dauer zwischen zwei Checkpoints."""
        return (
            self.checkpoints[end]["timestamp"]
            - self.checkpoints[start]["timestamp"]
        ) * 1000
```

## Performance Targets

| Phase | Target | Current |
|-------|--------|---------|
| Init | < 50ms | TBD |
| API Call | < 2000ms | TBD |
| Tool Exec | < 500ms | TBD |
| Compact | < 1000ms | TBD |
| Total | < 5000ms | TBD |

## Best Practices

1. **Checkpoint everything** — Alle wichtigen Phasen messen
2. **Track over time** — Performance-Trends analysieren
3. **Set targets** — Performance-Ziele definieren
4. **Alert on regression** — Bei Verschlechterung alarmieren

## Next Steps

- [Performance Optimization](/guide/performance-optimization)
- [SIN ReAct Loop](/guide/sin-react-loop)
