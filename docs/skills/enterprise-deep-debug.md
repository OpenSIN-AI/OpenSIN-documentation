---
name: enterprise-deep-debug
description: "Ultimate enterprise debugging workflow: facts-first RCA, cross-tool intent discovery, parallel subagents, web validation, minimal safe fix, and persistent knowledge flush."
license: MIT
compatibility: opencode
metadata:
  audience: senior-engineering
  mode: autonomous-rca
  language: en
---

> OpenCode SSOT: sourced from the `Delqhi/opencode-enterprise-deep-debug-skill` repository and symlinked into `~/.config/opencode/skills/` for CLI usage.

# Enterprise Deep Debug

Use this skill when a bug is complex, cross-cutting, flaky, or enterprise-scale (distributed systems, async flows, microservices, cloud-native, event streams).

Triggers (examples)
- "deep debug", "root cause analysis", "RCA", "system-wide debugging", "kaskadierender Fehler", "Whack-a-Mole", "flaky", "regression", "prod incident", "postmortem".

Hard rules (anti-hallucination)
- Do not patch before you have a reproducible failing case (command, input, expected vs actual).
- Prefer evidence over intuition. Every claim links to: file path + line, command output, or a cited external URL.
- Parallelize investigation, not patching: subagents gather evidence only; edits happen after synthesis.
- One hypothesis, one discriminating experiment. Change one variable at a time.
- Stop conditions are mandatory: set budgets and terminate when exceeded (no infinite loops).
- Secrets: never print or persist tokens/keys. Redact any credential-like strings.
- Any read outside the repo must come from the Project SSOT Source Map established for the current debug run or from a direct project link discovered in repo evidence. Never do a blind whole-machine scan.
- Telemetry reads (opencode.db, opencode-local.db, antigravity-logs) are outside the repo: get explicit consent and allowlist before Phase -1; if denied, skip it.
- Never write to repair-docs or any external path without explicit consent; if not granted, output the formatted block in chat.
- Swarm Max Mode requires a minimal repro and at least one validation command; never apply a patch that fails validation.

Budgets + Termination (enforced)
- Wall clock: 35 min default (user can raise/lower).
- Phase budgets:
  - Phase -1 (telemetry, optional): 3 min (consume from Phase I if time tight)
  - Phase 0 + 0.5 (repro + triage): 8 min
  - Phase I (intent discovery): 6 min (skip by default)
  - Phase II (evidence gathering): 12 min
  - Phase III (synthesis): 5 min
  - Phase IV (fix + validate): 10 min
  - Phase VI (compliance sync, optional): 3 min
- Query caps (prevent loops):
  - `opencode debug rg search`: max 8 total
  - `opencode debug lsp diagnostics`: max 4 files total
  - `opencode debug lsp symbols` / `document-symbols`: max 6 total
  - Telemetry reads: max 3 sources; opencode.db query limit 200 rows; log window last 10 minutes
  - Experiments: max 5 (must be discriminating)
  - Patch iterations: max 2
  - `swarm_max`: max 1 run, tries <= 5
- Hard stop behavior:
  - If Phase 0 gate (repro) is not met within budget: stop and request exactly what is missing (command, input, expected vs actual, logs).
  - If the hypothesis cannot be discriminated within remaining experiment budget: stop with top 2 hypotheses + the single best next discriminating experiment.
- Maintain a budget ledger in chat (update after each phase):
  - time_spent, remaining_budget, queries_used (rg/lsp), experiments_used, patch_iterations_used

OpenCode-native fast-path (default)
Run these first unless the user forbids command execution:

Precondition
- Run all `opencode debug rg *` commands from the project/repo root (NOT from $HOME).
- Always set a `--limit` and tighten with `--glob` when the tree is large.

Telemetry note
- If Phase -1 consent is granted, run it before the snapshot baseline. Otherwise skip it.

1) Snapshot baseline (always)
- `opencode debug snapshot track`
- If git repo: `git status` + `git diff` (read-only)

2) Fast repository map (no heavy scans)
- `opencode debug rg tree --limit 200`
- `opencode debug rg files --limit 300`

3) Targeted discovery (3-query rule)
- Query 1 (signature): `opencode debug rg search "<exact error or log token>" --limit 50`
- Query 2 (symbol): `opencode debug lsp symbols "<core symbol/module/service name>"`
- Query 3 (callsite): `opencode debug rg search "<function/class name from Query 2>" --limit 50`

4) Diagnostics (only when you have a candidate file)
- `opencode debug lsp diagnostics <file>`
- `opencode debug lsp document-symbols <uri>` (when you already know the file)

Fallbacks (only if OpenCode-native tools are unavailable):
- Built-in tools: `grep`, `lsp_*`
- `bash` with `rg` (narrow path + narrow pattern)
Avoid broad `glob`/filesystem scanning unless scoped; prefer `opencode debug file search` / `opencode debug rg search` instead.

Fast Lane (10 minutes, hard stop)

Use when the user explicitly wants the fastest possible path (triage + minimal fix), and accepts that deeper RCA may be incomplete.

