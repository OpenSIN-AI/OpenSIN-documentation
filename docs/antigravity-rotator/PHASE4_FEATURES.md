# Phase 4 Features: Policy Guard, Memory Wiki, QA Lab, Provider Aliases

Phase 4 adds higher-order safety and coordination tools inspired by the latest OpenClaw release.

## 1. Security Policy Guard (`src/policy_guard.py`)

### Key Capabilities
- Detects SSRF-style destination risks before request execution
- Flags env-injection patterns in workspace or configuration data
- Detects provider/auth alias collisions in registry documents

### Usage Example

```python
from src.policy_guard import SecurityPolicyGuard

guard = SecurityPolicyGuard()
findings = guard.scan_url("http://127.0.0.1/admin")
print(guard.render_report(findings))
```

CLI:

```bash
python3 -m main policy-guard url http://127.0.0.1/admin
```

---

## 2. Memory Wiki (`src/memory_wiki.py`)

### Key Capabilities
- Hot, warm, and cold memory tiers
- Log ingestion from files and sessions
- Dream-style synthesis into markdown summaries and triples
- Search across stored memory tiers

### Usage Example

```python
from src.memory_wiki import MemoryWiki

wiki = MemoryWiki()
wiki.ingest_event("provider alias collision fixed", source="session-1")
digest = wiki.sleep()
print(wiki.render_digest(digest))
```

CLI:

```bash
python3 -m main memory-wiki ingest logs/session.log
python3 -m main memory-wiki sleep
```

---

## 3. QA Lab (`src/qa_lab.py`)

### Key Capabilities
- Compares candidate outputs in parallel
- Ranks outputs with deterministic text metrics
- Produces JSON and text reports

### Usage Example

```python
from src.qa_lab import QALab

lab = QALab()
report = lab.compare_texts("ref", "alpha beta", {"candidate": "alpha beta"})
print(lab.render_report(report))
```

CLI:

```bash
python3 -m main qa-lab compare reference.txt --candidate best=best.txt
```

---

## 4. Provider Alias Registry (`src/provider_alias_registry.py`)

### Key Capabilities
- Registers provider bindings under stable aliases
- Rejects alias collisions
- Persists bindings to a lockfile

### Usage Example

```python
from src.provider_alias_registry import ProviderAliasRegistry

registry = ProviderAliasRegistry()
registry.register("balanced", "openai", profile="prod")
print(registry.resolve("balanced").provider)
```

CLI:

```bash
python3 -m main provider-alias register balanced openai --profile prod
```

---

## Architecture

```text
[ CLI ]
   |
   +--> policy_guard.py ---------> SSRF / env / registry checks
   +--> memory_wiki.py ----------> hot/warm/cold memory synthesis
   +--> qa_lab.py ----------------> parallel evaluation / ranking
   +--> provider_alias_registry.py -> alias lockfile / collision control
```

## Integration Guide

1. Run the policy guard on untrusted workspace config and local URLs before execution.
2. Use the memory wiki to distill logs and agent traces into reusable summaries.
3. Use QA Lab to compare candidate outputs before selecting a production model or prompt.
4. Use the alias registry to keep provider variants reproducible and collision-free.
