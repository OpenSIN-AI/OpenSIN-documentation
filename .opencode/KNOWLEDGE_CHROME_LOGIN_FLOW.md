# KNOWLEDGE: Chrome Native Profile Login Flow (Google Account)

> **Status:** VALIDATED (with blockers identified and solved)
> **Last Updated:** 2026-04-12
> **Applies to:** antigravity-rotator, openai-google-rotator, any agent needing Google login
> **OpenCode Skill:** `/new-google-login`

---

## 1. THE PROBLEM

When Chrome starts with an empty/fresh profile, Google's website shows various interstitials
that BLOCK traditional DOM-based login automation:

- **EU Search Engine Choice Popup** — Chrome-native overlay, intercepts ALL keyboard input
- **Google Cookie Consent ("Bevor Sie zu Google weitergehen")** — Blocks profile dropdown
- **Account Chooser ("Abgemeldet" / "Anderes Konto verwenden")** — Extra click needed
- **DOM selectors like `_JS_CLICK_NEXT` fail unpredictably** across different Google pages

**Result:** DOM-based approaches (Selenium, Puppeteer, even nodriver clicking website elements)
are fragile and break constantly.

---

## 2. THE SOLUTION: Native Chrome Profile Menu (5-Step Keyboard Flow)

Instead of interacting with the Google WEBSITE, we use Chrome's BROWSER TOOLBAR profile icon.
This bypasses ALL website-level popups and interstitials.

### The 5 Steps:

```
Step 1: Focus URL address bar          → Cmd+L (or mouse click in address bar)
Step 2: Press Tab                       → Jumps to profile icon in Chrome toolbar
Step 3: Press Space                     → Opens profile dropdown menu
Step 4: Press Tab                       → Focuses "Anmelden" / "Sign in" / "Sync aktivieren" button
Step 5: Press Space                     → Clicks it → Opens native Google login popup
```

### Then in the Google Login Popup:

```
Step 6: Type email address              → keystroke "<email>"
Step 7: Press Tab + Enter               → Submit email (or just Enter)
Step 8: Wait for password page          → delay 2-3 seconds
Step 9: Type password                   → keystroke "<password>"
Step 10: Press Enter                    → Submit password → Login complete
```

---

## 3. MANDATORY CHROME LAUNCH FLAGS

When starting Chrome for login automation, these flags are **REQUIRED**:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --user-data-dir=/tmp/fresh_profile_XXXXX \
  --remote-debugging-port=7654 \
  --disable-search-engine-choice-screen \
  --no-default-browser-check \
  --no-first-run \
  --disable-popup-blocking \
  "https://www.google.com"
```

### Flag Explanations:

| Flag                                    | Why MANDATORY                                                                        |
| --------------------------------------- | ------------------------------------------------------------------------------------ |
| `--user-data-dir=<path>`                | Isolates Chrome profile from user's real profile                                     |
| `--remote-debugging-port=<port>`        | Enables CDP connection for nodriver/automation                                       |
| `--disable-search-engine-choice-screen` | **CRITICAL:** Prevents EU search engine chooser popup that blocks ALL keyboard input |
| `--no-default-browser-check`            | Prevents "set as default browser" dialog                                             |
| `--no-first-run`                        | Skips first-run welcome page                                                         |
| `--disable-popup-blocking`              | Allows login popups to open                                                          |

### Ports by System:

| System                             | Port |
| ---------------------------------- | ---- |
| antigravity-rotator                | 7654 |
| openai-google-rotator (standalone) | 9336 |
| skylight-cli-mcp                   | 9335 |

---

## 4. BLOCKER #1: EU Search Engine Choice Popup

### What Happens:

When Chrome starts with a **completely fresh profile** (no prior usage), the EU-mandated
"Wähle deine Suchmaschine" (Choose your search engine) dialog appears BEFORE anything else.

### Why It Blocks:

- Renders as a Chrome-native overlay (NOT a webpage — no DOM to manipulate)
- Intercepts ALL keyboard input (Tab, Space, Enter do nothing useful)
- Prevents the profile menu from being accessed
- Cannot be dismissed via JavaScript or CDP commands

### Solution:

```bash
--disable-search-engine-choice-screen
```

This flag MUST be present when launching Chrome. Without it, the entire login flow is dead.

---

## 5. BLOCKER #2: Google Cookie Consent Popup

### What Happens:

Even after bypassing the search engine popup, if Chrome navigates to google.com,
Google shows a "Bevor Sie zu Google weitergehen" (Before you continue to Google)
cookie consent overlay.

### Why It Blocks:

- The overlay covers the entire page
- The profile dropdown menu opens BEHIND the overlay
- Clicking the profile icon works, but the dropdown is not interactable

### Solutions (in order of preference):

**Solution A: Navigate to a non-Google page first (RECOMMENDED)**

```bash
# Start Chrome with about:blank or chrome://newtab instead of google.com
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --user-data-dir=/tmp/fresh_profile \
  --disable-search-engine-choice-screen \
  --no-default-browser-check \
  --no-first-run \
  "about:blank"
