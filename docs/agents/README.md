# 🤖 A2A Agents — Documentation

> **Stand:** 2026-04-04 | **Total Agents:** 21 | **Status:** ✅ All configured

## Overview

A2A (Agent-to-Agent) Agents sind spezialisierte KI-Agenten die bestimmte Aufgaben autonom erledigen.

## Agent Registry

| # | Agent | Model | Fallback | Reasoning | Steps | Purpose |
|---|-------|-------|----------|-----------|-------|---------|
| 1 | [Atlas (Plan Executor)](./atlas-plan-executor.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Executes plans with high reasoning depth and unlimited steps |
| 2 | [Hephaestus (Deep Agent)](./hephaestus-deep-agent.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Deep analysis agent for complex code exploration and debugging |
| 3 | [Metis (Plan Consultant)](./metis-plan-consultant.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Strategic planning consultant for architecture and design decisions |
| 4 | [Momus (Plan Critic)](./momus-plan-critic.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Critical reviewer that identifies flaws and risks in plans |
| 5 | [Prometheus (Plan Builder)](./prometheus-plan-builder.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Builds comprehensive plans from requirements and constraints |
| 6 | [Sisyphus (Ultraworker)](./sisyphus-ultraworker.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Heavy computation agent for large-scale code transformations |
| 7 | [Sisyphus-Junior (Fast-Ultraworker)](./sisyphus-junior-fast-ultraworker.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Fast ultraworker for medium-complexity batch tasks |
| 8 | [artistry](./artistry.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Creative tasks including UI/UX design and visual content generation |
| 9 | [build](./build.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Code building, compilation, and package management |
| 10 | [compaction](./compaction.md) | — | openrouter/nvidia/nemotron-3-super-free | — | — | Context compaction and conversation summarization |
| 11 | [explore](./explore.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Codebase exploration and dependency analysis |
| 12 | [general](./general.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | General-purpose agent for everyday coding tasks |
| 13 | [librarian](./librarian.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Documentation management and knowledge base organization |
| 14 | [multimodal-looker](./multimodal-looker.md) | google/antigravity-gemini-3.1-pro | openrouter/nvidia/nemotron-3-super-free | — | — | Multimodal analysis for images, PDFs, and visual content |
| 15 | [omoc](./omoc.md) | — | openrouter/nvidia/nemotron-3-super-free | — | — | OMOC swarm coordination and multi-agent orchestration |
| 16 | [oracle](./oracle.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Architecture analysis and system design consulting |
| 17 | [plan](./plan.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Planning and roadmap creation for complex projects |
| 18 | [sin-executor-solo](./sin-executor-solo.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Solo execution agent for independent task completion |
| 19 | [sin-zeus](./sin-zeus.md) | openrouter/qwen/qwen3.6-plus:free | openrouter/nvidia/nemotron-3-super-free | — | — | Control-plane orchestration for SIN Code cloud workforce |
| 20 | [summary](./summary.md) | — | openrouter/nvidia/nemotron-3-super-free | — | — | Text summarization and content condensation |
| 21 | [title](./title.md) | — | openrouter/nvidia/nemotron-3-super-free | — | — | Title generation for sessions and documents |

## Agent Configuration

```json
{
  "agent": {
    "agent-name": {
      "model": "openrouter/qwen/qwen3.6-plus:free",
      "fallback": "openrouter/nvidia/nemotron-3-super-free",
      "maxSteps": 999999,
      "reasoning": "high"
    }
  }
}
```

---

*Last updated: 2026-04-04 by SIN-Zeus*