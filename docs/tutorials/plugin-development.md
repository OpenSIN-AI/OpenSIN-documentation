# Tutorial: Build a Custom Plugin

## Overview

Learn how to create a custom plugin for OpenSIN CLI.

## Step 1: Create Plugin Structure

```bash
mkdir my-plugin && cd my-plugin
npm init -y
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
      id: 'my-plugin',
      name: 'My Plugin',
      version: '0.1.0',
      description: 'My custom plugin',
      author: 'You',
      license: 'MIT',
    };
  }
}
```

## Step 4: Install

```bash
npm install -g .
```

## Step 5: Add to opencode.json

```json
{
  "plugin": ["opencode-plugin-my-plugin"]
}
```
