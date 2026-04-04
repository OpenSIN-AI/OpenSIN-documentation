# OCI VM Setup Guide

> **Status:** ✅ Active | **Type:** Infrastructure Setup

## Overview

Step-by-step guide for setting up OpenSIN infrastructure on Oracle Cloud A1.Flex VM.

## Prerequisites

- Oracle Cloud account
- A1.Flex VM (4 OCPU, 24GB RAM, 200GB storage)
- Ubuntu 22.04 LTS

## Installation

```bash
# Install Docker
curl -fsSL https://get.docker.com | sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Clone OpenSIN-backend
git clone git@github.com:OpenSIN-AI/OpenSIN-backend.git
cd OpenSIN-backend

# Start services
docker-compose up -d
```

## Post-Setup

1. Configure n8n API key
2. Set up Supabase
3. Configure OpenCode sync
4. Test all services

---

*Last updated: 2026-04-04 by SIN-Zeus*
