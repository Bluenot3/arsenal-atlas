# Visual Atlas

This is the visual layer of Arsenal Atlas. It is meant for Alex, designers, marketers, investors, and future Codex runs that need to see the platform as systems, screens, revenue loops, and product maps instead of long prose.

## 1. Platform Mindmap

```mermaid
mindmap
  root((Arsenal OS))
    Digital Workforce
      Agents
      Agent Builder
      Public Agents
      Channels
      Team Builder
    Business Operating System
      Business Spaces
      Smart Solution Plans
      ROI Model
      Proposal
      Night Shift
      Flex OS
      Client Portal
    Creation Engines
      Z-Engine
      Instruction Lab
      Experiences
      Admin Pages
    Memory And Proof
      Files
      Vault
      Knowledge
      Output Vault
      Replays
      Reports
    Distribution
      Arsenals
      Marketplace
      Discover
      Community
      Embeds
      Programs
    Revenue
      Subscriptions
      Credits
      Paid Arsenals
      Referral Rewards
      Creator Payouts
    Control Plane
      Admin Dashboard
      AI Route
      Provider Keys
      Model Routing
      Feature Flags
      Usage Logs
```

## 2. Feature Revenue Quadrant

```mermaid
quadrantChart
  title Arsenal feature priority by revenue and readiness
  x-axis Needs work --> Ready to sell
  y-axis Low direct revenue --> High direct revenue
  quadrant-1 Sell now
  quadrant-2 Productize next
  quadrant-3 Watch later
  quadrant-4 Polish first
  Business Spaces: [0.84, 0.95]
  Smart Solution Plans: [0.80, 0.90]
  Pricing and Credits: [0.88, 0.92]
  Admin AI Control Plane: [0.78, 0.82]
  Z-Engine Studio: [0.74, 0.80]
  Night Shift: [0.58, 0.90]
  Flex OS: [0.54, 0.84]
  Marketplace Commerce: [0.42, 0.88]
  Paid Arsenals: [0.56, 0.86]
  Experiences: [0.43, 0.68]
```

## 3. Screenshot Storyboard

```mermaid
flowchart LR
  A[1 Dashboard<br/>OS overview] --> B[2 Business Spaces<br/>B2B value]
  B --> C[3 Command Center<br/>workspace cockpit]
  C --> D[4 ROI<br/>measurable case]
  D --> E[5 Proposal<br/>sales proof]
  E --> F[6 Night Shift<br/>proactive work]
  F --> G[7 Output Vault<br/>proof layer]
  G --> H[8 Agent Builder<br/>digital worker]
  H --> I[9 Share Studio<br/>deploy everywhere]
  I --> J[10 Z-Engine<br/>creation engine]
  J --> K[11 Admin AI Map<br/>control plane]
  K --> L[12 Pricing<br/>conversion]
```

## 4. Business Spaces Screen Architecture

```mermaid
flowchart TB
  Shell[BusinessSpaceShell<br/>persistent side navigation] --> Overview[Overview<br/>status, readiness, next actions]
  Shell --> Command[Command Center<br/>business cockpit]
  Shell --> Planning[ROI + Smart Solution Plan<br/>value model]
  Shell --> Proposal[Proposal / Launch Kit<br/>buyer-facing proof]
  Shell --> Staff[Agents + AI Staff<br/>digital workforce]
  Shell --> Work[Flex OS / Work Queue / Assignments<br/>execution management]
  Shell --> Night[Night Shift<br/>scheduled proactive work]
  Shell --> Vault[Output Vault<br/>files, replays, proof artifacts]
  Shell --> Portal[Client Portal / Export<br/>external deliverables]
  Overview --> Planning
  Planning --> Proposal
  Proposal --> Staff
  Staff --> Work
  Work --> Vault
  Night --> Vault
  Vault --> Portal
  Portal --> Revenue[Paid plan, setup fee, credits]
```

## 5. Visual Reading Order

1. Start with the Platform Mindmap.
2. Show the Feature Revenue Quadrant.
3. Use the Business Spaces Screen Architecture to explain the flagship paid product.
4. Use the Screenshot Storyboard for marketing and investor capture order.
5. Use the Route Cluster Subway Map when Codex or engineering needs to understand navigation.
6. Use the Data Model Feature Families diagram when discussing backend trust and scale.
