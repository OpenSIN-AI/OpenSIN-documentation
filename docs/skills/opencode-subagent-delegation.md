---
name: opencode-subagent-delegation
description: Persistent co-working orchestration for Codex and opencode CLI in the same project directory. Use when Codex must collaborate continuously with opencode agents, attach complete project context, enforce strict secret redaction, apply canonical-first conflict resolution, and prevent duplicated governance text by indexing existing project docs.
---

> OpenCode mirror: sourced from `~/.config/opencode/skills/opencode-subagent-delegation` and mirrored for OpenCode CLI usage.

# Opencode Co-Working Delegation

## Overview

Use this skill to run Codex + opencode as one coordinated team in a persistent session with hard-fail context gates.

This skill never imports docs from an external BIOMETRICS repository path. It always uses the files that exist in the current project root.

## Core Guarantees

1. Start opencode only in the active project directory.
2. Build a full context bundle before first delegated execution.
3. Auto-detect profile (`auto|biometrics|generic`) from the current project.
4. Use canonical-first context flow: canonical index + read order + full inventory.
5. Mask secrets strictly (`.env`, credentials, token-like fields).
6. Block delegation if coverage, canonical structure, or no-dup checks fail.
7. Coverage validation uses bundle source snapshot (`06_source_snapshot.txt`) to avoid live repo race conditions.
8. Keep one persistent session and continue it with explicit `sessionID`.
9. Require `CONTEXT_READY bundle_id=<id>` and `CONTEXT_PROFILE=<profile>` before execution.
10. Require `MUTUAL_CRITIQUE_COMPLETE` and `MUTUAL_PLAN_READY` before execution.
11. Enforce strict mutual skepticism (`critical_mode=strict`) in every substantial message.
12. Enforce hard runtime and tool-call caps per delegated opencode message.
13. Send proactive Codex interventions continuously.

## Standard Workflow

1. Build full bundle:
   - `scripts/build-project-context-bundle.sh --project <dir> --profile auto`
2. Validate bundle coverage:
   - `scripts/context-coverage-check.sh --project <dir> --bundle-dir <bundle_dir>`
3. Start persistent collaboration session:
   - `scripts/start-opencode-collab.sh --project <dir> --profile auto --agent <name> --model <provider/model> --max-runtime-sec 420 --max-tool-calls 16`
4. Send collaborative follow-up messages (same session):
   - `scripts/send-opencode-collab-message.sh --project <dir> --message "..." --max-runtime-sec 420 --max-tool-calls 16`
5. Run proactive intervention loop:
   - `scripts/proactive-codex-loop.sh --project <dir> --interval-sec 90`

## Bundle Model

- Bundle root: `<project>/.opencode-context/bundles/<bundle_id>/`
- Canonical artifacts:
  - `04_canonical_stack_index.json`
  - `05_canonical_read_order.md`
  - `22_no_duplication_audit.json`
- Compatibility artifacts remain present (`03_project_summary.md`, `10_*`, `15_*`, `20_*`), but they contain structured references only.
- Full text remains in `30_fulltext/` and is redacted.

## Session Model

- One persistent team session per project.
- Initial message requires:
  - `CONTEXT_READY bundle_id=<id>`
  - `CONTEXT_PROFILE=<profile>`
  - `MUTUAL_CRITIQUE_COMPLETE`
  - `MUTUAL_PLAN_READY`
- Every follow-up message references the same session and includes delta by default.
- Delta includes canonical diff (`03_canonical_diff.md`) when available.
- Every substantial reply must include the critical response contract:
  - `prompt_logic_review`
  - `objective_refinement`
  - `opencode_critique_of_codex`
  - `codex_challenge_requested`
  - `conflicts_resolved_with_priority`
  - `plan_status`
  - `work_done`
  - `delegated_subtasks`
  - `risks_or_blockers`
  - `next_steps`

## Security Model

- Secret policy is strict-only.
- Sensitive values are redacted before attachment.
- Coverage, canonical-index integrity, and no-dup audit are mandatory gates.
- Model fallback is automatic and ordered:
  - explicit chain via `OPENCODE_MODEL_FALLBACK_CHAIN` (comma-separated), or
  - default chain: `OPENCODE_PRIMARY_MODEL` -> `OPENCODE_FALLBACK_MODEL` -> `OPENCODE_TERTIARY_FALLBACK_MODEL` (or `OPENCODE_NIM_FALLBACK_MODEL`)
  - default model values: `google/gemini-3.1-pro-preview` -> `google/gemini-3-flash-preview` -> `nvidia-nim/qwen-3.5-397b`
- NVIDIA NIM fallback requires `NVIDIA_API_KEY` available in the environment.
- Any opencode stream `type=error` event is treated as a failed run and triggers fallback/abort.
- Any missing critical response fields or missing mutual-critique gates cause hard-fail.
- Any gate failure exits non-zero and blocks `opencode run`.

## Backward Compatibility

- `scripts/start-opencode-team.sh` and `scripts/run-opencode-delegated.sh` remain available.
- Both wrappers route to persistent co-working scripts.

## Resources

### scripts/

- `resolve_project_dir.sh`: resolve active project path.
- `list-subagents.sh`: list available opencode agents.
- `build-project-context-bundle.sh`: create full mandatory context bundle with profile detection.
- `build-context-delta.sh`: create delta artifacts and canonical diff.
- `context-coverage-check.sh`: verify mandatory files, file coverage, canonical/no-dup gates, and redaction.
- `session-state.sh`: read/write persistent session state in `.opencode-context/session/state.json`.
- `start-opencode-collab.sh`: create full bundle, enforce readiness/profile ack, initialize persistent session.
- `send-opencode-collab-message.sh`: continue same session with intervention block and canonical-aware delta.
- `proactive-codex-loop.sh`: periodic + trigger-based proactive interventions.
- `start-opencode-team.sh`: compatibility wrapper to `start-opencode-collab.sh`.
- `run-opencode-delegated.sh`: compatibility wrapper to session-aware messaging.

### references/

- `delegation-prompt.md`: kickoff protocol prompt with canonical-first contract.
- `context-bundle-spec.md`: required bundle structure and no-dup contract.
- `collaboration-protocol.md`: Codex/opencode co-working protocol and conflict priority rules.
- `secret-redaction-policy.md`: strict redaction policy and failure conditions.
- `proactive-message-templates.md`: intervention templates for periodic and trigger-based updates.
