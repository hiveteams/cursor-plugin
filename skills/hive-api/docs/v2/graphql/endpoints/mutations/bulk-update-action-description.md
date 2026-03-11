# `bulkUpdateActionDescription`

- Type: `mutation`
- Returns: `Boolean`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update descriptions for multiple actions at once  Access: Requires user access to all actions  Parameters:   - actionIds: Array of action IDs to update   - workspaceId: The ID of the workspace   - description: The new description to set. Must be a valid HTML string. Use the corresponding markdown (<ul> for lists, <code> for code blocks, etc). Code blocks should be contained in a single tag.  Returns: Boolean indicating success

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `description` | `String!` | - | - |
| `isCollabUpdate` | `Boolean` | - | - |
| `forcePersistCollab` | `Boolean` | - | - |

## Signature

- `bulkUpdateActionDescription(actionIds: [ID!]!, workspaceId: ID!, description: String!, isCollabUpdate: Boolean, forcePersistCollab: Boolean)` -> `Boolean`