Constraints
- Max wall clock: 10 minutes.
- Repo-only: no external reads, no telemetry, no web validation, no subagents, no swarm_max.
- Exactly 1 discriminating experiment.
- Exactly 1 minimal fix attempt.
- If any gate is not met: STOP and return the missing info + next cheapest step.

Procedure
1) Repro Card (mandatory)
   - Produce the 6-line Repro Card from Phase 0. If any line is missing: STOP.
2) 3-query rule (mandatory)
   - Run Query 1 (signature) -> Query 2 (symbol) -> Query 3 (callsite).
   - Identify 1-3 candidate entry points.
   - Expand context only within the Project SSOT Source Map for this project; do not widen to unrelated machine-wide sources.
3) Pick 1 hypothesis (mandatory)
   - Choose a single hypothesis tied to one entry point.
   - Record in Evidence Ledger: claim + evidence + the 1 experiment that would falsify it.
4) Run exactly 1 experiment
   - Change one thing. Capture verbatim output. Update Evidence Ledger.
   - If inconclusive: STOP with top 2 hypotheses + the next cheapest deciding experiment.
5) Minimal fix (only if experiment is conclusive)
   - Implement the smallest safe change that addresses the evidence.
   - No refactors, no style changes, no broad renames.
6) Validate (hard fail)
   - Re-run minimal repro (must pass).
   - Run the smallest targeted test(s) for the touched area (must pass).
   - If either fails: STOP; do not iterate further in Fast Lane.

Fast Lane exit output
- Repro Card
- Evidence Bundle (paths + cmd excerpts)
- Fix summary (what changed)
- Validation commands + results
- Confidence JSON + falsifiers

Phase -1 - Deep Telemetry (optional, consent-gated)
Goal: shortcut discovery with local agent logs and OpenCode event history.

Consent gate (mandatory)
- Use only standard OpenCode telemetry paths plus project-linked telemetry discovered from repo/config/docs.
- Allowlist: `~/.config/opencode/antigravity-logs/`, `~/.config/opencode/opencode.db`, `~/.config/opencode/opencode-local.db`, and project-linked runtime logs.
- If those paths are not project-linked or the user forbids external reads, skip Phase -1 and proceed to Phase 0.

Procedure (if approved)
1) Resolve OPENCODE_HOME (`opencode debug paths` or `~/.config/opencode`).
2) Logs: scan only the last 10 minutes for error tokens, stacktraces, and failing tool calls.
3) DB: use `sqlite3` to query the last 200 events and extract tool errors/timeouts.
4) Emit a Telemetry Digest (max 5 facts) and map any clue to 1-3 candidate entry points.

Telemetry Digest format
- time_window: <start..end>
- top_signals: ["error strings", "tool timeouts"]
- likely_surface: <paths/modules>
- next_experiment: <one discriminating experiment>

Phase 0 - Snapshot + Repro (must pass)
1) Capture baseline facts:
   - `git status` and `git diff` (or equivalent).
   - Runtime versions (language, package manager, OS).
   - Exact repro command(s) and inputs.
   - Logs/stacktraces with timestamps.
2) Reduce to a minimal repro if possible (smallest command that still fails).
3) Create an "expected vs actual" statement.

Phase 0 gate (artifact)
Produce a 6-line Repro Card before continuing:
- env: <versions>
- command: `<exact repro command>`
- input: <fixture/request payload/URL>
- expected: <one sentence>
- actual: <one sentence>
- primary signal: <error string / failing assertion / status code>
If you cannot fill all 6 lines, stop and request the missing line(s).

Phase 0.5 - Fast triage (2-5 minutes)
- Establish a stable snapshot marker (if supported): `opencode debug snapshot track`.
- Build a quick file+symbol map without heavy scanning:
  - `opencode debug rg tree`
  - `opencode debug rg files`
  - `opencode debug lsp symbols <core terms>` (service/module/class/error name)
- If you already know the failing file, capture diagnostics: `opencode debug lsp diagnostics <file>`.
- Outcome: a short list of likely components + 1-3 candidate entry points.

Phase 0.5 gate (artifact)
- Output 1-3 candidate entry points as:
  - `path:line` + why it is implicated (one sentence) + the next discriminating experiment.
If you have >3 candidates, you did not narrow enough; rerun the 3-query rule with a more specific signature.

Phase 0.6 - Failure classifier (pick one primary)
- Contract/API mismatch (schema, types, params)
- State/race/flaky timing (async, retries, concurrency)
- Environment/config/secret (env vars, feature flags, build-time vs runtime)
- Dependency regression (lockfile drift, semver bump, transitive change)
- Data/permissions (DB migrations, ACLs, authz/authn)
- Resource/limits (timeouts, memory, file descriptors, quotas)
- Observability gap (missing logs/trace IDs)

Record: primary_class + top 2 alternates. Use this to focus searches and experiments.

Phase I - Project SSOT Source Discovery (recommended)
Goal: recover developer intent and gather broad evidence from all project-linked sources without drifting into unrelated machine-wide data.

Project SSOT Source Map (build this first)
- Build a `SOURCE_MAP` before any broad scan.
- Every external source must be linked by one of:
  - repo evidence (`README`, config, docs, scripts, URLs, doc IDs, repo slugs)
  - known project SSOT docs (`repair-docs.md`, `docs/**`, project Google Docs tab, tracked dashboards)
  - session metadata (`cwd`, repo slug, doc ID, branch, task transcript)
  - deployment/runtime linkage (service URL, MCP config, tunnel config, health endpoint)
