# `bulkUpdateActionLabels`

- Type: `mutation`
- Returns: `Boolean`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update labels for the provided action IDs.  Access: Requires user access to all actions  Parameters:   - actionIds: Array of action IDs to update   - workspaceId: The ID of the workspace   - labelIds: Array of label IDs to add or remove   - operation: The operation to perform (ADD, REMOVE)   - shouldUpdateChildren: Boolean to update children   - shouldUpdateRecurring: Boolean to update recurring  Returns: Boolean indicating success

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `labelIds` | `[ID!]!` | - | - |
| `operation` | `BatchOperation!` | - | - |
| `shouldUpdateChildren` | `Boolean` | - | - |
| `shouldUpdateRecurring` | `Boolean` | - | - |
| `isAutomated` | `Boolean` | - | - |

## Signature

- `bulkUpdateActionLabels(actionIds: [ID!]!, workspaceId: ID!, labelIds: [ID!]!, operation: BatchOperation!, shouldUpdateChildren: Boolean, shouldUpdateRecurring: Boolean, isAutomated: Boolean)` -> `Boolean`
