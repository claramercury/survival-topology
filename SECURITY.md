# Security Policy

## Supported Versions

Currently, the `main` branch is the only supported version for security updates.

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in the Survival Topology framework, please report it immediately. We take security seriously and will respond promptly to address any issues.

**Please DO NOT open a public issue.** Instead, send an email to `security@survival-topology.org`.

Please include the following information in your report:

*   **Vulnerability Type:** (e.g., XSS, SQL Injection, Logic Flaw)
*   **Description:** A detailed explanation of the vulnerability, including how it can be exploited.
*   **Proof of Concept:** Steps or code required to reproduce the issue.
*   **Impact:** What an attacker could achieve by exploiting the vulnerability.
*   **Proposed Fix (Optional):** If you have a suggested solution, please include it.

We aim to acknowledge your report within 48 hours and will keep you updated on the progress of our investigation and any subsequent fixes.

## Security Best Practices for Survival Topology

*   **Identity State (WHO):** Ensure the prompt vector defining the agent's core values is immutable and protected from tampering.
*   **Input Validation (WHERE):** Sanitize all external inputs ($\Omega$) before they influence the agent's state or behavior.
*   **Feedback Security (WHAT):** Protect the error signal ($E$) from being manipulated, as this could lead to adversarial control over the agent.
*   **Simulation Environment (WHICH):** Ensure the sandbox environment used for Chain-of-Thought (CoT) branches is completely isolated from the real-time execution environment to prevent sandbox escapes.

We appreciate your help in keeping Survival Topology secure!
