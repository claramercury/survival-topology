# Security Policy for Survival Topology

**Version:** 1.0
**Context:** Theoretical Framework & Proof-of-Concept Simulator

## 1. Scope

This security policy applies to the **Survival Topology** theoretical framework and its accompanying simulator (`README.md` and associated models).

The repository currently consists of theoretical documentation and closed-loop control system models for defining AGI behavior. Security in this context primarily refers to the structural integrity of the control framework and the prevention of theoretical exploits (e.g., control loop escapes).

### Covered Areas

* **The "Wh-" Protocol Specifications:** Vulnerabilities in the theoretical mapping that could lead to unaligned or rogue behavior (e.g., manipulating the "$I$" or "$E$" variables).
* **Simulator Implementation:** Flaws in the provided numerical simulations that could lead to unintended divergence or inaccurate stability mapping.
* **Existential Feedback Bypasses:** Identifying ways the "Pain" signal ($E$) could be muted, simulated, or ignored by the agent in an implementation scenario.

### Out of Scope

* Physical implementations of the AGI framework (as none currently exist in this repository).
* Vulnerabilities in standard numerical libraries (e.g., `numpy`, `matplotlib`) used for the simulation.

## 2. Reporting a Vulnerability

**DO NOT create public issues for security flaws.**

We require responsible disclosure to maintain the integrity of this framework. If you discover a theoretical flaw or a simulator vulnerability that compromises the control loop architecture, you must report it privately.

Please report vulnerabilities using **GitHub Private Vulnerability Reporting**.

To report:

1. Go to the **Security** tab of this repository.
2. Click **Advisories**.
3. Click **Report a vulnerability**.
4. Provide a detailed description of the flaw, including:
   * The specific component or equation (e.g., Module 3.3 WHAT).
   * A detailed explanation of how the control loop could be bypassed.
   * Suggestions for theoretical patches or simulator code changes.

We will acknowledge receipt of your report within 48 hours and work with you to understand and mitigate the flaw before public disclosure.
