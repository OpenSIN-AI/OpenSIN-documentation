---
title: "Multi-Agent Example"
---

# Multi-Agent Example

A complete example showing three OpenSIN agents collaborating to build, test, and deploy a feature.

## Scenario

Build a REST API endpoint that:

1. Accepts a JSON payload
2. Validates the input
3. Stores data in Supabase
4. Returns a formatted response
5. Includes comprehensive tests

## Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  SIN-Zeus    │────>│ SIN-Herakles │────>│  SIN-Tester  │
│ (Orchestrate)│     │ (Build API)  │     │ (Write Tests)│
└──────────────┘     └──────────────┘     └──────────────┘
       │                                          │
       │              ┌──────────────┐            │
       └────────────>│ SIN-Hermes   │<───────────┘
                      │ (Deploy)     │
                      └──────────────┘
```

## Step 1: Define the Orchestration

```typescript
import { Orchestrator } from "@opensin/agent-sdk";

const orchestrator = new Orchestrator({
  agents: {
    builder: "sin-herakles",
    tester: "sin-tester",
    deployer: "sin-hermes",
  },
});

const taskGraph = {
  "design-api": {
    agent: "builder",
    prompt: `Design a REST API endpoint POST /api/v1/items that:
      - Accepts { name: string, category: string, price: number }
      - Validates all fields (name 3-100 chars, price > 0)
      - Returns 201 with the created item including an auto-generated ID
      - Returns 400 with validation errors on bad input
      Output: TypeScript types and route handler code.`,
    depends: [],
  },
  "implement-api": {
    agent: "builder",
    prompt:
      "Implement the API endpoint based on the design. Use Supabase for storage.",
    depends: ["design-api"],
  },
  "write-tests": {
    agent: "tester",
    prompt: "Write unit and integration tests for the items API endpoint.",
    depends: ["implement-api"],
  },
  deploy: {
    agent: "deployer",
    prompt: "Deploy the updated API to the staging environment.",
    depends: ["write-tests"],
  },
};

const result = await orchestrator.executeGraph(taskGraph);
```

## Step 2: Builder Agent Output

SIN-Herakles produces the API code:

```typescript
// src/routes/items.ts
import { Router } from "express";
import { supabase } from "../db";
import { z } from "zod";

const ItemSchema = z.object({
  name: z.string().min(3).max(100),
  category: z.string().min(1),
  price: z.number().positive(),
});

const router = Router();

router.post("/api/v1/items", async (req, res) => {
  const parsed = ItemSchema.safeParse(req.body);

  if (!parsed.success) {
    return res.status(400).json({
      error: "Validation failed",
      details: parsed.error.issues,
    });
  }

  const { data, error } = await supabase
    .from("items")
    .insert(parsed.data)
    .select()
    .single();

  if (error) {
    return res.status(500).json({ error: "Database error" });
  }

  return res.status(201).json(data);
});

export default router;
```

## Step 3: Tester Agent Output

SIN-Tester generates the test suite:

```typescript
// tests/items.test.ts
import request from "supertest";
import { app } from "../src/app";

describe("POST /api/v1/items", () => {
  it("creates an item with valid data", async () => {
    const res = await request(app)
      .post("/api/v1/items")
      .send({ name: "Widget", category: "tools", price: 9.99 });

    expect(res.status).toBe(201);
    expect(res.body).toHaveProperty("id");
    expect(res.body.name).toBe("Widget");
  });

  it("rejects empty name", async () => {
    const res = await request(app)
      .post("/api/v1/items")
      .send({ name: "", category: "tools", price: 9.99 });

    expect(res.status).toBe(400);
    expect(res.body.error).toBe("Validation failed");
  });

  it("rejects negative price", async () => {
    const res = await request(app)
      .post("/api/v1/items")
      .send({ name: "Widget", category: "tools", price: -5 });

    expect(res.status).toBe(400);
  });

  it("rejects missing fields", async () => {
    const res = await request(app).post("/api/v1/items").send({});

    expect(res.status).toBe(400);
  });
});
```

## Step 4: Deployer Output

SIN-Hermes handles deployment:

```bash
# Automated deployment log
[sin-hermes] Building project...
[sin-hermes] Running tests... 4/4 passed
[sin-hermes] Deploying to staging...
[sin-hermes] Deployed: https://staging-api.opensin.ai/api/v1/items
[sin-hermes] Health check: 200 OK
[sin-hermes] Notifying team via Telegram...
```

## Key Takeaways

1. **Each agent has a focused role** -- builder builds, tester tests, deployer deploys
2. **Dependencies are explicit** -- tests can't run until implementation is done
3. **Independent tasks run in parallel** -- design-api has no dependencies, so it starts immediately
4. **Artifacts flow through the graph** -- each agent's output becomes the next agent's context
5. **Failures propagate cleanly** -- if tests fail, deployment is automatically skipped
