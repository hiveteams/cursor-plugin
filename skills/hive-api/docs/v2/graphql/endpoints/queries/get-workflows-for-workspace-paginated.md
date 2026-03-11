# `getWorkflowsForWorkspacePaginated`

- Type: `query`
- Returns: `WorkflowConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get all action templates for a workspace

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | 20 | - |
| `last` | `Int` | - | - |
| `before` | `ID` | - | - |
| `after` | `ID` | - | - |
| `searchParams` | `SearchParams` | - | - |

## Signature

- `getWorkflowsForWorkspacePaginated(workspaceId: ID!, first: Int, last: Int, before: ID, after: ID, searchParams: SearchParams)` -> `WorkflowConnection!`