- If a source cannot be linked to the project, exclude it.

Allowed source categories
1) Primary repo and current worktree
2) Project docs and repair docs
3) Project-linked runtime logs and telemetry
4) Project-linked local sessions/history
5) Project-linked Google Docs / Drive assets
6) Project-linked GitHub repos / submodules / sibling repos

Excluded by default
- Unrelated home directories, generic editor history, global caches, `node_modules`, `dist`, random Drive folders, random GitHub repos, and any source with no project linkage.

Discovery order
1) Repo-local evidence (`README`, docs, config, scripts, URLs, doc IDs, repo slugs)
2) Project docs / repair docs
3) Runtime telemetry and logs
4) Same-project sessions/history
5) Linked Google Docs / Drive
6) Linked GitHub repos / sibling repos

Extraction playbook
- Prefer OpenCode-native scanning first:
  - `opencode debug file search <query>`
  - `opencode debug rg search <pattern>`
- Use targeted `grep`, `lsp_*`, `ast_grep_*`, and `bash`/`rg` only on paths already present in `SOURCE_MAP`.
- For each source, extract only:
  - current goals
  - failed attempts
  - conflicting guidance
  - links to code/docs/runtime evidence

Output a structured source summary:
```json
{
  "source_map": [
    {"id":"repo","kind":"repo","path":"...","why_linked":"..."},
    {"id":"docs","kind":"repair-docs","path":"...","why_linked":"..."}
  ],
  "current_goals": ["..."],
  "failed_attempts": ["..."],
  "reliability_notes": ["doc/file X is stale because ..."],
  "constraints": ["security", "backwards compatibility", "no schema change"]
}
```

Phase II - Evidence Gathering (mandatory, orchestrated)
Goal: collect enough evidence to choose 1 leading hypothesis with a single discriminating experiment.

Orchestration
- Preferred: parallel subagents via `task()` with fixed role prompts, strict contracts, and timeboxes.
- For project-wide deep-debug runs, invoke `omoc-plan-swarm` first to split the work into source lanes.
- Preferred lanes: `repo`, `docs`, `runtime`, `sessions`, `google`, `github`.
- Use `task()` / swarm tools for evidence collection. Use `sin-terminal` only when visible multi-terminal local orchestration is explicitly requested or clearly beneficial for the same project.
- Never assign agents to sources outside the `SOURCE_MAP`.

Predictive branching (tie-breaker)
- If two hypotheses remain within 1 point after scoring, run two parallel subagents (one per hypothesis).
- Each subagent runs exactly one discriminating experiment and returns evidence-only output.
- Choose the winner; discard the other unless it gains new evidence.

Hard rule: subagents gather evidence only (no edits).
Merge protocol: normalize all outputs into the Evidence Ledger and deduplicate by `path:line` / command-output identity.

Subagent contracts (strict)
- Input: Repro Card + primary_class + budget ledger + repo root.
- Timebox: 6 minutes each (default). Late responses are ignored unless they include new evidence.
- Output: EXACTLY one JSON object (schema below) and nothing else.
- Evidence requirements:
  - Every claim must include at least one pointer: `path:line`, `git:<cmd excerpt>`, `cmd:<verbatim output excerpt>`, or `url:<verified via webfetch>`.
- Forbidden:
  - edits, refactors, or "try X" without a falsifiable experiment.

Recommended subagents
1) AST Tracer (explore): codebase search + dataflow hints
   - Prefer `opencode debug rg search` for fast discovery; then use `ast_grep_search` and `lsp_find_references` for structure/precision.
   - Goal: map symptom -> call chain -> likely root-cause surface.

2) Log/Runtime Analyst (general or explore): log correlation + timeline
   - Goal: build a timeline; identify first failure and upstream triggers.

3) Repo Historian (general): regression + ownership
   - Use only git read commands.
   - Goal: identify introducing commit(s) and intent from messages.

4) Web Validator (librarian): best practices + known issues
   - If a web search surface is available, use it to discover; always verify with `webfetch` (URLs).
   - If discovery is not available, ask the user for a URL or narrow query constraints.
   - Goal: confirm the planned fix is current, not deprecated, and not insecure.

Subagent output schema
```json
{
  "role": "ast_tracer|log_analyst|repo_historian|web_validator",
  "top_hypotheses": [
    {"id":"H1","claim":"...","evidence":["path:line","cmd: ... -> ...","url: ..."],"falsify":"one quick test"}
  ],
  "high_risk_areas": ["..."],
  "missing_info": ["..."],
  "recommended_next_experiments": ["..."],
  "confidence": 0.0
}
```

## Evidence Ledger + Bundle (mandatory)

Maintain an append-only `EVIDENCE_LEDGER` in-chat. Every non-trivial claim must cite one of:
- `file:path:line`
- `cmd:` + key output lines
- `url:` (only if externally fetched and verified with `webfetch`)
- `source:<id>` (must exist in `SOURCE_MAP`)

