# `getDashboards`

- Type: `query`
- Returns: `DashboardConnection`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Retrieves a paginated list of dashboards with filtering and sorting

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | 20 | - |
| `last` | `Int` | - | - |
| `after` | `ID` | - | - |
| `before` | `ID` | - | - |
| `searchParams` | `SearchParams` | - | - |
| `sortField` | `String` | "createdAt" | - |
| `sortOrder` | `Int` | 1 | - |
| `selector` | `JSONObject` | - | - |
| `excludedIds` | `[ID]` | - | - |
| `type` | `DashboardType` | - | - |

## Signature

- `getDashboards(workspaceId: ID!, first: Int, last: Int, after: ID, before: ID, searchParams: SearchParams, sortField: String, sortOrder: Int, selector: JSONObject, excludedIds: [ID], type: DashboardType)` -> `DashboardConnection`
