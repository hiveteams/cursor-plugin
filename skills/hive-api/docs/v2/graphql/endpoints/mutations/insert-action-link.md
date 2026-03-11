# `insertActionLink`

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

- `insertActionLink(source: ID!, target: ID!, lag: Int, type: DependencyType)` -> `ActionLink!`
