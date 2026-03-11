# `createTimer`

- Type: `mutation`
- Returns: `Timer!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Create a new timer, optionally associated with an action  Access: Requires user to be logged in and have access to the workspace. If actionId is provided, the action must belong to the same workspace.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | Workspace ID the timer belongs to |
| `actionId` | `ID` | - | Action ID to associate the timer with (optional) |
| `timerStatus` | `TimerStatus` | - | Initial status for the timer (paused or running). Defaults to paused. |

## Signature

- `createTimer(workspaceId: ID!, actionId: ID, timerStatus: TimerStatus)` -> `Timer!`
