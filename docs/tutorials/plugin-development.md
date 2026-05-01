# Tutorial: Build a Custom Plugin

## Overview

Learn how to create a custom plugin for OpenSIN CLI.

## Step 1: Create Plugin Structure

```bash
mkdir my-plugin && cd my-plugin
bun init -y
```

## Step 2: package.json

```json
{
  "name": "opencode-plugin-my-plugin",
  "version": "0.1.0",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "test": "vitest run"
  }
}
```

## Step 3: Create Plugin

```typescript
// src/plugin.ts
export class MyPlugin {
  getManifest() {
    return {
      id: "my-plugin",
      name: "My Plugin",
      version: "0.1.0",
      description: "My custom plugin",
      author: "You",
      license: "MIT",
    };
  }
}
```

## Step 4: Install

```bash
bun install -g .
```

## Step 5: Add to opencode.json

```json
{
  "plugin": ["opencode-plugin-my-plugin"]
}
```

---

## Relevante Mandate

| Mandat                       | Priority | Doku                                                |
| ---------------------------- | -------- | --------------------------------------------------- |
| **Vision-Gate**              | -7.0     | KEINE Browser-Aktion ohne Screenshot + Vision-Check |
| **DevTools-First**           | -1.0     | JEDER CSS-Selektor via DevTools verifizieren        |
| **Bun-Only**                 | -1.5     | `bun install` / `bun run` — npm ist verboten        |
| **Technologie-Souveränität** | -2.0     | nodriver + Chrome Profil — Playwright/etc. verboten |

→ [Alle Mandate](/best-practices/browser-automation)
