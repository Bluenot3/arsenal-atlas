# Data Visualization Dashboard Spec

This file describes the visuals an Atlas dashboard should render from the CSV files.

## Data Sources

- `data/feature-inventory.csv`
- `data/route-map.csv`
- `data/ai-routing-map.csv`
- `data/edge-functions.csv`
- `data/database-map.csv`
- `data/monetization-surfaces.csv`
- `data/admin-control-map.csv`
- `data/risk-register.csv`
- `data/screenshot-shotlist.csv`

## Recommended Charts

| Chart | Source | Purpose |
| --- | --- | --- |
| Feature status donut | feature-inventory | Show how many features are marketable, partial, risky, hidden, or unknown. |
| Revenue priority bar | feature-inventory | Rank features by revenue priority. |
| Risk severity heatmap | risk-register | Show high-risk areas by severity and priority. |
| Route cluster subway | route-map | Show user navigation by feature cluster. |
| AI route governance table | ai-routing-map | Show canonical vs dedicated/direct AI paths. |
| Edge function ownership treemap | edge-functions | Show which domains own backend execution. |
| Database family map | database-map | Show which tables support revenue-critical features. |
| Screenshot capture board | screenshot-shotlist | Track screenshot targets by priority and asset type. |

## Dashboard Layout

```txt
┌────────────────────────────────────────────────────────────────────┐
│ Atlas Visual Dashboard                                             │
├──────────────────────┬──────────────────────┬──────────────────────┤
│ Features mapped      │ Revenue-priority avg │ High/P0 risks         │
├──────────────────────┴──────────────────────┴──────────────────────┤
│ Feature status donut       | Revenue priority ranked bar            │
├────────────────────────────┬───────────────────────────────────────┤
│ AI route governance table  │ Risk severity heatmap                 │
├────────────────────────────┴───────────────────────────────────────┤
│ Route cluster subway / Business Spaces revenue engine               │
└────────────────────────────────────────────────────────────────────┘
```

## Filters

- Feature category.
- Status.
- Revenue priority.
- Risk level.
- Auth required.
- AI route/provider path.
- Screenshot priority.

## KPI Cards

- Total mapped features.
- Marketable-now features.
- P0/P1 risks.
- Revenue-priority 5 surfaces.
- AI features not fully on ai-route.
- Screenshot P0 targets.
