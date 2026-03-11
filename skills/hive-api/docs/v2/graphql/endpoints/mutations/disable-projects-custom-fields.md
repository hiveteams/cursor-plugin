# `disableProjectsCustomFields`

- Type: `mutation`
- Returns: `[Project!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Disables custom fields for specific projects.  This should be used to disable only project itemType custom fields.  Parameters:   - customFieldIds: Required. The IDs of the custom fields to disable   - projectIds: Required. The IDs of the projects to disable the custom fields for   - workspaceId: Required. The ID of the workspace to disable the custom fields for

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `customFieldIds` | `[ID!]!` | - | - |
| `projectIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |

## Signature

- `disableProjectsCustomFields(customFieldIds: [ID!]!, projectIds: [ID!]!, workspaceId: ID!)` -> `[Project!]!`
