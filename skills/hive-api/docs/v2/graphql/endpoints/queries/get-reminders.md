# `getReminders`

- Type: `query`
- Returns: `ReminderConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get reminders for a workspace for the current user

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | - | - |
| `after` | `String` | - | - |
| `last` | `Int` | - | - |
| `before` | `String` | - | - |

## Signature

- `getReminders(workspaceId: ID!, first: Int, after: String, last: Int, before: String)` -> `ReminderConnection!`
