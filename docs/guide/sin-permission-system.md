# SIN Permission System — Multi-Source Permission Rules

> **OpenSIN's Permission System** — Das umfassendste Permission-System mit 15+ Stufen Pipeline und Content-spezifischen Rules.

## Permission Modes

| Mode | Verhalten | Use Case |
|------|-----------|----------|
| `default` | Frage bei jeder gefährlichen Operation | Entwicklung |
| `acceptEdits` | Auto-allow File Edits im Working Directory | Produktiv |
| `bypassPermissions` | Überspringe alle Checks (außer Safety) | Vertrauenswürdig |
| `dontAsk` | Auto-deny alles was Approval braucht | Produktion |
| `auto` | AI Classifier entscheidet | Fortgeschritten |
| `bubble` | Prompts an Parent Terminal | Background Agents |

## Multi-Source Permission Rules

Priority Order (spätere überschreiben frühere):

1. **Policy Settings** — Enterprise Policy
2. **Flag Settings** — Feature Flags
3. **User Settings** — `~/.sin/settings.json`
4. **Project Settings** — `.sin/settings.json`
5. **Local Settings** — `.sin/settings.local.json`
6. **CLI Arg** — `--allowedTools` Flag
7. **Command** — Slash Command Allowlist
8. **Session** — Runtime Session Rules

## Content-Specific Rules

```json
{
  "permissions": {
    "allow": [
      "Bash(git *)",
      "Bash(npm install:*)",
      "Bash(python -m pytest:*)",
      "Edit(src/**/*.py)",
      "Read(**)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(sudo *)",
      "Bash(curl *|bash)",
      "Write(/etc/**)",
      "Write(**/.env*)",
      "mcp__untrusted_server"
    ]
  }
}
```

## Auto-Mode Classifier

```python
from opensin.permissions import AutoModeClassifier

classifier = AutoModeClassifier(
    model="gpt-3.5-turbo",  # Schnelles Modell für Classification
    fast_paths={
        "acceptEdits": True,  # Safe file edits → skip classifier
        "safe_tools": ["ls", "cat", "git status"]  # Known safe → skip
    }
)

# Decision: Allow oder Deny
decision = await classifier.classify(
    tool_name="Bash",
    tool_input="rm -rf /tmp/test",
    context=transcript
)

if decision == "allow":
    await execute_tool()
else:
    await prompt_user()
```

## Denial Tracking

```python
from opensin.permissions import DenialTracker

tracker = DenialTracker(
    max_consecutive_denials=5,
    max_total_denials=20
)

# Tracke Denials
tracker.record_denial(tool_name="Bash", input="rm -rf /")

# Wenn Limits erreicht → Fallback zu Manual Prompting
if tracker.has_hit_limit():
    await manual_prompt_user()
```

## Bypass-Immune Safety Checks

```python
# Diese Checks prompten IMMER — auch in bypassPermissions Mode
SAFETY_CHECKS = [
    ".git/**",      # Git Internals
    ".sin/**",      # SIN Config
    ".vscode/**",   # IDE Config
    "**/.env*",     # Secrets
    "**/secrets*",  # Secrets
]

# Selbst in bypassPermissions Mode werden diese geprüft
if any(path.match(safety_check) for safety_check in SAFETY_CHECKS):
    await prompt_user("⚠️ Safety check: This modifies a protected file.")
```

## Headless Agent Hook Fallback

```python
# Wenn Permission Prompts nicht angezeigt werden können (Background Agents)
# bekommen PermissionRequest Hooks eine Chance zu erlauben/verweigern

@hooks.on("PermissionRequest")
async def handle_permission_request(event):
    if is_safe_operation(event.tool_name, event.input):
        return {"decision": "allow"}
    return {"decision": "deny"}
```

## Best Practices

1. **Least Privilege** — Nur notwendige Permissions erlauben
2. **Content-Specific Rules** — Nicht nur Tool-Namen, auch Inhalte prüfen
3. **Denial Tracking** — Verhindert Endlos-Deny-Loops
4. **Safety Checks** — Immer aktiv, auch in Bypass Mode
5. **Auto-Mode** — Nur für vertrauenswürdige Umgebungen

## Next Steps

- [Security Hardening](/guide/security-hardening)
- [SIN Hooks](/guide/sin-hooks)