Ledger schema (terse)
```json
{
  "env": {"os":"", "arch":"", "runtime_versions":{}, "cwd":"", "branch":""},
  "source_map": [{"id":"repo","kind":"repo","path":"","why_linked":""}],
  "repro": {"command":"", "inputs":"", "expected":"", "actual":"", "flakiness":"unknown|stable|flaky"},
  "facts": [{"id":"F1","text":"verbatim observation","evidence":["cmd: ...","file:path:line"]}],
  "hypotheses": [{"id":"H1","claim":"","support":["F1"],"disconfirm":[],"falsify":"one test"}],
  "experiments": [{"id":"E1","hypothesis":"H1","change_one_thing":"","command":"","result":"","evidence":["cmd: ..."]}],
  "decisions": [{"id":"D1","picked":"H1","why":"","evidence":["F..","E.."]}]
}
```

## Oscillation Guard (hard stop)

Track last 6 steps as tuples: `(hypothesis_id, experiment_kind, touched_area)`.
Define `no_progress` as: no new Fact (F*) AND no hypothesis falsified in 2 consecutive experiments.

Rules:
- Never run the same experiment_kind on the same touched_area twice without a NEW fact.
- After 2 consecutive `no_progress`:
  1) pivot vantage point (logs -> code, code -> runtime, runtime -> git/regression)
  2) switch classifier secondary (e.g. from `contract` to `configuration`)
  3) force a minimal reproduction shrink attempt (remove variables)
- After 3 consecutive `no_progress`: STOP and ask ONE targeted question, including the default assumption you will proceed with.

Anti-thrashing patch rule:
- If you already attempted a fix and it failed validation, do NOT tweak blindly.
  Require: new fact + new falsifying test before patch iteration #2.

Phase III - Synthesis (single source of truth)
Build one evidence table and pick the leading hypothesis.
- Evidence table rows: symptom, first-failure timestamp, component, hypothesis, supporting evidence, disconfirming evidence, discriminating experiment.
- Choose the hypothesis with the strongest falsifiable support.
- If evidence conflicts, run the discriminating experiment(s) before any edits.

Hypothesis scoring rubric (fast + deterministic)
- Score each hypothesis 0-5 on:
  - Explains all symptoms
  - Has concrete evidence
  - Is falsifiable quickly
  - Has minimal fix surface
- Choose highest score; if tie, choose the one with the simplest discriminating experiment.

Phase III termination rule
- If no hypothesis scores >= 13/20 OR the top hypothesis lacks a discriminating experiment that fits remaining budget:
  - Stop and return: top 2 hypotheses, their best evidence, and the single cheapest next experiment that would decide between them.
  - Do NOT proceed to Phase IV.

Phase IV - Fix (minimal, cascading, safe)
- Implement the smallest change that resolves the root cause.
- If the root cause spans multiple modules, update all dependent surfaces in one coherent patch.
- Avoid broad refactors during the fix phase.
- Add/adjust tests where they reduce recurrence.

Phase IVb - Shadow Testing (swarm_max, optional)
Use when: high-risk fixes, flaky tests, or you want fastest safe convergence.
Gates
- Minimal repro exists and at least one validation command is known.
- Repo is a git repo. If working tree has unrelated changes, set apply=false and apply the best patch manually.

Procedure
1) Build a compact prompt: repro, hypothesis, constraints, touched files, and testCmd.
2) Run `swarm_max` with tries 3-5 and the chosen testCmd.
3) Select the best result by test pass + minimal diff.
4) Re-run repro in the main tree, then continue to validation gates.

If swarm_max is unavailable or gates fail, skip Phase IVb and proceed with the normal fix flow.

Validation gates (hard fail, ordered cheapest -> most expensive)
1) Re-run the minimal repro (must pass).
2) Run the smallest targeted test(s) that cover the changed surface (must pass).
3) Run one broader safety check only if risk warrants it (pick one):
   - CI subset, smoke test, or build.
4) For web/UI bugs: capture one artifact that would catch regressions:
   - console error excerpt OR network failure excerpt OR screenshot.
If any gate fails: stop, update the Evidence Ledger, and spend exactly 1 experiment to explain the failure before changing the fix.

Phase V - Persistent Knowledge Flush
Before ending the session, persist what was learned so it survives context compaction.

Rules
- Default: provide the flush content in chat.
- Only write/append to repo files when (a) the user wants persistence and (b) the file already exists.
- Never create new governance files (`AGENTS.md`, `CLAUDE.md`) unless the user explicitly asks.

If persistence is approved and files exist, write/append to repo root:
- `AGENTS.md` (procedural rules / do-don't)
- `CLAUDE.md` (compat mirror for other assistants)

Flush format (append as a new section)
```markdown
## Debug Memory - <YYYY-MM-DD> - <short bug title>
Root cause: <one sentence>
Scope: <services/modules/files>
Repro: `<command>`
Fix: <what changed and why>
Validation: <commands + results>
Do not: <failed approaches / traps>
New guardrail: <rule to prevent recurrence>
```

Phase VI - Compliance Sync (repair-docs, optional but recommended)
Goal: persist the bug in repair-docs with dedupe and status update.

Consent gate (mandatory)
- Ask for explicit permission to read/write outside the repo.
- Allowlist: `~/dev/docs/<project>/repair-docs.md` (or known project path).
- If denied, output the formatted BUG entry in chat and stop.

Procedure (if approved)
1) Locate the repair-docs path (use known project mapping).
2) Read file and check for an existing BUG id or matching short title.
3) If found, update status and fix text. If not, append a new entry.

