---
name: omoc-plan-swarm
description: "OMOC Plan Swarm -- activated when any agent receives a planning request. Triggers: plan, erstelle einen plan, create a plan, planung, planning, roadmap, strategy, strategie, konzept, blueprint. Instead of planning alone, the agent runs a 3-stage pipeline: parallel research, plan synthesis, critical review. Simple, small processes, fail-fast gates. Never plan alone."
license: MIT
compatibility: opencode
metadata:
  audience: all-agents
  workflow: omoc-pipeline
  trigger: plan
---

# OMOC Plan Swarm (v2 -- 2026-03-16)

> 3-stage pipeline. Small processes. Fail-fast. No monolith.

Successor note:
- Use `/check-plan-done` when the user wants one unified flow that both plans and executes.
- Keep `omoc-plan-swarm` as the planning-only core when execution is not part of the request.

---

## Design Principles (Stand 16.03.2026)

1. **Pipeline > Hierarchy** -- sequential stages with clear I/O contracts beat deep delegation trees
2. **3 stages, not 6** -- fewer handoffs = fewer failures = lower latency
3. **Small prompts** -- each stage prompt is under 15 lines, focused on ONE job
4. **Fail-fast gates** -- check output quality BEFORE passing to next stage
5. **Parallel only where independent** -- research tasks run in parallel, everything else is sequential
6. **No fictional agents** -- use real OpenCode tools (`task()`, `session_read()`, `background_output()`)
7. **Cost guardrails** -- token awareness, no unbounded loops
8. **No temp files** -- results stay in session context

---

## Trigger

This skill activates when any agent receives words like:
`plan`, `plane`, `planung`, `planning`, `erstelle einen plan`, `create a plan`, `roadmap`, `strategy`, `strategie`, `konzept`, `blueprint`, `architektur`

**Rule:** Do NOT research or plan yourself. Load this skill and follow the pipeline.

---

## Architecture

```
User/Agent
    |
    v
 STAGE 1: RESEARCH (parallel)
 +------------------+------------------+
 |                  |                  |
 v                  v                  |
 Librarian          Explore            |
 (web/docs)         (codebase)         |
 +------------------+------------------+
    |                  |
    +--------+---------+
             |
     [GATE 1: Research has substance?]
             |
             v
 STAGE 2: PLAN (sequential)
    task(category: "deep")
    synthesize research -> structured plan
             |
     [GATE 2: Plan has all required sections?]
             |
             v
 STAGE 3: REVIEW (sequential)
    task(category: "artistry")
    critical review + final revision
             |
     [GATE 3: No CRITICAL issues remain?]
             |
             v
 OUTPUT: Final plan returned to caller
```

**Total: 4 `task()` calls (2 parallel + 2 sequential)**

---

## Stage 1: RESEARCH (parallel)

Start both tasks simultaneously with `run_in_background: true`. Wait for both to complete.

### Task A: Librarian -- Web & Docs

```
task({
  subagent_type: "librarian",
  run_in_background: true,
  load_skills: [],
  description: "Web research for: [TOPIC]",
  prompt: `
Research the following topic. Focus on 2025-2026 sources only.

