---
title: "Security Best Practices"
---

# Security Best Practices

Guidelines for building secure agents, managing credentials, and hardening your OpenSIN deployment.

## Principle of Least Privilege

Every agent and tool should operate with the minimum permissions required:

```typescript
const permissions = new PermissionManager({
  mode: 'strict',
  allowlist: [
    '/workspace/src/**',    // only project source
    '/workspace/tests/**',  // only project tests
  ],
  denylist: [
    '**/.env',              // never read env files
    '**/.git/config',       // never read git credentials
    '**/node_modules/**',   // skip dependencies
  ],
})
```

## Credential Management

### Never Hardcode Secrets

```typescript
// WRONG - secret in code
const apiKey = 'sk-abc123...'

// RIGHT - from environment
const apiKey = process.env.OPENAI_API_KEY

// RIGHT - from SIN-PasswordManager
const apiKey = await sinPasswordManager.get('openai-key')
```

### Credential Isolation

Each execution environment has its own credential scope:

| Environment | Credential Source | Synced? |
|-------------|------------------|---------|
| Mac (local) | `~/.config/opencode/auth.json` | Source of truth |
| OCI VM | `~/.config/opencode/auth.json` | Local only |
| HF Space | Environment variables | Local only |

Auth files are **never synced** between machines. The `sin-sync` tool explicitly excludes:
- `auth.json`
- `token.json`
- `antigravity-accounts.json`
- `telegram_config.json`

### Token Rotation

Implement automatic token rotation for all long-lived credentials:

```typescript
// Automatic rotation via LaunchDaemon
// com.sin.opencode-rate-limit-watcher monitors usage
// and triggers token refresh before expiration
```

## Input Validation

### Tool Arguments

Validate all tool arguments before execution:

```typescript
function validatePath(path: string): boolean {
  // Reject path traversal
  if (path.includes('..')) return false
  
  // Reject absolute paths outside workspace
  if (path.startsWith('/') && !path.startsWith(workspace)) return false
  
  // Reject known sensitive paths
  const sensitive = ['.env', '.ssh', 'credentials']
  if (sensitive.some(s => path.includes(s))) return false
  
  return true
}
```

### Command Injection Prevention

The bash tool uses `execFile` (not `exec`) and passes arguments as arrays:

```typescript
// WRONG - vulnerable to injection
exec(`grep ${userInput} file.txt`)

// RIGHT - safe argument passing
execFile('grep', [userInput, 'file.txt'])
```

## MCP Server Security

### Allowlisting

Only load trusted MCP servers:

```json
{
  "mcpServers": {
    "trusted-server": {
      "command": "node",
      "args": ["server.js"],
      "permissions": {
        "filesystem": ["read"],
        "network": ["localhost:*"]
      }
    }
  }
}
```

### Confirmation Gates

Require user confirmation for destructive operations:

```typescript
const toolConfig = {
  'file:delete': { requireConfirmation: true },
  'bash:execute': { requireConfirmation: true },
  'git:push': { requireConfirmation: true },
  'file:read': { requireConfirmation: false },
}
```

## A2A Communication Security

### Mutual Authentication

All inter-agent communication must be authenticated:

```typescript
// Agent A sending a task to Agent B
const response = await fetch('https://agent-b.opensin.ai/a2a/v1', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${jwt}`,
    'X-Agent-ID': 'sin-hermes',
    'X-Fleet-ID': 'production',
  },
  body: JSON.stringify(taskPayload),
})
```

### Transport Encryption

- Production: HTTPS (TLS 1.3) required
- Internal: Cloudflare Tunnels for zero-trust networking
- Never transmit credentials over plaintext HTTP

## Logging Security

### Redaction

Never log sensitive data:

```typescript
function sanitizeLog(message: string): string {
  return message
    .replace(/sk-[a-zA-Z0-9]{20,}/g, 'sk-***REDACTED***')
    .replace(/Bearer [a-zA-Z0-9._-]+/g, 'Bearer ***REDACTED***')
    .replace(/password['":\s]*[^\s,}]+/gi, 'password: ***REDACTED***')
}
```

### Log Storage

All logs go to the GitLab LogCenter (encrypted at rest), never stored in plaintext on local disk beyond temporary buffering.

## Dependency Security

- Run `npm audit` on every CI build
- Pin exact dependency versions in `package-lock.json`
- Review all new dependencies before adding
- Use `Socket.dev` or similar for supply chain security

## Checklist

Before deploying an agent to production:

- [ ] All secrets in environment variables or vault (not hardcoded)
- [ ] Permission manager configured with explicit allow/deny lists
- [ ] Bash tool using `execFile` with dangerous command blocking
- [ ] MCP servers allowlisted with appropriate permission gates
- [ ] A2A endpoints require JWT authentication
- [ ] HTTPS enabled for all external communication
- [ ] Log redaction enabled for sensitive patterns
- [ ] Token rotation configured for all long-lived credentials
- [ ] `npm audit` passing with no critical vulnerabilities
