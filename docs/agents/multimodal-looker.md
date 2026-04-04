# multimodal-looker

> **Status:** ✅ Active | **Model:** google/antigravity-gemini-3.1-pro

## Configuration

| Setting | Value |
|---------|-------|
| **Model** | google/antigravity-gemini-3.1-pro |
| **Fallback** | openrouter/nvidia/nemotron-3-super-free |
| **Reasoning** | — |
| **Max Steps** | — |

## Raw Config

```json
{
  "model": "google/antigravity-gemini-3.1-pro",
  "options": {
    "reasoningEffort": "low"
  },
  "steps": 999999,
  "description": "Zero-Shot Object Detection & Vision Understanding via NVIDIA NIM",
  "fallback": "openrouter/nvidia/nemotron-3-super-free"
}
```

## Usage

```bash
opencode run --agent "multimodal-looker" "your task here"
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
