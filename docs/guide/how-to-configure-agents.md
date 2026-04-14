# 📋 How to Configure New Agents (A2A v5)

> **Target Audience:** Admins & Developers adding new agents to the OpenSIN-AI fleet.
> **Version:** 5.0.0 (April 2026)

## 1. Define the Agent
Determine the agent's name, team, and role.

```
Name: A2A-SIN-New-Agent
Team: Team Coding
Type: Coder Agent
```

## 2. Register in oh-my-sin.json
Open `oh-my-sin.json` and add the agent to its team's `members` array.

```json
"teams": {
    "team-code": {
        "name": "Team Coding",
        "members": ["...existing...", "A2A-SIN-New-Agent"]
    }
}
```

## 3. Run the Ultimate Skill
Use the `/create-a2a-sin-agent` skill in OpenCode.

```bash
/create-a2a-sin-agent
# Follow prompts for name, team, and capabilities
```

This will automatically generate:
- `agent.json` (with marketplace metadata)
- `A2A-CARD.md` (for discovery)
- `config/telegram-bot.yaml`
- `config/hf-space.yaml`
- `governance/*.json` (security and workflow rules)
- `Dockerfile` (production ready)

## 4. Update n8n Workflows
If this is a new Team, run the n8n workflow generator script:

```bash
python3 scripts/generate-n8n-workflows.py
# Import the resulting JSON into n8n via CLI or UI
```

## 5. Deploy to HF Space
The skill generates a space in `/tmp/hf-space-packages/<slug>`.

```bash
cd /tmp/hf-space-packages/a2a-sin-new-agent
hf repo create delqhi/a2a-sin-new-agent --type space
git push origin main
```

## 6. Verify Live Status
Check `http://92.5.60.87:8006` (Supabase) to ensure the agent is listed in the `agents` table.
