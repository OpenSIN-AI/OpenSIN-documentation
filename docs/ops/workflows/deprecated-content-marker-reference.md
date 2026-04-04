# Deprecated Content Marker — Reference Guide

> **Workflow:** deprecated-content-marker | **Category:** n8n Automation | **Status:** Active

## Overview

The **Deprecated Content Marker** workflow is part of the OpenSIN-AI n8n automation system.

## Trigger

| Type | Schedule | Description |
|------|----------|-------------|
| Schedule | Configurable | Runs on defined schedule |

## Nodes

| Node | Type | Purpose |
|------|------|---------|
| Trigger | Schedule/Cron | Initiates workflow execution |
| Action | HTTP/GitHub | Performs the main action |
| Process | Function | Processes and transforms data |
| Report | HTTP/Telegram | Sends notification or report |

## Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| Schedule | Configurable | When the workflow runs |
| Telegram Bot | Configured | For notifications |
| GitHub Auth | Configured | For repository access |

## Execution Flow

1. Trigger fires based on schedule
2. Action node fetches required data
3. Process node analyzes and transforms data
4. Report node sends results via Telegram

## Error Handling

| Error Type | Handling | Notification |
|------------|----------|--------------|
| API Failure | Retry with backoff | Telegram alert |
| Authentication | Log and alert | Telegram alert |
| Data Error | Skip and log | Daily report |
| Timeout | Retry once | Telegram alert |

## Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Execution Time | Less than 60s | Telegram alert |
| Error Rate | Less than 1 percent | GitHub issue |
| Success Rate | Greater than 99 percent | Daily report |

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Workflow not running | Check schedule configuration |
| Notifications not sent | Verify Telegram bot token |
| API errors | Check credentials and rate limits |

---

*Last updated: 2026-04-04 by SIN-Zeus*
