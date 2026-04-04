# SIN Permission System

> **OpenSIN's Permission Model** — Kontrolliere WAS Agenten tun dürfen.

## Permission Modes

| Mode | Verhalten | Use Case |
|------|-----------|----------|
| `auto` | KI entscheidet allow/deny | Produktiv, vertrauenswürdige Projekte |
| `ask` | Immer nachfragen | Neue Projekte, sensible Codebases |
| `deny` | Spezifische Tools blockieren | Produktion, kritische Systeme |

## Permission Rules

```json
{
  "permissions": {
    "allow": [
      "Bash(git *)",
      "Bash(ls *)",
      "Bash(cat *)",
      "Read(/**)",
      "Glob(**)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(sudo *)",
      "Bash(curl *|bash)",
      "Write(/etc/**)",
      "Write(**/.env*)"
    ],
    "ask": [
      "Bash(*)",
      "Write(/**)",
      "Edit(/**)"
    ]
  }
}
```

## Pattern Syntax

| Pattern | Bedeutung |
|---------|-----------|
| `Bash(git *)` | Alle git Commands |
| `Bash(cmd:*)` | Compound Commands |
| `Edit(//path/**)` | Alle Dateien in path |
| `mcp__servername` | MCP Server Tools |

## Conditional Permissions

```json
{
  "permissions": {
    "allow": [
      {
        "tool": "Bash",
        "pattern": "pytest *",
        "if": "cwd.contains('tests')"
      }
    ]
  }
}
```

## Enterprise Managed Permissions

```json
{
  "managed": {
    "policy": "strict",
    "rules": {
      "deny": [
        "Bash(rm *)",
        "Bash(curl *)",
        "Write(production/**)"
      ]
    },
    "enforce": true,
    "bypassDisabled": true
  }
}
```

## Next Steps

- [Security Hardening](/guide/security-hardening)
- [SIN Hooks](/guide/sin-hooks)
