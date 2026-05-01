# Scaling

Scale OpenSIN agents for high-throughput workloads.

## Horizontal Scaling

Add more agent replicas to handle increased load.

## Vertical Scaling

Increase resources (memory, CPU) for individual agents.

## Auto-Scaling

Configure auto-scaling based on metrics:

```yaml
minReplicas: 2
maxReplicas: 50
targetCPU: 70%
```

## Next Steps

- [Monitoring](/guide/monitoring)
- [Deployment](/guide/deployment)

---

## Relevante Mandate

| Mandat                  | Priority | Doku                                |
| ----------------------- | -------- | ----------------------------------- |
| **Bun-Only**            | -1.5     | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot**     | -5.0     | KEINE Diagnose ohne Beweis          |
| **Test-Beweis-Pflicht** | 0.0      | KEIN "Done" ohne echten Test-Lauf   |

→ [Alle Mandate](/best-practices/code-quality)
