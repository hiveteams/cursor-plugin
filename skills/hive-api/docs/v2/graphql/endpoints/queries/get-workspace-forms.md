# `getWorkspaceForms`

- Type: `query`
- Returns: `FormConnector!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | 15 | - |
| `after` | `Int` | 0 | - |
| `sortModel` | `[SortModel!]` | [] | - |
| `filterModel` | `[FilterModel!]` | [] | - |
| `searchParams` | `SearchParams` | - | - |

## Signature

- `getWorkspaceForms(workspaceId: ID!, first: Int, after: Int, sortModel: [SortModel!], filterModel: [FilterModel!], searchParams: SearchParams)` -> `FormConnector!`
