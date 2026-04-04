# Security Audit Checklist

Complete security audit checklist for production OpenSIN deployments.

## Pre-Launch Security Review

### Authentication & Authorization

- [ ] API keys rotated and stored in secrets manager
- [ ] No hardcoded credentials in code or config
- [ ] MFA enabled for admin accounts
- [ ] Service accounts use least-privilege permissions
- [ ] Token rotation configured (max 24h expiry)
- [ ] OAuth flows use PKCE
- [ ] Session tokens are httpOnly and secure

### Network Security

- [ ] TLS 1.3 enabled for all endpoints
- [ ] Certificate auto-renewal configured
- [ ] Firewall rules restrict access to required ports only
- [ ] VPC/private subnets for internal services
- [ ] No public database endpoints
- [ ] Rate limiting enabled on all APIs
- [ ] DDoS protection configured

### Data Protection

- [ ] PII detection and redaction active
- [ ] Encryption at rest (AES-256) for all data stores
- [ ] Encryption in transit (TLS) for all communications
- [ ] Database backups encrypted
- [ ] Log scrubbing removes sensitive data
- [ ] Data retention policies configured
- [ ] GDPR compliance verified

### Agent Security

- [ ] Prompt injection protection enabled
- [ ] Input validation on all agent inputs
- [ ] Output sanitization on all agent outputs
- [ ] Tool permissions follow least-privilege
- [ ] Sandboxing enabled for code execution
- [ ] Agent-to-agent communication authenticated
- [ ] Agent logs monitored for anomalies

### Infrastructure Security

- [ ] Container images scanned for vulnerabilities
- [ ] Base images are minimal (distroless/alpine)
- [ ] No root containers
- [ ] Read-only root filesystems
- [ ] Security contexts configured
- [ ] Network policies defined
- [ ] Pod security standards enforced

### Monitoring & Alerting

- [ ] Security events logged centrally
- [ ] Failed auth attempts alert after 5 failures
- [ ] Unusual API usage patterns detected
- [ ] Data exfiltration monitoring active
- [ ] Incident response playbook documented
- [ ] On-call rotation configured
- [ ] Escalation paths defined

## Code Security

### Static Analysis

- [ ] SAST tool running on all PRs
- [ ] Dependency scanning enabled
- [ ] Secret scanning active
- [ ] License compliance checked
- [ ] No critical/high vulnerabilities

### Dependencies

- [ ] All dependencies pinned to specific versions
- [ ] Automated dependency updates configured
- [ ] Known vulnerabilities patched within 48h
- [ ] No unmaintained dependencies
- [ ] Supply chain verification enabled

## Compliance

### SOC 2

- [ ] Access controls documented
- [ ] Change management process defined
- [ ] Risk assessment completed
- [ ] Monitoring and logging comprehensive
- [ ] Incident response tested

### GDPR

- [ ] Data processing agreement in place
- [ ] Right to erasure implemented
- [ ] Consent management active
- [ ] Data portability supported
- [ ] DPO appointed (if required)

## Penetration Testing

### Automated Scans

- [ ] OWASP ZAP scan passed
- [ ] Nmap scan shows no unexpected open ports
- [ ] SSL Labs grade A or A+
- [ ] Container scan shows no critical vulnerabilities

### Manual Testing

- [ ] Penetration test completed within last 90 days
- [ ] All findings remediated
- [ ] Retest completed for critical findings
- [ ] Report reviewed by security team

## Sign-Off

| Role | Name | Date | Status |
|------|------|------|--------|
| Security Lead | | | ☐ Approved |
| Engineering Lead | | | ☐ Approved |
| Product Owner | | | ☐ Approved |
| CTO | | | ☐ Approved |

## Next Steps

- [Security Hardening Guide](/guide/security-hardening)
- [SIN Permissions](/guide/sin-permissions)
- [Governance](/governance/SECURITY)
