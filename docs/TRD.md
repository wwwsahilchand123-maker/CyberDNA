# CyberDNA — Technical Requirements Document

## Architecture
```
React + TypeScript
       |
       v
FastAPI / Python API
       |
       +--> Evidence & Upload Services
       +--> Detection / Forensic Engine
       +--> Investigation / Findings
       +--> Timeline / Graph
       +--> Search / Reports
       +--> AI Provider
       |
       v
     SQLite / persistence layer
```

## Stack
- Frontend: React, TypeScript, Vite, Tailwind CSS.
- Backend: Python, FastAPI, Pydantic.
- Persistence: SQLite in the supplied local workflow.
- Testing: Pytest.
- Packaging: Docker / Docker Compose.
- AI: provider abstraction with deterministic local support.

## API boundaries
Route modules are separated by domain: dashboard, investigations, evidence, artifacts, findings, timeline, graph, search, reports, AI, and demo. The code remains the source of truth for exact route contracts.

## Forensic services
The detection engine creates findings from analyzed inputs; hashing and upload validation enforce evidence-handling boundaries; report generation converts investigation state into exportable output.

## Data requirements
Every accepted evidence object should preserve stable metadata and a cryptographic digest. Derived records should retain enough provenance to connect them to source artifacts/events.

## Security requirements
- Validate file size/type/name and required metadata before processing.
- Hash evidence before downstream analysis.
- Treat all uploaded content and query parameters as untrusted.
- Never execute user-controlled strings as shell/database commands.
- Keep secrets in environment configuration, not source control.
- Avoid verbose stack traces in production API responses.
- Keep AI output advisory and evidence-linked.

## Testing
Maintain regression coverage for API behavior, upload validation, hashing, risk logic, and detection rules. New detectors need positive, negative, boundary, and malformed-input cases where relevant.

## Deployment
Support local development and Docker. Production hardening should add HTTPS, authentication, secure headers, rate limits, secret management, logging, backups, and monitoring.

## Technical constraints
Prefer modular, typed interfaces and small testable services. Avoid hidden global state and keep external AI providers behind a stable interface.
