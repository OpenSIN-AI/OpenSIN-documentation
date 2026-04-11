# 🏗️ Antigravity Rotator 1.0.0 Architecture

This document describes the high-level architecture and the "No-Wall" hacker methods used to make this rotator the most robust version ever built.

## 1. Zero-Trust Chrome Session (Profile Wipe)
Most automation fails because of cookie residue or "Choose an account" prompts from previous sessions.
- **The Problem**: Persistent browser profiles accumulate state that leads to non-deterministic UI flows.
- **The Method**: Before every rotation, the `chrome_profile` directory is completely deleted (`shutil.rmtree`).
- **The Result**: Chrome starts 100% fresh. Google is forced to present the initial login screen, eliminating any "Account Chooser" or "Verify it's you" confusion based on previous sessions.

## 2. Human-Emulation (Enter Key Bypass)
React-based applications like Google Login often block simulated button clicks (DOM `.click()`) or have invisible overlays that trap the mouse.
- **The Problem**: Selectors like `#identifierNext` are often "visible" but not "interactable" in the React lifecycle, causing automation to hang.
- **The Method**: Instead of clicking the button, the bot types the email/password and then sends a native **Keyboard Enter** event.
- **The Result**: Form submission is triggered at the OS level, which React cannot block without breaking accessibility for real users. This bypasses 99% of UI-based bot detection.

## 3. The Trash-Recycling Cycle (Undelete API)
Google Workspace has aggressive abuse protection (Error 412) when creating many accounts in a short time.
- **The Problem**: Creating and deleting 50 accounts a day triggers abuse flags.
- **The Method**: Instead of `Create -> Use -> Delete`, we use a recycling loop. Accounts are moved to the Trash (Deleted status). The rotator searches for deleted accounts and uses the `service.users().undelete()` API.
- **The Result**: We recycle a small pool of `rotator-*` accounts indefinitely. To Google, this looks like normal administrative user management, bypassing account creation limits.

## 4. Ultra-Wide Virtual Terminal (PTY Scaling)
Opencode's TUI (`clack`) is extremely sensitive to line breaks. A 1000-character Google OAuth URL will wrap and break on a standard 80-character terminal.
- **The Problem**: Wrapped URLs contain hidden newline characters (`\n`), which corrupt the OAuth token when pasted into the Opencode TUI.
- **The Method**: The virtual terminal (`pexpect.spawn`) is initialized with `dimensions=(200, 4000)`.
- **The Result**: The entire URL/Code fits on a single horizontal line, ensuring bit-perfect input for the Opencode CLI.

## 5. Auto-Purge Self-Healing
To prevent the "Zombie Account" issue where old accounts still appear in the Opencode CLI or Google Workspace:
- **The Method**: Every successful rotation ends with a `cleanup_all_except(new_email)` call.
- **The Action**:
    1. **Local**: Scans `antigravity-accounts.json` and deletes every entry starting with `rotator-` except the new one.
    2. **Cloud**: Scans Google Workspace and deletes (moves to Trash) all other active `rotator-*` accounts.
- **The Result**: The system state is reset to "Single Active Rotator" after every run, preventing configuration drift.

## 6. Phase 1: Intelligence & Quality Modules
In Phase 1, the architecture is extended with specialized agents for diagnostics and quality assurance.

### 6.1 Enhanced Debugging System (`src/debugger.py`)
- **Purpose**: Provides a "Flight Recorder" for errors.
- **Mechanism**: Intercepts exceptions and matches them against a regex-based pattern registry. It maintains a persistent JSON database of errors to identify recurring issues and suggest proven solutions.

### 6.2 Code Review Bot (`src/code_review.py`)
- **Purpose**: Automated quality gate.
- **Mechanism**: Performs static analysis using AST (Abstract Syntax Tree) and regex scanning. It scores code based on security, complexity, and maintainability, ensuring that new features don't introduce technical debt or vulnerabilities.

## 7. Phase 2: Collaboration & Delivery Modules
Phase 2 adds workflow tools that make it easier to collaborate, generate tests, and inspect changes.

