# SIN Job Classifier — Task Classification

> **OpenSIN's Job Classifier** — Geklont aus Claude Code's jobs/classifier.ts. Automatische Task-Klassifizierung.

## Implementation

```python
from opensin.jobs import JobClassifier

classifier = JobClassifier(
    model="gpt-3.5-turbo",
    categories=["code", "research", "writing", "analysis", "other"],
    confidence_threshold=0.7
)

# Classify task
result = await classifier.classify("Write a Python function to sort a list")
print(f"Category: {result.category}")
print(f"Confidence: {result.confidence}")
```

## Categories

| Category | Description | Example |
|----------|-------------|---------|
| Code | Programming tasks | "Write a function" |
| Research | Information gathering | "Research AI trends" |
| Writing | Content creation | "Write a blog post" |
| Analysis | Data analysis | "Analyze this dataset" |
| Other | Everything else | "What's the weather?" |

## Best Practices

1. **Fast model** — GPT-3.5 für Klassifizierung reicht
2. **Confidence threshold** — Nur hohe Confidence akzeptieren
3. **Fallback** — Bei niedriger Confidence → "other"
4. **Track accuracy** — Klassifizierungsgenauigkeit messen
5. **Update categories** — Kategorien regelmäßig aktualisieren

## Next Steps

- [SIN Auto Classifier](/guide/sin-auto-classifier)
- [SIN Coordinator Mode](/guide/sin-coordinator-mode)
