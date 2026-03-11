# `getResourceAssignment`

- Type: `query`
- Returns: `ResourceAssignments`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get a resource assignment. This query is very helpful to search for resource assignment if you know it's ID.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` | - | The id of the resource assignment |

## Signature

- `getResourceAssignment(id: ID!)` -> `ResourceAssignments`
