import React, { useState, useCallback } from "react";
import { Routes, Route } from "react-router-dom";
import { AppShell } from "./layouts/AppShell";
import CommandCenter from "./pages/CommandCenter";
import EvidencePage from "./pages/Evidence";
import TimelinePage from "./pages/Timeline";
import ArtifactsPage from "./pages/Artifacts";
import InvestigationsPage from "./pages/Investigations";
import EvidenceGraphPage from "./pages/EvidenceGraph";
import AnomaliesPage from "./pages/Anomalies";
import AIInvestigatorPage from "./pages/AIInvestigator";
import ReportsPage from "./pages/Reports";
import SettingsPage from "./pages/Settings";

const App: React.FC = () => {
  const [refreshKey, setRefreshKey] = useState(0);
  const onDemoLoaded = useCallback(() => setRefreshKey((k) => k + 1), []);
  return <Routes><Route element={<AppShell refreshKey={refreshKey} onDemoLoaded={onDemoLoaded} />}>
    <Route path="/" element={<CommandCenter refreshKey={refreshKey} />} />
    <Route path="/evidence" element={<EvidencePage refreshKey={refreshKey} />} />
    <Route path="/timeline" element={<TimelinePage refreshKey={refreshKey} />} />
    <Route path="/artifacts" element={<ArtifactsPage refreshKey={refreshKey} />} />
    <Route path="/investigations" element={<InvestigationsPage refreshKey={refreshKey} />} />
    <Route path="/graph" element={<EvidenceGraphPage refreshKey={refreshKey} />} />
    <Route path="/anomalies" element={<AnomaliesPage refreshKey={refreshKey} />} />
    <Route path="/ai-investigator" element={<AIInvestigatorPage refreshKey={refreshKey} />} />
    <Route path="/reports" element={<ReportsPage refreshKey={refreshKey} />} />
    <Route path="/settings" element={<SettingsPage />} />
  </Route></Routes>;
};
export default App;
