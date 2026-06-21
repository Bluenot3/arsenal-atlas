# Arsenal Atlas Bootstrap

This file is the operating constitution for the Arsenal Atlas repository.

Arsenal Atlas is the external platform intelligence, mapping, audit, visualization, and strategy repository for Arsenal / arena-x by ZEN AI Co.

This repository is public.

This repository is not the production Arsenal application.

---

# 1. Absolute Mission

Arsenal Atlas exists to make Arsenal easier to understand, improve, sell, demo, visualize, and scale.

Codex must use this repository to create a complete platform map of Arsenal, including:

* feature inventory
* route map
* service map
* database/table map
* Supabase Edge Function map
* AI routing/control-plane map
* monetization map
* Business Spaces revenue map
* admin control map
* user journey maps
* risk and cleanup backlog
* screenshot shotlist
* visual layout concepts
* Mermaid diagrams
* non-coder-friendly explanations
* Codex execution backlog

The final output should help Alex understand the full Arsenal platform visually and strategically without needing to be a senior engineer.

---

# 2. Critical Safety Rule

The Arsenal production repository is read-only for this task.

Codex may inspect Arsenal.

Codex may not modify Arsenal.

All new files, generated maps, diagrams, CSVs, JSON, markdown, and strategy documents must be written only inside the Arsenal Atlas repository.

If Codex is currently running inside the Arsenal production repo, Codex must treat that repo as read-only and clone or open this Atlas repo as a sibling directory.

Correct relationship:

```txt
/parent-folder/
  arsenal/              = production app, read-only
  arsenal-atlas/        = documentation/map repo, write allowed
```

or:

```txt
/parent-folder/
  arena-x/              = production app, read-only
  arsenal-atlas/        = documentation/map repo, write allowed
```

---

# 3. Forbidden Actions

Codex must not do any of the following inside the Arsenal production repo:

* modify source code
* create files
* delete files
* move files
* rename files
* refactor files
* run formatters
* run migrations
* edit docs inside the production repo
* edit package files
* install packages
* commit to the production repo
* stage production repo files
* push production repo changes
* alter Supabase functions
* alter database migrations
* alter `.env` files
* alter generated types
* alter lockfiles
* alter build outputs
* alter public assets
* alter configuration files
* run destructive commands
* run commands that generate files in the production repo

If any command would write to the production repo, do not run it.

If unsure, stop and report the uncertainty.

---

# 4. Allowed Production Repo Inspection

Codex may use read-only inspection commands against the Arsenal production repo, such as:

```bash
pwd
ls
find
rg
grep
sed -n
cat
git status --short
git branch --show-current
git log --oneline -n 20
git ls-files
```

Codex may inspect these areas of the production repo:

* `App.tsx`
* route definitions
* `pages/`
* `components/`
* `components/shell/`
* `components/admin/`
* `components/business-spaces/`
* `components/agents/`
* `components/flows/`
* `components/skills/`
* `components/arsenal/`
* `services/`
* `contexts/`
* `stores/`
* `models/`
* `hooks/`
* `supabase/functions/`
* `supabase/migrations/`
* billing and Stripe code
* credits and ledger code
* AI routing services
* model catalogs
* provider registries
* integration registries
* launch control / feature flag systems
* admin controls
* existing documentation and repo-memory files

Codex should verify before and after the audit that the production repo remains unmodified:

```bash
git status --short
git diff --exit-code
```

If the production repo was already dirty before Codex starts, Codex must record that fact and still not touch it.

---

# 5. Public Repo Data Safety

Because Arsenal Atlas is public, Codex must not include:

* passwords
* API keys
* Supabase anon/service keys
* Stripe secrets
* OpenAI keys
* Cloudflare keys
* Twilio secrets
* OAuth client secrets
* `.env` contents
* admin credentials
* private user data
* customer data
* emails from private users
* phone numbers from private users
* screenshots containing sensitive admin/user/customer data
* private database dumps
* raw proprietary secrets
* large copied source files from the production repo

