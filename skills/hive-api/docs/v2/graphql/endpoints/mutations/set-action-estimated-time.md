# `setActionEstimatedTime`

- Type: `mutation`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used to create new action and subaction estimates  Access: Requires user access to the underlying action  Errors: Throws error if user does not have access to action.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `estimate` | `Int` | - | - |
| `estimates` | `[TimeTrackingEstimateItemInput!]` | - | - |

## Signature

- `setActionEstimatedTime(actionId: ID!, estimate: Int, estimates: [TimeTrackingEstimateItemInput!])` -> `Action`
