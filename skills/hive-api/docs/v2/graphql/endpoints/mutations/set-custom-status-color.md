# `setCustomStatusColor`

- Type: `mutation`
- Returns: `Workspace`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

This mutation is used to set the color of a custom status. ALWAYS run it after the addStatusToProjectView mutation (adding new status) to set the color of the new status. Pick the color that would logically fit the status name (e.g. "In Progress" -> "blue", "Done" -> "green", etc.).  Also could be used separately to update or remove the color of the status.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | The ID of the workspace |
| `status` | `String!` | - | The name of the status |
| `color` | `String` | - | The color of the status in HEX format. If not provided, the color will be removed. |

## Signature

- `setCustomStatusColor(workspaceId: ID!, status: String!, color: String)` -> `Workspace`
