# Envsitter Guard Plugin

.env file protection for OpenSIN CLI.

## Overview

Blocks access to sensitive environment files while allowing safe key listing via fingerprinting.

## Installation

```bash
bun add @opensin/plugin-envsitter
```

## Usage

```typescript
import { EnvsitterPlugin, protectEnvFiles, listEnvKeys } from '@opensin/plugin-envsitter';

const plugin = new EnvsitterPlugin();
const result = plugin.check('/path/to/.env');
if (result.blocked) console.log(result.reason);

const keys = plugin.listKeys('/path/to/.env');
keys.forEach(k => console.log(`${k.key}: ${k.fingerprint}`));
```

## API

### `protectEnvFiles(filePath, config): ProtectionResult`
Check if file access should be blocked.

### `listEnvKeys(envFilePath): EnvKeyInfo[]`
List .env keys without exposing values (SHA-256 fingerprint only).

### `EnvsitterPlugin`
Class with `check()`, `listKeys()`, `getConfig()`, `setConfig()` methods.

## Testing

```bash
bun test
# 16 tests passing
```

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
