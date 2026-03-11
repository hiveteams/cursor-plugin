# `getGoals`

- Type: `query`
- Returns: `GoalConnection`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Retrieve goals from a workspace with optional filtering and pagination  If asked to get a specific user's goals, ensure to filter by ownerIds.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspace` | `ID!` | - | The workspace ID to retrieve goals from |
| `first` | `Int` | 60 | Maximum number of goals to return (default: 60, max: 100) |
| `last` | `Int` | - | Maximum number of goals to return from the end |
| `after` | `ID` | - | Cursor for pagination - retrieve goals after this cursor |
| `before` | `ID` | - | Cursor for pagination - retrieve goals before this cursor |
| `searchParams` | `SearchParams` | - | Search parameters for filtering by goal name |
| `sortField` | `String` | "name" | Field to sort by (default: 'name') |
| `sortOrder` | `Int` | 1 | Sort order: 1 for ascending, -1 for descending (default: 1) |
| `selector` | `JSONObject` | - | MongoDB-style selector for filtering goals. Examples: { status: 'atRisk' } to filter by status, { teamOwners: { $in: ['teamId1'] } } to filter by team owners. Multiple filters can be combined. |
| `ownerIds` | `[ID]` | - | Owners ID to filter goals by |
| `excludedIds` | `[ID]` | - | Array of goal IDs to exclude from results |
| `specificIds` | `[ID]` | - | Array of goal IDs to retrieve |

## Signature

- `getGoals(workspace: ID!, first: Int, last: Int, after: ID, before: ID, searchParams: SearchParams, sortField: String, sortOrder: Int, selector: JSONObject, ownerIds: [ID], excludedIds: [ID], specificIds: [ID])` -> `GoalConnection`
