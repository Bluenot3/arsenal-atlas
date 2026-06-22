# Screen Layout Blueprints

These are layout-level maps, not production UI instructions. They show what each major screen should communicate in a screenshot, deck, or future redesign.

## Dashboard / Command Center

```txt
┌────────────────────────────────────────────────────────────────────┐
│ Global shell: logo, search/command, credits, user menu              │
├───────────────┬─────────────────────────────────────┬──────────────┤
│ Left nav      │ Primary mission panel               │ Right rail    │
│ - Dashboard   │ - next best action                  │ - credits     │
│ - Agents      │ - recent agents / spaces            │ - system tips │
│ - Spaces      │ - fast launch buttons               │ - upgrade CTA │
│ - Vault       │                                     │              │
├───────────────┴─────────────────────────────────────┴──────────────┤
│ Feature tiles: Agents | Business Spaces | Z-Engine | Vault | Market │
└────────────────────────────────────────────────────────────────────┘
```

Screenshot purpose: prove Arsenal is an operating system, not a single tool.

## Business Spaces Command Center

```txt
┌────────────────────────────────────────────────────────────────────┐
│ Business header: name, status, readiness, upgrade/execution state   │
├─────────────┬───────────────────────────────────────┬──────────────┤
│ Space nav   │ Command cockpit                       │ Proof rail    │
│ Overview    │ - business goal                       │ - ROI         │
│ ROI         │ - next actions                        │ - proposal    │
│ Proposal    │ - agents/work queue                   │ - outputs     │
│ Night Shift │ - blockers/approvals                  │ - portal      │
│ Vault       │ - launch readiness                    │              │
└─────────────┴───────────────────────────────────────┴──────────────┘
```

Screenshot purpose: show the flagship paid product and revenue path.

## Smart Solution Plan / ROI

```txt
┌────────────────────────────────────────────────────────────────────┐
│ Pain point + selected modules                                      │
├──────────────────────┬──────────────────────┬──────────────────────┤
│ Time saved           │ Annual value         │ Payback / ROI         │
├──────────────────────┴──────────────────────┴──────────────────────┤
│ Module cards: sales, support, onboarding, reporting, operations     │
├────────────────────────────────────────────────────────────────────┤
│ CTA: generate proposal | create Business Space | upgrade            │
└────────────────────────────────────────────────────────────────────┘
```

Screenshot purpose: make the business value measurable.

## Agent Builder

```txt
┌────────────────────────────────────────────────────────────────────┐
│ Agent identity: name, role, status, publish/share state             │
├──────────────┬──────────────────────────────────────┬───────────────┤
│ Config tabs  │ Instruction / tools / knowledge form │ Live preview   │
│ Instructions │                                      │ Chat test      │
│ Model        │                                      │ Run metadata   │
│ Knowledge    │                                      │ Save/version   │
│ Channels     │                                      │               │
└──────────────┴──────────────────────────────────────┴───────────────┘
```

Screenshot purpose: show a digital worker as configurable infrastructure.

## Z-Engine Studio

```txt
┌────────────────────────────────────────────────────────────────────┐
│ Prompt mode + model route + project recovery state                  │
├─────────────────────────────┬──────────────────────────────────────┤
│ Builder prompt / controls   │ Artifact preview                     │
│ - mode                      │ - app / motion / system / doc        │
│ - files/context             │ - save to Vault                      │
│ - generate/repair           │ - export/download                    │
└─────────────────────────────┴──────────────────────────────────────┘
```

Screenshot purpose: show Arsenal creating reusable assets.

## Files / Vault

```txt
┌────────────────────────────────────────────────────────────────────┐
│ Vault header: current path, search, filters, upload/create          │
├───────────────┬──────────────────────────────────────┬──────────────┤
│ File tree     │ File/artifact grid                   │ Preview rail  │
│ Spaces        │ - generated outputs                  │ metadata      │
│ Replays       │ - proposals                          │ provenance    │
│ Knowledge     │ - reports                            │ reuse CTA     │
└───────────────┴──────────────────────────────────────┴──────────────┘
```

Screenshot purpose: show that AI work leaves proof and reusable assets.

## Admin AI Systems Map

```txt
┌────────────────────────────────────────────────────────────────────┐
│ Admin shell: role, view-as, audit context                           │
├──────────────┬───────────────────────────────────────┬──────────────┤
│ Admin tabs   │ AI systems table                      │ Route health  │
│ Keys         │ - feature                             │ events        │
│ Providers    │ - provider/model                      │ fallbacks     │
│ Models       │ - credit/logging                      │ failures      │
│ Limits       │ - risk/readiness                      │              │
└──────────────┴───────────────────────────────────────┴──────────────┘
```

Screenshot purpose: prove AI governance, cost control, and enterprise readiness.

## Marketplace / Discover

```txt
┌────────────────────────────────────────────────────────────────────┐
│ Marketplace header: categories, search, creator CTA                 │
├──────────────────────┬──────────────────────┬──────────────────────┤
│ Agents               │ Prompt Packs         │ Arsenals             │
│ install / preview    │ install / save       │ paid access / demo   │
├──────────────────────┴──────────────────────┴──────────────────────┤
│ Trust row: reviews, creator, usage, admin reviewed, pricing         │
└────────────────────────────────────────────────────────────────────┘
```

Screenshot purpose: show distribution and future creator economy.
