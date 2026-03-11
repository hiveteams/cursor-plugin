# `getTimers`

- Type: `query`
- Returns: `TimerConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get timers for the current user in a workspace  Access: Requires user to be logged in and have access to the workspace

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | Workspace ID to get timers for |
| `status` | `TimerStatus` | - | Filter by timer status |
| `actionId` | `ID` | - | Filter by action ID |
| `first` | `Int` | - | - |
| `after` | `String` | - | - |
| `last` | `Int` | - | - |
| `before` | `String` | - | - |

## Signature

- `getTimers(workspaceId: ID!, status: TimerStatus, actionId: ID, first: Int, after: String, last: Int, before: String)` -> `TimerConnection!`