### 7.1 Live Collaboration (`src/live_collaboration.py`)
- **Purpose**: Shared edit sessions with revision tracking.
- **Mechanism**: Tracks participants, applies line-based edits, detects stale revisions, and persists sessions as JSON.

### 7.2 Automated Test Generation (`src/testgen.py`)
- **Purpose**: Produce runnable pytest smoke tests from source code.
- **Mechanism**: Parses AST signatures, infers safe sample inputs, and emits a test module for public functions and classes.

### 7.3 Visual Diff Viewer (`src/visual_diff.py`)
- **Purpose**: Review code changes quickly.
- **Mechanism**: Uses SequenceMatcher to build side-by-side and unified diff views with change-impact metrics.

## 8. Phase 3: Performance, Security, and Workspaces
Phase 3 adds operational tooling for profiling, security review, and multi-repo orchestration.

### 8.1 Performance Profiler (`src/profiler.py`)
- **Purpose**: Measure hot paths and script runtime.
- **Mechanism**: Wraps `cProfile`/`pstats` in callable and script helpers plus a scoped context manager.

### 8.2 Security Scanner (`src/security_scan.py`)
- **Purpose**: Detect risky Python code with AST-first analysis.
- **Mechanism**: Visits the syntax tree for dangerous calls, shell execution, and obvious secret assignment patterns.

### 8.3 Workspace Manager (`src/workspace_manager.py`)
- **Purpose**: Track multiple git repositories and worktrees.
- **Mechanism**: Uses git subprocess calls with an explicit cwd and stores registry data as JSON.

## 9. Phase 4: Policy, Memory, Evaluation, and Aliases
Phase 4 adds cross-cutting safety and coordination tools inspired by the latest OpenClaw features.

### 9.1 Security Policy Guard (`src/policy_guard.py`)
- **Purpose**: Catch SSRF and config injection issues before they execute.
- **Mechanism**: Resolves URLs to IPs, checks for restricted address ranges, scans env mappings for interpolation tokens, and inspects registry documents for alias collisions.

### 9.2 Memory Wiki (`src/memory_wiki.py`)
- **Purpose**: Turn logs into durable, searchable memory.
- **Mechanism**: Stores hot JSONL events, synthesizes warm markdown digests, and archives cold entries for later recall.

### 9.3 QA Lab (`src/qa_lab.py`)
- **Purpose**: Compare candidate outputs before promoting them.
- **Mechanism**: Runs deterministic text scoring in parallel and ranks candidates with a structured report.

### 9.4 Provider Alias Registry (`src/provider_alias_registry.py`)
- **Purpose**: Keep provider variants reproducible and collision-free.
- **Mechanism**: Stores alias bindings in a lockfile and rejects duplicate alias claims.

---

## 10. Phase 5: Routing, Search, and Workboards

### 10.1 Taskboard (`src/taskboard.py`)
- **Purpose**: Persist lightweight operational work items.
- **Mechanism**: Stores task records in SQLite with status transitions, reconciliation, and snapshot reporting.

### 10.2 SearXNG Client (`src/search_client.py`)
- **Purpose**: Query a trusted SearXNG endpoint for private search workflows.
- **Mechanism**: Normalizes trusted base URLs, fetches JSON search results, and renders human-readable or JSON reports.

### 10.3 Guardrails (`src/guardrails.py`)
- **Purpose**: Intercept unsafe prompts and outputs before they spread.
- **Mechanism**: Evaluates regex-backed input/output rules and supports blocking or redaction decisions.

### 10.4 Cron Allow-List (`src/cron_allowlist.py`)
- **Purpose**: Restrict scheduled commands to approved argv prefixes.
- **Mechanism**: Splits commands with shell-aware parsing, checks for metacharacters, and persists rule sets to JSON.

### 10.5 Failover Router (`src/failover_router.py`)
- **Purpose**: Route work to healthy providers with cooldown-aware fallback.
- **Mechanism**: Maintains route candidates, records success/failure outcomes, and skips candidates under cooldown.

---
**Branding**: OpenSIN / sincode
