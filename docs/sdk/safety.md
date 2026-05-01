---
title: "Safety & Permissions"
---

# Safety & Permissions

The Safety module detects dangerous commands before execution, and the Permission Manager controls which operations agents are allowed to perform.

## Safety Detector

The `SafetyDetector` scans commands for 13 categories of destructive patterns:

```typescript
import { SafetyDetector } from "@opensin/sdk";

const safety = new SafetyDetector();

safety.check("rm -rf /");
// { safe: false, reason: 'Destructive filesystem operation', pattern: 'rm-rf-root' }

safety.check("cat README.md");
// { safe: true }
```

### Blocked Patterns

| Category               | Pattern              | Example                       |
| ---------------------- | -------------------- | ----------------------------- |
| Filesystem destruction | `rm -rf /`           | `rm -rf /`                    |
| Disk formatting        | `mkfs`               | `mkfs.ext4 /dev/sda`          |
| Disk overwrite         | `dd of=/dev`         | `dd if=/dev/zero of=/dev/sda` |
| Fork bomb              | `:(){ :\|:& };:`     | Shell fork bomb               |
| World-writable root    | `chmod 777 /`        | `chmod -R 777 /`              |
| Destructive git        | `git reset --hard`   | `git reset --hard HEAD~10`    |
| Sudo removal           | `sudo rm`            | `sudo rm -rf /var`            |
| Service shutdown       | `shutdown`, `reboot` | `shutdown -h now`             |
| Network interface      | `ifconfig down`      | `ifconfig eth0 down`          |
| Firewall flush         | `iptables -F`        | `iptables -F`                 |
| Password change        | `passwd`             | `passwd root`                 |
| Crontab clear          | `crontab -r`         | `crontab -r`                  |
| History clear          | `history -c`         | `history -c && history -w`    |

### Integration with Bash Tool

```typescript
import { SafetyDetector } from "@opensin/sdk";

const safety = new SafetyDetector();

async function executeBash(command: string) {
  const check = safety.check(command);
  if (!check.safe) {
    return { error: `Blocked: ${check.reason}` };
  }
  // proceed with execFile...
}
```

## Permission Manager

The `PermissionManager` controls agent access to files, directories, and operations:

```typescript
import { PermissionManager } from "@opensin/sdk";

const permissions = new PermissionManager({
  mode: "interactive", // 'strict', 'permissive', 'interactive'
  allowlist: [
    "/workspace/src/**",
    "/workspace/tests/**",
    "/workspace/package.json",
  ],
  denylist: [
    "**/.env",
    "**/.env.*",
    "**/.git/config",
    "**/credentials*",
    "**/secrets*",
  ],
});
```

### Permission Modes

| Mode          | Behavior                                           |
| ------------- | -------------------------------------------------- |
| `strict`      | Only allowlisted paths, deny everything else       |
| `interactive` | Ask user for confirmation on non-allowlisted paths |
| `permissive`  | Allow everything except denylisted paths           |

### Checking Permissions

```typescript
const result = await permissions.check({
  tool: "write",
  path: "/workspace/src/app.ts",
  action: "modify",
});

if (result.allowed) {
  // proceed
} else if (result.needsConfirmation) {
  const confirmed = await askUser(`Allow write to ${result.path}?`);
  if (!confirmed) return { error: "Denied by user" };
} else {
  return { error: `Permission denied: ${result.reason}` };
}
```

### Tool-Level Permissions

Configure different permission levels per tool:

```typescript
const permissions = new PermissionManager({
  toolPermissions: {
    read: "auto-approve", // reading is always safe
    write: "confirm", // writing needs confirmation
    bash: "confirm", // shell commands need confirmation
    edit: "auto-approve", // editing existing files is safe
    glob: "auto-approve", // file search is safe
  },
});
```

## Combining Safety + Permissions

Use both layers together for defense-in-depth:

```typescript
const agent = new AgentLoop({
  model: "claude-sonnet-4-6",
  tools: toolRegistry,
  safety: new SafetyDetector(), // layer 1: block dangerous commands
  permissions: new PermissionManager({
    // layer 2: control file access
    mode: "interactive",
    denylist: ["**/.env", "**/secrets*"],
  }),
});
```

The safety detector runs first (blocking known destructive patterns), then the permission manager checks path-level access.

---

## Relevante Mandate

| Mandat                  | Priority | Regel                               |
| ----------------------- | -------- | ----------------------------------- |
| **Bun-Only**            | -1.5     | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot**     | -5.0     | KEINE Diagnose ohne Beweis          |
| **Test-Beweis-Pflicht** | 0.0      | KEIN "Done" ohne echten Test-Lauf   |

→ [Alle Mandate](/best-practices/code-quality)