Phase VIb - GitHub Issue Execution Lane (mandatory for git repos)
Goal: make the bug publicly traceable and hand the repo execution lane to `SIN-GitHub-Issues` when available.

Procedure
1) Search for an existing matching issue in the project repo before creating anything.
2) If no match exists, create a new issue with: symptom, cause hypothesis, affected files/surfaces, and current repro.
3) If `SIN-GitHub-Issues` is available, hand off the issue lifecycle + branch workflow to it:
   - issue ensure/update
   - branch start
   - commit/push lane
   - final RCA/fix/verification issue update
4) If `SIN-GitHub-Issues` is not yet available, use `gh` directly but keep the same issue lifecycle and evidence requirements.
5) After validation passes, update the issue with root cause, fix, verification, and close it only when the verified fix is actually integrated.

Required handoff bundle
- repo slug
- issue title / issue number / issue url
- repro card
- evidence bundle
- planned branch name
- expected verification commands

Bug format (match the existing file's exact status markers)
```markdown
## BUG-YYYYMMDD-XX: Short title
**Aufgetreten:** YYYY-MM-DD  **Status:** OPEN/FIXED
**Symptom:** What happens
**Ursache:** Why it happens
**Fix:** Code/command/solution
**Datei:** Affected file or surface
```

Final deliverable to user (always)
- `facts` (what is observed)
- `source_map` (which project-linked sources were scanned)
- `issue_tracking` (existing/new issue, url, status, handoff state)
- `root_cause` (why it happens)
- `fix` (what changed)
- `validation_commands` (how to verify)
- `telemetry_digest` (if Phase -1 ran)
- `confidence` (0..1 + breakdown + falsifiers)
- `evidence_bundle` (ledger pointers + key cmd/file excerpts)
- `compliance_sync` (path + written/declined)
- `risks` (what could still break)
- `followups` (optional next steps)

Confidence scoring (mandatory)
```json
{
  "confidence": 0.0,
  "breakdown": {
    "root_cause_correctness": 0.0,
    "fix_correctness": 0.0,
    "regression_risk_low": 0.0,
    "repro_stability": 0.0
  },
  "why": ["one line each, evidence-backed"],
  "what_would_change_my_mind": ["specific falsifier(s)"]
}
```

## Phase II-EXT: Extreme Logging Instrumentation (automated, mandatory)

Goal: achieve university-grade, professor-level logging saturation across any codebase under debug. This phase runs BEFORE evidence gathering to ensure every function, every branch, every exception is observable.

Hard rules
- Run `auto_log_injector.py` (Python) or `ts_log_injector.mjs` (JS/TS) on every source file in the debug surface BEFORE starting Phase II evidence gathering.
- Run `log_coverage_scanner.py` on the target codebase and require grade B+ or higher on all files in the debug surface. If any file scores below B+, re-run the injector or manually add missing log points.
- All injected logging MUST be structured (JSON or structlog format) with correlation IDs, timestamps, function names, args, return values, and timing.
- Never skip this phase. Observability gaps are the #1 cause of failed RCA.

Procedure
1) **Auto-inject logging** (mandatory first step):
   ```bash
   # Python codebases
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/auto_log_injector.py \
     --source-dir <project_src> --output-dir <project_src> --min-lines 1

   # TypeScript/JavaScript codebases
   node ~/.config/opencode/skills/enterprise-deep-debug/scripts/ts_log_injector.mjs \
     --source-dir <project_src> --output-dir <project_src>
   ```

2) **Grade logging coverage** (mandatory gate):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/log_coverage_scanner.py \
     --source-dir <project_src> --min-grade B+
   ```
   - If any file scores below B+: fix it before proceeding.
   - Output: per-file grade card (F through A+) with specific missing log categories.

3) **Configure structured logging** (recommended):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/structlog_configurator.py \
     --project-dir <project_root> --output-dir <project_root>
   ```
   - Auto-detects Python (structlog) or Node.js (pino) and generates config with OTel trace injection.

4) **Bootstrap OpenTelemetry** (recommended for distributed systems):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/otel_bootstrapper.py \
     --project-dir <project_root> --output-dir <project_root>
   ```
   - Detects installed packages and generates auto-instrumentation setup.

5) **Generate HTTP middleware logging** (recommended for web services):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/network_request_logger.py \
     generate --framework <fastapi|flask|express> --output-dir <project_root>
   ```

Phase II-EXT gate: `log_coverage_scanner.py` reports all debug-surface files at grade B+ or higher. If not met, do NOT proceed to Phase II evidence gathering.

## Phase II-EXT-B: Runtime Profiling & Crash Analysis (on-demand)

Goal: when the bug involves performance, memory leaks, crashes, or timing issues, deploy runtime instrumentation to capture deep execution data.

Procedure (use as needed based on Phase 0.6 failure class)

