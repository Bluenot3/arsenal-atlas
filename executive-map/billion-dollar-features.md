# Billion-Dollar Feature Clusters


## 1. Dashboard and command center

- What it is: First operating surface for agents, Business Spaces, Vault, marketplace, guidance, and next actions.
- Why it matters: Strengthens Arsenal's activation primitive and connects to a larger operating-system loop.
- Who pays for it: authenticated user buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/DashboardPage.tsx | services/guidanceContent.ts; services/zenDaily.ts | ai-route | profiles; agents; workspace_files; announcements
- What is missing: App.tsx routes /dashboard; dashboard CTAs point to agents, marketplace, keys, knowledge, Business Spaces.
- How to market it: Activation to agents, Business Spaces, and pricing
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level medium.


## 2. Agent builder, registry, and runtime

- What it is: Core digital-worker layer with instructions, models, knowledge, actions, sharing, and runtime.
- Why it matters: Strengthens Arsenal's agents primitive and connects to a larger operating-system loop.
- Who pays for it: builder buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/AgentsPage.tsx; pages/AgentDetailPage.tsx | services/agentRegistry.ts; services/ai.ts; services/llm.ts | ai-route; fetch-knowledge-url; agent-action-execute | agents; agent_versions; agent_skills; agent_memories; knowledge_sources
- What is missing: AiSystemsMap marks agent execution live but per-agent provider mapping partial and cost risk high.
- How to market it: Subscriptions, credits, paid agents, embeds
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 3 and risk level high.


## 3. Public agents, embeds, and share studio

- What it is: Turns agents into public or embedded assets that collect leads and prove value outside the app.
- Why it matters: Strengthens Arsenal's distribution primitive and connects to a larger operating-system loop.
- Who pays for it: public visitor and builder buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/AgentPublicPage.tsx; pages/AgentSharePage.tsx | services/embedTemplates.ts; services/agentChannels.ts | agent-channel-setup; agent-channel-broadcast; ai-route | agents; agent_channels; agent_channel_messages; leads
- What is missing: Routes /agent/:id and /agents/:id/share exist; channel UI recommends unified ai-route execution.
- How to market it: Lead capture, embeds, channel upgrades, white label
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 3 and risk level medium.


## 4. Agent channels

- What it is: Deploys agents to Slack, Discord, Telegram, WhatsApp, SMS, and web surfaces.
- Why it matters: Strengthens Arsenal's channels primitive and connects to a larger operating-system loop.
- Who pays for it: business operator buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/IntegrationsPage.tsx | services/agentChannels.ts; services/businessConnectionsCenter.ts | agent-slack-webhook; agent-discord-webhook; agent-telegram-webhook; agent-whatsapp-webhook; agent-sms-webhook; agent-channel-setup | agent_channels; agent_channel_messages; operator_event_logs
- What is missing: ChannelRouting says next infra upgrade is to migrate agent.run channel execution into ai-route.
- How to market it: Paid channel deployment and Business add-ons
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 4 and risk level high.


## 5. Business Spaces command center

- What it is: B2B operating space combining profile, agents, automations, ROI, proposals, outputs, portal, and exports.
- Why it matters: Strengthens Arsenal's business_spaces primitive and connects to a larger operating-system loop.
- Who pays for it: business buyer buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/BusinessSpacesPage.tsx; pages/BusinessSpaceDetailPage.tsx | services/businessSpaces.ts; services/businessSpaceAccess.ts; services/businessSpaceCommandCenter.ts | smart-solution-plan; night-shift-gate; night-shift-run | business_spaces; business_space_night_shifts; solution_plans
- What is missing: BusinessSpaceDetailPage gates execution tabs with FeatureGate business_spaces.manage.
- How to market it: Business subscriptions, setup fees, proposals, credits
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level medium.


## 6. Smart Solution Plan and ROI estimator

- What it is: Converts pain points into modules, ROI, proposal language, and implementation plans.
- Why it matters: Strengthens Arsenal's business_spaces primitive and connects to a larger operating-system loop.
- Who pays for it: business buyer buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/BusinessSpacesPage.tsx | services/smartSolutions.ts; services/businessSpaceRoi.ts | smart-solution-plan | solution_plans; solution_plan_usage; business_spaces
- What is missing: AiSystemsMap marks Business Spaces smart-solution plans live.
- How to market it: Lead magnet, paid plan, done-for-you sales
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level medium.


## 7. Night Shift scheduled work

