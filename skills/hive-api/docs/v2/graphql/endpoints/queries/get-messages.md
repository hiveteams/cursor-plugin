# `getMessages`

- Type: `query`
- Returns: `MessageConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Retrieves messages from groups (chats/DMs) in a workspace.  - If groupId is provided: searches/returns messages from that specific group - If groupId is omitted and text is provided: searches across all groups the user has access to - If both groupId and text are omitted: returns most recent messages (requires groupId)  To find messages in a chat with a specific person, first find the groupId with groups(members: [yourUserId, theirUserId]).  Access: Requires user to be a member of the group(s).  Errors: - "User must be logged in" - User is not authenticated - "User does not have access to workspace" - User is not a member of the workspace - "Either groupId or text must be provided" - Neither groupId nor text was provided - "User does not have access to this group" - User is not a member of the specified group

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | ID of the workspace |
| `groupId` | `ID` | - | Optional ID of the group. If omitted with text, searches all accessible groups. |
| `text` | `String` | - | Text to search within messages. Required if groupId is not provided. |
| `first` | `Int` | 10 | Number of messages to return (default: 10, max: 50) |

## Signature

- `getMessages(workspaceId: ID!, groupId: ID, text: String, first: Int)` -> `MessageConnection!`