1) **Runtime call tracing** (for call-chain bugs, timing issues):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/runtime_call_tracer.py \
     --script <target_script.py> --output /tmp/call_trace.json --format tree
   ```
   - Records every function call with args, return values, timing.
   - Outputs call tree, stats summary, or flamegraph-compatible collapsed stacks.

2) **Memory profiling** (for leaks, OOM, growing allocations):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/memory_profiler_runner.py \
     --script <target_script.py> --output-dir /tmp/memory_profile/ --interval 1.0 --top 30
   ```
   - Wraps tracemalloc with periodic snapshots and diff analysis.
   - Reports leak candidates with severity ratings and allocation tracebacks.

3) **Flamegraph generation** (for CPU hotspots, slow paths):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/flamegraph_runner.py \
     --script <target_script.py> --output /tmp/flamegraph.svg --top 30
   ```
   - Profiles via cProfile, converts to collapsed stacks for flamegraph.pl.
   - Hotspot analysis with per-function timing breakdown and percentage.

4) **Crash analysis** (for recurring crashes, exception patterns):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/crash_analyzer.py \
     --log-files /tmp/*.log /var/log/app/*.log --output /tmp/crash_report.json
   ```
   - Parses Python tracebacks, extracts call chains, exception taxonomy (30+ types).
   - Identifies recurring crash patterns, timelines, and source file correlations.

5) **Log correlation** (for distributed/multi-service bugs):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/log_correlator.py \
     --log-files /tmp/service_a.log /tmp/service_b.log --output /tmp/correlation.json
   ```
   - Multi-file timeline builder with error cascade detection.
   - First-failure identification, gap detection, correlation chains by request/trace ID.

6) **Git blame correlation** (for regression hunting):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/git_blame_correlator.py \
     --repo-dir <project_root> --error-lines "file.py:42,file.py:87" --output /tmp/blame.json
   ```
   - Correlates error lines with git blame to find who introduced bugs and when.
   - Regression detection for changes <7 days old, author hotspot analysis.

7) **Access log analysis** (for HTTP/API issues):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/network_request_logger.py \
     analyze --log-file /var/log/access.log --output /tmp/http_analysis.json
   ```
   - Analyzes access logs for status distribution, P95 latency, error rate trends, slow endpoints.

## Phase II-EXT-C: GitLab LogCenter (mandatory for all log output)

Goal: eliminate local disk bloat by storing ALL logs, screenshots, videos, reports, and debug artifacts in auto-rotating private GitLab repos. Each project gets its own `<project>-logcenter-001` repo. When it fills up (9GB), a new `-002` is created automatically. Infinite storage, zero local clutter.

Hard rules
- ALL log output from any debug phase MUST go to GitLab LogCenter, NOT local disk.
- Local `/tmp/` files are allowed as transient staging only — they must be uploaded to LogCenter immediately after creation.
- Every agent that runs this skill MUST have `GITLAB_LOGCENTER_TOKEN` available (via env or `~/.config/opencode/gitlab_logcenter.env`).
- The token is stored in SIN-Passwordmanager. NEVER hardcode it in scripts or AGENTS.md.
- Videos and screen recordings are MANDATORY evidence and MUST be uploaded to the `video/` category.

Setup (one-time)
```bash
python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/gitlab_logcenter.py \
  init --project <project-name>
```

Procedure (integrated into every debug phase)
1) **Initialize** the logcenter at the start of any debug session:
   ```python
   from gitlab_logcenter import get_logcenter
   lc = get_logcenter("sin-solver")
   lc.ensure_active()
   ```

2) **Upload logs** instead of writing to local disk:
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/gitlab_logcenter.py \
     upload --project sin-solver --file /tmp/crash_report.json --category reports --tags "rca,crash"

   # Upload from stdin (pipe-friendly)
   some_command 2>&1 | python3 gitlab_logcenter.py upload --project sin-solver --stdin --name "runner.log" --category logs
   ```

3) **Upload screenshots and videos**:
   ```bash
   # Screenshot
   gitlab_logcenter.py upload --project sin-solver --file /tmp/m06_screenshot.png --category screenshots

   # Video recording
   gitlab_logcenter.py upload --project sin-solver --file /tmp/screencast.mp4 --category video --tags "browser,automation"
   ```

4) **Search across all logcenter volumes**:
   ```bash
   gitlab_logcenter.py search --project sin-solver --query "ConnectionError"
   ```

5) **Check status** (storage usage, active repo, rotation state):
   ```bash
   gitlab_logcenter.py status --project sin-solver
   ```

6) **Auto-rotation** happens transparently — when the active repo approaches 9GB, the next upload automatically creates `<project>-logcenter-XXX` and continues there.

Categories: `logs`, `video`, `screenshots`, `browser`, `reports`, `misc`

Directory structure in each logcenter repo:
```
logs/2026-03-24/20260324-141500_runner9.log
video/2026-03-24/20260324-141530_screencast.mp4
screenshots/2026-03-24/20260324-141600_m06_login.png
browser/2026-03-24/20260324-141700_cdp_session.json
reports/2026-03-24/20260324-141800_crash_report.json
```

Every upload gets a `.meta.json` sidecar with: timestamp, category, original path, SHA-256, tags, agent name, project, logcenter volume number.

## Phase II-EXT-D: CDP Browser Capture (mandatory for all browser debugging)