- What it is: Schedules or runs overnight work with gates, pricing, replay, approval policy, and output reuse.
- Why it matters: Strengthens Arsenal's automation primitive and connects to a larger operating-system loop.
- Who pays for it: business operator buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/BusinessSpaceDetailPage.tsx | services/businessSpaceNightShift.ts; services/shiftOs.ts | night-shift-gate; night-shift-run; ai-route | business_space_night_shifts; operator_event_logs; workspace_files
- What is missing: Migration adds pricing/live fields and action policy; replay keeps honest queued/running/failed states.
- How to market it: Premium automation add-on and credit usage
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 3 and risk level medium.


## 8. Flex OS operator cockpit

- What it is: Operator cockpit for roles, queues, approvals, output vault, replays, and worklogs.
- Why it matters: Strengthens Arsenal's automation primitive and connects to a larger operating-system loop.
- Who pays for it: operator and admin buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/FlexOSPage.tsx; pages/BusinessSpaceDetailPage.tsx | services/businessSpaceFlex.ts; services/flexDeploymentPacks.ts; services/executionReplayStorage.ts | ai-route; flow-executor | operator_event_logs; flow_runs; workspace_files
- What is missing: Flex includes approvals, output-vault, replay, and Vault proof linkage.
- How to market it: Operator seats, agency operations, automation credits
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 3 and risk level medium.


## 9. Business proposal, portal, export, and readiness

- What it is: Turns setup into client-facing sales and delivery material.
- Why it matters: Strengthens Arsenal's business_spaces primitive and connects to a larger operating-system loop.
- Who pays for it: business buyer buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/BusinessSpaceDetailPage.tsx | services/businessSpaceProposal.ts; services/businessSpaceExport.ts | smart-solution-plan | business_spaces; workspace_files; solution_plans
- What is missing: Detail routes expose proposal, roi, portal, export behind paidBusinessSpaceAction.
- How to market it: Proposal export, client portal, service delivery
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level low.


## 10. Z-Engine studio

- What it is: Advanced creation/reasoning studio for systems, artifacts, projects, and reusable outputs.
- Why it matters: Strengthens Arsenal's creation primitive and connects to a larger operating-system loop.
- Who pays for it: creator and operator buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/ZEngineLab.tsx | services/zEngine.ts; services/zEngineCreate.ts; services/zEngineStream.ts | z-engine-stream; ai-route; tune-assist | z_engine_projects; credit_ledger; ai_route_events
- What is missing: AiSystemsMap says zengine.generate uses credit debit/refund and prompt-class artifacts.
- How to market it: Premium builder, credits, business artifacts
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level medium.


## 11. Z-Engine motion compositions

- What it is: Generates deterministic motion/visual artifacts with preview, ZIP, Vault save, and WebM where supported.
- Why it matters: Strengthens Arsenal's creation primitive and connects to a larger operating-system loop.
- Who pays for it: creator buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/ZEngineLab.tsx | services/zEngineStream.ts; services/workspaceFiles.ts | z-engine-stream; ai-route | z_engine_projects; workspace_files
- What is missing: AiSystemsMap marks motion compositions ready with browser-native preview and no render farm.
- How to market it: Premium creative/proposal assets
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level low.


## 12. Instruction Lab and Tune

- What it is: Prompt refinement, model comparison, prompt packs, and reusable instruction assets.
- Why it matters: Strengthens Arsenal's ai_workflow primitive and connects to a larger operating-system loop.
- Who pays for it: builder buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/InstructionLabPage.tsx | services/tune.ts; services/promptPacks.ts; services/projectVaultCredits.ts | tune-assist; instruction-preview; instruction-stream; prompt-pack-enhance; prompt-pack-install | prompt_packs; prompt_pack_installs; tune_admin_config; tune_usage_logs
- What is missing: TuneAdminPanel controls tasks, models, providers, endpoints, and daily caps.
- How to market it: Prompt packs, creator assets, credits
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level medium.


## 13. Files, Workspace, Vault, and proof layer

- What it is: Memory/proof layer for uploaded files, generated outputs, replays, proposals, reports, and knowledge.
- Why it matters: Strengthens Arsenal's workspace primitive and connects to a larger operating-system loop.
- Who pays for it: builder and operator buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/FilesPage.tsx | services/workspaceFiles.ts; services/vaultArtifacts.ts; services/vaultProofLayer.ts; services/workspaceGateway.ts | workspace-fs; fetch-knowledge-url | workspace_files; workspace_file_versions; knowledge_sources; vault_remote_jobs
- What is missing: Multiple routes alias to FilesPage; workspace-fs is server-side tool endpoint.
- How to market it: Storage limits, exports, client proof
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level medium.


## 14. Knowledge retrieval and grounding

