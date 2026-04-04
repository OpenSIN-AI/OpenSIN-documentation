# SIN Sandbox — Secure Code Execution

> **OpenSIN's Sandbox** — Geklont aus Claude Code's sandbox-adapter.ts. Sichere Ausführung von untrusted Code.

## Sandbox Architecture

```
User Request → Agent → Sandbox → Tool Execution → Result
                        ↓
                  Filesystem Rules
                  Network Rules
                  Git Escape Prevention
```

## Sandbox Configuration

```python
from opensin.sandbox import Sandbox

sandbox = Sandbox(
    filesystem={
        "allow_read": ["/workspace/**"],
        "allow_write": ["/workspace/output/**"],
        "deny_read": ["/etc/**", "/workspace/.env*"],
        "deny_write": ["/workspace/.git/**", "/workspace/config/**"]
    },
    network={
        "allow_domains": ["api.example.com", "pypi.org"],
        "deny_all": True  # Default deny
    },
    git_escape_prevention=True,
    auto_allow_bash_if_sandboxed=True
)
```

## Bare Git Repo Escape Prevention

```python
# Verhindert dass planted bare git repos die Sandbox escapen
# Erkennt: HEAD, objects, refs, hooks, config Dateien

class GitEscapePrevention:
    def check_write(self, path: str, content: bytes):
        if self.is_git_directory(path, content):
            if self.file_exists(path):
                raise SecurityError("Cannot modify existing git files")
            else:
                # Scrub non-existent git files post-command
                self.scrub_git_files(path)
```

## Auto-Allow Bash if Sandboxed

```python
# Wenn Sandbox aktiviert → sandboxed bash commands auto-allow
# Keine User-Approval nötig für sichere Commands

if sandbox.is_enabled and sandbox.is_command_safe(command):
    return PermissionDecision.ALLOW
```

## Dynamic Config Refresh

```python
# Sandbox Config wird bei Settings-Changes aktualisiert
# Ohne Neustart des Agents

settings.subscribe("sandbox", lambda new_config:
    sandbox.update_config(new_config)
)
```

## Platform-Specific Handling

| Platform | Sandbox Support | Notes |
|----------|----------------|-------|
| Linux | ✅ Full | bubblewrap |
| macOS | ✅ Full | seatbelt |
| Windows | ⚠️ Limited | Job objects |
| WSL2 | ⚠️ Partial | No glob patterns |

## Best Practices

1. **Least Privilege** — Nur notwendige Zugriffe erlauben
2. **Git Escape Prevention** — Immer aktiviert lassen
3. **Auto-Allow Sandboxed** — Weniger User-Prompts
4. **Dynamic Config** — Runtime Updates ohne Neustart
5. **Platform Warnings** — User über Limitationen informieren

## Next Steps

- [Security Hardening](/guide/security-hardening)
- [SIN Permissions](/guide/sin-permission-system)
