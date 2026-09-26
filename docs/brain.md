# CyberDNA — AI Project Context

## Mission
You are working on CyberDNA, a full-stack digital-forensics investigation application. Preserve traceability, deterministic behavior, and safe evidence handling.

## Repository map
- `backend/app/api/` — HTTP route modules.
- `backend/app/ai/` — AI provider interfaces/implementations.
- `backend/app/core/` — configuration, database, logging.
- `backend/app/forensic/` — detection, seed/demo data, report generation.
- `backend/app/models/` — persistence models.
- `backend/app/schemas/` — API contracts.
- `backend/app/services/` — hashing, uploads, risk, audit-related services.
- `frontend/src/components/` — reusable UI.
- `frontend/src/pages/` — screens/routes.
- `frontend/src/services/api.ts` — centralized API access.
- `frontend/src/types/` — typed domain models.
- `docs/` — product and architecture context.

## Development rules
1. Read existing code and nearby tests before changing behavior.
2. Prefer small modular changes over broad rewrites.
3. Reuse existing types/services instead of duplicating logic.
4. Add regression tests for changed security or forensic behavior.
5. Preserve backwards compatibility for existing API contracts unless intentionally versioning.
6. Never commit real evidence, credentials, tokens, private keys, or personal case data.
7. Treat uploads, filenames, search strings, and metadata as untrusted.
8. Do not execute user-controlled text through shell or dynamic code evaluation.
9. Evidence is source data; findings, AI explanations, and reports are derived outputs.
10. AI output is advisory. Do not fabricate evidence, timestamps, hashes, or findings.

## Common local commands
Backend:
```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```

Docker:
```bash
docker compose up --build
```

## Investigation data flow
```
Input
 -> validation
 -> hashing
 -> artifact processing
 -> detection
 -> findings
 -> timeline/graph
 -> risk/context
 -> AI assistance
 -> report
```

## Quality checklist
Before completing a change, confirm:
- tests cover the changed behavior;
- API errors are explicit;
- security-sensitive inputs are validated;
- evidence provenance is preserved;
- UI has loading/error/empty states;
- documentation matches the implementation.

## Source of truth
When this file conflicts with implementation details, inspect the current code and tests first, then update this document to restore alignment.
