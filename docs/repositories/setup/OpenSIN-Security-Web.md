# OpenSIN-Security-Web — Setup Guide

> **Repository:** OpenSIN-Security-Web | **Category:** Setup

## Prerequisites

- Node.js 18+
- Python 3.11+
- Git
- OpenCode CLI

## Installation

```bash
git clone git@github.com:OpenSIN-AI/OpenSIN-Security-Web.git
cd OpenSIN-Security-Web
npm install  # or pip install -r requirements.txt
```

## Configuration

```bash
cp .env.example .env
# Edit .env with your credentials
```

## Running

```bash
npm run dev  # or python -m opensin_security_web
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
