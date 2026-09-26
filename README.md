# CyberDNA

> **Digital Forensics Investigation Workspace** — from evidence intake to explainable findings, timelines, relationships, AI-assisted investigation, and reporting.

![Cybersecurity](https://img.shields.io/badge/domain-digital%20forensics-111827)
![Backend](https://img.shields.io/badge/backend-FastAPI-0f172a)
![Frontend](https://img.shields.io/badge/frontend-React%20%2B%20TypeScript-0f172a)
![Python](https://img.shields.io/badge/python-3.11%2B-0f172a)
![Testing](https://img.shields.io/badge/tests-Pytest-0f172a)

## Overview

CyberDNA is a full-stack forensic investigation platform for authorized security, incident-response, research, and educational workflows. It connects **evidence → artifacts → detections → findings → timeline → relationships → risk/context → investigation report** in a single workspace.

The design goal is not simply to display security data. It is to preserve **context and traceability** so that an investigator can move from a high-signal finding back to supporting evidence and surrounding events.

## Core capabilities

| Capability | What it provides |
|---|---|
| Evidence Intake | Validation, metadata capture, hashing, and controlled processing |
| Investigations | Case-centric workspace and state tracking |
| Artifact Analysis | Extracted forensic objects and metadata |
| Detection Engine | Rule-driven forensic findings |
| Timeline | Chronological reconstruction and contextual filtering |
| Evidence Graph | Relationships between evidence, artifacts, entities, and events |
| Risk & Anomalies | High-signal events and prioritization context |
| AI Investigator | Evidence-aware explanations and investigation assistance |
| Search | Cross-domain discovery across case data |
| Reports | Investigation summaries and export-oriented workflows |
| Demo Mode | Deterministic local data for repeatable development |

## System architecture

```text
                    +----------------------+
                    |   React + TypeScript  |
                    |   Investigator UI     |
                    +----------+-----------+
                               |
                          HTTP / JSON
                               |
                    +----------v-----------+
                    |       FastAPI        |
                    |   API / Orchestration|
                    +----------+-----------+
                               |
        +----------------------+----------------------+
        |          |            |         |            |
        v          v            v         v            v
     Evidence   Forensics   Cases     Timeline      AI Provider
     & Hashing  & Detection Findings  & Graph       Interface
        |          |            |         |            |
        +----------+------------+---------+------------+
                               |
                    +----------v-----------+
                    | Persistence / SQLite |
                    +----------------------+
```

## Investigation lifecycle

```
CREATE / OPEN CASE
       |
       v
INGEST EVIDENCE
       |
       +--> validate --> hash --> metadata
       |
       v
PROCESS ARTIFACTS
       |
       v
RUN DETECTIONS
       |
       v
FINDINGS + RISK CONTEXT
       |
       +--> TIMELINE
       +--> EVIDENCE GRAPH
       +--> AI INVESTIGATOR
       |
       v
GENERATE REPORT
```

## Technology

- **Frontend:** React, TypeScript, Vite, Tailwind CSS
- **Backend:** Python, FastAPI, Pydantic
- **Persistence:** SQLite in the included local workflow
- **AI:** provider abstraction with deterministic local support
- **Testing:** Pytest
- **Deployment:** Docker / Docker Compose
- **Forensic services:** evidence hashing, upload validation, detection engine, report generation, risk-oriented services

## Repository structure

```text
CyberDNA/
├── backend/
│   ├── app/
│   │   ├── api/          # domain API routes
│   │   ├── ai/           # AI provider layer
│   │   ├── core/         # config, DB, logging
│   │   ├── forensic/     # detection + report workflows
│   │   ├── models/       # persistence models
│   │   ├── schemas/      # API contracts
│   │   └── services/     # hashing, uploads, risk, audit
│   └── tests/
├── frontend/
│   └── src/
│       ├── components/
│       ├── hooks/
│       ├── layouts/
│       ├── pages/
│       ├── services/
│       └── types/
├── docs/
│   ├── PRD.md
│   ├── TRD.md
│   ├── UI_UX_DESIGN_BRIEF.md
│   ├── APP_FLOW.md
│   ├── ARCHITECTURE.md
│   └── brain.md
└── sample-data/
```

## Quick start

### Backend

```bash
cd backend
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Docker

```bash
docker compose up --build
```

### Tests

```bash
cd backend
pytest
```

## API domains

The backend is intentionally split by investigation responsibility:

`dashboard` · `investigations` · `evidence` · `artifacts` · `findings` · `timeline` · `graph` · `search` · `reports` · `ai` · `demo`

See the code for the exact routes and request/response contracts.

## Security & forensic integrity

CyberDNA is built around several trust boundaries:

1. **Evidence is untrusted input.** Validate before processing.
2. **Hash before analysis.** Preserve a cryptographic digest with accepted evidence.
3. **Findings are derived.** Do not overwrite source evidence with conclusions.
4. **AI is advisory.** Generated explanations should remain linked to available investigation context.
5. **Secrets stay outside Git.** Use environment configuration for credentials.
6. **Production errors stay controlled.** Do not leak stack traces or sensitive metadata.

> Use CyberDNA only with evidence you are authorized to collect and analyze.

## Documentation

| Document | Purpose |
|---|---|
| [PRD](docs/PRD.md) | Product goals, users, scope, outcomes |
| [TRD](docs/TRD.md) | Technical stack, architecture, APIs, security, testing |
| [UI/UX Brief](docs/UI_UX_DESIGN_BRIEF.md) | Visual and interaction system |
| [App Flow](docs/APP_FLOW.md) | Navigation, screens, actions, state transitions |
| [brain.md](docs/brain.md) | AI/developer context and repository rules |
| [Architecture](docs/ARCHITECTURE.md) | Existing architecture reference |

## Engineering direction

Planned evolution includes richer artifact parsers, more detection coverage, stronger evidence normalization, configurable case workflows, external AI provider adapters, CI quality gates, observability, and hardened report/export pipelines.

## License

Add the project's intended license before public redistribution if one has not already been selected.
