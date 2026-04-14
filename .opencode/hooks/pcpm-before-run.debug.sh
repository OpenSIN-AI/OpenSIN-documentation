#!/usr/bin/env bash
# DEBUG: PCPM beforeRun hook with verbose logging
set -euo pipefail

echo "🔍 [DEBUG] PCPM Hook starting..." >&2

BRAIN_CLI="/Users/jeremy/dev/global-brain/src/cli.js"
BRAIN_ROOT="/Users/jeremy/dev/global-brain"
PROJECT_ID="OpenSIN-documentation"
GOAL_ID="default-goal"
GOAL_DESC="Continue development"

CONTEXT_FILE="/tmp/pcpm-context-${PROJECT_ID}-${$}.json"

echo "🔍 [DEBUG] Calling brain CLI..." >&2
echo "   BRAIN_CLI: $BRAIN_CLI" >&2
echo "   CONTEXT_FILE: $CONTEXT_FILE" >&2

# Timeout protection: kill after 2s
(timeout 2s node "$BRAIN_CLI" context \
  --root "$BRAIN_ROOT" \
  --project "$PROJECT_ID" \
  --goal-id "$GOAL_ID" \
  --description "$GOAL_DESC" \
  > "$CONTEXT_FILE" 2>&1) || {
    echo "❌ [DEBUG] Brain CLI failed or timed out (exit: $?)" >&2
    echo "PCPM_CONTEXT_LOADED=false"
    exit 0
  }

if [ -f "$CONTEXT_FILE" ] && [ -s "$CONTEXT_FILE" ]; then
  SIZE=$(wc -c < "$CONTEXT_FILE")
  echo "✅ [DEBUG] Context generated (${SIZE} bytes)" >&2
  echo "PCPM_CONTEXT_LOADED=true"
  cat "$CONTEXT_FILE"
  rm -f "$CONTEXT_FILE"
else
  echo "⚠️  [DEBUG] Context file empty or missing" >&2
  echo "PCPM_CONTEXT_LOADED=false"
fi
