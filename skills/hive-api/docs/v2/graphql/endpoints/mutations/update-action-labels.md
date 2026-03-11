# `updateActionLabels`

- Type: `mutation`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update labels for an action  Access: Requires user access to the action  Parameters:   - actionId: The ID of the action to update   - labels: Optional array of label IDs to set, ['none'] to remove all   - rankInput: Optional rank information for repositioning   - shouldUpdateChildren: Optional flag to update child actions   - isAutomated: Optional flag to indicate automated update  Returns: The updated action

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `labels` | `[String!]` | - | - |
| `rankInput` | `RankInput` | - | - |
| `shouldUpdateChildren` | `Boolean` | - | - |
| `isAutomated` | `Boolean` | - | - |

## Signature

- `updateActionLabels(actionId: ID!, labels: [String!], rankInput: RankInput, shouldUpdateChildren: Boolean, isAutomated: Boolean)` -> `Action`
