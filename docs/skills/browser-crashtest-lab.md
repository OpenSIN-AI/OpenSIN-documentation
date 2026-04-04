---
name: browser-crashtest-lab
description: Full-browser crash-test and quality-audit workflow for web projects. Crawl pages, open links, click buttons, collect console/page/network failures, run accessibility and Lighthouse best-practice checks, and score visual/design quality. Use when users ask for aggressive E2E browser testing, "open every link", "click every button", UX/design quality grading, production readiness checks, or DevTools-level debugging.
---

> OpenCode mirror: sourced from `~/.config/opencode/skills/browser-crashtest-lab` and mirrored for OpenCode CLI usage.

# Browser Crashtest Lab

## Overview

Run deterministic multi-pass browser audits with parallel worker processes and produce a final PASS/WARN/FAIL readiness report. Use this skill when broad surface testing is required, not just a single user flow.

## Prerequisites

Run from any project directory:

```bash
command -v node >/dev/null 2>&1
command -v npx >/dev/null 2>&1
```

If missing, ask the user to install Node.js first.

Install runtime packages (project-local preferred):

```bash
pip3 install nodriver aiohttp
```

Lighthouse is pulled on demand with `npx lighthouse`.

For the second visual judge (NVIDIA Qwen), set:

```bash
export NVIDIA_API_KEY="..."
```

Ensure Codex CLI is available for the first visual judge:

```bash
command -v codex >/dev/null 2>&1
```

## Skill Path

```bash
export OPENCODE_HOME="${OPENCODE_HOME:-$HOME/.config/opencode}"
export CRASHLAB="$OPENCODE_HOME/skills/browser-crashtest-lab/scripts/browser_crashtest_audit.mjs"
```

## Quick Start

```bash
node "$CRASHLAB" \
  --url http://localhost:3000 \
  --workers 6 \
  --action-workers 6 \
  --link-workers 8 \
  --link-open-mode both \
  --design-zeugnis \
  --design-jury-mode dual \
  --design-fusion-mode union \
  --max-pages 120 \
  --max-actions-per-page 30 \
  --max-links-per-page 50 \
  --out-dir output/browser-crashtest
```

Then inspect:

- `output/browser-crashtest/report.md`
- `output/browser-crashtest/report.json`
- `output/browser-crashtest/design-zeugnis.md`
- `output/browser-crashtest/design-zeugnis.json`

## Workflow

1. Run a wide crawl with high worker count.
2. Read `report.md`, especially failing pages and repeated patterns.
3. Re-run headed for targeted debugging:

```bash
node "$CRASHLAB" \
  --url http://localhost:3000/settings \
  --workers 1 \
  --link-open-mode browser \
  --headed \
  --max-pages 15 \
  --out-dir output/browser-crashtest-headed
```

4. Re-run after fixes and compare status and score deltas.

5. Default Codex judge mode is `chat`: the skill writes a strict JSON template + instructions for this Codex chat model.
   - use `--design-codex-judge-mode chat` (default)
   - fill `output/browser-crashtest/design-judge-codex.json` from this chat review
   - rerun the same command (or use `auto` to try `exec` first, then chat/file fallback)
6. If you explicitly want CLI-driven codex runs, use:
   - `--design-codex-judge-mode exec`
7. If Codex CLI execution is blocked/unavailable and you intentionally disable strict LLM requirement, use:
   - `--no-design-llm-required --design-codex-judge-mode file`
   - `output/browser-crashtest/design-judge-codex.template.json`
   - `output/browser-crashtest/design-judge-codex.instructions.md`
   Then rerun the same command.

## Key Tuning Flags

- `--action-workers <n>`: Parallel micro-workers for button/click checks on each page.
- `--link-workers <n>`: Parallel micro-workers for link checks on each page.
- `--link-open-mode browser|http|both`:
  - `browser`: open links in real tabs (default).
  - `http`: fast status probes via browser context request API.
  - `both`: run both and merge results for stricter audits.
