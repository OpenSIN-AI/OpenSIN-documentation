# SIN Task Summary — Background Session Summaries

> **OpenSIN's Task Summary** — Geklont aus Claude Code's taskSummary.js. Zusammenfassungen für Background-Sessions.

## Implementation

```python
from opensin.summary import TaskSummary

summarizer = TaskSummary(
    model="gpt-3.5-turbo",
    max_length=500,
    include_key_decisions=True,
    include_code_changes=True
)

# Generate summary
summary = await summarizer.generate(session_messages)
print(summary)
```

## Summary Format

```markdown
# Task Summary

## Key Decisions
- Decision 1
- Decision 2

## Code Changes
- File 1: Description
- File 2: Description

## Open Questions
- Question 1
- Question 2

## Next Steps
- Step 1
- Step 2
```

## Best Practices

1. **Fast model** — GPT-3.5 für Summaries reicht
2. **Include key info** — Wichtige Entscheidungen und Änderungen
3. **Max length** — Summaries kurz halten
4. **Structured format** — Maschinenlesbar + menschlich lesbar
5. **Store with session** — Summary mit Session speichern

## Next Steps

- [SIN Session Memory](/guide/sin-session-memory)
- [SIN Dream Agent](/guide/sin-multi-agent-types)
