# `bulkUpdateActionsAssignees`

- Type: `mutation`
- Returns: `Boolean`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update actions assignees in bulk  IMPORTANT: - Set operation will override existing assignees and placeholder assignees. - Add/pull operation will add/pull assignees and placeholder assignees to existing ones.  The set and add/pull parameters are mutually exclusive. If you want to set the assignees, you should not pass any of the add/pull parameters. If you want to add or pull assignees, you should not pass the set parameter.  Access: Requires user access to all actions  Parameters:   - actionIds: Array of action IDs to update   - workspaceId: The ID of the workspace   - assigneesToSet: Array of user IDs to assign   - assigneesToAdd: Array of user IDs to add   - assigneesToPull: Array of user IDs to remove   - teamAssignee: The ID of the team to assign   - placeholderAssigneesToSet: Array of placeholder IDs to assign   - placeholderAssigneesToAdd: Array of placeholder IDs to add   - placeholderAssigneesToPull: Array of placeholder IDs to remove   - privacy: The privacy of the action   - shouldUpdateChildren: Boolean to update children   - shouldUpdateRecurring: Boolean to update recurring   - updatePlaceholderAssignees: Boolean to update placeholder assignees   - currentAssigneeId: The ID of the current assignee  Returns: Boolean indicating success

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `assigneesToSet` | `[ID!]` | [] | - |
| `assigneesToAdd` | `[ID!]` | [] | - |
| `assigneesToPull` | `[ID!]` | [] | - |
| `teamAssignee` | `ID` | - | - |
| `placeholderAssigneesToSet` | `[ID!]` | [] | - |
| `placeholderAssigneesToAdd` | `[ID!]` | [] | - |
| `placeholderAssigneesToPull` | `[ID!]` | [] | - |
| `privacy` | `ActionPrivacy` | - | - |
| `shouldUpdateChildren` | `Boolean` | - | - |
| `shouldUpdateRecurring` | `Boolean` | - | - |
| `updatePlaceholderAssignees` | `Boolean` | false | - |
| `currentAssigneeId` | `ID` | - | - |

## Signature

- `bulkUpdateActionsAssignees(actionIds: [ID!]!, workspaceId: ID!, assigneesToSet: [ID!], assigneesToAdd: [ID!], assigneesToPull: [ID!], teamAssignee: ID, placeholderAssigneesToSet: [ID!], placeholderAssigneesToAdd: [ID!], placeholderAssigneesToPull: [ID!], privacy: ActionPrivacy, shouldUpdateChildren: Boolean, shouldUpdateRecurring: Boolean, updatePlaceholderAssignees: Boolean, currentAssigneeId: ID)` -> `Boolean`
