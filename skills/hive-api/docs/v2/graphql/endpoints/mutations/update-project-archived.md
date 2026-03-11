# `updateProjectArchived`

- Type: `mutation`
- Returns: `Project`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update project archived status  Access: Requires user access to the project  Parameters:   - projectId: The ID of the project to update   - archived: The new archived state to set   - includeChildren: Whether to include children in the update  Returns: The updated project

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | - |
| `archived` | `Boolean!` | - | - |
| `includeChildren` | `Boolean` | false | - |

## Signature

- `updateProjectArchived(projectId: ID!, archived: Boolean!, includeChildren: Boolean)` -> `Project`
