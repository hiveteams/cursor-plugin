# `getLabels`

- Type: `query`
- Returns: `LabelWithChildrenConnection`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get labels matching a certain ID or matching a query string. If you input BOTH an array of ids and a search string, it'll search for IDs in that array that ALSO have the search string as a substring of their name. Probably not very useful, so just use one or the other. If you search by string, you will be limited to 20 results returned, so if you don't get what you are looking for, search more specifically

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `searchParams` | `LabelParams!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | 20 | - |
| `after` | `ID` | - | - |

## Signature

- `getLabels(searchParams: LabelParams!, workspaceId: ID!, first: Int, after: ID)` -> `LabelWithChildrenConnection`
