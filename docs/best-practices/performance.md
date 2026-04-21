---
title: "Performance Standards"
description: "Latency and throughput targets for the OpenSIN fleet."
---

# Performance Standards

In an autonomous agent system, latency is the enemy of reasoning. We enforce strict timing targets across all surfaces.

## ⚡ Latency Targets

| Layer | Max Latency | Monitoring Tool |
|-------|-------------|-----------------|
| **A2A Handshake** | < 150ms | NATS Monitor |
| **Tool Execution** | < 500ms | HookSystem Logs |
| **Model Inference** | < 2.0s | Antigravity Metrics |
| **Web UI Load** | < 800ms | Lighthouse / Pages |

## Optimization Mandates

1. **Neural-Bus Local Cache:** Never fetch metadata twice; use the Redis-backed cache for A2A discovery.
2. **Context Compaction:** Always compress prompts to the minimum necessary tokens to reduce inference time.
3. **Rust Engine Preference:** Use the Rust-based execution engine for heavy file operations or search.

---

## ⚖️ Performance Audits

Environments that consistently exceed 1.5s total loop latency are automatically flagged for hardware or network upgrade.
