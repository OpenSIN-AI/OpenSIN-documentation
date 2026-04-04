# SIN Enterprise Managed Settings

> **OpenSIN's Enterprise Configuration** — Zentrale Verwaltung für Teams und Organisationen.

## Overview

Enterprise Settings ermöglichen zentrales Management von Konfiguration, Permissions und Plugins für ganze Teams.

## Settings Hierarchie

```
1. Global:    ~/.sin/settings.json           (User)
2. Project:   .sin/settings.json             (Projekt)
3. Local:     .sin/settings.local.json       (Lokal, nicht committen)
4. Managed:   managed-settings.json          (Enterprise Policy)
5. Drop-ins:  managed-settings.d/*.json      (Enterprise Drop-ins)
6. Remote:    Server (fail-closed refresh)   (Cloud Policy)
```

Spätere überschreiben frühere Settings.

## Managed Settings

```json
{
  "managed": {
    "version": 1,
    "policy": "strict",
    "enforce": true,
    "settings": {
      "model": {
        "allowed": ["gpt-4", "gpt-3.5-turbo", "claude-sonnet"],
        "default": "gpt-4"
      },
      "permissions": {
        "deny": [
          "Bash(rm -rf *)",
          "Bash(sudo *)",
          "Write(production/**)"
        ]
      },
      "plugins": {
        "allowlist": [
          "code-review",
          "security-guidance",
          "commit-commands"
        ],
        "denylist": [
          "experimental-plugin"
        ]
      },
      "budget": {
        "daily_limit": 50.00,
        "monthly_limit": 1000.00
      }
    }
  }
}
```

## Drop-in Directory

```
managed-settings.d/
├── security-policy.json    # Security Rules
├── model-policy.json       # Allowed Models
├── plugin-policy.json      # Plugin Allowlist
└── budget-policy.json      # Budget Limits
```

## Remote Managed Settings

```json
{
  "remote": {
    "url": "https://settings.opensin.ai/api/v1/policies",
    "refresh_interval": 3600,
    "fail_closed": true,
    "auth": {
      "type": "bearer",
      "token_env": "SIN_ENTERPRISE_TOKEN"
    }
  }
}
```

Bei `fail_closed: true` werden bei Verbindungsproblemen die letzten bekannten Settings verwendet.

## MDM Configuration (macOS)

```xml
<!-- com.opensin.settings.plist -->
<dict>
    <key>ModelPolicy</key>
    <dict>
        <key>AllowedModels</key>
        <array>
            <string>gpt-4</string>
            <string>gpt-3.5-turbo</string>
        </array>
    </dict>
    <key>BudgetPolicy</key>
    <dict>
        <key>DailyLimit</key>
        <real>50.0</real>
    </dict>
</dict>
```

## Policy Enforcement

| Setting | User Override | Enterprise Override |
|---------|--------------|---------------------|
| Allowed Models | ❌ Nein | ✅ Ja |
| Budget Limits | ❌ Nein | ✅ Ja |
| Plugin Allowlist | ❌ Nein | ✅ Ja |
| Permission Rules | ❌ Nein | ✅ Ja |
| Theme/Color | ✅ Ja | ❌ Nein |

## Audit Logging

```json
{
  "audit": {
    "enabled": true,
    "log_path": "/var/log/sin/audit.log",
    "events": [
      "settings_changed",
      "policy_violation",
      "budget_exceeded",
      "plugin_installed"
    ]
  }
}
```

## Next Steps

- [SIN Permissions](/guide/sin-permissions)
- [Security Hardening](/guide/security-hardening)
