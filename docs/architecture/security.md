---
title: "Security Architecture"
---

# Security Architecture

OpenSIN implements defense-in-depth security across every layer of the stack, from the CLI tool system to the A2A fleet communication.

## Threat Model

OpenSIN agents execute arbitrary code, access filesystems, make network requests, and communicate with external services. The security architecture addresses:

| Threat                | Mitigation                                                      |
| --------------------- | --------------------------------------------------------------- |
| Shell injection       | `execFile` instead of `exec`, argument array passing            |
| Destructive commands  | Pattern-based command blocking (rm -rf /, mkfs, dd, fork bombs) |
| Path traversal        | Workspace-scoped file operations with path validation           |
| Credential leakage    | No secrets in logs, environment variable isolation              |
| Malicious MCP servers | Permission gates, user confirmation for dangerous operations    |
| Agent impersonation   | JWT-based A2A authentication, mutual TLS                        |
| Data exfiltration     | Network egress monitoring, allowlisted domains                  |

## CLI Security Layer

### Tool Permission System

Every tool operation goes through a permission check before execution:

```typescript
import { PermissionManager } from "@opensin/sdk";

const permissions = new PermissionManager({
  mode: "interactive", // ask user for dangerous ops
  allowlist: ["/workspace/**"],
  denylist: ["/etc/**", "/usr/**", "~/.ssh/**"],
});

// Check before file write
const allowed = await permissions.check({
  tool: "write",
  path: "/workspace/src/app.ts",
  action: "create",
});
```

### Bash Tool Hardening

The bash tool uses `execFile` (not `exec`) to prevent shell injection and blocks known destructive patterns:

```typescript
// Blocked patterns (13 categories):
const DANGEROUS_PATTERNS = [
  /rm\s+(-[a-z]*f[a-z]*\s+)?\/\s*$/, // rm -rf /
  /mkfs/, // filesystem format
  /dd\s+.*of=\/dev/, // disk overwrite
  /:\(\)\s*\{\s*:\|:\s*&\s*\}/, // fork bomb
  /chmod\s+777\s+\//, // world-writable root
  /git\s+reset\s+--hard/, // destructive git reset
  /sudo\s+rm/, // sudo removal
  // ... 6 more patterns
];
```

### Grep Safety

The grep tool defaults to **literal string search** (not regex) to prevent ReDoS attacks:

```typescript
// Safe by default - literal matching
grep({ pattern: "user.password", path: "./src" });

// Opt-in regex with try/catch protection
grep({ pattern: "user\\.pass.*", path: "./src", useRegex: true });
```

## A2A Security

### Authentication

All agent-to-agent communication requires authentication:

```
Agent A                          Agent B
   │                                │
   │── Bearer Token (JWT) ────────>│
   │                                │── Verify signature
   │                                │── Check expiration
   │                                │── Validate claims
   │<── 200 OK + Task Result ──────│
```

### Token Structure

```json
{
  "sub": "sin-hermes",
  "iss": "opensin-auth",
  "aud": "sin-solver",
  "iat": 1712000000,
  "exp": 1712003600,
  "scope": ["task:send", "task:read"],
  "fleet_id": "production"
}
```

### Transport Security

- **Production**: HTTPS required (TLS 1.3)
- **Internal fleet**: Cloudflare Tunnel (zero-trust networking)
- **Development**: HTTP allowed only on localhost

## MCP Security

MCP servers expose powerful capabilities. OpenSIN gates access through:

1. **Server allowlist**: Only approved MCP servers can be loaded
2. **Tool-level permissions**: Each MCP tool has a risk classification
3. **Confirmation gates**: High-risk operations require explicit user approval
4. **Sandboxing**: MCP processes run with minimal filesystem access

```json
{
  "mcpServers": {
    "sin-google-apps": {
      "permissions": {
        "read": "auto-approve",
        "write": "confirm",
        "delete": "confirm",
        "admin": "deny"
      }
    }
  }
}
```

## Secret Management

- **No hardcoded secrets**: All credentials stored in environment variables or secure vaults
- **SIN-PasswordManager**: A2A agent for centralized credential management
- **Token rotation**: Automatic rotation via LaunchDaemon watchers
- **Auth isolation**: Each agent has its own credential scope

### Credential Hierarchy

```
~/.config/opencode/auth/          # Auth tokens (never synced)
~/.config/opencode/auth.json      # Primary auth (local only)
~/.config/opencode/token.json     # API keys (local only)
```

## Audit & Compliance

- All tool invocations logged with timestamp, user, action, and result
- A2A task history persisted to Supabase
- Git-based audit trail for all code changes
- GitLab LogCenter for centralized log aggregation

## Reporting Vulnerabilities

See [SECURITY.md](https://github.com/OpenSIN-AI/OpenSIN-Code/blob/main/SECURITY.md) for responsible disclosure guidelines.
