---
name: create-auth-plugin
description: Build, debug, and deploy OpenCode auth plugins for any LLM provider (DeepSeek, Mistral, xAI, etc.). Covers the full lifecycle from scaffold to cache injection to token rotation watcher integration. Use when creating a new auth plugin or fixing a broken one.
---

# Create Auth Plugin for OpenCode

Comprehensive skill for building OpenCode authentication plugins that enable `opencode auth login --provider <name>` and seamless token rotation without session restart.

## Architecture Overview

OpenCode auth plugins are npm-style packages that provide:
1. **Auth hooks** — login flow (OAuth PKCE, Device Flow, API key)
2. **Config hooks** — register provider + models dynamically
3. **Loader hooks** — inject credentials into API requests at runtime

```
Plugin Package
├── package.json          # name, version, module: "index.ts", type: "module"
├── index.ts              # Re-exports: export { MyPlugin, default } from "./src/index"
├── src/
│   ├── index.ts          # Main plugin export (async function)
│   ├── constants.ts      # Provider ID, OAuth config, API config, models
│   ├── types.ts          # Credential and config interfaces
│   └── oauth.ts          # OAuth flow implementation (if applicable)
└── README.md
```

## Critical Rules (NEVER VIOLATE)

### 1. Plugin Loading Pipeline

OpenCode resolves plugins in this exact order:

```
opencode.json "plugin" array
    ↓
For each entry:
    ├── If starts with "file://" → load directly via Bun (ONLY tools/events work, NOT auth hooks)
    └── If npm-style name → resolve from ~/.cache/opencode/node_modules/<name>/
         ├── First: try `bun add <name>@latest` against npm registry
         ├── If 404: fall back to cached version in node_modules
         └── If no cache: plugin fails to load
```

**AUTH HOOKS ONLY WORK FROM NPM-RESOLVED PLUGINS.** The `file://` path only activates tool and event hooks. This is the #1 gotcha.

### 2. Cache Injection (For Unpublished Plugins)

If the plugin is NOT published to npm, you MUST manually inject it:

```bash
# Step 1: Copy plugin to cache node_modules
cp -R ~/.config/opencode/local-plugins/opencode-<name>-auth \
      ~/.cache/opencode/node_modules/opencode-<name>-auth

# Step 2: Add to cache package.json
# Edit ~/.cache/opencode/package.json and add:
#   "opencode-<name>-auth": "1.0.0"
# to the "dependencies" object

# Step 3: Reference in opencode.json plugin array (npm-style, NOT file://)
# "plugin": ["opencode-<name>-auth"]
```

**NEVER use `file:///path/to/plugin/index.ts`** in the plugin array for auth plugins. It will load without errors but auth hooks silently won't activate.

### 3. Export Pattern (MUST MATCH EXACTLY)

The plugin MUST export an async function that receives input and returns an object with `auth` and `config` properties. Study these working patterns:

**index.ts (re-export file):**
```typescript
export { MyProviderAuthPlugin, default } from "./src/index";
```

**src/index.ts (main plugin):**
```typescript
export const MyProviderAuthPlugin = async (_input: unknown) => {
  return {
    // REQUIRED: Auth hooks
    auth: {
      provider: PROVIDER_ID,  // Must match the provider key in opencode config
      loader: async (getAuth, provider) => { ... },
      methods: [ { type: 'oauth', label: '...', authorize: async () => { ... } } ],
    },
    // REQUIRED: Config hooks (registers provider + models)
    config: async (config: Record<string, unknown>) => { ... },
  };
};

export default MyProviderAuthPlugin;
```

### 4. package.json Requirements

```json
{
  "name": "opencode-<provider>-auth",
  "version": "1.0.0",
  "module": "index.ts",
  "type": "module",
  "devDependencies": {
    "@opencode-ai/plugin": "^1.1.48",
    "@types/node": "^22.0.0",
    "typescript": "^5.6.0"
  },
  "files": ["index.ts", "src", "README.md"],
  "engines": { "node": ">=20.0.0" }
}
```

**Critical fields:**
- `"module": "index.ts"` — Bun uses this to find the entry point
- `"type": "module"` — Required for ESM imports
- Name convention: `opencode-<provider>-auth`

## Plugin Anatomy — The Three Hooks

