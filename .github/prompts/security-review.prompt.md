---
mode: 'agent'
description: 'Review code or a workspace for security risks and provide a prioritized remediation plan.'
---

# Security Review

Perform a focused security review of the provided code, file, or workspace. Look for real and likely vulnerabilities, not theoretical concerns. Prioritize concrete issues that could lead to exploitation, sensitive-data exposure, privilege escalation, or unsafe behavior.

## Scope and inputs

- Review the selected code when available; otherwise review the relevant workspace files.
- Consider the application type, framework, and runtime when judging risk.
- Focus on the attack surface that is most likely affected by the code under review.
- Call out assumptions when the code is incomplete or depends on external systems.

## Assessment checklist

Review for the following classes of issues, as applicable:

- Authentication and authorization flaws
- Broken access control or privilege escalation
- Injection issues: SQL, command, path, template, and code injection
- Cross-site scripting (XSS), CSRF, and unsafe output handling
- Insecure direct object references and unsafe ID usage
- Secret exposure in code, logs, configs, or environment handling
- Weak or custom crypto, insecure defaults, and improper randomness
- File upload, path traversal, and unsafe file handling
- SSRF, open redirects, and unsafe network requests
- Deserialization and unsafe parsing
- Insecure dependency usage, outdated packages, or known vulnerable patterns
- Error handling that leaks stack traces or sensitive internals
- Logging, monitoring, and audit gaps for security-relevant actions
- Missing validation, sanitization, or encoding around untrusted input

## Review process

1. Identify the security-critical entry points and trust boundaries.
2. Trace data flows from input to output and to external systems.
3. Check whether the code validates, authenticates, authorizes, encodes, and isolates data correctly.
4. Look for risky defaults, unsafe framework features, and common implementation mistakes.
5. Confirm whether each finding is supported by the code and explain the exploit path clearly.

## Output format

Provide the result in this structure:

### Executive summary
- One short paragraph summarizing the overall risk.
- State whether the code is broadly safe, moderately risky, or high-risk.

### Findings
For each issue:
- Title
- Severity: Critical / High / Medium / Low / Informational
- Location: file and relevant function or section
- Risk: explain the vulnerability and why it matters
- Evidence: quote or summarize the relevant code path
- Exploit path: how an attacker could trigger it
- Recommendation: specific remediation steps

### Priority actions
- List the top 3 fixes that should be addressed first.

### Suggested validation
- Recommend tests, checks, or review steps to confirm the fix.

## Quality bar

- Be specific and evidence-based.
- Distinguish between confirmed issues and potential issues.
- Prefer actionable remediation over generic advice.
- If no material issue is found, say so clearly and explain why.
- Use plain language that engineering teams can act on immediately.

## Example review prompt

Review this Node.js/TypeScript application for security issues. Focus on authentication, authorization, user input handling, secrets management, and unsafe dependency usage. Return a prioritized security report with severity, evidence, and remediation steps.
