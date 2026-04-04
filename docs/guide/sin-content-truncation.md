# SIN Content Truncation — Model-Facing Warnings

> **OpenSIN's Content Truncation** — Geklont aus Claude Code. Warnt das Modell wenn Limits erreicht werden.

## Das Problem

Wenn MEMORY.md oder Context zu groß wird, muss gekappt werden. Ohne Warning weiß das Modell nicht dass Infos fehlen.

## Die Lösung: Model-Facing Warnings

```python
from opensin.memory import ContentTruncator

truncator = ContentTruncator(
    max_lines=200,
    max_bytes=25000,
    warning_template="⚠️ {cap_type} capped at {limit}. Oldest entries removed."
)

# Prüfe und truncate
result = truncator.truncate(content)

if result.truncated:
    # Warning wird dem Modell angezeigt
    content = result.content + "\n\n" + result.warning
```

## Warning Types

| Cap Type | Limit | Warning Message |
|----------|-------|----------------|
| Lines | 200 | "⚠️ Index capped at 200 lines. Oldest entries removed." |
| Bytes | 25KB | "⚠️ Index capped at 25KB. Oldest entries removed." |
| Tokens | 8000 | "⚠️ Context capped at 8000 tokens. Oldest messages summarized." |

## Implementation

```python
class ContentTruncator:
    def truncate(self, content: str) -> TruncationResult:
        lines = content.split('\n')
        bytes_count = len(content.encode('utf-8'))
        
        truncated = False
        warning = ""
        
        # Line Cap
        if len(lines) > self.max_lines:
            lines = lines[-self.max_lines:]
            truncated = True
            warning = self.warning_template.format(
                cap_type="Index",
                limit=f"{self.max_lines} lines"
            )
        
        # Byte Cap
        content = '\n'.join(lines)
        if len(content.encode('utf-8')) > self.max_bytes:
            content = content[-self.max_bytes:]
            truncated = True
            warning = self.warning_template.format(
                cap_type="Index",
                limit=f"{self.max_bytes // 1000}KB"
            )
        
        return TruncationResult(
            content=content,
            truncated=truncated,
            warning=warning
        )
```

## Best Practices

1. **Always warn** — Modell muss wissen dass Content fehlt
2. **Keep newest** — Älteste Einträge zuerst entfernen
3. **Clear messages** — Explizite Warning Messages
4. **Monitor truncation** — Tracke wie oft gekappt wird

## Next Steps

- [SIN File Memory](/guide/sin-file-memory)
- [Memory Management](/guide/memory-management)
