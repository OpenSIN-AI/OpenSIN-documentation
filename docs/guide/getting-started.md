---
title: Getting Started
description: The shortest honest path from docs.opensin.ai to a working OpenSIN CLI session.
---

# Getting Started

This page is the **V1 launch-path guide** for `docs.opensin.ai`.

Its job is simple: get an OSS user from the docs site to a working local OpenSIN CLI session as fast as possible, without pretending unfinished launch work is already done.

## What is verified today vs. what ships at V1

| Surface | Current state | Source |
|---|---|---|
| Installable TypeScript CLI | `OpenSIN-Code` is the canonical TypeScript CLI surface | [Canonical Repos](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/docs/CANONICAL-REPOS.md#2-autonomous-coding-surface-typescript) |
| Public launch target | V1 expects an `opensin` install flow from the hero CTA on `opensin.ai` | [OpenSIN-Code#1117](https://github.com/OpenSIN-AI/OpenSIN-Code/issues/1117) |
| Verified local path right now | Clone `OpenSIN-Code`, `bun install`, `bun run build`, then start the CLI from the repo | [OpenSIN-Code README](https://github.com/OpenSIN-AI/OpenSIN-Code/blob/main/README.md) |

**Translation:** the launch-day `curl | sh` story is part of the V1 gate, but the **source-build path is the verified path today** and is what this page documents first.

## 5-minute verified path today

### 1. Install prerequisites

```bash
brew install oven-sh/bun/bun
brew install git
```

OpenSIN docs follow the repo mandates: **Bun only** for JavaScript and TypeScript work.

### 2. Clone the canonical CLI repo

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code
```

### 3. Install dependencies and build

```bash
bun install
bun run build
```

If you want an extra confidence check before your first session:

```bash
bun test
```

### 4. Start the CLI

Use the repo's documented quick-start entrypoint:

```bash
opensin-code
```

If your shell does not yet expose the binary globally, use the repo-local workflow that the package scripts provide after `bun run build`.

### 5. Make your first useful call

Inside the CLI:

1. Run `/help` to confirm the command surface is loaded.
2. Ask for a concrete task, for example:

```text
Explain this repository and propose the smallest safe first change.
```

3. If you want planning first, use:

```text
/plan
```

That is the fastest honest path from docs to a working local OpenSIN session.

## Launch-day installer target

The V1 launch gate for `OpenSIN-Code` is stricter than the source-build flow above. Before launch, the following must also be true:

- the hero CTA on `opensin.ai` leads to a working installer flow,
- `opensin --help` shows the V1 command surface,
- error messages point at the right support repo and docs,
- telemetry opt-in is explicit and respects `DO_NOT_TRACK`.

Track that work in [OpenSIN-Code#1117](https://github.com/OpenSIN-AI/OpenSIN-Code/issues/1117).

## Where to go next

- [OpenSIN-Code CLI reference](/guide/opensin-code)
- [OpenSIN backend V1 API](/api/backend-v1)
- [Team manifest contract (`team.json`)](/api/team)
- [Agent author guide](/guide/how-to-configure-agents)
- [April 2026 consolidation](/changelog/2026-04-consolidation)

---

## Relevante Mandate

| Mandat | Priority | Doku |
|--------|----------|------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` — npm ist im OpenSIN-Ökosystem gebannt |
| **Annahmen-Verbot** | -5.0 | Nur dokumentieren, was mit Repo- oder Issue-Evidenz belegt ist |
| **Test-Beweis-Pflicht** | 0.0 | Kein "done" ohne echten Build- oder Laufnachweis |

→ [Alle Mandate](/best-practices/code-quality)
