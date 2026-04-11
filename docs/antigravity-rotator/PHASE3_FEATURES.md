# Phase 3 Features: Profiling, Security, and Workspace Management

Phase 3 adds operational tooling for performance, security, and multi-repo workflow control.

## 1. Performance Profiler (`src/profiler.py`)

### Key Capabilities
- Profiles callables and scripts with `cProfile`
- Produces deterministic summary text and JSON-ready output
- Supports scoped profiling with a context manager

### Usage Example

```python
from src.profiler import PerformanceProfiler

profiler = PerformanceProfiler()
result = profiler.profile_callable("sample", lambda: sum(range(1000)))
print(profiler.render_summary(result))
```

CLI:

```bash
python3 -m main profile tests/fixtures/phase3/profile_target.py
```

---

## 2. Security Scanner (`src/security_scan.py`)

### Key Capabilities
- AST-based detection of `eval`, `exec`, and shell execution
- Finds hardcoded secrets in obvious assignment patterns
- Scans individual files or entire directories
- Emits structured findings and plain-text reports

### Usage Example

```python
from src.security_scan import SecurityScanner

scanner = SecurityScanner()
findings = scanner.scan_file("tests/fixtures/phase3/vulnerable.py")
print(scanner.render_report(findings))
```

CLI:

```bash
python3 -m main scan-security tests/fixtures/phase3
```

---

## 3. Workspace Manager (`src/workspace_manager.py`)

### Key Capabilities
- Registers git repositories in a JSON registry
- Adds detached worktrees with explicit paths
- Returns status and branch metadata without changing process cwd
- Supports multiple named workspaces

### Usage Example

```python
from src.workspace_manager import WorkspaceManager

manager = WorkspaceManager()
manager.register_repo("demo", "/tmp/repo")
manager.add_worktree("demo", "/tmp/repo-wt")
print(manager.status("demo").to_dict())
```

CLI:

```bash
python3 -m main workspace list
```

---

## Architecture

```text
[ CLI ]
   |
   +--> profiler.py --------> cProfile / pstats
   +--> security_scan.py ---> AST visitor / findings
   +--> workspace_manager.py -> git subprocess / JSON registry
```

## Integration Guide

1. Use the profiler to measure slow paths before optimization.
2. Use the security scanner in CI or pre-commit hooks.
3. Use the workspace manager to coordinate multiple git worktrees without `os.chdir`.
