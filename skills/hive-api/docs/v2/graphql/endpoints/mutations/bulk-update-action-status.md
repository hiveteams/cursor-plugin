# `bulkUpdateActionStatus`

- Type: `mutation`
- Returns: `Boolean`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update status for multiple actions at once.  ALWAYS look for existing statuses in the project. Only add statuses if they're definitely different from the existing ones. Otherwise, don't add them and use the existing ones that have the same meaning.  Examples: Project has statuses: "To Do", "In Progress", "Review feedback", "Done"    1)     - User asks to update statuses: "update to feedback"     - Result: Action statuses are updated to "Review feedback"    2)     - User asks to update statuses: "set in progress"     - Result: Action statuses are updated to "In Progress"    3)     - User asks to update statuses: "mark as completed"     - Result: Action statuses are updated to "Done"  Access: Requires user access to all actions  Parameters:   - actionIds: Array of action IDs to update   - workspaceId: The ID of the workspace   - status: The new status to set   - rankInput: Optional rank information for repositioning   - shouldUpdateChildren: Optional flag to update child actions  Returns: Boolean indicating success

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `status` | `String!` | - | - |
| `rankInput` | `RankInput` | - | - |
| `shouldUpdateChildren` | `Boolean` | - | - |

## Signature

- `bulkUpdateActionStatus(actionIds: [ID!]!, workspaceId: ID!, status: String!, rankInput: RankInput, shouldUpdateChildren: Boolean)` -> `Boolean`
