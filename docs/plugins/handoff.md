# Session Handoff Plugin

Session handoff and continuity prompts for OpenSIN CLI.

## Overview

Generates session summaries for seamless context transfer between agents or sessions.

## Installation

```bash
bun add @opensin/plugin-handoff
```

## Usage

```typescript
import { HandoffPlugin, generateHandoffPrompt, captureSessionState } from '@opensin/plugin-handoff';

const plugin = new HandoffPlugin();
const state = plugin.capture({
  currentTask: 'Build feature X',
  openFiles: ['src/main.ts'],
  recentActions: ['Read file', 'Edit file'],
  pendingItems: ['Write tests'],
});
const result = plugin.generate();
console.log(result.prompt);
```

## API

### `captureSessionState(options): SessionState`
Capture current session state.

### `generateHandoffPrompt(state, config): HandoffPrompt`
Generate handoff prompt from session state.

### `HandoffPlugin`
Class with `capture()`, `generate()`, `getState()`, `getConfig()`, `setConfig()` methods.

## Testing

```bash
npm test
# 10 tests passing
```

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **Bun-Only** | -1.5 | `bun install` / `bun run` statt npm |
| **Annahmen-Verbot** | -5.0 | KEINE Diagnose ohne Beweis |
| **Test-Beweis-Pflicht** | 0.0 | KEIN "Done" ohne echten Test-Lauf |

→ [Alle Mandate](/best-practices/code-quality)