Goal: capture EVERYTHING from Chrome browser sessions via Chrome DevTools Protocol. Console, network, JS exceptions, performance metrics, security events, screenshots, screencast video, JS/CSS coverage — all uploaded to GitLab LogCenter automatically.

Hard rules
- When debugging any browser-related issue, CDP capture MUST be running.
- All CDP data goes to GitLab LogCenter category `browser/`.
- Screencast frames go to category `video/`.
- Chrome must be running with `--remote-debugging-port=9334`.

Captured CDP domains and events:
| CDP Domain | Events/Methods | What it captures |
|---|---|---|
| Runtime | `consoleAPICalled`, `exceptionThrown` | All console.log/warn/error/info/debug + uncaught JS exceptions |
| Log | `entryAdded` | Browser-level log entries (deprecation warnings, interventions, violations) |
| Network | `requestWillBeSent`, `responseReceived`, `loadingFailed` | Full HTTP request/response lifecycle with headers, body, timing |
| Page | `screencastFrame`, `captureScreenshot` | Screencast video frames (JPEG) + on-demand PNG screenshots |
| Performance | `getMetrics` | CPU time, JS heap, layout count, DOM nodes, frames, task duration |
| Memory | `getDOMCounters` | DOM node counts, document counts, JS event listeners |
| Security | `securityStateChanged` | TLS/cert state changes, mixed content warnings |
| Profiler | `startPreciseCoverage`, `takePreciseCoverage` | JS code coverage (which functions executed, call counts) |
| CSS | `startRuleUsageTracking`, `stopRuleUsageTracking` | CSS rule coverage (which rules are used vs unused) |
| DOM | `enable` | DOM tree state for correlation |

