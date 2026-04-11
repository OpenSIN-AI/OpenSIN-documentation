# 🚀 Phase 9 Features: Marketplace & Monetization

> **Status:** Implemented (Issue #46) — OpenSIN AI now has a full agent marketplace layer that Claude Code completely lacks.

Phase 9 gives every OpenSIN AI agent a discoverable pricing record, usage tracking, purchase management, and billing reports — all stored in a portable SQLite database that works identically on Mac, OCI VMs, and HF VMs.

---

## Why This Makes OpenSIN Better Than Claude Code

Claude Code has no concept of an agent marketplace, pricing models, or usage billing. OpenSIN AI agents can now be registered, purchased, metered, and billed — enabling a full SIN Solver commercial storefront without any external SaaS dependency.

---

## 1. AgentRegistry (`src/marketplace.py`)

Central SQLite-backed catalogue of all marketplace agents.

### Key Capabilities

- **Upsert Registration**: Register or update any agent with a single call — CI pipelines can re-register on every deploy without duplicates.
- **Versioned Metadata**: Each agent record carries `id`, `name`, `description`, `version`, `pricing_model`, `price`, `currency`, `tags`, and `author`.
- **Tag Filtering**: `list_agents(tag="security")` returns only agents whose tag list matches the substring.
- **CRUD**: `get_agent`, `list_agents`, `delete_agent` — all thread-safe via connection-per-call pattern.

### Usage

```python
from src.marketplace import AgentRegistry

registry = AgentRegistry()

# Register a new agent (or update existing)
agent = registry.register(
    agent_id="sin-security",
    name="SIN Security Scanner",
    description="AST-based vulnerability detection",
    pricing_model="per_call",
    price=0.02,
    tags=["security", "opensin"],
    author="OpenSIN",
)

# List all agents
agents = registry.list_agents()

# Filter by tag
security_agents = registry.list_agents(tag="security")
```

---

## 2. PricingEngine (`src/marketplace.py`)

Stateless cost calculator for usage events.

### Supported Pricing Models

| Model | Behaviour |
|-------|-----------|
| `free` | Always $0.00 |
| `per_call` | `price × quantity` |
| `per_token` | `price × (quantity / 1000)` |
| `flat_monthly` | $0 per-event (already paid via subscription) |

### Usage

```python
from src.marketplace import PricingEngine, AgentRegistry

registry = AgentRegistry()
agent = registry.get_agent("sin-security")

engine = PricingEngine()
cost = engine.compute_cost(agent, event_type="call", quantity=10)
# → $0.20 for 10 calls at $0.02 each
```

---

## 3. PurchaseManager (`src/marketplace.py`)

Records one-time purchases and monthly subscriptions, with active/expired state tracking.

### Key Capabilities

- **One-Time Purchase**: Grants lifetime access — `expires_at = NULL`.
- **Subscription**: Grants access for N months, then expires automatically.
- **Active Check**: `has_active_purchase(user_id, agent_id)` returns `True`/`False` for gate-keeping.
- **Cancellation**: `cancel_subscription(purchase_id)` marks a subscription inactive.

### Usage

```python
from src.marketplace import PurchaseManager

pm = PurchaseManager()

# Record a monthly subscription
purchase = pm.purchase(
    user_id="fleet@opensin.ai",
    agent_id="sin-security",
    purchase_type="subscription",
    amount_paid=9.99,
    months=1,
)

# Check entitlement
pm.has_active_purchase("fleet@opensin.ai", "sin-security")  # → True
```

---

## 4. UsageTracker (`src/marketplace.py`)

Records every call or token batch consumed by a user for an agent, with auto-pricing from the registry.

### Key Capabilities

- **Auto-Pricing**: If `cost` is not supplied, the tracker looks up the agent in the registry and calls `PricingEngine.compute_cost` automatically.
- **Manual Override**: Pass `cost=X` to override auto-pricing (useful for flat-rate deals).
- **Summary Aggregation**: `get_usage_summary` returns `total_calls`, `total_tokens`, `total_cost`, `event_count` filtered by user, agent, and/or date.
- **Event History**: `list_events` returns raw events newest-first for audit logs.

### Usage

```python
from src.marketplace import UsageTracker

tracker = UsageTracker()

# Record 5 calls (cost is auto-computed from registry)
for _ in range(5):
    tracker.record_usage("fleet@opensin.ai", "sin-security", "call", 1)

# Get aggregate summary
summary = tracker.get_usage_summary("fleet@opensin.ai", agent_id="sin-security")
# → {"total_calls": 5, "total_tokens": 0, "total_cost": 0.10, "event_count": 5}
```

---

## 5. BillingReport (`src/marketplace.py`)

Generates human-readable (ASCII) or JSON billing reports for any user.

### Key Capabilities

- **Per-Agent Breakdown**: Line items per agent showing calls, tokens, and cost.
- **Purchase History**: Lists all purchases (active and cancelled) with expiry info.
- **Month Filtering**: `month="2026-04"` filters usage events to that calendar month.
- **OpenSIN Branding**: All report headers carry the OpenSIN AI Marketplace brand.

### Usage

```python
from src.marketplace import BillingReport

reporter = BillingReport()
report = reporter.generate("fleet@opensin.ai", month="2026-04")
print(report["text"])
```

### Sample Report Output

```
============================================================
  OpenSIN AI Marketplace — Billing Report
  User    : fleet@opensin.ai
  Period  : April 2026
============================================================

USAGE SUMMARY
----------------------------------------
  Total calls  : 5
  Total tokens : 0
  Total cost   : $0.100000 USD

AGENT BREAKDOWN
----------------------------------------
  [sin-security] SIN Security Scanner
    Model: per_call | Calls: 5 | Tokens: 0 | Cost: $0.100000

PURCHASES
----------------------------------------
  a1b2c3d4… | sin-security | subscription | $9.99 | ACTIVE | expires: 2026-05-11T12:00:00.000000Z

  TOTAL PAID (active subscriptions/purchases): $9.99 USD
============================================================
```

---

## 6. CLI Subcommands

All marketplace operations are available via `python3 -m main marketplace <subcommand>`.

```bash
# List all registered agents
python3 -m main marketplace list-agents
python3 -m main marketplace list-agents --tag security --json

# Register a new agent
python3 -m main marketplace register-agent sin-security "SIN Security" "AST vuln scan" per_call 0.02 \
  --tags security,opensin --author OpenSIN

# Record a purchase
python3 -m main marketplace purchase fleet@opensin.ai sin-security \
  --type subscription --amount 9.99 --months 1

# Record a usage event
python3 -m main marketplace record-usage fleet@opensin.ai sin-security call 5

# Generate billing report
python3 -m main marketplace billing-report fleet@opensin.ai --month 2026-04
python3 -m main marketplace billing-report fleet@opensin.ai --json
```

---

## 7. Test Coverage

Phase 9 adds **35 new tests** in `tests/test_marketplace.py`:

| Test Class | Tests |
|------------|-------|
| `TestAgentRegistry` | 8 |
| `TestPricingEngine` | 5 |
| `TestPurchaseManager` | 7 |
| `TestUsageTracker` | 7 |
| `TestBillingReport` | 6 |
| `TestMarketplaceIntegration` | 1 (end-to-end pipeline) |
| **Total** | **35** |

All 163 tests pass (128 existing + 35 new).

---

## 8. Architecture Highlights

- **Zero external dependencies**: Uses only Python stdlib (`sqlite3`, `json`, `uuid`, `datetime`).
- **Thread-safe**: Every public method opens its own connection (no shared state).
- **WAL journal mode**: Allows concurrent readers alongside a single writer.
- **Portable**: Same `.db` file works on Mac, OCI VM, and HF VM — no server setup needed.
- **OpenSIN branding**: All outputs, reports, and CLI help strings carry the OpenSIN AI brand.
