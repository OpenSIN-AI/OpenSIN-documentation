# OpenSIN-Code — Setup Guide

> **Repository:** OpenSIN-Code | **Category:** Setup

## Prerequisites

- Node.js 18+
- Python 3.11+
- Git
- OpenCode CLI

## Installation

```bash
git clone git@github.com:OpenSIN-AI/OpenSIN-Code.git
cd OpenSIN-Code
npm install  # or pip install -r requirements.txt
```

## Configuration

```bash
cp .env.example .env
# Edit .env with your credentials
```

## Running

```bash
npm run dev  # or python -m opensin_code
```

## Testing

```bash
npm test  # or pytest
```

## Deployment

```bash
npm run build
npm run deploy
```

---

*Last updated: 2026-04-04 by SIN-Zeus*
