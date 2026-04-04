# SIN Skill Search — Experimental Skill Discovery

> **OpenSIN's Skill Search** — Geklont aus Claude Code's skillSearch/prefetch.ts. Experimentelle Skill-Suche.

## Implementation

```python
from opensin.skills import SkillSearch

search = SkillSearch(
    index_path=".sin/skills/index.json",
    max_results=5,
    relevance_threshold=0.7
)

# Search skills
results = await search.search("Python testing best practices")
for skill in results:
    print(f"{skill.name}: {skill.relevance}")
```

## Skill Prefetch

```python
from opensin.skills import SkillPrefetcher

prefetcher = SkillPrefetcher(
    search=search,
    max_prefetch=3,
    prefetch_on_idle=True
)

# Prefetch skills when idle
await prefetcher.prefetch_relevant_skills(user_context)
```

## Best Practices

1. **Experimental feature** — Noch in Entwicklung
2. **Relevance threshold** — Nur relevante Skills anzeigen
3. **Prefetch on idle** — Skills im Hintergrund vorladen
4. **Update index** — Skill-Index regelmäßig aktualisieren
5. **User feedback** — User-Feedback für Verbesserung nutzen

## Next Steps

- [SIN Skills](/guide/sin-skills)
- [SIN Plugin System](/guide/sin-plugins)
