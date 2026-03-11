# `disableActionCustomFields`

- Type: `mutation`
- Returns: `[Project!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Disables custom fields for actions in specific projects.  This should be used to disable only action itemType custom fields.  Parameters:   - customFieldIds: Required. The IDs of the custom fields to disable   - projectIds: Required. The IDs of the projects to disable the custom fields for   - workspaceId: Required. The ID of the workspace to disable the custom fields for   - removeFromActions: Optional. Whether to remove the custom fields from the actions

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `customFieldIds` | `[ID!]!` | - | - |
| `projectIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `removeFromActions` | `Boolean` | false | - |

## Signature

- `disableActionCustomFields(customFieldIds: [ID!]!, projectIds: [ID!]!, workspaceId: ID!, removeFromActions: Boolean)` -> `[Project!]!`
