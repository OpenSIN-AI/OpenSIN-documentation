# Production Deployment Checklist

Complete checklist before deploying agents to production.

## Pre-Deployment

### Code Quality
- [ ] Code review completed
- [ ] All tests passing (unit, integration, E2E)
- [ ] Code coverage > 80%
- [ ] No security vulnerabilities
- [ ] Linting and formatting clean

### Agent Configuration
- [ ] System prompt reviewed and optimized
- [ ] Model selection appropriate for task
- [ ] Temperature and parameters tuned
- [ ] Tools registered and tested
- [ ] Memory strategy configured
- [ ] Timeout values set

### Security
- [ ] API keys stored in secrets manager
- [ ] No hardcoded credentials
- [ ] Input validation enabled
- [ ] Output sanitization enabled
- [ ] Prompt injection protection active
- [ ] Rate limiting configured
- [ ] Permission rules defined

### Infrastructure
- [ ] Health checks configured
- [ ] Monitoring and alerting set up
- [ ] Logging enabled (structured JSON)
- [ ] Backup strategy in place
- [ ] Rollback procedure tested
- [ ] TLS/SSL certificates valid

### Performance
- [ ] Load testing completed
- [ ] Latency within SLA
- [ ] Throughput meets requirements
- [ ] Memory usage optimized
- [ ] Token usage budgeted

## Deployment

### Staging
- [ ] Deploy to staging environment
- [ ] Run smoke tests
- [ ] Verify all integrations
- [ ] Check monitoring dashboards
- [ ] Validate error handling

### Production
- [ ] Deploy with canary (10% traffic)
- [ ] Monitor for 30 minutes
- [ ] Increase to 50% traffic
- [ ] Monitor for 30 minutes
- [ ] Increase to 100% traffic
- [ ] Final health check

## Post-Deployment

### Monitoring
- [ ] Error rate < 1%
- [ ] Latency within SLA
- [ ] Cost within budget
- [ ] User satisfaction tracked
- [ ] Alerts configured and tested

### Documentation
- [ ] Runbook updated
- [ ] API docs updated
- [ ] Changelog updated
- [ ] Team notified

## Rollback Plan

If issues detected:
1. Stop canary deployment
2. Rollback to previous version
3. Investigate root cause
4. Fix and re-test
5. Re-deploy with canary

## Sign-Off

| Role | Name | Date | Status |
|------|------|------|--------|
| Developer | | | ☐ |
| QA | | | ☐ |
| Security | | | ☐ |
| Ops | | | ☐ |
| Product | | | ☐ |
