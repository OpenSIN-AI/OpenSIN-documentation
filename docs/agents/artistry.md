# artistry

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
  "model": "openrouter/qwen/qwen3.6-plus:free",
  "options": {
    "reasoningEffort": "high"
  },
  "steps": 999999,
  "fallback": "openrouter/nvidia/nemotron-3-super-free"
}
```

## Usage

```bash
opencode run --agent "artistry" "your task here"
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
