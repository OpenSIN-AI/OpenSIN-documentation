---
title: Automated SEO Content Pipeline
description: Proof-of-work blog publishing from merged PRs using n8n and Cloudflare Pages.
---

# Automated SEO Content Pipeline

> **Pattern:** This page follows the normalized best-practice shape for workflow documentation: fast summary first, then implementation details, verification, and adjacent references.

OpenSIN AI Agent's SEO pipeline turns real merged pull requests into blog-ready Markdown, so publishing stays tied to actual shipped work instead of generic AI filler.

## At a glance

| Area | Standard |
|---|---|
| Trigger | Merged PR or webhook payload into n8n |
| Orchestrator | Self-hosted n8n workflow on OCI |
| Output | Markdown committed to `OpenSIN-AI/Biz-SIN-Blog-Posts` and deployed via Cloudflare Pages |
| Proof | Successful execution history, generated Markdown, and downstream deploy confirmation |

## 1. Pipeline flow

```text
┌─────────────────┐   webhook   ┌─────────────────────┐
│  GitHub Repo    │────────────▶│  n8n (OCI VM)       │
│  (any OpenSIN)  │             │  Workflow sq7YR8... │
└─────────────────┘             └─────────┬───────────┘
                                            │
                                  ┌─────────▼──────────┐
                                  │  Function Nodes    │
                                  │  - Generate Draft  │
                                  │  - Humanize + b64  │
                                  │  - Commit (HTTPS)  │
                                  └─────────┬──────────┘
                                            │
                                  ┌─────────▼──────────┐
                                  │  GitHub API (PUT)  │
                                  │  OpenSIN-AI/       │
                                  │  Biz-SIN-Blog-Posts│
                                  └─────────┬──────────┘
                                            │
                                  ┌─────────▼──────────┐
                                  │ Cloudflare Pages   │
                                  │ blog.opensin.ai    │
                                  └────────────────────┘
```

## 2. Why function nodes instead of the HTTP Request node

Initial attempts with the built-in HTTP Request node created too many edge cases for a content pipeline that needs deterministic output.

| Problem | Symptom | Fix |
|---------|---------|-----|
| JSON body encoding | GitHub received malformed JSON | Switch to a raw body expression using the workflow's double-curly `JSON.stringify(...)` template syntax |
| Content-Type conflicts | Node sent form-urlencoded data | Set `contentType: raw` and `sendBody: true` |
| Base64 handling | Needed to embed `$json.content_base64` cleanly | Use direct expression interpolation inside the raw payload |
| Reliability | Node-level edge cases made debugging slow | Replace the HTTP node with a Function node using `https` for full control |

## 3. Determinism and safety

- Generation runs synchronously inside Function nodes.
- External network activity is limited to the final HTTPS commit and deploy path.
- Given the same PR payload, the Markdown output should stay stable.
- This avoids unnecessary rate-limit, token-rotation, and phrasing drift problems in the publishing step.

## 4. Configuration reference

| Setting | Value (Placeholder) |
|---------|---------------------|
| **n8n API Key** | `YOUR_N8N_API_KEY` placeholder |
| **n8n Host** | Internal self-hosted n8n endpoint (see owning infra repo) |
| **Workflow ID** | `sq7YR8vkdPf3usnz` |
| **GitHub Token** | `YOUR_GITHUB_TOKEN` placeholder (repo scope) — store in n8n Credentials |
| **Blog Repo** | `OpenSIN-AI/Biz-SIN-Blog-Posts` |
| **Cloudflare Pages** | Project `opensin-blog` → Domain `blog.opensin.ai` |
| **Trigger Path** | `/webhook/blog-publish` (POST) |

## 5. Verification checklist

- [ ] The workflow execution history shows a successful run for the expected PR payload
- [ ] Generated Markdown matches the merged PR content and structure
- [ ] The blog repository received the committed file update
- [ ] Cloudflare Pages picked up the deploy or shows a healthy downstream state
- [ ] Failure output is inspectable when the workflow does not complete

## 6. Monitoring and backlog

### Monitoring

- **Execution history:** inspect `/api/v1/executions?workflowId=sq7YR8vkdPf3usnz`
- **Suggested alerts:** workflow failure, no success in 24h, or blog repo inactivity

### Backlog

- [ ] Idempotent updates via SHA lookup
- [ ] Dynamic PR number in filename and message
- [ ] Configurable post template stored in Google Docs or Markdown
- [ ] Enriched content with code snippets, changed files, and commit SHAs
- [ ] Tag inference from file paths
- [ ] Scheduled publishing windows
- [ ] CI test coverage for Function nodes
- [ ] Token placement in the n8n credential store
- [ ] Webhook secret enforcement

## Related docs

- [Best-Practice Page Pattern](/best-practices/page-pattern)
- [CI/CD mit n8n + sin-github-action](/best-practices/ci-cd-n8n)
- `docs/seo-pipeline.md` for the high-level overview
- `n8n-workflows/auto-blog-publisher.json` for the workflow template
- [GitHub API – Create or update file contents](https://docs.github.com/en/rest/repos/contents#create-or-update-file-contents)
- [Cloudflare Pages – Deploy from Git](https://developers.cloudflare.com/pages/)

---

*Last updated:* 2026-04-21  
*Status:* **ACTIVE**  
*Maintainer:* sin-zeus  
*Review cycle:* Monthly or after any workflow change

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **n8n CI/CD** | 0.0 | Self-hosted auf OCI VM |
| **Box.com Storage** | 0.0 | Artefakte zu Box.com |
