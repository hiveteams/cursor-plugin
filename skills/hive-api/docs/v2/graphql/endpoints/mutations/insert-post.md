# `insertPost`

- Type: `mutation`
- Returns: `Post!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Creates a new news post.  You can also specify the category of the post and the attachment file id or even predefined reactions to post.  Access: Requires user access to the workspace  Examples: {   "body": "This is a <b>very exciting</b> news post",   "workspaceId": "REDACTED_WORKSPACE_ID",   "category": "news" }

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID` | - | Post unique ID. Can be omitted, will be generated automatically |
| `body` | `String!` | - | Post body. Must be a valid HTML string |
| `workspaceId` | `ID!` | - | Workspace ID |
| `fileId` | `ID` | - | Attachment file ID. File should be pre-uploaded to Hive |
| `category` | `String` | - | Post category. Omit if you want to use no category |

## Signature

- `insertPost(_id: ID, body: String!, workspaceId: ID!, fileId: ID, category: String)` -> `Post!`
