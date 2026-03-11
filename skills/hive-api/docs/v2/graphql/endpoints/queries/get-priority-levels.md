# `getPriorityLevels`

- Type: `query`
- Returns: `[PriorityLevel!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get priority levels for a workspace or specific entities  Access: Requires workspace access  Parameters:   - workspaceId: The ID of the workspace   - formId: Optional form ID to filter priority levels   - actionId: Optional action ID to filter priority levels   - specificIds: Optional array of specific priority level IDs to include   - excludedIds: Optional array of priority level IDs to exclude  Returns: Array of priority levels

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `formId` | `ID` | - | - |
| `actionId` | `ID` | - | - |
| `specificIds` | `[ID]` | - | - |
| `excludedIds` | `[ID]` | - | - |

## Signature

- `getPriorityLevels(workspaceId: ID!, formId: ID, actionId: ID, specificIds: [ID], excludedIds: [ID])` -> `[PriorityLevel!]!`