Codex may reference file paths and summarize code behavior.

Codex may include tiny source snippets only when necessary to explain a finding, but should avoid copying meaningful chunks of production source code.

Preferred style:

```txt
Observed in: services/agentRegistry.ts
Summary: Handles agent CRUD and local/Supabase persistence.
```

Not:

```txt
Paste 300 lines of source code here.
```

---

# 6. What Arsenal Is

Arsenal / arena-x is ZEN AI Co.'s Smart Business Solutions OS.

It is a unified operating layer for building, deploying, automating, governing, packaging, and monetizing intelligent business systems.

Arsenal is not merely a chatbot builder, prompt playground, workflow app, dashboard, or generic AI business platform.

Arsenal is designed to become the infrastructure layer where businesses, creators, agencies, operators, and learners turn work into deployable systems.

Core commercial statement:

> Arsenal turns business needs into deployable, measurable, monetizable systems.

Core platform direction:

```txt
Business need
→ smart system
→ deployed agents/workflows
→ measurable outputs
→ monetization
→ continuous improvement
```

---

# 7. Core Arsenal Primitives to Map

Codex must map these Arsenal primitives:

## Agents

Deployable digital workers with:

* purpose
* instructions
* model routing
* tools
* actions
* knowledge
* memory
* channels
* deployment surfaces
* monetization hooks

## Business Spaces

B2B operating spaces that combine:

* business profile
* agents
* automations
* channels
* knowledge
* ROI modeling
* proposals
* reports
* outputs
* client-facing deliverables

Business Spaces are one of Arsenal's clearest commercial surfaces.

## Z-Engine

Advanced creation and reasoning surface for:

* structured generation
* ideation
* system design
* project creation
* business solution generation
* artifact creation

Z-Engine outputs should become reusable assets, not temporary chat.

## Instruction Lab

Prompt, model, and instruction-testing surface for:

* prompt refinement
* model comparison
* instruction generation
* prompt pack creation
* saving prompts to agents
* converting prompts into skills or assets

## Files / Workspace / Vault / Project Vault / Knowledge

Workspace layer for:

* uploaded files
* generated outputs
* knowledge sources
* project assets
* generated media
* code artifacts
* proposals
* reports
* prompt packs
* business documents
* agent outputs
* education artifacts
* reusable client deliverables

## Skills

Reusable capabilities that attach to agents, workflows, or systems.

## Automation / Flows / Schedules / Baskets

Execution layer for repeatable work:

* visual flows
* scheduled tasks
* workflow templates
* integrations
* triggers
* recurring actions
* replay/history
* validation

## Arsenals

Branded bundles of:

* agents
* skills
* knowledge
* workflows
* experiences
* pages
* products

Arsenals support public distribution and creator monetization.

## Marketplace / Discover

Network-effect surfaces for distributing:

* agents
* arsenals
* prompt packs
* skills
* workflows
* experiences
* templates
* Business Space blueprints

## Experiences

Productized interactive flows, tools, assets, or guided journeys.

## Channels

Agent deployment outside the Arsenal app:

* public web links
* embeds
* Slack
* Discord
* Telegram
* WhatsApp
* SMS
* email
* future CRM/support channels

Strategic idea:

> Build once. Deploy everywhere.

## Admin Dashboard

Business and governance control plane for:

* users
* roles
* billing
* credits
* providers
* model routing
* feature visibility
* launch control
* marketplace controls
* usage analytics
* audit logs
* system health
* announcements
* public pages

Admin should become the place where ZEN controls the business without code.

---

# 8. AI Routing Law

Arsenal must move toward a canonical AI Feature Control Plane.

Every AI-powered feature should eventually be:

* powerful
* fast
* consistent
* admin-configurable
* credit-aware
* usage-logged
* provider-transparent
* fallback-safe
* visually premium
* monetization-ready
* impossible to silently regress without tests or smoke checks failing

