---
title: Team Manifest Contract
description: Canonical documentation for OpenSIN marketplace team manifests and team.json.
---

# Team Manifest Contract

OpenSIN V1 treats each `Team-SIN-*` offering as a **structured marketplace manifest**.

That manifest lives in `team.json` and is validated by the canonical schema in `OpenSIN-overview`.

## Canonical sources

- Schema: [`schemas/team.schema.json`](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/schemas/team.schema.json)
- Product decision: [Product Vision → Marketplace Option A](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/PRODUCT-VISION.md#marketplace--entschieden-option-a-metadata-manifeste)
- Canonical templates: [`templates/teams/`](https://github.com/OpenSIN-AI/OpenSIN-overview/tree/main/templates/teams)

## Why this contract exists

The marketplace should not be driven by ad-hoc markdown or manually duplicated sales copy.

Instead, one `team.json` file answers:

- what the bundle is called,
- which agents belong to it,
- how it is priced,
- what permissions and budgets it needs,
- what marketing copy the marketplace should render.

## Required top-level fields

The schema currently requires these fields:

| Field | Meaning |
|---|---|
| `$schema_version` | manifest format version |
| `id` | canonical Team-SIN repo name |
| `name` | human-readable bundle name |
| `slug` | marketplace URL slug |
| `tier` | bundle placement in the product model |
| `status` | lifecycle state |
| `marketing` | summary + bullets for the marketplace card and detail page |
| `agents` | A2A agents unlocked by the bundle |
| `pricing` | commercial model |

## Important clarification: old tier words vs current schema

The launch-gate issue for docs was written with shorthand labels like `core-included`, `bundle`, and `addon`.

The **current canonical schema** is slightly more precise:

- `tier` expresses where the team sits in the product model: `marketplace`, `core-included`, `enterprise`
- `pricing.model` expresses how it is sold: `free-with-pro`, `monthly-addon`, `metered`, `enterprise-quote`

So in practice:

| Older shorthand | Current schema expression |
|---|---|
| core-included | `tier: core-included` + `pricing.model: free-with-pro` |
| addon | `tier: marketplace` + `pricing.model: monthly-addon` |
| enterprise bundle | `tier: enterprise` + `pricing.model: enterprise-quote` |

## Worked examples from the live templates

### Example 1 — included with Pro

Source template:

- [`Team-SIN-Code-Core.json`](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/templates/teams/Team-SIN-Code-Core.json)

Key shape:

```json
{
  "id": "Team-SIN-Code-Core",
  "tier": "core-included",
  "pricing": {
    "model": "free-with-pro"
  }
}
```

What it means:

- the team ships with every Pro subscription,
- no separate marketplace purchase is required,
- the bundle still declares real agents, permissions, budgets, and provenance.

### Example 2 — monthly add-on bundle

Source template:

- [`Team-SIN-Commerce.json`](https://github.com/OpenSIN-AI/OpenSIN-overview/blob/main/templates/teams/Team-SIN-Commerce.json)

Key shape:

```json
{
  "id": "Team-SIN-Commerce",
  "tier": "marketplace",
  "pricing": {
    "model": "monthly-addon",
    "monthly_addon_eur": 19
  }
}
```

What it means:

- the team is sold as a marketplace add-on,
- the bundle unlocks multiple agents,
- the pricing model is explicit and machine-readable.

### Example 3 — enterprise shape in the schema

The current templates fetched from `OpenSIN-overview/templates/teams/` are using:

- one `core-included` example,
- multiple `marketplace` + `monthly-addon` examples.

The schema also reserves enterprise bundles through:

```json
{
  "tier": "enterprise",
  "pricing": {
    "model": "enterprise-quote"
  }
}
```

That shape is part of the **canonical contract**, even if the currently published template set has not started using it yet.

## Fields frontend and backend both care about

### For `website-my.opensin.ai`

- `name`
- `slug`
- `tagline`
- `marketing.summary`
- `marketing.bullets`
- `status`
- `pricing`

### For `chat.opensin.ai` and `OpenSIN-backend`

- `agents`
- `permissions`
- `budgets`
- `pricing`
- `provenance`

## Authoring rules

- Keep runtime code in the `A2A-SIN-*` repo, not in the manifest.
- Keep bundle composition in `team.json`.
- Treat `OpenSIN-overview/templates/teams/` as the canonical authoring location when the overview repo is the SSOT.

## Next steps

- [API Overview](/api/overview)
- [OpenSIN Backend V1 API](/api/backend-v1)
- [Agent Author Guide](/guide/how-to-configure-agents)
