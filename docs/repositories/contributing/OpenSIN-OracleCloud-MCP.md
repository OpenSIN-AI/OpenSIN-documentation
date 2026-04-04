# OpenSIN-OracleCloud-MCP — Contributing Guide

> **Repository:** OpenSIN-OracleCloud-MCP | **Organization:** OpenSIN-AI | **Status:** ✅ Active

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## Code Standards

- **TypeScript** for agents and services
- **Python** for scripts and automation
- **Conventional commits** for all commits
- **ESLint + Prettier** for TypeScript formatting
- **Black + isort** for Python formatting

## Pull Request Process

1. Update documentation for any changes
2. Add or update tests as appropriate
3. Ensure CI/CD pipeline passes
4. Request review from at least one team member
5. Address review comments
6. Merge after approval

## Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

feat(agents): add new marketing agent
fix(api): resolve authentication issue
docs(readme): update setup instructions
chore(deps): update dependencies
test(agents): add unit tests for agent
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Code style changes |
| `refactor` | Code refactoring |
| `test` | Test changes |
| `chore` | Maintenance tasks |

## Branch Naming

- `feature/description` — New features
- `fix/description` — Bug fixes
- `docs/description` — Documentation
- `chore/description` — Maintenance
- `release/version` — Release branches

## Testing Requirements

- Unit tests: > 80% coverage
- Integration tests: All API endpoints
- E2E tests: Critical user journeys

## Code Review Guidelines

- Be respectful and constructive
- Focus on the code, not the person
- Suggest improvements, not just criticisms
- Acknowledge good work
- Review within 48 hours

---

*Last updated: 2026-04-04 by SIN-Zeus*
