# `setStoryPoints`

- Type: `mutation`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Set the agile story point value for an action  Access: Requires user access to the action  Parameters:   - actionId: The ID of the action to update   - storyPoints: The new story point value

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `storyPoints` | `Int!` | - | - |

## Signature

- `setStoryPoints(actionId: ID!, storyPoints: Int!)` -> `Action`
