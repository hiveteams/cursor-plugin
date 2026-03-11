# `deleteTimer`

- Type: `mutation`
- Returns: `Boolean!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Delete a timer (soft delete)  Access: Requires user to be the owner of the timer

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `timerId` | `ID!` | - | - |

## Signature

- `deleteTimer(timerId: ID!)` -> `Boolean!`
