# CyberDNA — Application Flow

## Entry
```
Open app
  -> Command Center
  -> Select Investigation
  -> Investigation Workspace
```

## Investigation flow
```
Create/Open Case
   -> Evidence
   -> Validate + Hash
   -> Process Artifacts
   -> Run Detection
   -> Findings
   -> Timeline / Graph
   -> AI Investigator
   -> Report
```

## Main navigation
**Command Center** → overview, active cases, high-signal findings.

**Investigations** → list, create, open, and inspect cases.

**Evidence** → upload, validate, hash, browse, and inspect source evidence.

**Artifacts** → extracted artifacts and metadata.

**Findings** → detection results, severity/risk, provenance.

**Timeline** → chronological reconstruction with filters.

**Evidence Graph** → relationships between evidence, artifacts, entities, and events.

**Anomalies** → unusual patterns and risk signals.

**AI Investigator** → evidence-aware explanations and investigation assistance.

**Reports** → generate and review investigation output.

**Settings** → configuration and operational preferences.

## Button behavior
- **Create Investigation** → validate required fields → create case → open workspace.
- **Upload Evidence** → select file → validate → hash → upload/process → refresh case context.
- **Run Analysis** → verify inputs → execute detector pipeline → create findings → show results.
- **Open Finding** → show finding details + related artifacts/events.
- **View Timeline** → focus on related time window.
- **Explore Graph** → focus graph on selected evidence/entity.
- **Ask AI Investigator** → send bounded case context → return explanation with visible advisory status.
- **Generate Report** → validate report data → render/export report → provide status.

## Required UI states
Loading, empty, success, validation error, processing, partial result, API failure, permission/authorization failure, and retry.

## Safety states
Any action that modifies or deletes investigation state must show scope and require confirmation. Failed processing must not be presented as a successful forensic result.