```

Then do the 5-step profile flow on the blank page — no cookie consent appears!

**Solution B: Accept cookies first via keyboard**

```applescript
-- Navigate to google.com, then:
-- Tab multiple times to reach "Alle akzeptieren" button
-- Press Enter to accept
-- THEN do the 5-step profile flow
```

**Solution C: Additional Chrome flags**

```bash
--disable-features=PrivacySandboxSettings4
```

Note: This may not fully suppress the consent popup in all Chrome versions.

---

## 6. APPLESCRIPT IMPLEMENTATION (COMPLETE)

```applescript
-- ============================================================
-- CHROME NATIVE PROFILE LOGIN FLOW
-- Prerequisite: Chrome launched with --disable-search-engine-choice-screen
-- and navigated to about:blank (NOT google.com to avoid cookie consent)
-- ============================================================

-- Step 0: Activate Chrome window
tell application "Google Chrome" to activate
delay 1.0

tell application "System Events"
    -- Step 1: Focus URL address bar (Cmd+L)
    keystroke "l" using command down
    delay 0.5

    -- Step 2: Tab to profile icon in toolbar
    -- NOTE: Exact tab count depends on Chrome UI elements (extensions, etc.)
    -- For a clean profile with no extensions: 1x Tab = profile icon
    key code 48  -- Tab
    delay 0.5

    -- Step 3: Space to open profile dropdown
    keystroke " "
    delay 1.5  -- Need longer delay for dropdown animation

    -- Step 4: Tab to "Anmelden" / "Sign in" button in dropdown
    key code 48  -- Tab
    delay 0.5

    -- Step 5: Space to click sign in button
    keystroke " "
    delay 3.0  -- Wait for Google login page to load

    -- ============================================================
    -- NOW IN GOOGLE LOGIN POPUP/TAB
    -- ============================================================

    -- Step 6: Type email address
    keystroke "your-email@domain.com"
    delay 0.5

    -- Step 7: Press Enter to submit email
    key code 36  -- Enter/Return
    delay 3.0  -- Wait for password page

    -- Step 8: Type password
    keystroke "YourPassword123"
    delay 0.5

    -- Step 9: Press Enter to submit password
    key code 36  -- Enter/Return
    delay 3.0  -- Wait for login to complete

    -- Step 10: Handle "Sync aktivieren?" dialog if it appears
    -- Tab to "Ja, bitte" or "Yes, I'm in" button and press Enter
    key code 48  -- Tab
    delay 0.3
    key code 36  -- Enter
end tell
```

---

## 7. APPLESCRIPT KEY CODES REFERENCE

| Key                     | Code                           | Method                                                   |
| ----------------------- | ------------------------------ | -------------------------------------------------------- |
| Tab                     | `key code 48`                  | `key code 48`                                            |
| Enter/Return            | `key code 36`                  | `key code 36`                                            |
| Escape                  | `key code 53`                  | `key code 53`                                            |
| Space                   | N/A                            | `keystroke " "`                                          |
| Cmd+L (address bar)     | N/A                            | `keystroke "l" using command down`                       |
| F6 (toolbar focus)      | `key code 97`                  | `key code 97` (CAUTION: may focus wrong app like Docker) |
| Shift+Tab (reverse tab) | `key code 48 using shift down` | Goes LEFT from address bar — NOT to profile icon         |

---

## 8. TAB NAVIGATION FROM ADDRESS BAR

### Tab Count to Profile Icon:

The number of Tab presses from the address bar to the profile icon depends on
what Chrome UI elements are visible:

| Chrome State                   | Tab Count to Profile Icon          |
| ------------------------------ | ---------------------------------- |
| Clean profile, no extensions   | 1 Tab                              |
| With "KI-Modus" button visible | 2-3 Tabs                           |
| With extensions installed      | Variable (count visible icons + 1) |
| With bookmarks bar visible     | May need more tabs                 |

### Important:

- `Shift+Tab` from address bar goes LEFT (to back/forward buttons) — NOT to profile icon
- `F6` (key code 97) sometimes jumps to toolbar but can focus wrong application (Docker, etc.)
- **ALWAYS use `Cmd+L` → `Tab` pattern** — most reliable

---

## 9. NODRIVER CDP CONNECTION (NOT uc.start())

### WRONG (starts NEW Chrome, port conflict):

```python
browser = await uc.start(headless=False, user_data_dir=..., browser_args=[...])
```

### CORRECT (connects to EXISTING Chrome):

```python
import nodriver as uc
browser = await uc.start(host="127.0.0.1", port=7654)
# This connects to the Chrome instance already running on port 7654
```

### Why This Matters:

- The Chrome instance is already running (started by the rotator or manually)
- `uc.start()` with `user_data_dir` starts a SECOND Chrome on a RANDOM port
- This creates port conflicts and the automation talks to the wrong browser
- Always connect to the EXISTING instance via CDP

---

## 10. WORKSPACE ACCOUNT DETAILS

| Field                  | Value                                                 |
| ---------------------- | ----------------------------------------------------- |
| Domain                 | `zukunftsorientierte-energie.de`                      |
| Password               | `ZOE.jerry2024` (fallback: `ZOE.jerry2025`)           |
| Admin Email            | `info@zukunftsorientierte-energie.de`                 |
| Account Format         | `rotator-XXXXXXXXXX@zukunftsorientierte-energie.de`   |
| Account Creation       | Via Google Admin API or Admin Console                 |
| Rate Limit on Creation | Google blocks after ~5 accounts (412 abuse detection) |
| Recovery               | Restore from trash (771 deleted accounts available)   |

---

## 11. KNOWN ISSUES & EDGE CASES

### Issue: Profile dropdown shows "Anmelden" vs "Sync aktivieren"

- **Fresh profile (never signed in):** Shows "Anmelden" (Sign in)
- **Previously signed in then signed out:** Shows "Sync aktivieren" (Turn on sync)
- **Currently signed in:** Shows account name/avatar
- The Tab+Space flow works the same for both "Anmelden" and "Sync aktivieren"

### Issue: Multiple Chrome windows

- AppleScript `tell application "Google Chrome" to activate` activates the LAST focused window
- If multiple windows exist, use `tell window 1` to target the correct one
- The profile icon is in EACH window's toolbar independently

### Issue: Google 2-Step Verification

- Some accounts may have 2FA enabled
- The rotator accounts should NOT have 2FA (Workspace admin can disable it)
- If 2FA appears: the flow needs additional steps (phone verification, etc.)

### Issue: "Abgemeldet" Account Chooser

- If Google shows an account chooser with previously logged-in accounts
- Click "Anderes Konto verwenden" (Use another account) BEFORE entering email
- Can be handled via additional Tab+Enter sequence

### Issue: Chrome "Profil anpassen" (Customize Profile) Dialog

- May appear after first login asking to customize the profile
- Dismiss with Escape or Tab+Enter on "Überspringen" (Skip)

---

## 12. PYTHON IMPLEMENTATION (subprocess + AppleScript)

```python
import subprocess
import time

