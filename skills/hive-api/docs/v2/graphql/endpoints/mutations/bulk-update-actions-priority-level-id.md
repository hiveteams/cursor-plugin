# `bulkUpdateActionsPriorityLevelId`

- Type: `mutation`
- Returns: `Boolean`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update priority level for multiple actions at once.  Always call getPriorityLevels before calling this function to get the priority level IDs and ensure that priorityLevelId exists.  Access: Requires user access to all actions  Parameters:   - actionIds: Array of action IDs to update   - workspaceId: The ID of the workspace   - priorityLevelId: The ID of the priority level to set (null to unset)   - shouldUpdateRecurring: Optional flag to update recurring instances  Returns: Boolean indicating success

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `priorityLevelId` | `ID` | - | - |
| `shouldUpdateRecurring` | `Boolean` | - | - |
| `rank` | `Float` | - | - |

## Signature

- `bulkUpdateActionsPriorityLevelId(actionIds: [ID!]!, workspaceId: ID!, priorityLevelId: ID, shouldUpdateRecurring: Boolean, rank: Float)` -> `Boolean`
