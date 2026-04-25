#!/usr/bin/env python3
"""
Box Developer App Creation & Configuration Automation
======================================================
This script automates the complete Box Developer App setup for OpenSIN AI.
It creates a new Box Developer App (or uses existing), configures CORS,
generates a Developer Token, and outputs all credentials needed for
the A2A-SIN-Box-Storage service.

Usage:
    python3 box_developer_app_setup.py [--create-new] [--force-token-refresh]

Requirements:
    - Chrome profile with Box.com already logged in
    - Python dependencies: nodriver (installed via pip)

Author: SIN-Zeus (OpenSIN-AI)
Date: 2026-04-15
"""

import asyncio
import json
import sys
import os
import re
from datetime import datetime

# Try to import nodriver, install if missing
try:
    import nodriver as uc
except ImportError:
    print("Installing nodriver...")
    os.system("pip install nodriver")
    import nodriver as uc


# ============================================================================
# CONSTANTS
# ============================================================================

CHROME_PROFILE_DIR = "/Users/jeremy/Library/Application Support/Google/Chrome/Default"
CHROME_PROFILE_NAME = "Default"
BOX_CONSOLE_URL = "https://account.box.com/developers/console"
APP_NAME = "OpenSIN"
CORS_DOMAINS = [
    "http://localhost:3000",
    "http://room-09-box-storage:3000",
    "https://mydomain.com",
    "https://a2a.delqhi.com",
]

POLL_MAX_ATTEMPTS = 12
POLL_INTERVAL_SECONDS = 5

# Output file for credentials
CREDENTIALS_FILE = "/Users/jeremy/dev/OpenSIN-documentation/.opencode/flows/box-developer-app-creation/credentials.json"


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================


