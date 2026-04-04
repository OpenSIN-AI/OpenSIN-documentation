# SIN Compiled Features — Build Tier Architecture

> **OpenSIN's Build Tiers** — Geklont aus Claude Code's feature flags. Ein Codebase, verschiedene Builds.

## Build Tier Architecture

```
Single Codebase
├── Community Build → Essential Features Only
├── Pro Build → Essential + Advanced Features
└── Enterprise Build → All Features + Custom
```

## Feature Flag System

```python
from opensin.features import FeatureFlags

# Build-spezifische Feature Flags
FEATURES = {
    # Core Features (alle Builds)
    "QUERY_ENGINE": True,
    "TOOL_SYSTEM": True,
    "HOOK_SYSTEM": True,
    "PERMISSION_SYSTEM": True,
    
    # Advanced Features (Pro + Enterprise)
    "COORDINATOR_MODE": False,    # Enterprise only
    "HISTORY_SNIP": True,         # Pro + Enterprise
    "REACTIVE_COMPACT": True,     # All builds
    "CONTEXT_COLLAPSE": False,    # Enterprise only
    "EXPERIMENTAL_SKILL_SEARCH": False,  # Experimental
    "TEMPLATES": True,            # Pro + Enterprise
    "BG_SESSIONS": False,         # Enterprise only
    
    # Enterprise Features
    "MULTI_TENANCY": False,       # Enterprise only
    "AUDIT_LOGGING": False,       # Enterprise only
    "SSO_INTEGRATION": False,     # Enterprise only
}
```

## Conditional Compilation

```python
# Compile-time feature resolution
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

## Build Configuration

```yaml
# build.yml
builds:
  community:
    features:
      QUERY_ENGINE: true
      TOOL_SYSTEM: true
      HOOK_SYSTEM: true
      PERMISSION_SYSTEM: true
      HISTORY_SNIP: true
      REACTIVE_COMPACT: true
      TEMPLATES: true
      
  pro:
    features:
      <<: *community
      COORDINATOR_MODE: false
      CONTEXT_COLLAPSE: false
      EXPERIMENTAL_SKILL_SEARCH: true
      BG_SESSIONS: false
      
  enterprise:
    features:
      <<: *pro
      COORDINATOR_MODE: true
      CONTEXT_COLLAPSE: true
      BG_SESSIONS: true
      MULTI_TENANCY: true
      AUDIT_LOGGING: true
      SSO_INTEGRATION: true
```

## Performance Impact

| Build | Bundle Size | Startup Time | Features |
|-------|------------|--------------|----------|
| Community | 2.1MB | 150ms | 7 |
| Pro | 2.8MB | 180ms | 10 |
| Enterprise | 3.5MB | 220ms | 14 |

## Best Practices

1. **Compile-time resolution** — Feature flags zur Compile-Zeit
2. **Dead code elimination** — Unused Code wird entfernt
3. **Progressive enhancement** — Community → Pro → Enterprise
4. **Monitor impact** — Tracke Bundle Size und Startup Time
5. **Test all builds** — CI/CD für jeden Build-Tier

## Next Steps

- [SIN Feature Flags](/guide/sin-feature-flags)
- [Performance Optimization](/guide/performance-optimization)
