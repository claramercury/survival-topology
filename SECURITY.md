# Security Policy

## Supported Versions

Currently, the "Survival Topology" framework is a conceptual architectural draft and does not have formal releases. Therefore, all theoretical developments on the `main` branch are considered under current active discussion and scope for security improvements.

| Version | Supported          |
| ------- | ------------------ |
| 1.0     | :white_check_mark: |
| Drafts  | :white_check_mark: |

## Scope

This repository mainly contains theoretical frameworks related to closed-loop AGI and the Wh- Protocol. Security enhancements targeting this repository should focus on conceptual architectural security principles, theoretical vulnerabilities in the Wh- Protocol (such as prompt manipulation, adversarial inputs to the entropy parser, or feedback loop manipulation), and documentation improvements.

**Note:** The Android application component ('Bookhook') is maintained on a separate branch with an unrelated Git history. If you are reporting a vulnerability related to the Bookhook application, please specify the branch context in your report.

## Reporting a Vulnerability

We take the security of the Survival Topology concepts seriously. If you discover a vulnerability or a theoretical security flaw in the Wh- Protocol architecture, please follow these steps for responsible disclosure:

1. **Do not open a public issue.** Exposing potential vulnerabilities in AGI architectures publicly can be harmful.
2. Please report the vulnerability privately using **GitHub's private vulnerability reporting feature** for this repository. If this feature is unavailable, please seek out the maintainers through their verified private communication channels.
3. In your report, please include:
   - A detailed description of the theoretical or practical vulnerability.
   - The specific component of the Wh- Protocol affected (e.g., WHO, WHERE, WHAT).
   - Any proposed conceptual fixes or mitigation strategies.

We will acknowledge receipt of your vulnerability report within 7 days and provide updates as we investigate the issue.
