# `bulkUpdateActionsTitles`

- Type: `mutation`
- Returns: `Boolean`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update different titles for multiple actions at once  Access: Requires user access to all actions  Parameters:   - actionTitleUpdates: Array of {actionId, title} pairs to update   - workspaceId: The ID of the workspace  Behavior:   - Empty titles are not allowed (will throw error)   - Only updates the specific actions in the batch (does not update recurring series)  Returns: Boolean indicating success

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionTitleUpdates` | `[ActionTitleUpdateInput!]!` | - | - |
| `workspaceId` | `ID!` | - | - |

## Signature

- `bulkUpdateActionsTitles(actionTitleUpdates: [ActionTitleUpdateInput!]!, workspaceId: ID!)` -> `Boolean`
