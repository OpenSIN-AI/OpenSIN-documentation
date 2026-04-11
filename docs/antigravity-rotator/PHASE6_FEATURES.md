# Phase 6 Features: Subagent & Remote Control API

> **Sprint 2 — Issue #36**
> Programmatic subagent spawning, monitoring, and fleet orchestration for the Antigravity Rotator.

---

## 1. SubagentManager (`src/subagent_manager.py`)

The SubagentManager is the core engine for spawning and tracking background subagent processes. It provides a thread-safe, SQLite-backed API for the full subagent lifecycle.

### Key Capabilities
- **Spawn**: Start background `opencode run` processes with any supported agent type
- **Status**: Query the lifecycle state of any subagent (queued → running → completed/failed/killed/zombie)
- **Read**: Capture stdout/stderr from running or completed agents
- **Kill**: Gracefully terminate running agents (SIGTERM → SIGKILL escalation)
- **Reconcile**: Detect and clean up zombie processes after manager restarts
- **Fleet Status**: Render a human-readable dashboard of all agents
- **Purge**: Delete old terminal entries to prevent unbounded DB growth

### Supported Agent Types
| Type | Purpose |
|------|---------|
| `explore` | Fast codebase search and file discovery |
| `librarian` | Documentation lookup and reference retrieval |
| `oracle` | Architecture advice and design review |
| `general` | Multi-purpose worker for arbitrary tasks |

### Usage Examples

```python
from src.subagent_manager import SubagentManager

manager = SubagentManager()

# 1. Spawn a subagent
handle = manager.spawn("explore", "find all Python files with security issues")
print(f"Spawned: {handle.id} (PID: {handle.pid})")

# 2. Check status
status = manager.status(handle.id)
print(f"Status: {status.status}")

# 3. Read output
output = manager.read(handle.id)
print(output)

# 4. Kill a running agent
manager.kill(handle.id)

# 5. Fleet dashboard
print(manager.render_fleet_status())

# 6. Cleanup
manager.reconcile()         # Mark zombies
manager.purge_terminal()    # Delete old entries
```

---

## 2. RemoteControl (`src/remote_control.py`)

The RemoteControl facade provides high-level orchestration on top of SubagentManager. It enables batch operations that are common in fleet management.

### Key Capabilities
- **Parallel Dispatch**: Spawn multiple agents in a single call with fail-fast validation
- **Wait All**: Block until all agents finish (with configurable timeout)
- **Collect Results**: Gather output from multiple completed agents
- **Batch Summary**: Render a formatted summary of dispatch results

### Usage Examples

```python
from src.remote_control import RemoteControl

rc = RemoteControl()

# 1. Dispatch multiple agents in parallel
result = rc.dispatch_parallel([
    {"agent_type": "explore", "task": "find all API endpoints"},
    {"agent_type": "oracle", "task": "review security architecture"},
    {"agent_type": "general", "task": "generate test coverage report"},
])

# 2. Wait for all to finish (max 10 minutes)
completed = rc.wait_all(result, timeout=600)

# 3. Collect results
outputs = rc.collect_results(result)
for agent_id, output in outputs.items():
    print(f"Agent {agent_id}: {output[:200]}")

# 4. Batch summary
print(rc.render_batch_summary(result))
```

---

## 3. CLI Commands

All subagent operations are accessible via the CLI:

```bash
# Spawn a new subagent
python3 -m main subagent spawn explore "analyze codebase structure"
python3 -m main subagent spawn oracle "review security design" --timeout 300

# List all subagents
python3 -m main subagent list
python3 -m main subagent list --status running
python3 -m main subagent list --json

# Get status of a specific subagent
python3 -m main subagent status sa_abc123def456
python3 -m main subagent status sa_abc123def456 --json

# Read output from a subagent
python3 -m main subagent read sa_abc123def456

# Kill a running subagent
python3 -m main subagent kill sa_abc123def456

# Fleet status dashboard
python3 -m main subagent fleet-status

# Reconcile zombie processes
python3 -m main subagent reconcile

# Purge old entries (default: older than 24 hours)
python3 -m main subagent purge
python3 -m main subagent purge --older-than 3600
```

---

## 4. Architecture

```text
[ User / CLI / Daemon ]
        |
        v
[ RemoteControl (Facade) ]
        |
        +--→ dispatch_parallel() → spawn N agents
        +--→ wait_all()          → poll until all terminal
        +--→ collect_results()   → gather stdout from each
        +--→ render_*()          → human-readable status
        |
        v
[ SubagentManager (Engine) ]
        |
        +--→ spawn()      → subprocess.Popen + reader thread
        +--→ status()     → SQLite lookup + PID refresh
        +--→ read()       → return captured stdout
        +--→ kill()       → SIGTERM → SIGKILL escalation
        +--→ reconcile()  → detect zombie PIDs
        +--→ purge()      → delete old terminal entries
        |
        v
[ SQLite DB ]                    [ OS Processes ]
subagents.db                     opencode run "task" --format json
  ├── id                           ├── stdout → captured by reader thread
  ├── agent_type                   ├── stderr → captured by reader thread
  ├── status                       └── exit_code → harvested on completion
  ├── task
  ├── pid
  ├── output
  └── ...
```

## 5. Integration Guide

1. **From the Daemon**: The rotator daemon can spawn subagents for auxiliary tasks (e.g., pre-rotation health checks) using `SubagentManager.spawn()`.
2. **From the CLI**: Users can manage subagents interactively via `python3 -m main subagent`.
3. **From Other Modules**: Import `RemoteControl` for batch orchestration in Python code.
4. **Fleet Monitoring**: Use `fleet-status` or `render_fleet_status()` for real-time visibility.
5. **Cleanup Automation**: Schedule `reconcile` and `purge` via cron or the daemon's guardian cycle.

---
**Branding**: OpenSIN / sincode