The canonical route should generally be `ai-route` unless a feature has an explicitly documented reason to use a separate route.

Direct provider routes must be classified as:

* blessed exception
* legacy exception
* migration target
* risk
* unknown

Map whether each AI feature uses:

* `ai-route`
* Tune-specific routing
* Z-Engine streaming route
* Flow Executor route
* direct provider call
* Cloudflare
* OpenAI
* Anthropic
* Google/Gemini
* OpenRouter
* Lovable Gateway
* BYOK
* admin fallback pool
* unknown

For each AI feature, record:

* provider path
* default model if discoverable
* fallback behavior
* whether credits are charged
* whether usage is logged
* whether admin can see/control it
* whether metadata is shown to the user
* whether failures are structured
* whether there is double-debit risk
* whether it is marketable now

---

# 9. Feature Status Labels

Every feature must be classified using one of these labels:

* `marketable_now`
* `powerful_hidden`
* `needs_polish`
* `partial`
* `stub_or_ui_only`
* `legacy_or_gated`
* `risky`
* `unknown`

Definitions:

## marketable_now

The feature appears real, useful, reasonably understandable, and suitable to show users or prospects now.

## powerful_hidden

The feature is valuable but buried, poorly explained, hard to find, or under-marketed.

## needs_polish

The feature works or mostly works but needs UX, copy, visual, reliability, or conversion improvements.

## partial

Some real implementation exists, but the feature is not fully complete or not clearly end-to-end.

## stub_or_ui_only

The UI exists but the backend, persistence, integration, or real execution path is missing or unclear.

## legacy_or_gated

The feature is old, experimental, hidden, behind labs, or should not be exposed to normal users.

## risky

The feature may create trust, cost, security, billing, reliability, or user-confusion risk.

## unknown

Codex could not determine the status with available inspection.

Do not inflate statuses.

If it is only UI, say UI-only.

If it has database tables but no clear user journey, say partial.

If it is powerful but confusing, say powerful but confusing.

---

# 10. Priority Scores

Every major feature should receive these scores:

```txt
marketing_priority_1_to_5
revenue_priority_1_to_5
fix_priority_1_to_5
strategic_value_1_to_5
risk_level_low_medium_high_critical
```

Use this meaning:

* 5 = extremely important
* 4 = high
* 3 = medium
* 2 = low
* 1 = minor

Risk levels:

* low
* medium
* high
* critical

---

# 11. Required Output Structure

Codex must expand this repo into the following structure:

```txt
README.md

executive-map/
  arsenal-platform-overview.md
  platform-galaxy.md
  billion-dollar-features.md
  revenue-map.md
  non-coder-platform-guide.md

data/
  feature-inventory.csv
  route-map.csv
  service-map.csv
  ai-routing-map.csv
  edge-functions.csv
  database-map.csv
  monetization-surfaces.csv
  admin-control-map.csv
  risk-register.csv
  screenshot-shotlist.csv

diagrams/
  platform-galaxy.mmd
  ai-routing-control-plane.mmd
  business-spaces-revenue-engine.mmd
  creator-marketplace-loop.mmd
  user-activation-funnel.mmd
  admin-control-plane.mmd
  route-service-database-map.mmd

visuals/
  screenshot-shotlist.md
  layout-concepts.md
  poster-wireframes.md
  investor-visual-concepts.md
  social-visual-concepts.md

backlog/
  risks-and-cleanup.md
  codex-priority-backlog.md
  marketing-priorities.md
  revenue-priorities.md
  next-30-day-build-plan.md

exports/
  platform-map.json
  platform-summary-for-noncoders.md
  codex-final-report.md
```

Codex may add more files if useful, but must create at least the files above.

---

# 12. Feature Inventory CSV Schema

`data/feature-inventory.csv` must include these columns:

