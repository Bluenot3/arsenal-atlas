# Codex Priority Backlog

## Centralize remaining high-risk AI routes

- Priority: P0
- Files likely involved: services/llm.ts; components/ChatInterface.tsx; supabase/functions/ai-route/index.ts
- Reason: Direct provider paths weaken cost control
- Expected impact: Credits and admin policy become consistent
- Risk: High
- Tests needed: Static route audit plus ai-route debit/fallback tests
- Definition of done: All non-BYO platform-paid chat/media paths use ai-route or have documented blessed exception.

## Night Shift credit lifecycle tests

- Priority: P0
- Files likely involved: services/businessSpaceNightShift.ts; services/shiftOs.ts; supabase/functions/night-shift-*
- Reason: Premium automation needs trustable billing
- Expected impact: Safe paid Night Shift launch
- Risk: High
- Tests needed: Reserve/debit/refund/idempotency tests
- Definition of done: Queued/running/failed/completed/admin-bypass paths reconcile with credit_ledger.

## Business Spaces buyer journey polish

- Priority: P1
- Files likely involved: pages/BusinessSpacesPage.tsx; components/business-spaces/*
- Reason: This is the clearest revenue surface
- Expected impact: Higher conversion to Pro/Premium
- Risk: Medium
- Tests needed: Authenticated visual QA on preview and paid modes
- Definition of done: Free preview, upgrade, create, ROI, proposal, Night Shift, and export paths are obvious and gated.

## Marketplace first paid asset

- Priority: P1
- Files likely involved: pages/MarketplacePage.tsx; services/promptPacks.ts; services/arsenalPaidAccess.ts
- Reason: Many marketplace pieces exist but paid flow is unclear
- Expected impact: Unlock creator revenue loop
- Risk: Medium
- Tests needed: Checkout entitlement and creator payout smoke tests
- Definition of done: One prompt pack or Arsenal can be listed, purchased, installed, and attributed to a creator.

## Knowledge retrieval provider map

- Priority: P1
- Files likely involved: services/knowledgeRetrieval.ts; components/admin/AiSystemsMap.tsx
- Reason: Provider/cost path is unknown
- Expected impact: Better trust and pricing
- Risk: Medium
- Tests needed: Static provider/route tests
- Definition of done: AI Systems Map shows provider/model/logging/credit behavior for knowledge retrieval.

## Web search provider map

- Priority: P1
- Files likely involved: services/webSearch.ts; services/webintel.ts; supabase/functions/web-search
- Reason: Provider/cost path is unknown
- Expected impact: Better research reliability
- Risk: Medium
- Tests needed: Function contract and logging tests
- Definition of done: Admin can see provider, usage, failures, and cost posture for web search.

## Admin role matrix tests

- Priority: P0
- Files likely involved: pages/AdminDashboard.tsx; components/admin/*; supabase/functions/admin-users
- Reason: Admin controls are powerful
- Expected impact: Protect billing, users, keys, and flags
- Risk: High
- Tests needed: Role-based static and integration tests
- Definition of done: Support/Billing/Internal/Security Master roles can only access intended write actions.

## Automation entitlement contract

- Priority: P0
- Files likely involved: services/flows.ts; services/schedules.ts; supabase/functions/flow-executor; schedule-tick
- Reason: Automation can become costly
- Expected impact: Paid automation becomes sellable
- Risk: High
- Tests needed: Flow executor entitlement/credit tests
- Definition of done: All execution paths enforce plan, credits, and structured failure.

## Public screenshot demo seed

- Priority: P1
- Files likely involved: demo data setup; screenshot plan
- Reason: Atlas needs public-safe visuals
- Expected impact: Faster marketing/investor assets
- Risk: Low
- Tests needed: Manual visual QA
- Definition of done: Demo account has safe agents, Business Spaces, files, admin views, and public pages.

## Route/navigation clarity pass

- Priority: P2
- Files likely involved: App.tsx; components/shell/*; pages/LabsPage.tsx
- Reason: 91 routes plus aliases are hard to explain
- Expected impact: Better activation
- Risk: Medium
- Tests needed: Route map diff and visual QA
- Definition of done: Main nav promotes marketable paths; Labs/legacy routes stay admin-only.
