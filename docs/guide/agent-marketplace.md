# Agent Marketplace

Discover, share, and monet AI agents in the OpenSIN ecosystem.

## Overview

The OpenSIN Agent Marketplace is a centralized platform where developers can:

- **Discover** pre-built agents for common tasks
- **Share** their own agents with the community
- **Monetize** premium agents
- **Rate & Review** agents

## Browsing Agents

### Categories

| Category | Description | Count |
|----------|-------------|-------|
| Research | Research and analysis agents | 15+ |
| Writing | Content creation agents | 20+ |
| Coding | Development agents | 12+ |
| Marketing | Social media and SEO agents | 18+ |
| Support | Customer service agents | 8+ |
| Data | Analysis and visualization agents | 10+ |
| Business | Operations and strategy agents | 14+ |
| Education | Teaching and tutoring agents | 6+ |

### Search & Filter

```bash
# Search agents
opensin marketplace search "research"

# Filter by category
opensin marketplace list --category research

# Filter by rating
opensin marketplace list --min-rating 4.5

# Filter by price
opensin marketplace list --free-only
opensin marketplace list --premium
```

## Installing Agents

### From CLI

```bash
# Install a free agent
opensin marketplace install researcher-pro

# Install a premium agent
opensin marketplace install writer-premium --purchase

# List installed agents
opensin marketplace installed
```

### From Code

```python
from opensin.marketplace import Marketplace

marketplace = Marketplace()

# Search agents
agents = marketplace.search("research", category="research")

# Install agent
agent = marketplace.install("researcher-pro")

# Use installed agent
result = await agent.send("Research AI trends")
```

## Publishing Agents

### Prepare Your Agent

```python
# agent.py
from opensin import Agent
from opensin.marketplace import AgentManifest

manifest = AgentManifest(
    name="my-researcher",
    version="1.0.0",
    description="Advanced research agent with web search capabilities",
    author="Your Name",
    category="research",
    tags=["research", "analysis", "web-search"],
    license="MIT",
    price=0,  # 0 = free, >0 = premium (USD/month)
    requirements=["opensin-sdk>=1.0", "requests"],
    tools=["web_search", "summarizer"],
    system_prompt="You are an expert researcher..."
)

agent = Agent(
    name="my-researcher",
    model="gpt-4",
    manifest=manifest
)
```

### Publish to Marketplace

```bash
# Package agent
opensin marketplace package ./my-agent

# Publish
opensin marketplace publish ./my-agent-package.tar.gz

# Update existing agent
opensin marketplace update ./my-agent
```

### Marketplace Listing

Your listing includes:
- Agent name and description
- Category and tags
- Screenshots and demos
- Pricing (free or premium)
- Reviews and ratings
- Installation count
- Documentation

## Monetization

### Pricing Tiers

| Tier | Price | Features |
|------|-------|----------|
| Free | $0 | Basic functionality |
| Starter | $5/mo | Enhanced features |
| Pro | $15/mo | Full features + priority |
| Enterprise | Custom | Custom solutions |

### Revenue Share

- **Developer:** 80% of revenue
- **OpenSIN Platform:** 20% of revenue
- **Payout:** Monthly via Stripe

### Analytics Dashboard

Track your agent's performance:
- Installation count
- Active users
- Revenue
- Ratings and reviews
- Usage statistics

## Quality Standards

### Submission Requirements

- [ ] Clear description and documentation
- [ ] Working code examples
- [ ] Test coverage > 80%
- [ ] Security review passed
- [ ] Performance benchmarks met
- [ ] No hardcoded secrets
- [ ] Proper error handling

### Review Process

1. **Automated Checks** — Code quality, security, tests
2. **Manual Review** — Documentation, functionality
3. **Approval** — Published to marketplace
4. **Monitoring** — Ongoing quality checks

## Best Practices

1. **Clear naming** — Use descriptive agent names
2. **Good documentation** — Include usage examples
3. **Error handling** — Handle edge cases gracefully
4. **Security** — Never expose secrets
5. **Performance** — Optimize for speed and cost
6. **Updates** — Keep agents up to date
7. **Support** — Respond to user feedback

## Next Steps

- [Agent Basics](/guide/agent-basics)
- [Custom Agents](/tutorials/custom-agents)
- [Best Practices](/best-practices/agent-design)