TOPIC: [insert task description]
DATE: [today's date]

Deliver:
1. Current best practices (with source URLs)
2. Technology versions that are stable/production-ready NOW
3. Known anti-patterns to avoid
4. Community consensus (what do experts recommend?)

Output: One structured markdown section per point. Include URLs.
Do NOT pad with filler. Only verified, current information.
  `
})
```

### Task B: Explore -- Codebase

```
task({
  subagent_type: "explore",
  run_in_background: true,
  load_skills: [],
  description: "Codebase analysis for: [TOPIC]",
  prompt: `
Analyze the codebase for the following planning task.

TASK: [insert task description]
PATH: [project path]

Deliver:
1. Project structure and current tech stack (versions from lock files)
2. Existing patterns and code quality (good parts + debt)
3. Dependencies: outdated, vulnerable, or unused
4. Integration points that could break during changes
5. Gaps: what's missing for production-readiness?

Output: One structured markdown section per point. Use file:line references.
Be exhaustive but concise. No filler.
  `
})
```

### Gate 1: Research Quality Check

Before proceeding, verify:
- [ ] Librarian returned concrete findings (not just "I couldn't find much")
- [ ] Explore returned file references and specific findings
- [ ] Both outputs are >200 words of substance

**If a task returned empty/weak results:** Re-run that specific task with a more focused prompt. Do NOT proceed with garbage input -- that guarantees a garbage plan.

---

## Stage 2: PLAN (sequential)

Feed both research outputs into one planning task.

```
task({
  category: "deep",
  load_skills: [],
  run_in_background: false,
  description: "Create plan for: [TOPIC]",
  prompt: `
Create a production-ready plan based on these research findings.

TASK: [insert task description]
WEB RESEARCH: [paste Librarian output]
CODEBASE ANALYSIS: [paste Explore output]

Use this EXACT structure:

# Plan: [Title]
Created: [date] | Scope: [what]

## Summary
[3 sentences: what, why, expected result]

## Current State
[from codebase analysis -- strengths, weaknesses, critical gaps]

## Tech Decisions
[from web research -- what to use, what version, why]

## Phases

### Phase 1: [name] -- CRITICAL
- [ ] Task (effort: S/M/L, deps: none/...)
- [ ] Task ...

### Phase 2: [name] -- HIGH
- [ ] Task ...

### Phase 3: [name] -- MEDIUM (optional)
- [ ] Task ...

## Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|

## Done Criteria
- [ ] Criterion 1
- [ ] Criterion 2

RULES:
- Every task must be concrete and actionable (no "consider doing X")
- Effort estimates are mandatory
- Phase 1 must be the critical path -- smallest set of work that unblocks everything
- Maximum 3 phases. If you need more, the scope is too big -- split it.
  `
})
```

### Gate 2: Plan Completeness Check

Before proceeding, verify the plan contains:
- [ ] Summary section
- [ ] At least one phase with concrete tasks
- [ ] Effort estimates on tasks
- [ ] Risks section
- [ ] Done criteria

**If sections are missing:** Ask the planning task to fill them. Do NOT send an incomplete plan to review.

---

## Stage 3: REVIEW (sequential)

One reviewer that combines strategic advice AND critical opposition. No need for two separate agents.

```
task({
  category: "artistry",
  load_skills: [],
  run_in_background: false,
  description: "Critical review of plan for: [TOPIC]",
  prompt: `
You are reviewing a plan. Be direct and critical. No praise needed.

PLAN:
[paste plan from Stage 2]

Review checklist:
1. CRITICAL GAPS: What's missing that would cause failure?
2. FALSE ASSUMPTIONS: What does the plan assume that isn't proven?
3. PRIORITY ERRORS: Is Phase 1 actually the critical path?
4. SCOPE: Is this realistic or overambitious?
5. TECH CHOICES: Are the technology decisions sound for 2026?
6. NEW DEBT: Does this plan CREATE technical debt instead of solving it?

Output format:

## Verdict: APPROVED / NEEDS REVISION

## Issues (sorted by severity)
### CRITICAL (must fix before proceeding)
- ...
### HIGH (should fix)
- ...
### LOW (nice to have)
- ...

## Suggested Changes
[Concrete rewrites, not vague advice]

RULES:
- If the plan is solid, say APPROVED and list only minor improvements.
- If there are CRITICAL issues, say NEEDS REVISION and be specific about what to change.
- Never say "looks good overall" -- either it passes or it doesn't.
  `
})
```

### Gate 3: Review Resolution

- **APPROVED with no CRITICAL issues:** Deliver the plan to the user/caller. Done.
- **NEEDS REVISION with CRITICAL issues:** Integrate the reviewer's suggested changes into the plan yourself (do not spawn another agent). Then deliver.
- **Maximum 1 revision round.** If after revision the plan still has critical gaps, deliver it with a clear "OPEN ISSUES" section and let the user decide.

---

## Rules

### Do
- Start both research tasks in **parallel** (never sequentially)
- Check each gate **before** proceeding to the next stage
- Keep prompts **short and focused** (one job per task)
- Return the final plan directly -- no temp files needed

### Don't
- Don't spawn more than 4 `task()` calls total (2 research + 1 plan + 1 review)
- Don't add extra "consultation" or "delegation" stages
- Don't write intermediate results to disk
- Don't use agents for work you can do yourself (e.g., integrating review feedback)
- Don't loop more than once on review feedback

### Cost Awareness
- Librarian + Explore run in parallel = ~1 LLM round of latency
- Plan + Review run sequentially = ~2 LLM rounds
- Total pipeline: **~3 rounds of latency** (vs 6+ in the old design)
- If a research task returns weak results, re-run only THAT task, not both

---

## Tool Reference

| Stage | Tool | Purpose |
|-------|------|---------|
| Research | `task(subagent_type: "librarian", run_in_background: true)` | Web & docs research |
| Research | `task(subagent_type: "explore", run_in_background: true)` | Codebase analysis |
| Research | `background_output(task_id: "...")` | Check if research is done |
| Plan | `task(category: "deep", run_in_background: false)` | Synthesize plan |
| Review | `task(category: "artistry", run_in_background: false)` | Critical review |

---

## Example

```
User: "Erstelle einen Plan fuer die Migration zu ESM modules"

Agent:
1. Loads this skill
2. Starts Librarian ("ESM migration best practices 2026") + Explore (scans codebase for CJS patterns) in parallel
3. Gate 1: Both returned substance? Yes -> proceed
4. Feeds findings into Plan task -> gets structured plan with 2 phases
5. Gate 2: Plan has all sections? Yes -> proceed
6. Feeds plan into Review task -> gets APPROVED with 2 LOW suggestions
7. Gate 3: No CRITICAL issues -> integrates LOW suggestions, returns final plan
```

Total time: ~3 LLM rounds. Total tasks: 4. No temp files. No fictional agents.
