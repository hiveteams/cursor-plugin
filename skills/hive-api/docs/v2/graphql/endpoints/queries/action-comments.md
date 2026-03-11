# `actionComments`

- Type: `query`
- Returns: `MessageConnection`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `first` | `Int` | 20 | - |
| `after` | `String` | - | - |
| `last` | `Int` | - | - |
| `before` | `String` | - | - |
| `sortField` | `String` | "createdAt" | - |
| `sortOrder` | `Int` | -1 | - |
| `reverse` | `Boolean` | true | - |

## Signature

- `actionComments(actionId: ID!, first: Int, after: String, last: Int, before: String, sortField: String, sortOrder: Int, reverse: Boolean)` -> `MessageConnection`
