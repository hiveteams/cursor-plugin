# `updateTimerStatus`

- Type: `mutation`
- Returns: `Timer!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update timer status (start, pause, or complete) - start: Sets status to running and adds a new session entry - pause: Sets status to paused and closes current session entry - complete: Sets status to completed and closes current session entry  Access: Requires user to be the owner of the timer

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `timerId` | `ID!` | - | - |
| `operation` | `TimerOperation!` | - | Operation to perform on the timer |
| `timezone` | `String` | - | Optional timezone override for start operation (defaults to user's timezone) |

## Signature

- `updateTimerStatus(timerId: ID!, operation: TimerOperation!, timezone: String)` -> `Timer!`
