# Onboarding & First-Run Setup

OpenSIN onboarding is owned by
[`Infra-SIN-Dev-Setup`](https://github.com/OpenSIN-AI/Infra-SIN-Dev-Setup),
specifically the `user-onboarding/` surface.

This page summarizes the public-safe onboarding flow without hardcoding legacy
or environment-specific implementation details.

## Canonical Entry Point

```bash
git clone https://github.com/OpenSIN-AI/Infra-SIN-Dev-Setup.git
cd Infra-SIN-Dev-Setup/user-onboarding
./scripts/onboard.sh
```

## What Onboarding Should Do

The first-run flow should prepare a user to operate OpenSIN safely and with the
canonical stack:

- install the required local tooling
- connect the user to the canonical OpenCode configuration
- prepare browser automation and authentication surfaces
- verify the local machine can run OpenSIN workflows

## Scope Boundaries

This public doc does **not** hardcode:

- internal IP addresses
- private secret backends
- internal-only control-plane endpoints
- provider-specific credentials that may change across environments

Those details belong in the owning infrastructure repos and private runbooks.

## Where To Go Next

- [Getting Started](/guide/getting-started)
- [Installation](/guide/installation)
- [Agent Configuration](/guide/agent-configuration)
- [Infra-SIN-Dev-Setup / user-onboarding](https://github.com/OpenSIN-AI/Infra-SIN-Dev-Setup/tree/main/user-onboarding)
