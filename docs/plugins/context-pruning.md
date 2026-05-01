# Context Pruning Plugin

Dynamic context pruning for token optimization in OpenSIN CLI.

## Overview

The Context Pruning Plugin automatically detects when conversation context exceeds token limits and intelligently prunes older messages while preserving critical information.

## Installation

```bash
npm install @opensin/plugin-context-pruning
```

## Configuration

```json
{
  "maxTokens": 8000,
  "keepLastN": 4,
  "keepSystemPrompt": true,
  "keepRecentToolOutputs": 2
}
```

## Usage

```typescript
import {
  ContextPruningPlugin,
  pruneContext,
  countTokens,
} from "@opensin/plugin-context-pruning";

const plugin = new ContextPruningPlugin({ maxTokens: 8000 });
const result = plugin.prune(messages);
console.log(`Pruned ${result.prunedCount} messages`);
```

## API

### `countTokens(text: string): number`

Estimate token count for a string.

### `countContextTokens(messages: ContextMessage[]): TokenCount`

Count tokens across all messages, broken down by role.

### `pruneContext(messages, config): PruningResult`

Prune messages that exceed token limit.

### `ContextPruningPlugin`

Class with `shouldPrune()`, `prune()`, `getConfig()`, `setConfig()` methods.

## Testing

```bash
npm test
# 12 tests passing
```
