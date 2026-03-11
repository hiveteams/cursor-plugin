# `getApprovalTemplates`

- Type: `query`
- Returns: `ApprovalTemplateConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

List all available approval templates in a workspace. Use this to discover which approval templates can be applied to actions. Templates provide pre-configured approval workflows with stages and approvers that can be reused across multiple actions.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | ID of the workspace to get templates from |
| `searchParams` | `SearchParams` | - | Optional search parameters to filter templates |
| `first` | `Int` | 20 | Maximum number of templates to return |
| `last` | `Int` | - | Return last N templates |
| `after` | `ID` | - | Cursor for pagination (return templates after this cursor) |
| `before` | `ID` | - | Cursor for pagination (return templates before this cursor) |
| `sortField` | `String` | "name" | Field to sort results by |

## Signature

- `getApprovalTemplates(workspaceId: ID!, searchParams: SearchParams, first: Int, last: Int, after: ID, before: ID, sortField: String)` -> `ApprovalTemplateConnection!`
