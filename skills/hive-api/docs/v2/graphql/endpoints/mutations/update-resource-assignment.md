# `updateResourceAssignment`

- Type: `mutation`
- Returns: `ResourceAssignments`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update a resource assignment. ALWAYS use search to find the resource assignment before updating it. If the resource assignment is not found, DONT RUN THE MUTATION. If the resource assignment is found, update resource assignment.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` | - | The id of the resource assignment to update |
| `workspaceId` | `ID!` | - | The workspace id |
| `resourceAssignment` | `UpdateResourceAssignmentInput!` | - | The resource assignment to update |

## Signature

- `updateResourceAssignment(id: ID!, workspaceId: ID!, resourceAssignment: UpdateResourceAssignmentInput!)` -> `ResourceAssignments`
