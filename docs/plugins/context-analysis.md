# Context Analysis Plugin

Token usage tracking and cost estimation for OpenSIN CLI.

## Overview

Tracks token usage per turn, session-level statistics, and cost estimation.

## Installation

```bash
bun add @opensin/plugin-context-analysis
```

## Usage

```typescript
import { ContextAnalysisPlugin, estimateCost } from '@opensin/plugin-context-analysis';

const plugin = new ContextAnalysisPlugin('session-1');
plugin.recordTurn(1000, 500);
plugin.recordTurn(2000, 1000);

const stats = plugin.getTokenUsage();
console.log(`Total: ${stats.totalTokens} tokens`);

const cost = plugin.getCostEstimate();
console.log(`Cost: ${cost.totalCost} ${cost.currency}`);
```

## API

### `estimateCost(inputTokens, outputTokens, config): CostEstimate`
Estimate cost for token usage.

### `ContextAnalysisPlugin`
Class with `recordTurn()`, `getTokenUsage()`, `getCostEstimate()`, `getTurnCost()`, `reset()`, `getConfig()`, `setConfig()` methods.

## Testing

```bash
npm test
# 11 tests passing
```
