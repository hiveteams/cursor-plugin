# `updateActionAssignees`

- Type: `mutation`
- Returns: `Action`
- Deprecated: yes
- Deprecation reason: Use updateActionAssignees instead!
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update assignees for an action  Access: Requires user access to the action  Parameters:   - actionId: The ID of the action to update   - assignees: Optional array of user IDs to assign ['none'] to unassign   - placeholderAssignees: Optional array of placeholder IDs to assign   - teamAssignee: Optional team ID to assign   - rankInput: Optional rank information for repositioning   - shouldUpdateChildren: Optional flag to update child actions (default: false)   - externalAssigneeName: Optional name for external assignee   - isAutomated: Optional flag to indicate automated update  Returns: The updated action

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `assignees` | `[String!]` | - | - |
| `placeholderAssignees` | `[ID!]` | - | - |
| `teamAssignee` | `ID` | - | - |
| `rankInput` | `RankInput` | - | - |
| `shouldUpdateChildren` | `Boolean` | false | - |
| `externalAssigneeName` | `String` | - | - |
| `isAutomated` | `Boolean` | - | - |

## Signature

- `updateActionAssignees(actionId: ID!, assignees: [String!], placeholderAssignees: [ID!], teamAssignee: ID, rankInput: RankInput, shouldUpdateChildren: Boolean, externalAssigneeName: String, isAutomated: Boolean)` -> `Action`
