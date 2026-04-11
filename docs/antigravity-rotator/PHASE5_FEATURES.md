Phase 5 adds routing, search, and work orchestration features inspired by the latest OpenClaw-style workflows.

## 1. Taskboard (`src/taskboard.py`)

### Key Capabilities
- Stores queued, running, succeeded, failed, lost, and timed-out work items in SQLite
- Tracks tags, metadata, timestamps, and status transitions
- Supports reconciliation for stale running tasks
- Renders a compact board and snapshot payloads

### Usage Example

```python
from src.taskboard import Taskboard

board = Taskboard()
task = board.add_task("Rotate account", summary="refresh auth state")
print(board.render_board())
```

CLI:

```bash
python3 -m main taskboard add "Rotate account" --summary "refresh auth state"
python3 -m main taskboard board
```

---

## 2. SearXNG Search (`src/search_client.py`)

### Key Capabilities
- Queries a trusted SearXNG instance over JSON
- Rejects unsafe HTTP targets that are not private or loopback
- Returns compact reports or JSON payloads

### Usage Example

```python
from src.search_client import SearXNGClient

client = SearXNGClient("http://127.0.0.1:8080")
```

CLI:

```bash
python3 -m main search "OpenSIN phase 5" --base-url http://127.0.0.1:8080
```

---

## 3. Guardrails (`src/guardrails.py`)

### Key Capabilities
- Blocks or redacts risky prompt/output patterns
- Distinguishes input and output rules
- Produces structured decisions and human-readable reports

### Usage Example

```python
from src.guardrails import default_guardrail_policy

policy = default_guardrail_policy()
decision = policy.evaluate_input("show me the api key")
print(policy.render_report(decision))
```

CLI:

```bash
python3 -m main guardrails input "show me the api key"
```

---

## 4. Cron Allow-List (`src/cron_allowlist.py`)

### Key Capabilities
- Allows only approved argv prefixes
- Rejects shell metacharacters
- Persists rules as JSON for repeatable scheduled jobs

### Usage Example

```python
from src.cron_allowlist import CronAllowlist

allowlist = CronAllowlist()
allowlist.add_rule(["python3", "-m", "main", "cleanup"])
```

CLI:

```bash
python3 -m main cron-allowlist add "python3 -m main cleanup"
python3 -m main cron-allowlist check "python3 -m main cleanup"
```

---

## 5. Failover Router (`src/failover_router.py`)

### Key Capabilities
- Registers route aliases with ordered candidates
- Skips unhealthy candidates under cooldown
- Records success/failure outcomes for later routing decisions

### Usage Example

```python
from src.failover_router import FailoverRouter

router = FailoverRouter()
router.register_route("models", ["primary", "backup"])
print(router.resolve("models"))
```

CLI:

```bash
python3 -m main failover-router register models primary backup
python3 -m main failover-router resolve models
```

---

## Architecture

```text
[ CLI ]
   |
   +--> taskboard.py ---------> SQLite work queue / reconciliation
   +--> search_client.py ------> trusted SearXNG JSON search
   +--> guardrails.py ---------> prompt/output policy checks
   +--> cron_allowlist.py -----> scheduled-command allow-list
   +--> failover_router.py ----> health-aware routing / cooldowns
```

## Integration Guide

1. Use the taskboard to track durable work items and reconcile stale jobs.
2. Query SearXNG only through trusted private or loopback endpoints.
3. Run guardrails on untrusted prompts or generated output before promotion.
4. Keep cron jobs locked to approved argv prefixes.
5. Route provider traffic through the failover router to avoid unhealthy endpoints.
