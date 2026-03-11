# `getAction`

- Type: `query`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get an action by ID  Access: Requires user access to the action  Parameters:   - actionId: The ID of the action to retrieve  Returns: The requested action

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |

## Signature

- `getAction(actionId: ID!)` -> `Action`
