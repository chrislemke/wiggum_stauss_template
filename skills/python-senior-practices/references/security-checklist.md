# Security Checklist

Use this checklist when touching untrusted input, credentials, authentication, external integrations, or dependency management.

## Input and Serialization

- Validate and normalize all external input at system boundaries.
- Reject invalid payloads early with explicit errors.
- Never use `eval` or `exec` on untrusted input.
- Never deserialize untrusted data using `pickle`.
- Sanitize logs to avoid leaking PII or secrets.

## Auth and Secrets

- Hash passwords with `argon2` or `bcrypt`.
- Compare secrets/tokens with constant-time checks where relevant.
- Store secrets in environment variables or a dedicated secrets manager.
- Rotate credentials and avoid long-lived static keys.

## Data Access

- Parameterize SQL and other query languages.
- Apply least privilege for DB/service accounts.
- Limit data returned to fields required for the operation.
- Enforce authorization checks close to business actions.

## Network and External Calls

- Enforce TLS for external service communication.
- Use explicit timeouts and retry policies with caps.
- Validate response schemas from third-party APIs.
- Treat third-party payloads as untrusted input.

## Dependency and Supply Chain

- Pin dependencies and review major version jumps.
- Run vulnerability scanning (`pip-audit` or equivalent) in CI.
- Remove unused dependencies and transitive bloat.
- Prefer well-maintained packages with clear release practices.

## Operational Controls

- Use structured logging and avoid printing secrets.
- Emit security-relevant audit events for sensitive actions.
- Fail closed on authorization checks.
- Document incident response ownership for critical services.
