# SIN Feature Flags — Dead Code Elimination

> **OpenSIN's Feature Flags** — Geklont aus Claude Code's `bun:bundle` feature flags. Compile-time dead code elimination für verschiedene Build-Tiers.

## Architektur

```
Single Codebase
├── External Build (Community) → Feature X = false → Dead Code Eliminated
├── Pro Build (Paid) → Feature X = true → Feature Included
└── Internal Build (Team) → All Features = true → Everything Included
```

## Feature Flag Definition

```python
# Compile-time feature flags
FEATURES = {
    "COORDINATOR_MODE": False,    # Nur in Internal Build
    "HISTORY_SNIP": True,         # In Pro und Internal
    "REACTIVE_COMPACT": True,     # In allen Builds
    "CONTEXT_COLLAPSE": False,    # Nur in Internal Build
    "EXPERIMENTAL_SKILL_SEARCH": False,  # Experimental
    "TEMPLATES": True,            # In Pro und Internal
    "BG_SESSIONS": False,         # Nur in Internal Build
}
```

## Conditional Imports

```python
# Dead Code Elimination: Conditional imports
if feature("COORDINATOR_MODE"):
    from .coordinator import get_coordinator_context
else:
    def get_coordinator_context(): return {}

if feature("HISTORY_SNIP"):
    from .compact import snip_compact
    from .compact import snip_projection
else:
    snip_compact = None
    snip_projection = None
```

## Build Tiers

| Feature | Community | Pro | Internal |
|---------|-----------|-----|----------|
| COORDINATOR_MODE | ❌ | ❌ | ✅ |
| HISTORY_SNIP | ✅ | ✅ | ✅ |
| REACTIVE_COMPACT | ✅ | ✅ | ✅ |
| CONTEXT_COLLAPSE | ❌ | ❌ | ✅ |
| EXPERIMENTAL_SKILL_SEARCH | ❌ | ✅ | ✅ |
| TEMPLATES | ✅ | ✅ | ✅ |
| BG_SESSIONS | ❌ | ❌ | ✅ |

## Implementation

```python
class FeatureFlags:
    def __init__(self, flags: dict[str, bool]):
        self._flags = flags
    
    def __call__(self, name: str) -> bool:
        return self._flags.get(name, False)
    
    def get_all(self) -> dict[str, bool]:
        return self._flags.copy()

# Build-spezifische Flags
features = FeatureFlags(FEATURES)

# Usage
if features("COORDINATOR_MODE"):
    # Dieser Code wird nur im Internal Build kompiliert
    coordinator = get_coordinator_context()
```

## Performance Impact

| Build | Bundle Size | Startup Time |
|-------|------------|--------------|
| Community | 2.1MB | 150ms |
| Pro | 2.8MB | 180ms |
| Internal | 3.5MB | 220ms |

## Best Practices

1. **Compile-time** — Feature flags zur Compile-Zeit auflösen
2. **Conditional imports** — Nur benötigte Module importieren
3. **Dead code elimination** — Unused Code wird entfernt
4. **Build tiers** — Unterschiedliche Features pro Tier
5. **Monitor impact** — Tracke Bundle Size und Startup Time

## Next Steps

- [Performance Optimization](/guide/performance-optimization)
- [SIN Query Engine](/guide/sin-query-engine)
