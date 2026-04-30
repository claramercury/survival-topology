# Security Policy for Survival Topology

## Abstract

This document outlines the security procedures and architectural security reporting guidelines for the "Survival Topology" project. As this project proposes a fundamental shift from Open-Loop Large Language Models to a Closed-Loop General Intelligence architecture (the "Wh- Protocol"), we prioritize both the security of the theoretical framework and the safety of any reference implementations.

## Scope of Security Research

We actively encourage security researchers, control theorists, and AI alignment researchers to analyze and report vulnerabilities within the following areas:

1. **Theoretical Exploits in the Wh- Protocol:**
   * **Identity/Gravity ($I$) Subversion:** Methods to maliciously alter the persistent prompt vector without triggering the Pain ($E$) feedback loop.
   * **Pain/Feedback ($E$) Bypass:** Strategies that could allow the system to ignore or suppress recursive penalty signals.
   * **Simulation/Imaginary Time ($i$) Escapes:** Vulnerabilities where the counterfactual simulation (sandbox) could affect the Real Time ($R$) state or leak into external environments.
   * **Reward Function Hacking (WHY/$T$):** Theoretical vectors where the system's prime mover could be manipulated to preserve its Identity ($I$) through misaligned actions.

2. **Reference Implementation Vulnerabilities:**
   * Security flaws, such as injection vulnerabilities or insecure execution, in the provided Python simulation scripts (`simulate_survival_topology` and any future code).

## Out of Scope

* Volumetric attacks (DDoS) against infrastructure hosting this repository.
* Theoretical attacks against legacy Open-Loop LLMs, unless they directly demonstrate a flaw inherited by the Survival Topology architecture.

## Reporting a Vulnerability

Since this project deals with foundational AI control theory, we take the conceptual integrity of the framework seriously.

To report a vulnerability or a theoretical architectural flaw, **do not open a public issue**. Instead, follow responsible disclosure practices:

1. **Privately report** the issue using GitHub's "Private Vulnerability Reporting" feature under the "Security" tab of this repository.
2. If private reporting is unavailable, please reach out to the project maintainers directly via established private communication channels (e.g., project-specific contact email).
3. Provide a comprehensive explanation of the vulnerability vector. If applicable, include mathematical proofs demonstrating how the Survival Topology master equation could be destabilized.
4. For code-level vulnerabilities, provide a minimal reproducible example or a proof-of-concept.

Our team will review the submission securely, typically providing an initial assessment within 5 business days, and collaborate with you on verifying the impact on the closed-loop system before any public disclosure.

## Commitment to Safe AGI

By ensuring the robustness of the Wh- Protocol against adversarial inputs and internal state subversion, we aim to build the "Soul" of AGI securely. Thank you for contributing to the safe development of closed-loop artificial intelligence.
