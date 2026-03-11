# `updateTimer`

- Type: `mutation`
- Returns: `Timer!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update a timer's action association  Access: Requires user to be the owner of the timer. If actionId is provided, requires access to the new action's workspace.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `timerId` | `ID!` | - | - |
| `actionId` | `ID` | - | New action ID to associate the timer with (optional, pass null to remove association) |

## Signature

- `updateTimer(timerId: ID!, actionId: ID)` -> `Timer!`
