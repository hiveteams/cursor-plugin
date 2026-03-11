# `addPostReaction`

- Type: `mutation`
- Returns: `Post!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Adds a reaction emoji to a post.  Access: Requires user access to the workspace.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `postId` | `ID!` | - | ID of the post to add reaction to |
| `emoji` | `String!` | - | Emoji string (e.g. ':thumbsup:') |

## Signature

- `addPostReaction(postId: ID!, emoji: String!)` -> `Post!`
