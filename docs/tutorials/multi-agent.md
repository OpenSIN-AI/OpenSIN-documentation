---
title: Multi-Agent Teams Tutorial
description: Learn how to coordinate multiple agents
---

# Multi-Agent Teams Tutorial

Learn how to create and manage teams of OpenSIN agents.

## Step 1: Create Individual Agents

```bash
opensin agent create researcher --model openai/gpt-5.4
opensin agent create writer --model openai/gpt-5.4
opensin agent create reviewer --model openai/gpt-5.4
```

## Step 2: Create a Team

```bash
opensin team create research-team \
  --agents researcher,writer,reviewer \
  --strategy sequential
```

## Step 3: Execute Team Tasks

```bash
opensin team exec research-team \
  --task "Research AI trends, write a comprehensive report, and review it for accuracy"
```

## Team Strategies

| Strategy   | Description                       | Use Case             |
| ---------- | --------------------------------- | -------------------- |
| sequential | Agents work one after another     | Pipeline workflows   |
| parallel   | Agents work simultaneously        | Independent tasks    |
| consensus  | Agents vote on outcomes           | Decision making      |
| leader     | One agent coordinates others      | Complex coordination |
| pipeline   | Output of one feeds input of next | Data processing      |

## Next Steps

- [Advanced Orchestration](/tutorials/advanced-orchestration)
- [A2A Protocol](/guide/a2a-protocol)

---

## Relevante Mandate

| Mandat                   | Priority | Doku                                                    |
| ------------------------ | -------- | ------------------------------------------------------- |
| **Bun-Only**             | -1.5     | `bun install` / `bun run` statt npm                     |
| **LLM via opencode CLI** | -2.5     | `opencode run --format json` — KEINE direkten API-Calls |
| **A2A-Agenten-Pflicht**  | -200.0   | SELBST MACHEN via `create-a2a-sin-agent`                |
| **Kommentar-Pflicht**    | -6.0     | EXTREM umfangreiche Kommentare                          |

→ [Alle Mandate](/best-practices/a2a-communication)
