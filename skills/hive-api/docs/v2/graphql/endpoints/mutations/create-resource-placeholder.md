# `createResourcePlaceholder`

- Type: `mutation`
- Returns: `ResourcePlaceholder!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Create a new resource placeholder for the workspace.  Resource placeholders are virtual team members that can be assigned to projects and actions before actual people are hired or designated for those roles.  IMPORTANT: Only workspace administrators can set billRate and costRate values. Regular users can only set the name and roleTagId.  Use cases: • Planning projects before hiring specific team members • Creating role-based assignments in project templates   • Resource planning and capacity management • Budgeting and cost estimation for future roles  Parameters: • name: Required. The display name for the placeholder (e.g., "Senior Developer", "Marketing Manager") • workspaceId: Required. The workspace where this placeholder will be created • roleTagId: Optional. Associates the placeholder with a specific role/skill tag • billRate: Optional. The hourly billing rate (admin only) • costRate: Optional. The hourly cost rate (admin only)  Returns: The created ResourcePlaceholder object

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `name` | `String!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `billRate` | `Float` | - | - |
| `costRate` | `Float` | - | - |
| `roleTagId` | `ID` | - | - |

## Signature

- `createResourcePlaceholder(name: String!, workspaceId: ID!, billRate: Float, costRate: Float, roleTagId: ID)` -> `ResourcePlaceholder!`
