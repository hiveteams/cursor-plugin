# `copyAction`

- Type: `mutation`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Copy/duplicate an action including its subactions, attachments, approval rounds, and dependencies. Returns the newly created action.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | The ID of the action to duplicate |
| `shouldAddCopySign` | `Boolean!` | - | Whether to append '(copy)' to the duplicated action's title |
| `assigneeForSubaction` | `[String!]` | - | User IDs to assign as assignees on copied subactions (empty array keeps original assignees) |
| `isPlaceholdersAssignee` | `Boolean!` | - | Whether the assigneeForSubaction values are placeholder IDs rather than user IDs |
| `lowestRank` | `Boolean` | - | Place the copied action at the lowest rank (bottom of list). Defaults to false (top of list) |
| `projectId` | `ID` | - | Optional target project ID. When provided, copies the action into a different project and clears project-specific fields (sections, phases) |

## Signature

- `copyAction(actionId: ID!, shouldAddCopySign: Boolean!, assigneeForSubaction: [String!], isPlaceholdersAssignee: Boolean!, lowestRank: Boolean, projectId: ID)` -> `Action`
