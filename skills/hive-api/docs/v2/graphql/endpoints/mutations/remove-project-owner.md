# `removeProjectOwner`

- Type: `mutation`
- Returns: `Project`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Remove a user from the project owner list.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | Project ID to remove owner from |
| `ownerId` | `ID!` | - | User ID to remove as owner |
| `workspaceId` | `ID!` | - | Workspace ID of the project |

## Signature

- `removeProjectOwner(projectId: ID!, ownerId: ID!, workspaceId: ID!)` -> `Project`
