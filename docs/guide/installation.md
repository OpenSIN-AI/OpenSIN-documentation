---
title: Installation
description: Install OpenSIN on your system
---

# Installation

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git (for version control)

## Install via pip

```bash
pip install opensin-cli
```

## Install from Source

```bash
git clone https://github.com/OpenSIN-AI/OpenSIN.git
cd OpenSIN
pip install -e .
```

## Configure Environment

Create a `.env` file in your project directory:

```bash
# LLM Provider API Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# OpenSIN Configuration
OPENSIN_BASE_URL=https://api.opensin.ai
OPENSIN_LOG_LEVEL=INFO
```

## Verify Installation

```bash
opensin --version
opensin health
```

## Next Steps

- [Quick Start](/guide/quick-start) — Build your first agent
- [Getting Started](/guide/getting-started) — Overview of OpenSIN
