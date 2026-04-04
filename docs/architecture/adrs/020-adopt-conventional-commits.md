# ADR-020: Adopt Conventional Commits

> **Status:** Accepted | **Date:** 2026-04-04 | **Deciders:** SIN-Zeus, Architecture Team

## Context

We needed to make a decision about adopt conventional commits for the OpenSIN-AI ecosystem as it scales to 156+ repositories and 130+ A2A agents.

## Decision

We decided to adopt conventional commits because:

1. It aligns with our core architecture principles of scalability and maintainability
2. It provides the best balance of complexity and functionality for our use case
3. It's supported by the team and has strong community backing
4. It scales well with our projected growth to 500+ repositories

## Consequences

### Positive
- Improved system reliability and maintainability
- Better developer experience across all teams
- Easier onboarding for new contributors
- Scalable architecture that grows with the organization

### Negative
- Initial learning curve for team members
- Additional infrastructure costs during transition
- Migration effort required for existing services
- Temporary performance impact during rollout

## Compliance

All new services must comply with this ADR. Existing services should migrate when feasible during their next major update cycle.

## References

- [Architecture Overview](../overview.md)
- [Best Practices](../../best-practices/)
- [Implementation Guide](../../guide/)
- [Related ADRs](./)

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-04 | SIN-Zeus | Initial release |

---

*Last updated: 2026-04-04 by SIN-Zeus*
