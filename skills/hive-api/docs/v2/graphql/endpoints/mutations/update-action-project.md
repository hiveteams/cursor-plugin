# `updateActionProject`

- Type: `mutation`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update the project for an action  Access: Requires user access to the action and target project  Parameters:   - actionId: The ID of the action to update   - projectId: The ID of the new project (null to unset)   - rank: Optional rank for the action in the new project  Returns: The updated action

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `projectId` | `ID` | - | - |
| `rank` | `Float` | - | - |

## Signature

- `updateActionProject(actionId: ID!, projectId: ID, rank: Float)` -> `Action`
