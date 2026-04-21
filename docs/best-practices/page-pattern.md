---
title: Best-Practice Page Pattern
description: Repeatable VitePress-first structure for OpenSIN best-practice pages.
---

# Best-Practice Page Pattern

> **Pattern rule:** New best-practice pages should use Markdown-first structure, shared VitePress containers, and a stable section order. Raw HTML is a last resort, not the default layout tool.

## Standard page shape

| Section | Purpose | Preferred format |
|---|---|---|
| Mandate / scope | State the non-negotiable rule up front | blockquote or custom container |
| At a glance | Give operators the fast read | table |
| Core rules | Explain the required behavior | `##` sections with short `###` subsections |
| Verification checklist | Define what proves the rule was followed | checklist |
| Related docs | Point to adjacent canon | Markdown links |
| Metadata / mandates | Preserve status and ownership | short footer + table |

## Authoring rules

- Prefer Markdown headings, lists, tables, admonitions, and fenced code blocks over custom HTML wrappers.
- Keep one primary narrative per page: mandate, implementation pattern, verification, then references.
- Use raw HTML only when Markdown and standard VitePress containers cannot express the content.
- If a page is already clear and consistent, preserve it instead of rewriting for style alone.

## Starter skeleton

```md
---
title: Example Best Practice
description: One-line summary of the rule and why it exists.
---

# Example Best Practice

> **Mandate:** One sentence describing the rule.

## At a glance

| Area | Standard |
|---|---|
| Required | ... |
| Forbidden | ... |
| Proof | ... |

## 1. Core rule

### What
...

### Why
...

### Why not otherwise
...

## Verification checklist

- [ ] expected proof exists
- [ ] repo-native validation passed
- [ ] related docs stayed in sync

## Related docs

- [Adjacent page](/path)

---

*Last updated:* YYYY-MM-DD  
*Status:* **ACTIVE**  
*Maintainer:* team-or-owner
```

## When to break the pattern

Only break this structure when the page is acting as a reference catalog, changelog, or API surface where a different layout is clearly more readable.
