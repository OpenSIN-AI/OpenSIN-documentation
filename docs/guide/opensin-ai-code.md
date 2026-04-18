# OpenSIN-AI Code — Python Agent Development Platform

> **Update April 2026:** The standalone `OpenSIN-AI/opensin-ai-code` repository has been consolidated into the OpenSIN monorepo as `opensin_agent_platform/`.
>
> **New location:** [`OpenSIN-AI/OpenSIN/opensin_agent_platform`](https://github.com/OpenSIN-AI/OpenSIN/tree/main/opensin_agent_platform)

OpenSIN-AI Code is the Python-based Agent Development Platform. It was originally shipped as its own repo; as of the April 2026 consolidation it lives inside `OpenSIN` next to the other canonical Python packages (`opensin_core`, `opensin_cli`, `opensin_api`, `opensin_sdk`).

> **Status:** Preserved as reference material under `OpenSIN/opensin_agent_platform/`. Not yet wired into the `OpenSIN` build. The follow-up rationalization will port genuinely useful logic into `opensin_core` and retire the folder. See [`opensin_agent_platform/README.md`](https://github.com/OpenSIN-AI/OpenSIN/blob/main/opensin_agent_platform/README.md) for the plan.

## Why consolidated

- The standalone repo advertised `pip install opensin-ai-code` but shipped no `pyproject.toml`, so the install path never worked.
- It duplicated ground already covered by `opensin_core` in the `OpenSIN` repo (both define `hooks`, `plugins`, `skills`, QueryEngine, Tool/Permission/Memory systems).

Full rationale: [OpenSIN-overview consolidation report](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CONSOLIDATION-2026-04.md).

## Getting the source

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN.git
cd OpenSIN/opensin_agent_platform
```

All 100 Python files and 26 subsystem packages are preserved exactly as they were in the standalone repo.

## See also

- [OpenSIN Repository](https://github.com/OpenSIN-AI/OpenSIN) — the canonical Python monorepo
- [OpenSIN-AI Code Agent Comparison](opensin-ai-agent-features.md)
- [OpenSIN-AI Agent Feature Spec](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/opensin-ai-agent-feature-spec.md)
- [Canonical Repos Map](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md)
