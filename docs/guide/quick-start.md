# Quick Start

Use this page when you want the **shortest possible path** to a real OpenSIN session.

For the full, launch-gate-safe explanation, use [Getting Started](/guide/getting-started).

## Verified quick path today

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code
bun install
bun run build
opensin-code
```

Inside the CLI:

```text
/help
Explain this repository and propose the smallest safe first change.
```

## Why this page does not promise `curl | sh` yet

The V1 launch plan expects a public installer flow, but that work is still tracked in [OpenSIN-Code#1117](https://github.com/OpenSIN-AI/OpenSIN-Code/issues/1117).

Until that gate closes, the source-build route above is the honest quick path.

## Next steps

- [Getting Started](/guide/getting-started)
- [OpenSIN-Code CLI Reference](/guide/opensin-code)
- [Agent Author Guide](/guide/how-to-configure-agents)
- [Backend V1 API](/api/backend-v1)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` — npm ist im OpenSIN-Ökosystem gebannt |
| **Annahmen-Verbot** | -5.0 | Nur dokumentieren, was mit Repo- oder Issue-Evidenz belegt ist |
| **Test-Beweis-Pflicht** | 0.0 | Kein "Done" ohne echten Build- oder Laufnachweis |

→ [Alle Mandate](/best-practices/code-quality)