### Hook 1: `auth.loader`

Called on EVERY API request. Returns `{ apiKey, baseURL }` or `null`.

```typescript
loader: async (
  getAuth: () => Promise<{ type: string; access?: string; refresh?: string; expires?: number }>,
  provider: { models?: Record<string, { cost?: { input: number; output: number } }> },
) => {
  // Zero out costs (free via OAuth)
  if (provider?.models) {
    for (const model of Object.values(provider.models)) {
      if (model) model.cost = { input: 0, output: 0 };
    }
  }

  const auth = await getAuth();
  if (!auth || auth.type !== 'oauth') return null;

  // Optional: refresh if expired
  if (auth.expires && Date.now() > auth.expires - 60_000 && auth.refresh) {
    // refresh logic here
  }

  return {
    apiKey: auth.access ?? '',
    baseURL: 'https://api.provider.com/v1',
  };
},
```

### Hook 2: `auth.methods`

Defines login flows shown in `opencode auth login --provider <name>`.

**OAuth PKCE (browser redirect):**
```typescript
methods: [{
  type: 'oauth' as const,
  label: 'Sign in with Provider (OAuth)',
  authorize: async () => {
    // Build auth URL, open browser, wait for callback
    return {
      url: authorizationUrl,
      instructions: 'Complete sign-in in your browser',
      method: 'manual' as const,  // or 'auto' for polling
      callback: async () => ({
        type: 'success' as const,
        access: accessToken,
        refresh: refreshToken,
        expires: expiryTimestamp,
      }),
    };
  },
}],
```

**Device Flow (code display + polling):**
```typescript
methods: [{
  type: 'oauth' as const,
  label: 'Provider (Device Flow)',
  authorize: async () => {
    const deviceAuth = await requestDeviceAuthorization();
    openBrowser(deviceAuth.verification_uri_complete);
    return {
      url: deviceAuth.verification_uri_complete,
      instructions: `Code: ${deviceAuth.user_code}`,
      method: 'auto' as const,  // OpenCode polls automatically
      callback: async () => {
        // Poll token endpoint until user approves
        while (notExpired) {
          await sleep(interval);
          const token = await pollDeviceToken(deviceAuth.device_code);
          if (token) {
            return { type: 'success', access: token.access_token, refresh: token.refresh_token, expires: ... };
          }
        }
        return { type: 'failed' as const };
      },
    };
  },
}],
```

### Hook 3: `config`

Registers the provider and its models dynamically. Called during OpenCode bootstrap.

```typescript
config: async (config: Record<string, unknown>) => {
  const providers = (config.provider as Record<string, unknown>) || {};

  providers[PROVIDER_ID] = {
    npm: '@ai-sdk/openai-compatible',  // or specific SDK
    name: 'Provider Name',
    options: { baseURL: 'https://api.provider.com/v1' },
    models: {
      'model-id': {
        id: 'model-id',
        name: 'Model Name',
        reasoning: false,
        limit: { context: 128000, output: 8192 },
        cost: { input: 0, output: 0 },
        modalities: { input: ['text'], output: ['text'] },
      },
    },
  };

  config.provider = providers;
},
```

## Auth Storage

OpenCode stores auth in `~/.local/share/opencode/auth.json`:

```json
{
  "google": { "type": "oauth", "access": "...", "refresh": "...", "expires": 1234567890 },
  "qwen-code": { "type": "oauth", "access": "...", "refresh": "...", "expires": 1234567890 },
  "openrouter": { "type": "oauth", "access": "...", "refresh": "...", "expires": 1234567890 }
}
```

Key: `provider` ID from `auth.provider` field.

For token rotation without session restart, atomically update the provider's entry in `auth.json`. OpenCode's built-in retry reads fresh credentials on next attempt.

## Token Rotation Integration

To enable automatic token swap on rate limit (like Antigravity/Qwen):

### 1. Create Token Pool

```
~/.open-auth-rotator/<provider>/
├── pool.json         # Token pool with multiple accounts
├── swap_token.py     # Atomic swap script
├── state.json        # Swap count tracking
└── rotator.log       # Swap history
```

**pool.json format:**
```json
{
  "current_index": 0,
  "tokens": [
    {
      "label": "account-1",
      "status": "active",
      "access_token": "...",
      "refresh_token": "...",
      "expires": 1234567890
    }
  ]
}
```

