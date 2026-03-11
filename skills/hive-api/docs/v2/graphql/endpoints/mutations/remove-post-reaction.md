# `removePostReaction`

- Type: `mutation`
- Returns: `Post!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Removes a reaction emoji from a post.  Access: Requires user access to the workspace.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `postId` | `ID!` | - | ID of the post to remove reaction from |
| `emoji` | `String!` | - | Emoji string to remove |

## Signature

- `removePostReaction(postId: ID!, emoji: String!)` -> `Post!`
