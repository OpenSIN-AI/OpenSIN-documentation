# Troubleshooting

Common issues and their solutions.

## Agent Not Responding

1. Check agent status: `Check the OpenSIN-Code CLI output and logs`
2. Verify API connectivity
3. Check logs: `Review logs in the terminal output`

## High Error Rate

1. Review error patterns
2. Check rate limits (For Google accounts and OpenAI pools, see [Dual Auth Rotators](/examples/dual-auth-rotators))
3. Verify input format

## High Latency

1. Reduce context window
2. Use streaming responses
3. Implement caching

## Next Steps

- [Monitoring](/guide/monitoring)
- [Getting Started](/guide/getting-started)
