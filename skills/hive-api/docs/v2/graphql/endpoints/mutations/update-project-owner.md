# `updateProjectOwner`

- Type: `mutation`
- Returns: `Project`
- Deprecated: yes
- Deprecation reason: Use addProjectOwner or removeProjectOwner instead!
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | - |
| `ownerId` | `ID!` | - | - |
| `workspaceId` | `ID!` | - | - |

## Signature

- `updateProjectOwner(projectId: ID!, ownerId: ID!, workspaceId: ID!)` -> `Project`
