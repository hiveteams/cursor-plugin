# `getDashboardWidgets`

- Type: `query`
- Returns: `[DashboardWidget!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Retrieves all widgets associated with a specific dashboard. Common use cases: 1. Loading a dashboard's initial state 2. Refreshing dashboard content 3. Exporting dashboard configuration

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `dashboardId` | `ID!` | - | - |

## Signature

- `getDashboardWidgets(dashboardId: ID!)` -> `[DashboardWidget!]!`
