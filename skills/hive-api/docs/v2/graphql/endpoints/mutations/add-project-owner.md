# `addProjectOwner`

- Type: `mutation`
- Returns: `Project`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Add a user to the project owner list.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | Project ID to add owner to |
| `ownerId` | `ID!` | - | User ID to add as owner |
| `workspaceId` | `ID!` | - | Workspace ID of the project |

## Signature

- `addProjectOwner(projectId: ID!, ownerId: ID!, workspaceId: ID!)` -> `Project`
