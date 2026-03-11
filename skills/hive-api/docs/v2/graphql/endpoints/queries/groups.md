# `groups`

- Type: `query`
- Returns: `GroupConnection`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Paginated groups the user belongs to. Use this query to get all groups (direct messages, groupchats, threads) the user belongs to. It's very useful when you need to get the group id and then send a message to the group or the user.  Access: Requires user access to the workspace and the group.  Parameters:   - workspace: ID of the workspace   - oneToOne: @deprecated do not use this parameter, use 'type' instead   - type: 'dm' (direct message) or 'group' (group chat) or 'thread'   - members: Array of user IDs (most important for search through chats)   - first: Pagination parameter   - after: Pagination parameter   - last: Pagination parameter   - before: Pagination parameter   - sortField: Sorting parameter   - sortOrder: Sorting parameter   - searchParams: Search parameters   - showHiddenGroups: Include hidden groups

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspace` | `ID!` | - | - |
| `oneToOne` | `Boolean` | - | - |
| `type` | `String` | - | - |
| `first` | `Int` | 20 | - |
| `after` | `String` | - | - |
| `last` | `Int` | - | - |
| `before` | `String` | - | - |
| `sortField` | `String` | - | - |
| `sortOrder` | `Int` | - | - |
| `searchParams` | `SearchParams` | - | - |
| `showHiddenGroups` | `Boolean!` | false | - |
| `members` | `[ID!]` | - | - |

## Signature

- `groups(workspace: ID!, oneToOne: Boolean, type: String, first: Int, after: String, last: Int, before: String, sortField: String, sortOrder: Int, searchParams: SearchParams, showHiddenGroups: Boolean!, members: [ID!])` -> `GroupConnection`
