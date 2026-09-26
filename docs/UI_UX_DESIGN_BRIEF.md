# CyberDNA — UI/UX Design Brief

## Product feel
CyberDNA should feel like a modern SOC/forensics workstation: dense enough for analysts, but structured enough for students and first-time users.

## Visual language
- Primary palette: near-black/slate surfaces with cool cyan/blue accents.
- Status semantics: success, warning, danger, and informational states must be visually distinct and also communicated with text/icons.
- Cards: restrained radius, thin borders, clear hierarchy.
- Data views: tables, timelines, graph nodes, and evidence panels should prioritize scannability.

## Typography
Use a modern sans-serif system stack. Large display type is reserved for page titles; body text should remain compact and readable. Use monospace only for hashes, IDs, paths, timestamps with technical meaning, and code.

## Layout
- Persistent application shell with sidebar/top context.
- Main workspace uses wide responsive panels.
- Secondary details open in drawers or dedicated detail views rather than replacing the user's investigation context.

## Navigation
Core destinations: Command Center, Investigations, Evidence, Artifacts, Findings, Timeline, Evidence Graph, Anomalies, AI Investigator, Reports, Settings.

## Interaction rules
- Primary actions are visually obvious and stateful.
- Destructive or irreversible actions require explicit confirmation.
- Long-running processing shows progress.
- Every asynchronous action has loading, success, error, and empty states.
- Clicking a finding should expose supporting evidence/context where available.

## Accessibility
Use semantic HTML, keyboard navigation, visible focus, sufficient contrast, descriptive labels, and non-color-only status communication.

## Responsive behavior
Desktop is the primary forensic workspace. Tablet layouts collapse secondary panels. Mobile should remain usable for review and case monitoring, while extremely dense graph/table tasks may use horizontal scrolling or focused subviews.

## Motion
Use short, purposeful transitions for panel changes, filtering, graph updates, and status changes. Avoid decorative animation that distracts from evidence analysis.
