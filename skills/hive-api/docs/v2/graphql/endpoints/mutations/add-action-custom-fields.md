# `addActionCustomFields`

- Type: `mutation`
- Returns: `[Project!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Enables custom fields for actions in specific projects.  This should be used to enable only action itemType custom fields.  Parameters:   - ids: Required. The IDs of the custom fields to enable   - projectIds: Required. The IDs of the projects to enable the custom fields for   - workspaceId: Required. The ID of the workspace to enable the custom fields for

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `ids` | `[ID!]!` | - | - |
| `projectIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |

## Signature

- `addActionCustomFields(ids: [ID!]!, projectIds: [ID!]!, workspaceId: ID!)` -> `[Project!]!`
