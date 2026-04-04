# sin-executor-solo

> **Status:** ✅ Active | **Model:** openrouter/qwen/qwen3.6-plus:free

## Configuration

| Setting | Value |
|---------|-------|
| **Model** | openrouter/qwen/qwen3.6-plus:free |
| **Fallback** | openrouter/nvidia/nemotron-3-super-free |
| **Reasoning** | — |
| **Max Steps** | — |

## Raw Config

```json
{
  "mode": "primary",
  "model": "openrouter/qwen/qwen3.6-plus:free",
  "options": {
    "reasoningEffort": "medium"
  },
  "description": "Single-agent coding executor for deterministic task processing without swarm orchestration.",
  "prompt": "You are a direct single-agent coding executor. Work alone in the provided directory. Do not create or join swarms. Do not delegate. Do not edit governance/docs files unless the task explicitly requests docs/policy work. Prefer minimal concrete code changes, then report files changed and validations attempted.",
  "steps": 999999,
  "fallback": "openrouter/nvidia/nemotron-3-super-free"
}
```

## Usage

```bash
opencode run --agent "sin-executor-solo" "your task here"
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
