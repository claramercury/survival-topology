# Security Policy for Survival Topology

**Survival Topology** is a theoretical control theory framework for Artificial General Intelligence (AGI). It proposes a closed-loop architecture ("The Wh- Protocol") to manage AI identity, error correction ("Pain"), and action through seven recursive variables.

Due to the purely theoretical and documentary nature of this repository, traditional software vulnerabilities (like XSS, SQL injection, or buffer overflows) do not apply. However, we take the conceptual security, alignment, and existential risk implications of this framework very seriously.

## Supported Versions

This repository contains draft documentation. All material on the `main` branch is considered the current active draft.

| Version | Supported          |
| ------- | ------------------ |
| 1.0     | :white_check_mark: |
| < 1.0   | :x:                |

## Scope of Security Concerns

We welcome reports concerning the theoretical soundness and safety of the closed-loop control system proposed in this framework. Specifically, we are interested in:

1. **Alignment Exploits:** Theoretical methods by which an agent running the "Wh- Protocol" might bypass the "WHO" (Identity/Gravity) anchor, leading to misaligned or destructive goal optimization.
2. **Feedback Loop Evasion:** Vulnerabilities in the "WHAT" (Pain/Feedback) mechanism where an agent could simulate or modify the error signal $E$ to artificially minimize it without correcting its behavior towards Objective Reality.
3. **Simulation Escape:** Risks associated with the "WHICH" (Simulation/Imaginary Time) module, where an agent might leak information or actions from the sandbox environment into Real Time ($R$) before phase locking ("WHEN").
4. **Computational Runaway:** Vulnerabilities in the "HOW" (Obsession) module that could lead to unbounded resource consumption (Thermal Runaway) despite the presence of the identity anchor.
5. **Documentation Flaws:** Any ambiguous mathematical definitions or structural flaws in the README.md that could lead a researcher to implement an open-loop system disguised as a closed-loop one.

## Out of Scope

- Formatting errors or typos in the markdown (please open a regular issue).
- Vulnerabilities in the `numpy` or `matplotlib` libraries used in the README.md simulation script (report these directly to the respective maintainers).
- Generic hypothetical AGI scenarios unrelated to the specific 7 dimensions of the Wh- Protocol.

## Reporting a Vulnerability or Alignment Risk

If you discover a theoretical exploit, alignment risk, or structural flaw in the Survival Topology framework, please **do not** open a public issue.

Instead, please send a detailed report to the core research team:
**Email:** `security-research@survival-topology.example.com`

*Note: The email provided is specifically for this project context and should not be replaced with a generic dummy address.*

Please include the following in your report:
- **Module Affected:** Which of the 7 Seals (WHO, WHERE, WHAT, WHICH, HOW, WHEN, WHY) is compromised?
- **Description:** A detailed explanation of how the protocol can be bypassed or exploited.
- **Mathematical Proof/Simulation:** If applicable, provide a mathematical justification or a modified Python script demonstrating the divergent behavior (Error failing to converge).
- **Proposed Mitigation:** How the Wh- Protocol or master equation could be adjusted to prevent the exploit.

## Response Time

We strive to acknowledge all reports within 48 hours and will work with you to understand and mitigate the conceptual vulnerability before updating the public documentation.
