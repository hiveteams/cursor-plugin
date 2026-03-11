# `bulkUpdateActionsTitle`

- Type: `mutation`
- Returns: `Boolean`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update titles for multiple actions at once  Access: Requires user access to all actions  Parameters:   - actionIds: Array of action IDs to update   - workspaceId: The ID of the workspace   - title: The new title to set   - shouldUpdateRecurring: Optional flag to update recurring instances   - allowEmpty: Optional flag to allow empty titles  Returns: Boolean indicating success

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `title` | `String!` | - | - |
| `shouldUpdateRecurring` | `Boolean` | - | - |
| `allowEmpty` | `Boolean` | - | - |

## Signature

- `bulkUpdateActionsTitle(actionIds: [ID!]!, workspaceId: ID!, title: String!, shouldUpdateRecurring: Boolean, allowEmpty: Boolean)` -> `Boolean`
