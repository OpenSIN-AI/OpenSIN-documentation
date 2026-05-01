# Deployment

Deploy OpenSIN agents to production environments.

## Options

| Platform            | Best For          | Cost        |
| ------------------- | ----------------- | ----------- |
| Hugging Face Spaces | Quick prototyping | Free        |
| Docker              | Self-hosted       | Server cost |
| Kubernetes          | Production scale  | Variable    |
| AWS Lambda          | Serverless        | Pay per use |

## Quick Deploy

```bash
opensin deploy hf --space my-opensin-app --hardware cpu-basic
```

## Next Steps

- [Monitoring](/guide/monitoring)
- [Scaling](/guide/scaling)

---

## Relevante Mandate

| Mandat                  | Priority | Doku                                |
| ----------------------- | -------- | ----------------------------------- |
| **Bun-Only**            | -1.5     | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot**     | -5.0     | KEINE Diagnose ohne Beweis          |
| **Test-Beweis-Pflicht** | 0.0      | KEIN "Done" ohne echten Test-Lauf   |

→ [Alle Mandate](/best-practices/code-quality)