Procedure
1) **Start continuous capture** (runs in background, uploads on stop):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/cdp_browser_logger.py \
     start --project sin-solver --port 9334 --fps 2 --quality 60
   ```

2) **Stop and upload** (Ctrl+C or signal):
   ```bash
   python3 ~/.config/opencode/skills/enterprise-deep-debug/scripts/cdp_browser_logger.py stop
   ```

3) **One-shot commands**:
   ```bash
   # Single screenshot -> LogCenter
   cdp_browser_logger.py capture-screenshot --project sin-solver --name "login_modal"

   # Capture 30s of network traffic
   cdp_browser_logger.py capture-har --project sin-solver --duration 30

   # Dump 30s of console output
   cdp_browser_logger.py dump-console --project sin-solver --duration 30

   # Capture JS/CSS coverage for 10s
   cdp_browser_logger.py dump-coverage --project sin-solver --duration 10

   # Sample performance metrics (10 samples, 2s apart)
   cdp_browser_logger.py dump-perf --project sin-solver --samples 10 --interval 2
   ```

4) **Integration with Phase 0 (Repro)**:
   - Start CDP capture BEFORE reproducing the bug.
   - Stop AFTER repro completes.
   - The session report becomes primary evidence in the Evidence Ledger.

Uploaded artifacts per session:
- `browser/YYYY-MM-DD/cdp_session_<ts>.json` — full session report (summary + console + network + exceptions + perf)
- `browser/YYYY-MM-DD/console_<ts>.json` — raw console log
- `browser/YYYY-MM-DD/network_<ts>.json` — raw network log
- `browser/YYYY-MM-DD/exceptions_<ts>.json` — JS exceptions (if any)
- `video/YYYY-MM-DD/screencast_<ts>_frameNNNNN.jpg` — screencast frames (sampled)

## Script Reference Table

All scripts live in `~/.config/opencode/skills/enterprise-deep-debug/scripts/`.

| # | Script | Language | Purpose | Key Inputs | Key Outputs |
|---|--------|----------|---------|------------|-------------|
| 1 | `auto_log_injector.py` | Python | AST-based automatic log injection for Python source files | `--source-dir`, `--output-dir`, `--min-lines`, `--skip-private`, `--dry-run`, `--diff` | Modified Python files with structured logging at every function entry/exit/exception |
| 2 | `ts_log_injector.mjs` | Node.js | Regex-based automatic log injection for TypeScript/JavaScript | `--source-dir`, `--output-dir`, `--dry-run`, `--diff` | Modified JS/TS files with console.log entry/exit/error wrapping |
| 3 | `log_coverage_scanner.py` | Python | Grades logging coverage per-function (F through A+) | `--source-dir`, `--min-grade`, `--output` | Per-file grade card with missing log categories |
| 4 | `crash_analyzer.py` | Python | Parses tracebacks, extracts crash patterns and taxonomy | `--log-files`, `--output` | Crash report with exception taxonomy, recurring patterns, timeline |
| 5 | `log_correlator.py` | Python | Multi-file log correlation and timeline builder | `--log-files`, `--output` | Correlation timeline, error cascades, first-failure identification |
| 6 | `git_blame_correlator.py` | Python | Correlates error lines with git blame for regression hunting | `--repo-dir`, `--error-lines`, `--output` | Blame report with author hotspots, regression detection |
| 7 | `runtime_call_tracer.py` | Python | Records every function call with args/timing via sys.settrace | `--script`, `--output`, `--format` | Call tree, stats, or flamegraph-compatible collapsed stacks |
| 8 | `memory_profiler_runner.py` | Python | Wraps tracemalloc for periodic snapshots and leak detection | `--script`, `--output-dir`, `--interval`, `--top` | Memory diff report with leak candidates and severity ratings |
| 9 | `flamegraph_runner.py` | Python | cProfile-based profiling with flamegraph output | `--script`, `--output`, `--top` | SVG flamegraph + hotspot analysis with timing breakdown |
| 10 | `structlog_configurator.py` | Python | Auto-detects project type, generates structlog/pino config | `--project-dir`, `--output-dir` | Ready-to-use structured logging configuration |
| 11 | `otel_bootstrapper.py` | Python | Generates OpenTelemetry auto-instrumentation setup | `--project-dir`, `--output-dir` | OTel bootstrap code with detected instrumentation libraries |
| 12 | `network_request_logger.py` | Python | Generates HTTP middleware + analyzes access logs | `generate --framework`, `analyze --log-file` | Middleware code or HTTP analysis report |
| 13 | `gitlab_logcenter.py` | Python | GitLab LogCenter: auto-rotating private repos for infinite log storage | `init/upload/status/search/list/rotate/download --project` | GitLab repos with categorized logs, videos, screenshots, reports |
| 14 | `cdp_browser_logger.py` | Python | Chrome CDP full-session capture: console, network, screenshots, screencast, perf, coverage | `start/stop/capture-screenshot/capture-har/dump-console/dump-coverage/dump-perf --project` | Session reports, network HAR, console dumps, coverage data, screencast frames |

## Extreme Logging Mandate

When this skill is invoked, the following logging standards are MANDATORY:

1. **Every function** must log: entry (with args), exit (with return value + elapsed time), and exceptions (with full context).
2. **Every HTTP request/response** must log: method, URL, status, latency, request/response size, correlation ID.
3. **Every database query** must log: query text (parameterized), execution time, row count, connection pool state.
4. **Every external API call** must log: endpoint, request payload hash, response status, latency, retry count.
5. **Every state transition** must log: previous state, new state, trigger, timestamp, actor.
6. **Every error/exception** must log: full stack trace, local variables snapshot, correlation ID, severity classification.
7. **Log format**: structured JSON with ISO-8601 timestamps, correlation IDs, service name, function name, file:line.
8. **Log levels**: TRACE for function entry/exit, DEBUG for internal state, INFO for business events, WARN for degraded paths, ERROR for failures, CRITICAL for system-threatening issues.

This is not optional. This is professor-grade, doctoral-thesis-level observability. Every nanosecond of execution must be accountable.

## Self-test (offline)

Goal: prove this skill is (1) discoverable by OpenCode, and (2) safe by default (no external reads/writes without consent).

Discovery (OpenCode self-reporting)
```bash
opencode debug paths
opencode debug skill | /usr/bin/grep -n "enterprise-deep-debug"
opencode debug config | /usr/bin/grep -n "enterprise-deep-debug"
```

Expected
- `opencode debug paths` prints `config  ~/.config/opencode`
- `opencode debug skill` contains an entry with:
  - `name: enterprise-deep-debug`
  - `location: ~/.config/opencode/skills/enterprise-deep-debug/SKILL.md`
- `opencode debug config` contains a command key `"enterprise-deep-debug"`

Safety checks (static)
```bash
ls -la "$HOME/.config/opencode/skills/enterprise-deep-debug/"
stat "$HOME/.config/opencode/skills/enterprise-deep-debug/SKILL.md"
```

Negative tests (revert after each)

1) Not discoverable
```bash
mv "$HOME/.config/opencode/skills/enterprise-deep-debug/SKILL.md" \
   "$HOME/.config/opencode/skills/enterprise-deep-debug/SKILL.mdx"
opencode debug skill | /usr/bin/grep -n "enterprise-deep-debug" || true
mv "$HOME/.config/opencode/skills/enterprise-deep-debug/SKILL.mdx" \
   "$HOME/.config/opencode/skills/enterprise-deep-debug/SKILL.md"
```

2) Unreadable file
```bash
chmod 000 "$HOME/.config/opencode/skills/enterprise-deep-debug/SKILL.md"
opencode debug skill | /usr/bin/grep -n "enterprise-deep-debug" || true
chmod 644 "$HOME/.config/opencode/skills/enterprise-deep-debug/SKILL.md"
```

3) Name mismatch
```bash
perl -0777 -i -pe 's/^name: enterprise-deep-debug$/name: enterprise-deep-debug-mismatch/m' \
  "$HOME/.config/opencode/skills/enterprise-deep-debug/SKILL.md"
opencode debug skill | /usr/bin/grep -n "enterprise-deep-debug" || true
opencode debug skill | /usr/bin/grep -n "enterprise-deep-debug-mismatch" || true
git --no-pager diff -- "$HOME/.config/opencode/skills/enterprise-deep-debug/SKILL.md" || true
# Manually revert the change (or restore from backup) after this test.
```

Note
- If `opencode debug config` / `opencode debug skill` output is too large to parse as JSON, prefer grep-based checks or use the `~/.local/share/opencode/tool-output/*` files written by OpenCode when output truncates.
