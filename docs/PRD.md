# CyberDNA — Product Requirements Document

## Product vision
CyberDNA is a digital-forensics investigation workspace that helps an authorized investigator move from evidence intake to findings, timeline context, relationship analysis, explanation, and reporting in one traceable workflow.

## Target users
- Cybersecurity students and educators practicing forensic investigation.
- Security analysts and incident responders working with authorized evidence.
- Developers building or testing forensic analysis workflows.

## Core user problem
Forensic evidence is often spread across files, artifacts, timestamps, detections, and analyst notes. CyberDNA organizes those signals into a connected investigation model while keeping derived findings distinguishable from source evidence.

## Goals
1. Make evidence ingestion and validation explicit.
2. Surface forensic findings with provenance and context.
3. Connect evidence, entities, and events through timeline and graph views.
4. Provide explainable AI assistance without silently changing evidence.
5. Produce investigation-ready reports.
6. Provide deterministic local/demo data for repeatable development.

## Key features
Evidence upload and hashing, investigations/cases, artifact and finding management, timeline reconstruction, evidence graph, anomaly/risk views, search, reports, and AI Investigator assistance.

## UX principles
Clarity, traceability, progressive disclosure, fast scanning, safe defaults, and visible system states.

## Success measures
- Users can create/open an investigation without needing to understand internal services.
- Uploaded evidence has a visible validation/hash path.
- A finding can be traced to related artifacts/events.
- Timeline and graph views provide useful cross-context navigation.
- AI explanations reference available case context and remain advisory.
- Reports can be generated from the investigation state.

## Non-goals
CyberDNA does not replace formal chain-of-custody procedures, specialist acquisition tools, expert forensic judgement, or jurisdiction-specific legal requirements.
