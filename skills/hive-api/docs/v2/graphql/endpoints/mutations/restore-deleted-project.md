# `restoreDeletedProject`

- Type: `mutation`
- Returns: `Project`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used to restore deleted projects in the trash bin  Access: Requires project access  Errors: Throws error if user doesn't have access to the project

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | - |

## Signature

- `restoreDeletedProject(projectId: ID!)` -> `Project`