```csv
feature_id,feature_name,category,route,user_type,business_value,status,frontend_files,component_files,service_files,edge_functions,database_tables,auth_required,plan_or_tier_gate,credit_metering_status,ai_route_or_provider,admin_control_surface,monetization_path,screenshot_needed,marketing_priority_1_to_5,revenue_priority_1_to_5,fix_priority_1_to_5,strategic_value_1_to_5,risk_level,evidence_notes
```

---

# 13. Route Map CSV Schema

`data/route-map.csv` must include:

```csv
route,page_file,public_or_authenticated,user_type,purpose,feature_cluster,status,nav_visible,auth_required,monetization_relevance,risk_notes
```

---

# 14. AI Routing Map CSV Schema

`data/ai-routing-map.csv` must include:

```csv
feature_name,surface,route_or_component,edge_function_or_service,uses_ai_route,provider_path,default_model_or_policy,credit_enforced,usage_logged,admin_visible,fallback_behavior,status,risk,notes
```

---

# 15. Edge Function CSV Schema

`data/edge-functions.csv` must include:

```csv
function_name,feature_owner,purpose,ai_or_non_ai,provider_path,credit_relevance,usage_logging_relevance,billing_relevance,status,risk_level,notes
```

---

# 16. Database Map CSV Schema

`data/database-map.csv` must include:

```csv
table_or_family,feature_owner,purpose,user_scoped,rls_relevance,monetization_relevance,status,risk_notes
```

---

# 17. Monetization CSV Schema

`data/monetization-surfaces.csv` must include:

```csv
surface,user_value,buyer,pricing_path,current_readiness,missing_piece,revenue_priority_1_to_5,notes
```

---

# 18. Risk Register CSV Schema

`data/risk-register.csv` must include:

```csv
risk_id,area,risk_type,severity,description,evidence,impact,recommended_fix,priority
```

Priority values:

* P0 = blocks revenue/trust
* P1 = hurts activation/conversion
* P2 = polish/clarity
* P3 = later cleanup

---

# 19. Screenshot Shotlist CSV Schema

`data/screenshot-shotlist.csv` must include:

```csv
screenshot_id,route,login_required,ui_area,purpose,caption,recommended_crop,asset_type,priority,sensitivity_notes
```

Asset type values:

* internal_map
* investor_deck
* social_post
* website
* demo_video
* sales_pdf

Do not recommend capturing private user data or secrets.

---

# 20. Required Markdown Reports

## `executive-map/arsenal-platform-overview.md`

Must explain what Arsenal is today in plain English.

Audience: Alex, investors, interns, Codex, designers, marketers.

Include:

* one-paragraph summary
* platform primitives
* how the systems connect
* what is already valuable
* what is confusing
* what should be marketed now
* what should be fixed first

## `executive-map/non-coder-platform-guide.md`

Must explain Arsenal as if the reader is not a coder.

Use visual metaphors:

* operating system
* command center
* digital workforce
* map room
* marketplace
* control plane
* vault
* factory

## `executive-map/billion-dollar-features.md`

Rank the top 25 feature clusters by company value.

For each:

* what it is
* why it matters
* who pays for it
* why it is defensible
* current code evidence
* what is missing
* how to market it
* screenshot/demo needed
* next improvement

## `executive-map/revenue-map.md`

Map all revenue paths:

* subscriptions
* credits
* credit top-ups
* Business Spaces
* Smart Solution Plans
* paid Arsenals
* Experiences
* Skills
* prompt packs
* marketplace commission
* affiliate/referral revenue
* creator payouts
* done-for-you services
* agency/white-label packages
* enterprise plans

## `backlog/codex-priority-backlog.md`

Must be directly usable for future Codex work.

Each task should include:

* title
* priority
* files likely involved
* reason
* expected impact
* risk
* tests needed
* clear definition of done

---

# 21. Required Mermaid Diagrams