### 2. Swap Script Pattern

The swap script must atomically update BOTH:
- `~/.local/share/opencode/auth.json` → provider entry
- Provider-specific creds file (if any, e.g., `~/.qwen/oauth_creds.json`)

```python
#!/usr/bin/env python3
"""Atomic token swap for <provider>."""
import json, os, shutil, tempfile

AUTH_JSON = os.path.expanduser("~/.local/share/opencode/auth.json")
POOL_JSON = os.path.expanduser("~/.open-auth-rotator/<provider>/pool.json")
PROVIDER_ID = "<provider-id>"  # Must match auth.json key

def atomic_write(path, data):
    """Write via temp file + rename for atomicity."""
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, path)  # Atomic on POSIX
    except:
        os.unlink(tmp)
        raise

def swap():
    pool = json.load(open(POOL_JSON))
    tokens = pool["tokens"]
    next_idx = (pool["current_index"] + 1) % len(tokens)
    next_token = tokens[next_idx]

    # Update auth.json atomically
    auth = json.load(open(AUTH_JSON))
    auth[PROVIDER_ID] = {
        "type": "oauth",
        "access": next_token["access_token"],
        "refresh": next_token.get("refresh_token", ""),
        "expires": next_token.get("expires", 0),
    }
    atomic_write(AUTH_JSON, auth)

    # Update pool index
    pool["current_index"] = next_idx
    atomic_write(POOL_JSON, pool)
```

### 3. Watcher Integration

Add rate limit detection to `~/.open-auth-rotator/antigravity/core/watcher_log_scan.py`:

```python
import re

_PROVIDER_RATE_LIMIT_PATTERN = re.compile(
    r"providerID=<provider-id>.*(429|rate.limit|Arrearage|usage_limit|InvalidApiKey)",
    re.IGNORECASE,
)

def _scan_logs_provider(log_lines: list[str]) -> bool:
    """Return True if <provider> rate limit detected in recent logs."""
    for line in log_lines:
        if _PROVIDER_RATE_LIMIT_PATTERN.search(line):
            return True
    return False
```

Add swap trigger to `~/.open-auth-rotator/antigravity/core/watcher_loop.py`:

```python
_PROVIDER_SWAP_SCRIPT = os.path.expanduser("~/.open-auth-rotator/<provider>/swap_token.py")
_PROVIDER_COOLDOWN_SECS = 30
_last_provider_swap = 0

# In main loop:
if _scan_logs_provider(recent_lines):
    now = time.time()
    if now - _last_provider_swap > _PROVIDER_COOLDOWN_SECS:
        result = subprocess.run([sys.executable, _PROVIDER_SWAP_SCRIPT, "--force"],
                                capture_output=True, text=True, timeout=15)
        _last_provider_swap = now
```

## Step-by-Step: Create a New Auth Plugin

### Phase 1: Scaffold

```bash
PROVIDER="deepseek"  # Change this
PLUGIN_DIR=~/.config/opencode/local-plugins/opencode-${PROVIDER}-auth

mkdir -p $PLUGIN_DIR/src
```

1. Create `package.json` with correct `name`, `module`, `type`
2. Create `src/constants.ts` with provider ID, OAuth endpoints, API config, model list
3. Create `src/types.ts` with credential interfaces
4. Create `src/index.ts` with the three hooks (auth.loader, auth.methods, config)
5. Create `index.ts` re-export file
6. Create `src/oauth.ts` if using OAuth (PKCE or Device Flow)

### Phase 2: Verify with Bun

```bash
cd ~/.cache/opencode
bun -e "const mod = require('opencode-${PROVIDER}-auth'); console.log(Object.keys(mod))"
# Must output: [ "MyProviderAuthPlugin", "default" ]
```

### Phase 3: Inject into Cache