- `--design-zeugnis`: Enable strict design jury and professor-style design report.
- `--design-llm-required`: Fail when any required judge is missing (default on).
- `--design-jury-mode dual`: Use Codex app visual judge + NVIDIA Qwen 3.5.
- `--design-codex-judge-mode auto|exec|chat|file`: Codex judge source (default `chat`).
- `--design-codex-model <name>`: Codex model override for local CLI judge runs (default `gpt-5.3-codex`).
- `--design-codex-timeout-ms <n>`: Timeout for Codex judge execution.
- `--design-codex-attempts <n>`: Codex judge attempts (default `3`).
- `--design-fusion-mode union`: Fail if one judge fails.
- `--design-qwen-endpoint <url>`: Optional explicit endpoint override if base URL routing differs.
- `--design-qwen-model <name>`: Qwen model name (default `qwen3.5-397b-a17b`).
- `--design-qwen-attempts <n>`: Qwen judge attempts (default `3`).
- `--design-viewports 390x844,768x1024,1440x900`: Multi-viewport evidence capture.
- `--design-min-score-fail 920`: Hard fail threshold on 1000 scale.
- `--design-max-evidence-images <n>`: Global cap for captured judge evidence.
- `--design-codex-max-evidence-images <n>`: Codex-specific evidence cap (default `6`).
- `--design-qwen-max-evidence-images <n>`: Qwen-specific evidence cap (default `18`).
- `--design-codex-judge-file <path>`: Optional explicit path for codex judge JSON.

## What The Audit Enforces

- Crawl + coverage: Discover internal pages by BFS and test them in parallel processes.
- Link resilience: Open discovered links in a real browser by default and flag 4xx/5xx or request failures.
- Interaction resilience: Attempt safe button/control clicks with per-page parallel micro-workers.
- Runtime stability: Capture `console` errors/warnings, `pageerror`, and failed network requests.
- Accessibility baseline: Run axe-core (if installed).
- Best-practice baseline: Run Lighthouse categories (`performance`, `accessibility`, `best-practices`, `seo`) on sampled pages.
- Visual/UX heuristics: Compute a design score and classify:
  - `big-player-quality`
  - `solid`
  - `needs-polish`
  - `high-risk`
- Design Zeugnis: run dual-model jury and emit strict, evidence-based findings (`P0`..`P3`) plus release verdict.

## Dual-Model Jury Mode

- Judge A (no API, default): this Codex chat model reviews evidence and writes `design-judge-codex.json`.
- Judge A optional CLI path: local `codex exec` with attached evidence images.
- Judge A fallback artifact path: `design-judge-codex.template.json` + `design-judge-codex.instructions.md`.
- Judge B (API): NVIDIA Qwen 3.5 (`qwen3.5-397b-a17b`) runs multimodal judgement.
- Fusion: `union` gate => if one judge says `FAIL`, final design verdict is `FAIL`.

## Professorisches Design-Zeugnis

- Tone is intentionally hard and factual (`--design-tone professor`).
- Every finding must provide concrete evidence, impact, and a directly executable fix.
- Non-parseable/invalid judge output is retried and then treated as hard failure in strict mode.

## Hard Gate Criteria

- Any `P0` finding in deterministic checks or either model judge.
- Missing required judge output with `--design-llm-required`.
- Overall design score below `--design-min-score-fail`.
- Critical WCAG/Core Web Vitals issues.
- Codex CLI account quota/usage-limit errors in strict mode.

## Judge Disagreement

- Disagreement is tracked in `design-zeugnis.json -> fusion.disagreement`.
- `PASS` requires both model judges to pass and no hard-fail condition.
- If judges disagree without `P0`, final verdict is at least `WARN`.

## Optional DevTools MCP Escalation

When browser output is not enough (complex runtime/perf anomalies), start Chrome DevTools MCP:

```bash
"$OPENCODE_HOME/skills/browser-crashtest-lab/scripts/chrome_devtools_mcp_probe.sh" \
  output/browser-crashtest/devtools-mcp.log
```

Then connect from an MCP-capable client and inspect console, network, performance, and screenshots interactively.

## Guardrails

- Avoid destructive actions by default; the script skips likely destructive controls (`delete`, `pay`, `purchase`, etc.).
- For authenticated apps, ensure the app is logged in before running wide audits.
- Keep artifacts under `output/browser-crashtest*` and avoid new top-level artifact folders.
- If a page is behind bot protection/CAPTCHA, document it and test critical flows manually.

## References

Open only what is needed:

- Research-backed stack and links: `references/stack-2026-02-26.md`
- Worldclass standards and dual-judge policy: `references/design-worldclass-standards-2026-02-27.md`