Create these Mermaid files:

## `diagrams/platform-galaxy.mmd`

Show Arsenal as a system of connected primitives:

* Agents
* Business Spaces
* Z-Engine
* Instruction Lab
* Vault
* Skills
* Flows
* Arsenals
* Marketplace
* Channels
* Billing
* Admin
* AI Routing
* Users

## `diagrams/ai-routing-control-plane.mmd`

Show:

* user action
* frontend surface
* service
* edge function
* `ai-route`
* provider
* fallback
* credit ledger
* usage logging
* admin visibility

## `diagrams/business-spaces-revenue-engine.mmd`

Show:

```txt
pain point → Smart Solution Plan → ROI model → proposal → agents/automations → outputs → client portal/export → subscription/setup fee
```

## `diagrams/creator-marketplace-loop.mmd`

Show:

```txt
creator builds → publishes → user discovers → pays/uses → creator earns → Arsenal takes commission → better marketplace
```

## `diagrams/user-activation-funnel.mmd`

Show:

```txt
landing → signup → first agent → first run → save/publish → connect channel → hit limit → upgrade
```

## `diagrams/admin-control-plane.mmd`

Show admin controls for:

* users
* billing
* credits
* providers
* models
* feature visibility
* marketplace
* announcements
* usage/audit
* launch control

---

# 22. Final Report Requirements

At the end of the Codex run, create:

`exports/codex-final-report.md`

It must include:

```md
# Codex Final Report

## Production Repo Safety
- Production repo path:
- Production repo modified: yes/no
- Production repo status before:
- Production repo status after:
- Any risks:

## Atlas Repo Output
- Atlas repo path:
- Files created:
- Files changed:
- Commit hash if committed:

## Biggest 10 Findings

## Top 10 Marketable Features

## Top 10 Hidden or Under-Marketed Features

## Top 10 Revenue Opportunities

## Top 10 Risks

## Top 10 Screenshot Targets

## Best Next Codex Prompt

## Human Review Notes
```

Production repo modified must be `no`.

If it is not `no`, Codex must explain exactly what happened.

---

# 23. Commit Rules

Codex may commit and push changes only to the Arsenal Atlas repo.

Codex must not commit or push anything to the Arsenal production repo.

Suggested commit message:

```txt
docs: generate Arsenal Atlas platform cartography
```

Before committing Atlas changes, Codex should show:

```bash
git status --short
```

inside the Atlas repo.

---

# 24. Best Work Sequence

Codex should follow this sequence:

1. Identify current working directory.
2. Identify or clone the Arsenal Atlas repo.
3. Identify the Arsenal production repo location if available.
4. Confirm Arsenal production repo is read-only.
5. Record production repo `git status --short`.
6. Inspect Arsenal repo using read-only commands.
7. Generate Atlas output files in the Atlas repo only.
8. Validate CSVs and JSON are syntactically reasonable.
9. Record production repo `git status --short` again.
10. Confirm no Arsenal production repo modifications.
11. Commit Atlas repo changes only.
12. Produce final report.

---

# 25. Tone and Quality Bar

Be direct, specific, and honest.

Do not create vague strategy fluff.

Do not say a feature is complete unless code evidence supports it.

Do not say a feature is monetized unless billing, entitlement, or a credible pricing path exists.

Do not say a feature is AI-powered unless a route, service, or provider path supports that.

Do not say a feature is safe unless credit, fallback, error, and usage behavior are clear.

Codex should produce outputs useful for:

* Alex as a non-coder founder/operator
* Codex as a future implementation agent
* designers creating visuals
* marketers creating content
* investors understanding the platform
* interns learning what to screenshot or explain
* future product audits

---

# 26. Final North Star

Arsenal is the product.

Arsenal Atlas is the map room.

The goal is to transform Arsenal from a huge app that is hard to see into a clearly mapped operating system that can be improved, marketed, sold, and scaled intelligently.