```bash
# Copy to cache
cp -R $PLUGIN_DIR ~/.cache/opencode/node_modules/opencode-${PROVIDER}-auth

# Add to cache package.json
python3 -c "
import json
p = json.load(open('$HOME/.cache/opencode/package.json'))
p['dependencies']['opencode-${PROVIDER}-auth'] = '1.0.0'
json.dump(p, open('$HOME/.cache/opencode/package.json', 'w'), indent=2)
"

# Add to opencode.json plugin array (npm-style name, NOT file://)
python3 -c "
import json
c = json.load(open('$HOME/.config/opencode/opencode.json'))
plugins = c.get('plugin', [])
name = 'opencode-${PROVIDER}-auth'
if name not in plugins:
    plugins.append(name)
    c['plugin'] = plugins
    json.dump(c, open('$HOME/.config/opencode/opencode.json', 'w'), indent=2)
"
```

### Phase 4: Verify Loading

```bash
# Start a new opencode session and check logs
ls -lt ~/.local/share/opencode/log/ | head -1
# Then grep for plugin loading:
grep -i "${PROVIDER}" ~/.local/share/opencode/log/<latest>.log
# Must see:
#   INFO service=plugin path=opencode-${PROVIDER}-auth loading plugin
#   WARN service=bun pkg=opencode-${PROVIDER}-auth ... using cached
# Must NOT see:
#   ERROR service=plugin ... failed to load plugin
```

### Phase 5: Token Rotation (Optional)

```bash
mkdir -p ~/.open-auth-rotator/${PROVIDER}
# Create pool.json, swap_token.py, state.json
# Add watcher integration (scan pattern + swap trigger)
# Create CLI symlink: ln -sf ~/.open-auth-rotator/${PROVIDER}/swap_token.py ~/.local/bin/${PROVIDER}-swap
# Restart watcher: launchctl kickstart -k gui/$(id -u)/com.openantigravity.ratelimit-watcher
```

## Debugging Checklist

| Symptom | Cause | Fix |
|---------|-------|-----|
| Plugin loads but auth not available | Using `file://` path instead of npm name | Inject into `~/.cache/opencode/node_modules/` and use npm-style name |
| `404 Not Found` on npm registry | Plugin not published to npm | Expected warning — cache fallback works if plugin is in node_modules |
| `Plugin export is not a function` | Wrong export pattern | Must export async function as default, not an object |
| Provider not found in auth login | Plugin's `config` hook not registering provider | Check `config` hook sets `providers[PROVIDER_ID]` correctly |
| Token swap doesn't take effect | Not updating auth.json atomically | Use `os.replace()` pattern (atomic on POSIX) |
| Session restart required after swap | auth.json key doesn't match provider ID | Provider ID in plugin must match key in auth.json |
| `bun add` fails with 404 | Plugin not on npm | Add `cachedVersion` entry to `~/.cache/opencode/package.json` |

## Reference: Working Plugin Locations

| Plugin | Cache Path | Provider ID | Auth Type |
|--------|-----------|-------------|-----------|
| Antigravity | `~/.cache/opencode/node_modules/opencode-antigravity-auth/` | `google` | OAuth (Google) |
| Qwen | `~/.cache/opencode/node_modules/opencode-qwencode-auth/` | `qwen-code` | Device Flow |
| OpenRouter | `~/.cache/opencode/node_modules/opencode-openrouter-auth/` | `openrouter` | OAuth PKCE |

## Reference: SDK Compatibility

| Provider API Style | `npm` field in config | Notes |
|--------------------|-----------------------|-------|
| OpenAI-compatible | `@ai-sdk/openai-compatible` | Most providers (OpenRouter, DeepSeek, Mistral, Together, etc.) |
| Anthropic-compatible | `@ai-sdk/anthropic` | Direct Anthropic API |
| Google Generative AI | `@ai-sdk/google` | Gemini models |
| Custom | `@ai-sdk/openai-compatible` | Set `baseURL` in options |

## Anti-Patterns (NEVER DO)

1. **NEVER** use `file:///` for auth plugins — auth hooks silently won't activate
2. **NEVER** add a static provider block in `opencode.json` that conflicts with the plugin's `config` hook — the static block overrides the plugin
3. **NEVER** use `"main"` instead of `"module"` in package.json — Bun needs `"module"`
4. **NEVER** export non-function values — OpenCode expects `export default async (_input) => { ... }`
5. **NEVER** forget to set `"type": "module"` — ESM imports will fail
6. **NEVER** hardcode API keys in the plugin — use the `loader` hook with `getAuth()` to read from auth.json
7. **NEVER** update auth.json non-atomically — use temp file + `os.replace()` to prevent corruption during concurrent reads
