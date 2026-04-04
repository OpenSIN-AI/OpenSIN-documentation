# sovereign-research (Deep Research Swarm & CEO Edition)

(opencode - Skill) The March 2026 gold standard for deep, multi-source research. Fuses a bounded multi-agent swarm with the A2A-SIN-Research pipeline, enabling Perplexity-killer answers, live authenticated multi-platform crawling (via A2A-SIN-Authenticator), and persistent Drive artifacts. Inspired by Gemini Deep Research workflows.

## Triggers

**MANDATORY USE:** Keywords "research", "find out", "what is the best", "compare", "state of the art", "deep dive", "investigate", "analyze topic", "deep research".

## Architecture

This skill replaces linear, single-agent searches with an **Aggressive Multi-Agent Swarm**:

```
User Query
    |
    v
[Phase 1: Swarm Fan-Out (Parallel)]
    ├─> Librarian Task A: Google Search & Webfetch (General Context)
    ├─> Librarian Task B: Exa Search (Category filtered: papers/company)
    ├─> Explore Task C: GitHub/Code search (grep_app_searchGitHub)
    └─> Explore Task D: Authenticated Portal Search (X, Discord, Custom via A2A-SIN-Authenticator)
    |
    v
[Phase 2: Source Gather & Validate]
    Wait for tasks (background_output) -> deduplicate, score authority, date-check
    |
    v
[Phase 3: Deep Research (Optional / Complex Queries)]
    sin.research.run (A2A-SIN-Research) -> NotebookLM swarms, NIM analysis, Drive persistence
    |
    v
[Phase 4: Review & Synthesis]
    Artistry Task: Critical Review (Gaps, counter-arguments, missing sources)
    Output: Structured cited answer with confidence scores.
```

## Protocol

### Step 1: Deep Research Swarm Fan-Out (Max 5-10 Minutes)

Launch parallel background tasks using the `task` tool to gather maximum context without blocking. 

```javascript
// Example: Launching parallel subagents
task({
  subagent_type: "librarian",
  run_in_background: true,
  load_skills: [],
  description: "Exa-based academic/company research",
  prompt: "Run websearch_web_search_exa for [Query]. Deep read the top 3 URLs using webfetch. Return structured findings."
});

task({
  subagent_type: "explore",
  run_in_background: true,
  load_skills: [],
  description: "Codebase & GitHub research",
  prompt: "Use grep_app_searchGitHub to find real implementations of [Query]. Return code patterns."
});
```

*For Authenticated Portals (e.g., hundreds of platforms like X, Discord, Reddit, custom enterprise tools):*
Request `A2A-SIN-Authenticator` to handle mass-platform login and cookie injection via `webauto-nodriver-mcp` or `curl_cffi`, allowing the explore agents to read auth-gated data safely.

### Step 2: Gather & Source Validation

Check `background_output(task_id=...)` for all launched agents. Do not proceed until you have gathered all findings.

Validate the sources:
- Score authority (Official Docs > Blogs > Forums).
- Flag stale content (>6 months old).
- Ensure explicit traceability: every claim MUST link directly to its source URL.

### Step 3: A2A Deep Research (For Highly Complex Queries)

Only invoke if the query spans 10+ sources, requires video/image parsing, or requires persistent artifacts.

```bash
# Plan first
sin-research run-action '{"action":"sin.research.plan","query":"...","targetDepth":"deep","includeAuthSources":true}'

# Then execute
sin-research run-action '{"action":"sin.research.run","query":"...","targetDepth":"deep","confirm":true}'
```
This triggers the native A2A backend to spin up NotebookLM instances, process multimodal data (NVIDIA NIM), and persist to Google Drive.

### Step 4: Verification & Synthesis

Launch a final **Artistry** task to review the synthesized findings:
```javascript
task({
  subagent_type: "artistry",
  run_in_background: false,
  load_skills: [],
  description: "Critical review of research",
  prompt: "Review these findings. Are there gaps? False claims? Uncited sources? Provide concrete rewrites."
})
```

Return the final structured answer to the user:
```markdown
## Answer
<Direct answer to the query>

## Key Findings
1. <Finding with [Source 1] citation>
2. <Finding with [Source 2] citation>

## Sources
| # | Source | Authority | Date | URL |
|---|--------|-----------|------|-----|
| 1 | Official Docs | High | 2026-03 | https://... |

## Confidence: <HIGH/MEDIUM/LOW>
## Research Depth: <SWARM/DEEP>
```

## Anti-Patterns

- NEVER return search results without launching parallel background agents first. Deep research requires volume.
- NEVER cite a source without verifying its date (stale = warning).
- NEVER run `sin.research.run` for simple factual queries (waste of NotebookLM quota).
- **NEVER autonomously switch technologies during research.** Technology decisions are EXCLUSIVELY the user's prerogative.
- **PERMANENTLY BANNED technologies:** Camoufox, Playwright, Puppeteer, Selenium, any Firefox-based browser automation. The ONLY approved browser automation stack is **nodriver + Chrome profile**, **webauto-nodriver-mcp**, **CDP**, and **curl_cffi**. Violation = immediate ban from the project.

## Integration Points

- **A2A-SIN-Authenticator**: Controls mass-platform auth orchestration. Provides authenticated handles/sessions to `webauto-nodriver-mcp`/`curl_cffi` so research agents can bypass auth gates.
- **A2A-SIN-Research** (`sin.research.*`): Full deep-research pipeline with NVIDIA NIM, NotebookLM, Drive persistence.
- **google_search** / **websearch_web_search_exa**: Live crawling.
- **grep_app_searchGitHub**: Real code pattern search across 1M+ public GitHub repos.