- What it is: Grounds agents and business systems with files, URLs, and reusable context.
- Why it matters: Strengthens Arsenal's knowledge primitive and connects to a larger operating-system loop.
- Who pays for it: builder buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/FilesPage.tsx; pages/AgentDetailPage.tsx | services/knowledgeRetrieval.ts; services/assistantKnowledge.ts; services/uploads.ts | fetch-knowledge-url; web-search | knowledge_sources; workspace_files
- What is missing: AiSystemsMap marks knowledge retrieval/embeddings provider and model unknown.
- How to market it: Higher-tier knowledge limits and business proof
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 4 and risk level medium.


## 15. Skills registry

- What it is: Reusable capabilities that attach to agents, workflows, and future marketplace products.
- Why it matters: Strengthens Arsenal's skills primitive and connects to a larger operating-system loop.
- Who pays for it: builder buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/SkillsPage.tsx | services/skills.ts; services/skillImport.ts; services/skillTemplates.ts | ai-route | skills; agent_skills
- What is missing: Skill mesh includes imported/native source and review/risk metadata.
- How to market it: Paid skills marketplace and agent add-ons
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 3 and risk level medium.


## 16. Automation, flows, schedules, and baskets

- What it is: Repeatable execution layer for triggers, tools, scheduled channel actions, replays, and containers.
- Why it matters: Strengthens Arsenal's automation primitive and connects to a larger operating-system loop.
- Who pays for it: operator buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/AutomationPage.tsx; pages/FlowsPage.tsx; pages/SchedulesPage.tsx; pages/BasketsPage.tsx | services/flows.ts; services/flowValidator.ts; services/schedules.ts; services/scheduledChannelActions.ts | flow-executor; flow-tool-execute; schedule-tick; reminder-tick | flows; flow_runs; flow_schedules; baskets; basket_items
- What is missing: schedule-tick invokes flow-executor; execution monetization/entitlement needs deeper audit.
- How to market it: Automation credits, schedules, integrations
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 4 and risk level high.


## 17. Arsenals, Fleet Architect, and product bundles

- What it is: Bundles agents, skills, knowledge, workflows, experiences, pages, and products into distributable assets.
- Why it matters: Strengthens Arsenal's arsenals primitive and connects to a larger operating-system loop.
- Who pays for it: creator and buyer buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/ArsenalsPage.tsx; pages/ArsenalEditorPage.tsx; pages/FleetArchitectPage.tsx; pages/ArsenalPublicPage.tsx | services/arsenalTemplates.ts; services/fleetArchitect.ts; services/arsenalPaidAccess.ts | ai-route; create-arsenal-access-checkout; confirm-arsenal-access | arsenals; arsenal_pages; arsenal_products; arsenal_access_grants
- What is missing: Paid Arsenal checkout/confirmation and access grants exist.
- How to market it: Paid Arsenals, creator bundles, marketplace commission
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 3 and risk level medium.


## 18. Marketplace, Discover, and community

- What it is: Distribution loop for agents, arsenals, prompt packs, skills, templates, and social proof.
- Why it matters: Strengthens Arsenal's marketplace primitive and connects to a larger operating-system loop.
- Who pays for it: creator and buyer buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/MarketplacePage.tsx; pages/DiscoverPage.tsx; pages/CommunityPage.tsx | services/discover.ts; services/store.ts; services/promptPacks.ts | agent-community-post; prompt-pack-install; prompt-pack-enhance | community_posts; community_categories; discover_likes; prompt_packs; prompt_pack_installs
- What is missing: Marketplace pieces exist, but paid listing and payout journey need productization.
- How to market it: Paid listings, creator commission, prompt-pack sales
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 4 and risk level medium.


## 19. Experiences generator and entitlements

- What it is: Productized interactive tools or guided journeys with entitlement potential.
- Why it matters: Strengthens Arsenal's experiences primitive and connects to a larger operating-system loop.
- Who pays for it: creator and buyer buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/ExperiencesPage.tsx; pages/ExperienceEditorPage.tsx | services/experiences.ts; services/experienceEntitlements.ts; services/experienceUsageStore.ts | experience-generate; experience-entitlement | experience_usage_events; experience_usage_monthly
- What is missing: AdminExperiencesPanel controls OpenAI model/temperature for experience-generate.
- How to market it: Paid experiences and usage limits
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 4 and risk level medium.


## 20. Pricing, subscriptions, credits, and top-ups

