# `getWorkspace`

- Type: `query`
- Returns: `Workspace`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get a workspace by ID  Access: Requires workspace access or be a member of the workspace  Parameters:   - workspaceId: The ID of the workspace to retrieve  Returns: The requested workspace

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |

## Signature

- `getWorkspace(workspaceId: ID!)` -> `Workspace`
