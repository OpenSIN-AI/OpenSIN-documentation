# Safety Net Plugin

Destructive command protection for OpenSIN CLI.

## Overview

Intercepts dangerous git/filesystem operations with confirmation prompts.

## Installation

```bash
bun add @opensin/plugin-safety-net
```

## Usage

```typescript
import { SafetyNetPlugin, checkCommandSafety, DANGEROUS_PATTERNS } from '@opensin/plugin-safety-net';

const plugin = new SafetyNetPlugin();
const result = plugin.check('git push --force');
if (!result.safe) console.log(result.reasons);
```

## Dangerous Patterns

- `git push --force` / `git push -f`
- `git reset --hard`
- `rm -rf`
- `git clean -fdx`
- Fork bombs
- `mkfs.*`
- Custom patterns via config

## API

### `checkCommandSafety(command, config): SafetyCheckResult`
Check if a command is safe to execute.

### `SafetyNetPlugin`
Class with `check()`, `isSafe()`, `getConfig()`, `setConfig()` methods.

## Testing

```bash
bun test
# 14 tests passing
```

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
