#!/usr/bin/env bash
set -euo pipefail
REPO_OWNER=${REPO_OWNER:-OpenSIN-AI}
REPO_NAME=${REPO_NAME:-OpenSIN-documentation}
PR_LIMIT=${PR_LIMIT:-20}
STATE_DIR=${STATE_DIR:-/tmp/opensin-pr-watcher}
mkdir -p "$STATE_DIR"
OUT="$STATE_DIR/${REPO_OWNER}-${REPO_NAME}-pr-feedback.json"
python3 - "$REPO_OWNER" "$REPO_NAME" "$PR_LIMIT" "$OUT" <<'INNER'
import json
import subprocess
import sys
from pathlib import Path
owner, repo, limit, out_path = sys.argv[1:5]
result = subprocess.run([
    "gh", "pr", "list",
    "--repo", f"{owner}/{repo}",
    "--state", "open",
    "--limit", limit,
    "--json", "number,title,updatedAt"
], capture_output=True, text=True, check=True)
out = Path(out_path)
out.write_text(result.stdout)
items = json.loads(result.stdout or "[]")
summary = {
    "open_prs": len(items),
    "latest_updated_at": items[0]["updatedAt"] if items else None,
    "titles": [item["title"] for item in items[:5]],
}
print(json.dumps(summary, indent=2))
INNER
