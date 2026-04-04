# Create GitHub App

> Automate GitHub App creation for OpenSIN organization using browser automation.

## Purpose

Create GitHub Apps programmatically using webauto-nodriver browser automation. This skill automates the GitHub App creation flow that normally requires manual UI interaction.

## Prerequisites

- webauto-nodriver MCP server running on http://localhost:8765/mcp
- Chrome logged into GitHub account with admin access to target organization
- `anonymous` skill loaded for browser automation tools

## Usage

When the user asks to create a GitHub App, follow these steps:

### 1. Prepare App Configuration

Gather required information:
- **App name**: e.g., `opnsin-code`
- **Homepage URL**: e.g., `https://opensin.ai`
- **Webhook URL**: e.g., `http://92.5.60.87:5678/webhook/github`
- **Webhook secret**: Generate random secret
- **Callback URL**: e.g., `https://opensin.ai/auth/callback`
- **Permissions**: Issues (RW), Pull Requests (RW), Metadata (R), Contents (R)
- **Events**: issues, issue_comment, pull_request, pull_request_review
- **Organization**: Target org for installation

### 2. Browser Automation Flow

```python
# Step 1: Navigate to GitHub Apps settings
goto({"url": "https://github.com/settings/apps/new"})

# Step 2: Fill form fields
# GitHub App name
observe_screen()  # Find coordinates
click({"x": <name_field_x>, "y": <name_field_y>})
type_text({"text": "opnsin-code"})

# Homepage URL
press_key({"key": "Tab"})
type_text({"text": "https://opensin.ai"})

# Webhook URL (expand webhook section first)
press_key({"key": "Tab"})
press_key({"key": "Tab"})  # Navigate to webhook checkbox
press_key({"key": "Space"})  # Check webhook
press_key({"key": "Tab"})  # Move to webhook URL field
type_text({"text": "http://92.5.60.87:5678/webhook/github"})

# Webhook secret
press_key({"key": "Tab"})
type_text({"text": "<random-secret>"})

# Step 3: Configure permissions
# Scroll to permissions section
press_key({"key": "PageDown"})

# Repository permissions
# Use observe_screen to find permission toggles and click them

# Step 4: Subscribe to events
# Use observe_screen to find event checkboxes

# Step 5: Create the app
# Scroll to bottom and click "Create GitHub App"
observe_screen()
click({"x": <create_button_x>, "y": <create_button_y>})

# Step 6: Extract App ID and Client ID
# After creation, scrape the app settings page
observe_screen({"include_dom": "true"})
```

### 3. Post-Creation Steps

After app is created:
1. **Generate Private Key**: Navigate to app settings → Private keys → Generate
2. **Install in Organization**: Navigate to app settings → Install App → Select org
3. **Save Credentials**: Store App ID, Client ID, Client Secret, Private Key in sin-passwordmanager

## Best Practices

- Always use `observe_screen()` before clicking to get current page state
- Use DOM analysis to find form fields precisely
- Add delays between actions (GitHub has rate limiting)
- Take screenshots at each major step for debugging
- Handle GitHub's 2FA if prompted

## Error Handling

| Error | Recovery |
|-------|----------|
| Form validation error | Read error message, fix field, retry |
| Rate limit | Wait 60 seconds, retry |
| 2FA required | Prompt user for 2FA code |
| App name taken | Suggest alternative name |

## Example

User: "Create a GitHub App called @opnsin-code for OpenSIN-AI"

Agent:
1. Navigate to https://github.com/settings/apps/new
2. Fill form with app details
3. Configure permissions and events
4. Submit form
5. Generate private key
6. Install in OpenSIN-AI organization
7. Save credentials to password manager
