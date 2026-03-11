# `removePost`

- Type: `mutation`
- Returns: `Boolean!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Soft deletes a news post by setting deleted to true.  Access: Requires user to be the post creator or a workspace admin.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `postId` | `ID!` | - | ID of the post to remove |

## Signature

- `removePost(postId: ID!)` -> `Boolean!`
