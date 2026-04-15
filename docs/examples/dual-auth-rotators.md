# Dual Auth Rotators: Antigravity + OpenAI Google

This page records the final working state of the two separate auth-rotation systems we stabilized:

- `openAntigravity-auth-rotator`
- `openai-google-rotator`

The main goal was to stop expensive false-positive Google account rotations while keeping `openai/gpt-5.4` usable through the OpenAI token pool.

## Final status

- `openai/gpt-5.4` is working again.
- The OpenAI token pool is healthy again.
- The antigravity daemon should be treated as **off by default** unless explicitly needed.
- Antigravity auto-rotation is now documented as **Claude-only**, never Gemini-only, never generic 429-based.

## Architecture split

These systems must stay logically separate.

### 1. Antigravity rotator

Purpose:

- rotate Antigravity Google accounts only when a **real Claude-specific** rate-limit condition happens
- avoid wasting paid Google accounts on unrelated errors

Required trigger policy:

- allowed:
  - `rate-limited for claude`
  - `rate_limited for claude`
  - `No Antigravity accounts configured`
  - `No Antigravity accounts available`
  - `[RateLimit] ... claude`
- forbidden:
  - Gemini quota events
  - generic `429`
  - generic `RATE_LIMIT_EXCEEDED`
  - OpenAI rate-limit errors
  - permission-denied errors
  - auth side effects
  - guardian checks
  - token-expiry side effects

### 2. OpenAI Google rotator

Purpose:

- create fresh OpenAI auth tokens through Google SSO + ChatGPT onboarding + `opencode auth login`
- push the fresh token into the Supabase-backed `openai_tokens` pool
- feed the OCI gateway so `openai/gpt-5.4` works again

Operational rule:

- when debugging this path, run **only** `openai-google-rotator`
- do **not** auto-start or couple the antigravity daemon during OpenAI pool debugging

## Root cause summary

## Antigravity false positives

The expensive bug came from overly broad rate-limit matching.

Observed failure mode:

- antigravity debug logs contained many generic quota messages
- watcher logic matched generic `429` / `RATE_LIMIT_EXCEEDED`
- Gemini or short-reset quota messages incorrectly triggered a paid Google account rotation

One confirmed false-positive pattern looked like this:

```text
Response Body (429): ... "You have exhausted your capacity on this model. Your quota will reset after 1s." ... "reason": "RATE_LIMIT_EXCEEDED"
```

That message was **not enough evidence** for a Claude rotation.

## Session crash behavior

Another issue was that temporary zero-account states caused plugin crashes with messages like:

```text
No Antigravity accounts configured. Run opencode auth login
```

That crash behavior created the impression that sessions had to be manually restarted. The safer behavior is to wait/retry instead of crashing immediately.

## OpenAI Google flow breakage

The OpenAI rotator broke after native Chrome dialog handling was replaced with DOM/JS assumptions.

Important fact:

- the Chrome sign-in / profile confirmation dialogs in this flow are **native OS dialogs**
- they are **not** normal DOM elements
- the old AppleScript-based key sequence was the correct mechanism

The restored working approach uses the native dialog path again, including the historical:

- `Shift+Cmd+M`
- `Tab`
- `Enter`

## Implemented fixes

## Antigravity safeguards

Documented safe behavior for `~/.config/openAntigravity-auth-rotator/`:

- `src/watcher.py`
  - strict Claude-only whitelist matching
  - Gemini and generic quota messages ignored
- `main.py`
  - lock-file protection against duplicate rotations
  - safer daemon-loop behavior
  - guardian/token-expiry suppression for auto-rotation
- cached plugin behavior
  - wait/retry on temporary zero-account state
  - avoid crashing active sessions during short-lived pool transitions

## OpenAI pool recovery

Documented safe behavior for `/Users/jeremy/dev/openai-google-rotator/` and OCI gateway components:

- restored AppleScript-based native Chrome dialog handling in `fast_runner.py`
- kept OpenAI debugging independent from antigravity daemon behavior
- updated `.env` to use the direct Supabase endpoint:

```text
SUPABASE_URL=http://92.5.60.87:8006
```

- ensured fresh tokens were pushed into `openai_tokens`
- reset stale active tokens when they were known-dead
- restored OCI gateway `OPENAI_BASE` to:

```text
http://92.5.60.87:4100/v1
```

## Validation evidence

The following outcomes were confirmed during the recovery:

- Claude-only watcher test cases behaved correctly
  - Claude trigger: accepted
  - `No Antigravity accounts`: accepted
  - Gemini 429: ignored
  - generic 429: ignored
  - generic `RATE_LIMIT_EXCEEDED`: ignored
  - OpenAI rate-limit message: ignored
  - permission-denied message: ignored
- `openai-google-rotator` completed an end-to-end success run
  - Google login
  - ChatGPT onboarding
  - `opencode auth login`
  - OAuth callback
  - `push_to_pool.py`
- success log ended with:

```text
✅ PIPELINE ERFOLGREICH!
```

- the user later confirmed the final recovered state:
  - GPT model works again
  - pool is healthy again

## Important operational rules

## Do

- keep the antigravity daemon off unless it is explicitly needed
- treat Antigravity rotation as a Claude-specific protection only
- test OpenAI pool recovery independently
- prefer evidence from current logs and pool state over assumptions

## Do not

- do not rotate paid Google accounts on Gemini-only quota events
- do not treat any generic `429` as sufficient evidence
- do not merge OpenAI debugging and antigravity daemon testing into one uncontrolled run
- do not replace native Chrome dialog handling with DOM-only automation for this flow

## Known follow-up note

One separate Antigravity-side error was observed and should be treated as a different class of problem:

```text
Forbidden ... cloudaicompanion.companions.generateChat ... project rising-fact-p41fc
```

That is a project/permission issue, not evidence that the antigravity watcher should rotate accounts.

## Related paths

- `~/.config/openAntigravity-auth-rotator/main.py`
- `~/.config/openAntigravity-auth-rotator/src/watcher.py`
- `~/.config/openAntigravity-auth-rotator/src/rotator.py`
- `~/.config/openAntigravity-auth-rotator/src/config.py`
- `~/.cache/opencode/node_modules/opencode-antigravity-auth/dist/src/plugin.js`
- `/Users/jeremy/dev/openai-google-rotator/fast_runner.py`
- `/Users/jeremy/dev/openai-google-rotator/push_to_pool.py`
- `/Users/jeremy/dev/openai-google-rotator/token_pool.py`
- `/opt/llm-gateway/gateway.py`

## Outcome

The recovery goal for this round is complete:

- prevent wasteful antigravity false positives
- preserve separation between the two rotators
- restore a healthy OpenAI token pool
- restore working `openai/gpt-5.4`
