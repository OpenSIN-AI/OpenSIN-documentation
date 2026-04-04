# Troubleshooting

## Common Issues

### Agent Not Starting

**Problem:** Agent fails to start with an error.

**Solution:**
1. Check your API keys are set correctly
2. Verify your model configuration
3. Check network connectivity
4. Review logs for specific errors

```bash
# Check environment variables
echo $OPENAI_API_KEY
echo $ANTHROPIC_API_KEY

# Test network connectivity
curl -I https://api.openai.com
```

### Message Not Sending

**Problem:** Agent cannot send messages.

**Solution:**
1. Verify agent is running
2. Check message format
3. Verify recipient exists
4. Check network connectivity

### Team Task Not Completing

**Problem:** Team task hangs or fails.

**Solution:**
1. Check individual agent status
2. Verify task workflow
3. Check orchestrator configuration
4. Review task logs

### MCP Server Not Loading

**Problem:** MCP server fails to load.

**Solution:**
1. Verify server path
2. Check server dependencies
3. Verify server configuration
4. Check server logs

## Getting Help

If you're still having issues:

- [GitHub Issues](https://github.com/OpenSIN-AI/OpenSIN/issues)
- [Discord](https://discord.gg/opensin)
- [Email](mailto:support@opensin.ai)
