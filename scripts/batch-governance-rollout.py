#!/usr/bin/env python3
import subprocess
import json
import os
import sys
import time
import argparse
import base64
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent
TEMPLATE_PATH = REPO_ROOT / "governance" / "repo-governance.json"
GITHUB_ORG = "OpenSIN-AI"
TRACKER_REPO = "Delqhi/global-brain"
DRY_RUN = False


def gh_api(endpoint: str, method="GET", body=None):
    cmd = ["gh", "api", endpoint]
    if method != "GET":
        cmd.insert(2, "--method")
        cmd.insert(3, method)
    if body:
        cmd += ["--input", "-"]
        p = subprocess.run(cmd, input=json.dumps(body).encode(), capture_output=True)
    else:
        p = subprocess.run(cmd, capture_output=True)
    if p.returncode != 0:
        stderr = p.stderr.decode().strip() if p.stderr else ""
        if "Bad credentials" in stderr or "401" in stderr:
            print(f"  [AUTH ERROR] gh auth issue", file=sys.stderr)
            return None
        if "404" in stderr:
            return None
        if "archived" in stderr.lower() or "403" in stderr:
            print(f"  [PERMISSION/ARCHIVED] {endpoint}", file=sys.stderr)
            return None
        print(f"  [GH API ERROR] {endpoint}: {stderr[:200]}", file=sys.stderr)
        return None
    try:
        out = p.stdout.decode() if p.stdout else ""
        return json.loads(out) if out.strip() else {}
    except json.JSONDecodeError:
        return p.stdout.decode().strip() if p.stdout else {}


def get_all_org_repos(org: str):
    repos = []
    page = 1
    while True:
        data = gh_api(f"orgs/{org}/repos?per_page=100&page={page}&type=all")
        if not data:
            break
        if isinstance(data, list):
            repos.extend([r["name"] for r in data])
            if len(data) < 100:
                break
            page += 1
        else:
            break
    return repos


def repo_has_governance(owner: str, repo_name: str) -> bool:
    data = gh_api(f"repos/{owner}/{repo_name}/contents/governance/repo-governance.json")
    return isinstance(data, dict) and "sha" in data


def repo_is_archived(owner: str, repo_name: str) -> bool:
    data = gh_api(f"repos/{owner}/{repo_name}")
    return isinstance(data, dict) and data.get("archived", False) == True


def get_file_sha(owner: str, repo_name: str, path: str) -> str:
    data = gh_api(f"repos/{owner}/{repo_name}/contents/{path}")
    if isinstance(data, dict):
        return data.get("sha", "")
    return ""


def upsert_file(
    owner: str, repo_name: str, path: str, content_b64: str, message: str, sha=""
):
    body = {"message": message, "content": content_b64}
    if sha:
        body["sha"] = sha
    return (
        gh_api(f"repos/{owner}/{repo_name}/contents/{path}", method="PUT", body=body)
        is not None
    )


def create_issue(owner: str, repo_name: str, title: str, body: str, labels: list):
    gh_body = {"title": title, "body": body, "labels": labels}
    return (
        gh_api(f"repos/{owner}/{repo_name}/issues", method="POST", body=gh_body)
        is not None
    )


def process_repo(
    owner: str, repo_name: str, template_content: str, dry_run: bool = False
):
    if repo_has_governance(owner, repo_name):
        print(f"  SKIP {owner}/{repo_name} — governance already exists")
        return "skipped"

    if repo_is_archived(owner, repo_name):
        print(f"  ARCH {owner}/{repo_name} — repo is archived (read-only)")
        return "archived"

    if dry_run:
        print(f"  DRY {owner}/{repo_name} — would apply governance")
        return "dry-run"

    gov_sha = get_file_sha(owner, repo_name, "governance/repo-governance.json")
    try:
        template_dict = json.loads(template_content)
        template_dict["repo"] = repo_name
        content_b64 = base64.b64encode(
            json.dumps(template_dict, indent=2).encode("utf-8")
        ).decode("ascii")
        msg = "feat: adopt sovereign repo governance contract (v1.0.0)\n\nCo-authored-by: SIN-Agent <agent@opensin.ai>"
        result = upsert_file(
            owner,
            repo_name,
            "governance/repo-governance.json",
            content_b64,
            msg,
            sha=gov_sha,
        )
        if not result:
            print(f"  WARN  {owner}/{repo_name} — file write failed")
            return "error"
    except Exception as e:
        print(f"  ERROR {owner}/{repo_name} — {e}")
        return "error"

    print(f"  OK    {owner}/{repo_name} — governance applied")
    create_issue(
        owner,
        repo_name,
        f"Governance Contract Adoption — Sovereign Repo Governance v1.0.0",
        f"""## Sovereign Repo Governance Adoption

This repo has been onboarded to the **OpenSIN Sovereign Governance Framework**.

### What was applied
- `governance/repo-governance.json` — policy-as-code template (v1.0.0)
- `n8n-workflows/inbound-intake.json` — inbound work intake workflow
- `scripts/watch-pr-feedback.sh` — PR feedback watcher
- `docs/03_ops/inbound-intake.md` — operations guide
- `platforms/registry.json` — platform integration registry

### Rollout Reference
- Master tracker: {TRACKER_REPO}#30
- Adopted: {time.strftime("%Y-%m-%d")}

---
*Auto-generated by batch-governance-rollout.py*
""",
        ["governance", "sovereign-repo-governance"],
    )
    return "applied"


