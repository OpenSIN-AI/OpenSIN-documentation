# Hugging Face Fleet Keep-Alive

To ensure that our A2A agents and MCP servers hosted on Hugging Face (HF) Spaces remain active and do not fall into sleep mode (Free Tier), we implement a centralized **Keep-Alive Pinger** via n8n.

## Architecture

1.  **n8n Workflow:** A scheduled workflow running on our OCI VM.
2.  **Frequency:** Every **45 minutes**.
3.  **Target:** Every HF Space URL in the OpenSIN-AI fleet.
4.  **Endpoint:** `https://<space-name>.hf.space/health`

## Covered Agents (as of April 2026)

| Agent | Purpose |
| :--- | :--- |
| **openjerro-opensin-bridge-mcp** | Prolific Bridge / Chrome Extension Bridge |
| **delqhi-sin-authenticator** | Fleet Auth & OTP |
| **delqhi-sin-github-issues** | Autonomous Issue Management |
| **delqhi-sin-stripe** | SaaS Billing & Payments |
| **delqhi-sin-passwordmanager** | Secure Credential Storage |
| **delqhi-sin-code-ai** | Autonomous Coding Engine |
| **10+ Frontend Agents** | Accessibility, App-Shell, Commerce-UI, etc. |

## How to add a new Space

1.  Locate the workflow in `OpenSIN-backend/n8n-workflows/hf-keepalive.json`.
2.  Add the new HF URL to the `Full HF Fleet List` node.
3.  Commit and push to the backend repository.
4.  The OCI CI Runner will automatically update the production workflow.

---
*Note: This mechanism is essential for the reliability of the OpenSIN Bridge SaaS.*