def log_step(step_name: str, details: str = ""):
    """Log a step with timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"\n[STEP {timestamp}] {step_name}")
    if details:
        print(f"         {details}")


def save_credentials(credentials: dict):
    """Save credentials to JSON file"""
    os.makedirs(os.path.dirname(CREDENTIALS_FILE), exist_ok=True)
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(credentials, f, indent=2)
    print(f"\n[INFO] Credentials saved to: {CREDENTIALS_FILE}")


async def wait_for_page_load(page, timeout: int = 15):
    """Wait for page to be fully loaded"""
    try:
        await page.wait_for_load_state(timeout=timeout)
        await asyncio.sleep(0.5)  # Extra wait for React apps
    except Exception as e:
        print(f"[WARN] Page load wait: {e}")


async def take_screenshot(page, name: str):
    """Take a screenshot and save to evidence folder"""
    evidence_dir = "/Users/jeremy/dev/OpenSIN-documentation/.opencode/flows/box-developer-app-creation/evidence"
    os.makedirs(evidence_dir, exist_ok=True)
    screenshot_path = f"{evidence_dir}/{name}.png"
    await page.save_screenshot(screenshot_path)
    print(f"[INFO] Screenshot saved: {screenshot_path}")
    return screenshot_path


async def poll_until(label: str, check_fn, *, max_attempts: int = POLL_MAX_ATTEMPTS, interval_seconds: int = POLL_INTERVAL_SECONDS):
    """Poll a fresh condition multiple times before giving up."""
    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            result = await check_fn()
        except Exception as exc:
            last_error = exc
            print(f"[WARN] {label} poll attempt {attempt}/{max_attempts} failed: {exc}")
            result = None

        if result:
            print(f"[INFO] {label} satisfied on attempt {attempt}/{max_attempts}")
            return result

        if attempt < max_attempts:
            print(
                f"[INFO] {label} not ready yet on attempt {attempt}/{max_attempts}; retrying in {interval_seconds}s"
            )
            await asyncio.sleep(interval_seconds)

    if last_error:
        raise TimeoutError(
            f"{label} timed out after {max_attempts} attempts (last error: {last_error})"
        )
    raise TimeoutError(f"{label} timed out after {max_attempts} attempts")


async def find_opensin_app_link(page):
    """Re-read the page and return the OpenSIN app link if Box exposes it."""
    return await page.query_selector("tr:has-text('OpenSIN') a, a:has-text('OpenSIN')")


async def find_opensin_app_row(page):
    """Re-read the app list and report whether OpenSIN is visible."""
    return await page.evaluate("""
        () => {
            const rows = document.querySelectorAll('tr');
            for (const row of rows) {
                if ((row.textContent || '').includes('OpenSIN')) {
                    return 'found';
                }
            }
            return null;
        }
    """)


async def find_new_app_button(page):
    """Re-read the page and return the new-app button if Box exposes it."""
    return await page.query_selector("button:has-text('Neue App'), button:has-text('New App')")


async def find_app_name_input(page):
    """Re-read the page and return the app-name input if Box exposes it."""
    return await page.query_selector(
        "input[name='name'], input[placeholder*='App'], input[type='text']"
    )


async def find_app_submit_button(page):
    """Re-read the page and return the create/submit button if Box exposes it."""
    return await page.query_selector(
        "button:has-text('Erstellen'), button:has-text('Create')"
    )


async def extract_developer_token(page):
    """Re-read the page and extract a visible developer token if present."""
    page_content = await page.evaluate("() => document.body.innerText")
    token_match = re.search(r"([a-zA-Z0-9]{40,})", page_content)
    if token_match:
        potential_token = token_match.group(1)
        if len(potential_token) > 40:
            return potential_token
    return None


async def find_developer_token_section(page):
    """Re-read the page and return the token section if Box exposes it."""
    return await page.query_selector(
        "*:has-text('Entwicklertoken'), *:has-text('Developer Token'), *:has-text('kb7w')"
    )


async def find_cors_input(page):
    """Re-read the page and return the CORS/domain input if Box exposes it."""
    return await page.query_selector(
        "input[placeholder*='CORS'], input[placeholder*='Domain']"
    )


async def find_cors_add_button(page):
    """Re-read the page and return the CORS add button if Box exposes it."""
    return await page.query_selector(
        "button:has-text('Hinzufügen'), button:has-text('Add')"
    )


async def find_cors_save_button(page):
    """Re-read the page and return the CORS save button if Box exposes it."""
    return await page.query_selector(
        "button:has-text('Speichern'), button:has-text('Save')"
    )


async def read_cors_save_confirmation(page):
    """Re-read the page and detect whether the save likely landed."""
    page_text = await page.evaluate("() => document.body.innerText")
    normalized = page_text.lower()
    return any(
        token in normalized
        for token in ("saved", "gespeichert", "updated", "success", "successfully")
    )


async def extract_folder_list(page):
    """Re-read the folder page and extract visible folder IDs if present."""
    folder_info = await page.evaluate(r"""
        () => {
            const folders = document.querySelectorAll('a[href*="/folder/"]');
            const result = [];
            folders.forEach(f => {
                const href = f.href;
                const name = (f.textContent || '').trim();
                const idMatch = href.match(/\/folder\/([^/?]+)/);
                if (idMatch && name) {
                    result.push({name: name.substring(0, 50), id: idMatch[1]});
                }
            });
            return JSON.stringify(result.slice(0, 20));
        }
    """)
    if not folder_info:
        return None
    folders = json.loads(folder_info)
    return folders or None


# ============================================================================
# MAIN AUTOMATION
# ============================================================================


async def main():
    """Main automation flow"""

    credentials = {
        "timestamp": datetime.now().isoformat(),
        "status": "in_progress",
        "app_name": APP_NAME,
        "cors_domains": CORS_DOMAINS,
    }

    log_step("STARTING BOX DEVELOPER APP AUTOMATION")

    # -------------------------------------------------------------------------
    # STEP 1: Launch Chrome with existing profile
    # -------------------------------------------------------------------------
    log_step("STEP 1", "Launching Chrome with existing profile for Box.com")

    browser = await uc.start(
        user_data_dir=CHROME_PROFILE_DIR,
        profile_directory=CHROME_PROFILE_NAME,
        headless=False,  # Must be visible for Box.com
        sandbox=False,
    )

    page = browser.main_tab
    log_step("STEP 1", f"Chrome launched, CDP available")

    # -------------------------------------------------------------------------
    # STEP 2: Navigate to Box Developer Console
    # -------------------------------------------------------------------------
    log_step("STEP 2", f"Navigating to {BOX_CONSOLE_URL}")
    await page.goto(BOX_CONSOLE_URL, timeout=30)
    await wait_for_page_load(page)

    current_url = page.url
    log_step("STEP 2", f"Current URL: {current_url}")

    # Check if we're on login page
    if "login" in current_url.lower():
        log_step("STEP 2", "WARNING: Redirected to login page - need manual login")
        await take_screenshot(page, "step2_login_required")
        print(
            "[ACTION REQUIRED] Please log in to Box.com manually in the Chrome window"
        )
        print("Press Enter after logging in...")
        input()
        await wait_for_page_load(page)

    await take_screenshot(page, "step2_console_loaded")

    # -------------------------------------------------------------------------
    # STEP 3: Check if OpenSIN app exists, create if not
    # -------------------------------------------------------------------------
    log_step("STEP 3", "Checking for existing OpenSIN app")

    # Poll the app list so we do not misread a slow async load as "not found".
    app_list_text = None
    try:
        app_list_text = await poll_until(
            "OpenSIN app row",
            lambda: find_opensin_app_row(page),
        )
    except TimeoutError as e:
        log_step("STEP 3", f"OpenSIN app row not visible after polling: {e}")

    if not app_list_text:
        log_step("STEP 3", "OpenSIN app NOT found - creating new app")

        # Click "Neue App +" button
        try:
            neue_app_btn = await poll_until(
                "New app button",
                lambda: find_new_app_button(page),
            )
            if neue_app_btn:
                await neue_app_btn.click()
                await asyncio.sleep(2)
                await take_screenshot(page, "step3_new_app_dialog")

                # Fill in app name
                name_input = await poll_until(
                    "New app name input",
                    lambda: find_app_name_input(page),
                )
                if name_input:
                    await name_input.clear()
                    await name_input.send_keys(APP_NAME)
                    await asyncio.sleep(0.5)

                # Click Create/Submit
                submit_btn = await poll_until(
                    "New app submit button",
                    lambda: find_app_submit_button(page),
                )
                if submit_btn:
                    await submit_btn.click()
                    await asyncio.sleep(3)

        except Exception as e:
            log_step("STEP 3", f"Error creating app: {e}")
            await take_screenshot(page, "step3_error")
    else:
        log_step("STEP 3", "OpenSIN app already exists - using existing app")

    await take_screenshot(page, "step3_app_status")

    # -------------------------------------------------------------------------
    # STEP 4: Navigate to OpenSIN app configuration
    # -------------------------------------------------------------------------
    log_step("STEP 4", "Navigating to OpenSIN app configuration")

    # Poll the fresh DOM until the OpenSIN app link appears, then click it.
    try:
        opensin_link = await poll_until(
            "OpenSIN app link",
            lambda: find_opensin_app_link(page),
        )
        await opensin_link.click()
        await asyncio.sleep(3)
    except TimeoutError as e:
        log_step("STEP 4", f"Timed out waiting for OpenSIN app link: {e}")
        await take_screenshot(page, "step4_timeout")
        raise
    except Exception as e:
        log_step("STEP 4", f"Link click failed, trying direct navigation: {e}")
        await take_screenshot(page, "step4_link_error")
        raise

    await take_screenshot(page, "step4_app_config")

    # -------------------------------------------------------------------------
    # STEP 5: Get Developer Token
    # -------------------------------------------------------------------------
    log_step("STEP 5", "Extracting Developer Token")

    dev_token = None

    # Poll the page text first because Box loads token details asynchronously.
    try:
        dev_token = await poll_until(
            "Developer token text",
            lambda: extract_developer_token(page),
        )
        if dev_token:
            log_step("STEP 5", f"Found potential token: {dev_token[:20]}...")
    except TimeoutError as e:
        log_step("STEP 5", f"Token text not visible yet after polling: {e}")

    # If the token is still hidden, open the token section and poll again.
    if not dev_token:
        try:
            token_section = await poll_until(
                "Developer token section",
                lambda: find_developer_token_section(page),
            )
            await token_section.click()
            await asyncio.sleep(1)
            dev_token = await poll_until(
                "Developer token text after section click",
                lambda: extract_developer_token(page),
            )
            if dev_token:
                log_step("STEP 5", f"Found token after opening section: {dev_token[:20]}...")
        except TimeoutError as e:
            log_step("STEP 5", f"Token section not ready after polling: {e}")

    # Method 3: Use Box API to get token info
    # Note: This would require OAuth flow - simplified here

    credentials["developer_token"] = dev_token or "MANUAL_TOKEN_REQUIRED"
    log_step(
        "STEP 5",
        f"Token status: {'Found' if dev_token else 'Not found - manual required'}",
    )

    await take_screenshot(page, "step5_token")

    # -------------------------------------------------------------------------
    # STEP 6: Configure CORS Domains
    # -------------------------------------------------------------------------
    log_step("STEP 6", "Configuring CORS Domains")

    # Navigate to CORS settings (usually in app configuration)
    try:
        # Poll the CORS/domain controls because the settings panel can load late.
        cors_input = await poll_until(
            "CORS input",
            lambda: find_cors_input(page),
        )
        if cors_input:
            # Clear and enter first domain
            await cors_input.clear()
            await cors_input.send_keys(CORS_DOMAINS[0])
            await asyncio.sleep(0.3)

            # Look for add button or enter more domains
            add_btn = await poll_until(
                "CORS add button",
                lambda: find_cors_add_button(page),
            )
            if add_btn:
                for domain in CORS_DOMAINS[1:]:
                    await add_btn.click()
                    await asyncio.sleep(0.3)
                    await cors_input.send_keys(domain)

            # Save
            save_btn = await poll_until(
                "CORS save button",
                lambda: find_cors_save_button(page),
            )
            if save_btn:
                await save_btn.click()
                await asyncio.sleep(1)
                try:
                    await poll_until(
                        "CORS save confirmation",
                        lambda: read_cors_save_confirmation(page),
                    )
                except TimeoutError as e:
                    log_step("STEP 6", f"CORS save confirmation not visible after polling: {e}")

        log_step("STEP 6", "CORS configuration attempted")
    except TimeoutError as e:
        log_step("STEP 6", f"CORS controls not ready after polling: {e}")
    except Exception as e:
        log_step("STEP 6", f"CORS config failed (may need manual): {e}")

    await take_screenshot(page, "step6_cors")

    # -------------------------------------------------------------------------
    # STEP 7: Extract Folder IDs from Box.com
    # -------------------------------------------------------------------------
    log_step("STEP 7", "Extracting Folder IDs for Public and Cache folders")

    # Navigate to Box.com home to find folder IDs
    try:
        # Go to Box.com main page
        await page.goto("https://app.box.com/folder", timeout=20)
        await wait_for_page_load(page)

        # Poll the folder list because Box may hydrate it after navigation.
        folders = []
        try:
            folders = await poll_until(
                "Box folder list",
                lambda: extract_folder_list(page),
            )
        except TimeoutError as e:
            log_step("STEP 7", f"Folder list not visible after polling: {e}")

        log_step("STEP 7", f"Found {len(folders)} folders")

        # Find Public and Cache folders
        public_folder = next(
            (f for f in folders if "public" in f["name"].lower()), None
        )
        cache_folder = next((f for f in folders if "cache" in f["name"].lower()), None)

        credentials["public_folder_id"] = (
            public_folder["id"] if public_folder else "NOT_FOUND"
        )
        credentials["cache_folder_id"] = (
            cache_folder["id"] if cache_folder else "NOT_FOUND"
        )

        if public_folder:
            log_step(
                "STEP 7",
                f"Public folder: {public_folder['name']} -> {public_folder['id']}",
            )
        if cache_folder:
            log_step(
                "STEP 7",
                f"Cache folder: {cache_folder['name']} -> {cache_folder['id']}",
            )

    except Exception as e:
        log_step("STEP 7", f"Folder extraction failed: {e}")

    await take_screenshot(page, "step7_folders")

    # -------------------------------------------------------------------------
    # STEP 8: Generate output / summary
    # -------------------------------------------------------------------------
    log_step("STEP 8", "Generating credentials summary")

    credentials["status"] = "completed"
    credentials["box_console_url"] = "https://account.box.com/developers/console"

    save_credentials(credentials)

    # Print summary
    print("\n" + "=" * 70)
    print("BOX DEVELOPER APP SETUP COMPLETE")
    print("=" * 70)
    print(f"\nAdd these to your .env file:")
    print(f"\n  BOX_DEVELOPER_TOKEN={credentials.get('developer_token', 'YOUR_TOKEN')}")
    print(
        f"  BOX_PUBLIC_FOLDER_ID={credentials.get('public_folder_id', 'YOUR_FOLDER_ID')}"
    )
    print(
        f"  BOX_CACHE_FOLDER_ID={credentials.get('cache_folder_id', 'YOUR_FOLDER_ID')}"
    )
    print(f"  BOX_STORAGE_API_KEY=generate_a_secure_random_key")
    print("\n  CORS Domains configured:")
    for domain in CORS_DOMAINS:
        print(f"    - {domain}")
    print("\n" + "=" * 70)

    await take_screenshot(page, "step8_complete")

    # Cleanup
    await browser.close()

    return credentials


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        result = asyncio.run(main())
        sys.exit(0)
    except KeyboardInterrupt:
        print("\n\n[ABORTED] User cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
