# `getBuzzCommands`

- Type: `query`
- Returns: `BuzzCommandConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get slash commands for a workspace. Can filter by specific IDs or search by name prefix.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `specificIds` | `[ID!]` | - | Filter by specific command IDs |
| `name` | `String` | - | Search by command name (case-insensitive prefix match) |
| `first` | `Int` | - | - |
| `last` | `Int` | - | - |
| `after` | `String` | - | - |
| `before` | `String` | - | - |
| `sortField` | `String` | "name" | - |
| `sortOrder` | `Int` | 1 | - |

## Signature

- `getBuzzCommands(workspaceId: ID!, specificIds: [ID!], name: String, first: Int, last: Int, after: String, before: String, sortField: String, sortOrder: Int)` -> `BuzzCommandConnection!`
