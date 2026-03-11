# `updatePost`

- Type: `mutation`
- Returns: `Post!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Updates the body content of a news post.  Access: Requires user to be the post creator.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `postId` | `ID!` | - | ID of the post to update |
| `body` | `String!` | - | New body content. Must be a valid HTML string |

## Signature

- `updatePost(postId: ID!, body: String!)` -> `Post!`
