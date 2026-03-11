# `messagesEasySearch`

- Type: `query`
- Returns: `MessageConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Searches through messages in a workspace  Very useful for searching through existing private conversations or chat groups. Supports search by the group type or id. Could return total count of messages.  Access: Requires user access to the workspace, groups if used.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `text` | `String!` | - | Text to search within messages, required. Use a plain string to search for an exact match. e.g. "Hello, World!" If you don't know the exact phrase, you can use the AND and OR Lucene query syntax e.g "Hello AND World" or "Hello OR World" If you want to inject the exact phrase, use quotes around the phrase. e.g. ""Hello, World!" query" |
| `workspaceId` | `ID!` | - | ID of the workspace |
| `users` | `[ID!]` | - | Array of user IDs that sent the messages |
| `groups` | `[ID!]` | - | Array of group IDs to search within |
| `limit` | `Int!` | - | Limit the number of messages to return |
| `includeTotalCount` | `Boolean` | - | Whether to include the total count of messages |

## Signature

- `messagesEasySearch(text: String!, workspaceId: ID!, users: [ID!], groups: [ID!], limit: Int!, includeTotalCount: Boolean)` -> `MessageConnection!`
