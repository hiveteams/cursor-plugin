# `updateActionLink`

- Type: `mutation`
- Returns: `ActionLink!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `source` | `ID!` | - | - |
| `target` | `ID!` | - | - |
| `lag` | `Int` | - | - |
| `type` | `DependencyType` | - | - |

## Signature

- `updateActionLink(source: ID!, target: ID!, lag: Int, type: DependencyType)` -> `ActionLink!`
