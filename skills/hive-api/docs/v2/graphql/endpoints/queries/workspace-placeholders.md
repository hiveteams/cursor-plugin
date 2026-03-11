# `workspacePlaceholders`

- Type: `query`
- Returns: `[ResourcePlaceholder!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get all resource placeholders for a workspace  Access: Requires user access to the workspace  Parameters:   - workspaceId: The ID of the workspace   - specificIds: Array of specific resource placeholder IDs to return  Returns: Array of ResourcePlaceholder objects

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `specificIds` | `[ID!]` | - | - |

## Signature

- `workspacePlaceholders(workspaceId: ID!, specificIds: [ID!])` -> `[ResourcePlaceholder!]!`
