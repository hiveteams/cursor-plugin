# `goalsEasySearch`

- Type: `query`
- Returns: `GoalConnection`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `text` | `String!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `assignees` | `[ID]` | - | - |
| `limit` | `Int!` | - | - |

## Signature

- `goalsEasySearch(text: String!, workspaceId: ID!, assignees: [ID], limit: Int!)` -> `GoalConnection`