- What it is: Direct revenue spine for Plus, Pro, Premium, credit packs, portal management, and Stripe webhooks.
- Why it matters: Strengthens Arsenal's monetization primitive and connects to a larger operating-system loop.
- Who pays for it: buyer buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/PricingPage.tsx; pages/ProfilePage.tsx | services/stripeConfig.ts; services/arsenalCredits.ts; services/platformCreditRules.ts | create-checkout; customer-portal; check-subscription; create-credit-topup-checkout; stripe-webhook | credit_accounts; credit_ledger; credit_settings; credit_topup_packs; subscribers
- What is missing: RevenueReadinessPanel marks subscription, portal, credit top-up, settings, and webhook paths ready.
- How to market it: Subscriptions, top-ups, usage metering
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level medium.


## 21. Referral rewards, partners, and creator payouts

- What it is: Acquisition/payout loop for referrals, commissions, Stripe Connect, partner applications, and creator earnings.
- Why it matters: Strengthens Arsenal's monetization primitive and connects to a larger operating-system loop.
- Who pays for it: partner and creator buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/PartnersPage.tsx; pages/PartnerDashboardPage.tsx; pages/RevenuePage.tsx; pages/AdminPartnersPage.tsx | services/referralRewards.ts; services/arsenalPaidAccess.ts | create-connect-account; stripe-webhook | partner_profiles; partner_referrals; partner_commissions; referral_program_settings
- What is missing: AdminReferralRewardsPanel tracks commission statuses and settings; Connect onboarding is used by revenue/profile surfaces.
- How to market it: Affiliate revenue, creator payouts, marketplace commission
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level medium.


## 22. Admin dashboard and control plane

- What it is: Business governance layer for users, billing, credits, providers, models, flags, marketplace, usage, audit, and communications.
- Why it matters: Strengthens Arsenal's admin primitive and connects to a larger operating-system loop.
- Who pays for it: admin buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/AdminDashboard.tsx; pages/AdminPagesPage.tsx; pages/AdminPartnersPage.tsx | services/adminAudit.ts; services/accessControl.ts; services/adminPages.ts | admin-users; verify-provider-key; create-connect-account; ai-route | platform_admins; admin_api_keys; platform_feature_flags; admin_audit_log; admin_app_pages
- What is missing: AdminDashboard tabs include users, keys, providers, Z-Engine, tier defaults, limits, usage, audit, credits, operators, partners, pages.
- How to market it: Operational leverage and reliable paid AI
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level high.


## 23. AI Route control plane

- What it is: Canonical server-side AI policy path for provider keys, model routing, credits, usage, fallbacks, and admin test routing.
- Why it matters: Strengthens Arsenal's ai_control primitive and connects to a larger operating-system loop.
- Who pays for it: platform buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/AdminDashboard.tsx | services/aiRouteClient.ts; services/apiRouter.ts; services/modelCatalog.ts | ai-route | admin_api_keys; tier_key_defaults; model_key_routes; ai_route_events; credit_ledger; usage_limit_configs
- What is missing: ai-route checks admins, feature flags, tier gates, daily limits, admin keys, fallbacks, credits, and events.
- How to market it: Credit-safe AI usage and provider margin
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 3 and risk level high.


## 24. Media generation and Arsenal Senses

- What it is: Image/video generation plus perception routes for captions, transcription, object detection, summarization, and realtime rooms.
- Why it matters: Strengthens Arsenal's ai_media primitive and connects to a larger operating-system loop.
- Who pays for it: creator and business buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: components/BrandKitGenerator.tsx; components/ChatInterface.tsx | services/ai.ts; services/mediaAnalysis.ts; services/cloudflareVideoModels.ts; services/realtimeRooms.ts | ai-route; media-analyze; realtime-room; openai-image-probe | ai_route_events; credit_ledger; platform_feature_flags
- What is missing: AiSystemsMap says image.generate charges 1 credit and video.generate is Pro/Premium/admin with 8s cap.
- How to market it: Media credits and Pro/Premium gates
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 2 and risk level medium.


## 25. Business integrations and connections center

- What it is: Maps OAuth/provider/channel/business app connections into automation and deployment readiness.
- Why it matters: Strengthens Arsenal's integrations primitive and connects to a larger operating-system loop.
- Who pays for it: business operator buyers, creators, agencies, or admins depending on the surface.
- Why it is defensible: Combines product surface, route/service implementation, database state, and platform context rather than being a single prompt wrapper.
- Current code evidence: pages/IntegrationsPage.tsx | services/businessConnectionsCenter.ts; services/notionConnector.ts; services/linkedinConnector.ts | notion-oauth; linkedin-oauth; linkedin-publish; verify-provider-key | user_oauth_connections; linkedin_autopost_posts; agent_channels
- What is missing: businessConnectionsCenter enumerates AI providers and connector statuses.
- How to market it: Advanced connectors, agency setup, enterprise
- Screenshot/demo needed: yes
- Next improvement: Address fix priority 4 and risk level medium.