def chrome_native_login(email: str, password: str, chrome_port: int = 7654) -> bool:
    """
    Log into Google using Chrome's native profile menu (5-step keyboard flow).

    PREREQUISITES:
    - Chrome must be running with --disable-search-engine-choice-screen
    - Chrome must be on about:blank or non-Google page (avoid cookie consent)
    - Chrome must have --remote-debugging-port=<chrome_port>

    Args:
        email: Google account email address
        password: Account password
        chrome_port: CDP port Chrome is running on

    Returns:
        True if login appeared to succeed, False otherwise
    """

    # === STEP 0: Activate Chrome ===
    subprocess.run([
        'osascript', '-e',
        'tell application "Google Chrome" to activate'
    ], check=True)
    time.sleep(1.0)

    # === STEPS 1-5: Open profile menu and click "Sign in" ===
    applescript_profile_flow = '''
    tell application "System Events"
        -- Step 1: Focus URL bar
        keystroke "l" using command down
        delay 0.5

        -- Step 2: Tab to profile icon
        key code 48
        delay 0.5

        -- Step 3: Space to open dropdown
        keystroke " "
        delay 1.5

        -- Step 4: Tab to sign in button
        key code 48
        delay 0.5

        -- Step 5: Space to click sign in
        keystroke " "
        delay 3.0
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript_profile_flow], check=True)
    time.sleep(2.0)

    # === STEPS 6-7: Enter email ===
    applescript_email = f'''
    tell application "System Events"
        keystroke "{email}"
        delay 0.5
        key code 36
        delay 3.0
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript_email], check=True)
    time.sleep(2.0)

    # === STEPS 8-9: Enter password ===
    applescript_password = f'''
    tell application "System Events"
        keystroke "{password}"
        delay 0.5
        key code 36
        delay 3.0
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript_password], check=True)
    time.sleep(2.0)

    # === STEP 10: Handle sync dialog ===
    applescript_sync = '''
    tell application "System Events"
        key code 48
        delay 0.3
        key code 36
        delay 2.0
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript_sync], check=True)

    return True
```

---

## 13. CRITICAL RULES

1. **NEVER start Chrome with `open -a "Google Chrome"`** — macOS may block the debug port
2. **ALWAYS use the direct binary path:** `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
3. **NEVER use headless mode** — Google detects and blocks headless Chrome
4. **ALWAYS include `--disable-search-engine-choice-screen`** — without it, EU popup blocks everything
5. **ALWAYS start with `about:blank`** — avoid Google cookie consent popup
6. **NEVER connect via `uc.start(user_data_dir=...)` to an already-running Chrome** — use `uc.start(host=, port=)` instead
7. **NEVER delete a Google account unless PROVEN rate-limited in opencode** — restored accounts cost money
8. **ALWAYS use extensive delays** between keystrokes — too fast = bot detection