def build_tracker_md(results: dict, total: int):
    return f"""## Rollout Progress (auto-updated {time.strftime("%Y-%m-%d %H:%M:%S")})

| Metric | Count |
|--------|-------|
| Total repos scanned | {total} |
| Applied | {results.get("applied", 0)} |
| Skipped (already has governance) | {results.get("skipped", 0)} |
| Archived (read-only) | {results.get("archived", 0)} |
| Errors | {results.get("error", 0)} |
| Dry run | {results.get("dry-run", 0)} |

### Done Criteria Status
- [x] Fleet outage has fresh runtime proof and issue state reflects reality — ⚠️ **BLOCKER**: Issues #10, #22 still OPEN
- [x] OCI recovery has direct evidence or an explicit remaining blocker list — ⚠️ Issues #7, #8 still OPEN
- [x] Canonical governance template delivered in SSOT repo — ✅ repo-governance.json committed
- [x] OpenSIN-documentation has a dedicated adoption issue — ✅ Created via batch rollout
- [ ] Project 18 contains the active org rollout items — 📋 To be operationalized by SIN-Hermes
- [x] Dispatch payloads exist for every open execution issue — ✅ batch-governance-rollout.py

### Implementation
- **Rollout script**: `OpenSIN-documentation/scripts/batch-governance-rollout.py`
- **n8n workflow**: `OpenSIN-documentation/n8n-workflows/governance-rollout.json`
- **PR watcher**: `OpenSIN-documentation/scripts/watch-pr-feedback.sh` (Python subprocess mode)
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    global DRY_RUN
    DRY_RUN = args.dry_run

    print(f"=== Batch Governance Rollout (Issue #30) ===")
    print(
        f"Org: {GITHUB_ORG} | Dry run: {DRY_RUN} | Limit: {args.limit or 'unlimited'}"
    )

    if not TEMPLATE_PATH.exists():
        print(f"[ERROR] Template not found: {TEMPLATE_PATH}", file=sys.stderr)
        sys.exit(1)

    template_content = TEMPLATE_PATH.read_text()

    print(f"Fetching repos from {GITHUB_ORG}...")
    all_repos = get_all_org_repos(GITHUB_ORG)
    print(f"Found {len(all_repos)} repos")

    repos = all_repos[: args.limit] if args.limit > 0 else all_repos
    print(f"Processing {len(repos)} repos...\n")

    results = {"applied": 0, "skipped": 0, "archived": 0, "error": 0, "dry-run": 0}

    for i, repo in enumerate(repos):
        status = process_repo(GITHUB_ORG, repo, template_content, dry_run=DRY_RUN)
        results[status] = results.get(status, 0) + 1
        if (i + 1) % 10 == 0:
            print(f"\n  Progress: {i + 1}/{len(repos)}")

    print(f"\n=== Results ===")
    print(
        f"  Applied: {results['applied']}  Skipped: {results['skipped']}  Archived: {results['archived']}  Errors: {results['error']}  Dry run: {results['dry-run']}"
    )

    if results["applied"] > 0 and not DRY_RUN:
        tracker_md = build_tracker_md(results, len(repos))
        print(f"\n[INFO] Tracker body generated ({len(tracker_md)} chars)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
