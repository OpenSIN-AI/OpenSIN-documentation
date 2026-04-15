<!---
  ===========================================================================
  OpenSIN Documentation — Best Practices: Automated SEO Content Pipeline
  ===========================================================================
  Enthält KEINE echten Tokens. Code‑Beispiele verwenden Credential‑Referenzen.
  ===========================================================================
--->

---
title: Automated SEO Content Pipeline
description: Proof-of-work blog publishing from merged PRs using n8n and Cloudflare Pages.
---

# Automated SEO Content Pipeline

OpenSIN AI Agent’s SEO pipeline automatically turns **real merged pull requests**
into high‑quality blog posts, avoiding generic AI fluff and satisfying Google’s
E‑E‑A‑T guidelines.

## Architecture Deep Dive

### Components

```
┌─────────────────┐   webhook   ┌─────────────────────┐
│  GitHub Repo    │────────────▶│  n8n (OCI VM)      │
│  (any OpenSIN)  │             │  Workflow sq7YR8...│
└─────────────────┘             └─────────┬───────────┘
                                            │
                                  ┌──────────▼──────────┐
                                  │  Function Nodes     │
                                  │  - Generate Draft   │
                                  │  - Humanize + b64   │
                                  │  - Commit (HTTPS)   │
                                  └──────────┬───────────┘
                                            │
                                  ┌──────────▼──────────┐
                                  │  GitHub API (PUT)   │
                                  │  Delqhi/opensin-    │
                                  │  blog-content       │
                                  └──────────┬───────────┘
                                            │
                                  ┌──────────▼──────────┐
                                  │  Cloudflare Pages   │
                                  │  blog.opensin.ai    │
                                  └─────────────────────┘
```

### Why n8n Function Nodes Instead of HTTP Request?

Initially we tried the built‑in HTTP Request node. Problems encountered:

| Problem | Symptom | Fix |
|---------|---------|-----|
| JSON body encoding | GitHub received malformed JSON | Switch to raw body expression: `&#123;&#123; JSON.stringify({...}) &#125;&#125;` |
| Content‑Type conflicts | Node sent form‑urlencoded | Set `contentType: raw` and `sendBody: true`. |
| Base64 handling | Needed to embed `$json.content_base64` | Expression `&#123;&#123; $json.content_base64 &#125;&#125;` works. |
| Reliability | Various edge cases | Final solution: replace HTTP node with Function node using `https` – full control. |

### Determinism Guarantee

- All text generation occurs **synchronously** inside Function nodes.
- No external network calls except final HTTPS commit.
- Given same PR data, Markdown output is identical.
- Avoids LLM rate limits, token rotation failures, non‑deterministic phrasing.

## Configuration Reference

| Setting | Value (Placeholder) |
|---------|---------------------|
| **n8n API Key** | `<YOUR_N8N_API_KEY>` |
| **n8n Host** | `http://92.5.60.87:5678` |
| **Workflow ID** | `sq7YR8vkdPf3usnz` |
| **GitHub Token** | `<YOUR_GITHUB_TOKEN>` (repo scope) – store in n8n Credentials |
| **Blog Repo** | `Delqhi/opensin-blog-content` |
| **Cloudflare Pages** | Project `opensin-blog` → Domain `blog.opensin.ai` |
| **Trigger Path** | `/webhook/blog-publish` (POST) |

## Monitoring & Alerts

- **Execution history**: via n8n API `/api/v1/executions?workflowId=sq7YR8vkdPf3usnz`.
- **Suggested alerts**: workflow failure, no success in 24 h, blog repo inactive.

## Future Improvements

- [ ] Idempotent updates via SHA lookup.
- [ ] Dynamic PR number in filename and message.
- [ ] Configurable post template stored in Google Docs or Markdown file.
- [ ] Enriched content: code snippets, changed files list, commit SHAs.
- [ ] Tag inference from file paths.
- [ ] Scheduled publishing (SEO‑friendly hours).
- [ ] CI test suite for Function nodes.
- [ ] Move GitHub token to n8n Credential Store.
- [ ] Add webhook secret for authentication.

## Related Documents

- OpenSIN‑overview → `docs/seo-pipeline.md` (high‑level overview).
- n8n Workflow Template → `n8n-workflows/auto-blog-publisher.json`.
- GitHub API – Create or update file contents: <https://docs.github.com/en/rest/repos/contents#create-or-update-file-contents>
- Cloudflare Pages – Deploy from Git: <https://developers.cloudflare.com/pages/>

---

*Document version:* 2026‑04‑10  
*Maintainer:* sin‑zeus  
*Review cycle:* Monthly or after any workflow change.

---

## Relevante Mandate

| Mandat | Priority | Regel |
|--------|----------|-------|
| **n8n CI/CD** | 0.0 | Self-hosted auf OCI VM |
| **Box.com Storage** | 0.0 | Artefakte zu Box.com |
