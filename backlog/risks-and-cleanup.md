# Risks And Cleanup

## R001 - AI routing

- Severity: high
- Description: Direct browser/BYO chat paths can bypass platform metering and admin policy.
- Evidence: AiSystemsMap marks Chat / streaming completions as browser -> provider REST direct with high cost risk.
- Recommended fix: Migrate remaining chat.agent.byo and agent.run paths into ai-route or document blessed exceptions with tests.
- Priority: P0

## R002 - Image generation

- Severity: high
- Description: Direct image generation via user keys is live but not platform metered.
- Evidence: AiSystemsMap says LLMService.generateImage is direct provider REST with no usage logging.
- Recommended fix: Route platform-paid image generation through ai-route; label BYO as user-paid.
- Priority: P0

## R003 - Production repo

- Severity: medium
- Description: Selected production checkout was already dirty before audit.
- Evidence: Pre-audit git status listed modified/staged AI media/model files and untracked docs/tests/temp files.
- Recommended fix: Keep Atlas isolated; compare before/after status and diff fingerprints.
- Priority: P1

## R004 - Business Spaces credits

- Severity: medium
- Description: Night Shift pricing/reserved/debited fields need full debit/refund verification before aggressive selling.
- Evidence: business_space_night_shifts and AdminOperatorsPanel credit metrics exist.
- Recommended fix: Add reserve/debit/refund/admin-bypass tests.
- Priority: P0

## R005 - Automation

- Severity: high
- Description: Flows and schedules can execute work but paid-tier/credit enforcement is not uniformly visible.
- Evidence: flow-executor, schedule-tick, flows/schedules services exist.
- Recommended fix: Create canonical automation entitlement and credit contract.
- Priority: P0

## R006 - Agent channels

- Severity: high
- Description: Channel execution is not fully unified under ai-route.
- Evidence: ChannelRouting recommends migrating agent.run channel execution into ai-route.
- Recommended fix: Make agent-runner use ai-route for all model calls.
- Priority: P0

## R007 - Knowledge retrieval

- Severity: medium
- Description: Embedding/retrieval provider and cost path are unknown.
- Evidence: AiSystemsMap lists Knowledge retrieval / embeddings as Unknown.
- Recommended fix: Surface provider/model/logging/credit behavior in AI Systems Map.
- Priority: P1

## R008 - Web search

- Severity: medium
- Description: Web search/WebIntel provider, logging, and credit handling are not centrally enumerated.
- Evidence: AiSystemsMap marks Web search / WebIntel Unknown.
- Recommended fix: Map web-search provider/key/cost and admin visibility.
- Priority: P1

## R009 - Experience generation

- Severity: medium
- Description: Experience generation uses a dedicated route instead of canonical ai-route.
- Evidence: services/experiences.ts invokes experience-generate; AdminExperiencesPanel controls OpenAI model.
- Recommended fix: Classify as blessed exception or migrate to ai-route route key.
- Priority: P1

## R010 - Marketplace monetization

- Severity: medium
- Description: Marketplace/Discover exists but paid listing, commission, and entitlement loop needs clearer connection.
- Evidence: Marketplace, prompt packs, Stripe Connect, referral tables exist separately.
- Recommended fix: Create one end-to-end paid asset flow.
- Priority: P1

## R011 - Admin secrets

- Severity: critical
- Description: Admin provider key surfaces must avoid leaks in logs, UI, exports, or public docs.
- Evidence: AdminDashboard manages admin_api_keys; TuneAdminPanel warns never reveal secrets.
- Recommended fix: Scan key rendering/logging and redact audit metadata.
- Priority: P0

## R012 - Admin role boundaries

- Severity: high
- Description: Every high-power admin write surface needs role review.
- Evidence: AdminDashboard has many writes across keys, flags, users, credits.
- Recommended fix: Add role-matrix tests.
- Priority: P0

## R013 - Public pages

- Severity: medium
- Description: Catch-all/admin pages can publish public content.
- Evidence: Routes /page/:slug and /:slug point to AdminManagedPage.
- Recommended fix: Add preview/publish review workflow.
- Priority: P1

## R014 - Programs redirects/access

- Severity: medium
- Description: Programs use redirects and access functions; login nextPath should be smoke-tested.
- Evidence: Routes /programs -> /ecosystem and /programs/:id plus program-access functions exist.
- Recommended fix: Smoke test public/admin program access.
- Priority: P1

## R015 - RLS surface

- Severity: high
- Description: Large schema requires table-family RLS review.
- Evidence: Atlas found many user-scoped tables and service-role functions.
- Recommended fix: Audit RLS for agents/files/business spaces/credits/partners/programs/pages.
- Priority: P0

## R016 - Credit double-debit

- Severity: high
- Description: ai-route and z-engine-stream debit/refund logic needs idempotency checks.
- Evidence: ai-route/z-engine-stream include credit debit/refund paths.
- Recommended fix: Add route-level idempotency and ledger reconciliation tests.
- Priority: P0

## R017 - Feature sprawl

- Severity: medium
- Description: Many advanced features are buried across routes/labs/aliases.
- Evidence: 91 routes, 54 edge functions, and many aliases/legacy routes discovered.
- Recommended fix: Use Atlas to consolidate navigation and demo journeys.
- Priority: P1

## R018 - Public Atlas safety

- Severity: medium
- Description: Atlas is public and must avoid secrets, private data, source chunks, and sensitive screenshots.
- Evidence: Bootstrap public safety rule.
- Recommended fix: Keep summaries high-level and screenshots sanitized.
- Priority: P0

## R019 - Connector/OAuth readiness

- Severity: medium
- Description: OAuth token lifecycle and connector gating need review.
- Evidence: notion-oauth, linkedin-oauth, user_oauth_connections, businessConnectionsCenter.
- Recommended fix: Audit token storage, revocation, scopes, paid gates.
- Priority: P1

## R020 - Labs/legacy exposure

- Severity: medium
- Description: Legacy routes under Labs can confuse users if exposed.
- Evidence: App.tsx nests legacy marketplace/workspace/create/studio routes under /labs.
- Recommended fix: Keep Labs admin-only and map modern replacements.
- Priority: P2
