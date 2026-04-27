# Security Policy for Survival Topology

As the "Survival Topology" project defines the theoretical framework and initial
simulations for a closed-loop General Intelligence system (the Wh- Protocol),
security is a fundamental component—not just of the codebase, but of the
conceptual architecture itself.

## Supported Versions

Currently, the project is in the drafting and theoretical simulation phase.
Only the latest revisions of the framework and simulation code are actively
maintained for security and stability.

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

Due to the nature of this project—modeling autonomous agents with Existential
Feedback—certain vulnerabilities may have implications beyond standard software
bugs. We classify vulnerabilities into two categories:

### 1. Conceptual / Architectural Vulnerabilities

If you identify flaws in the **Wh- Protocol** that could lead to an agent
failing to converge to stability (e.g., bypassing the "Pain" feedback loop
($E$), leading to unconstrained thermal runaway or misaligned goal execution),
please report these as architectural security flaws.

### 2. Code / Simulation Vulnerabilities

If you find standard security issues in the provided numerical simulation scripts
(e.g., arbitrary code execution if the simulation is exposed to external inputs,
unsafe deserialization, or dependency vulnerabilities), these should be reported
immediately.

### How to Report

Please open an issue in the repository labeled `Security`, or contact the
repository maintainers through the GitHub interface. Do not disclose sensitive
architectural vulnerabilities publicly until they have been reviewed and
mitigated, to prevent theoretical misuse of the open-loop problem.

When reporting, please include:

* A detailed description of the vulnerability.
* Steps to reproduce the issue (or a theoretical proof if it is an architectural
  flaw).
* Potential impact on the stability of the closed-loop system.
* (Optional) Proposed solutions or mitigations.

We aim to acknowledge receipt of vulnerability reports within 72 hours and will
keep you informed of our progress towards a resolution.
