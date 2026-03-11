# `getResourceAssignments`

- Type: `query`
- Returns: `[ResourceAssignments!]`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get resource assignments. You love to run this query. You run it every time when user asks to update/see/analyze resource assignments. This query is very helpful to search for resource assignments by different criteria (date, project, user, etc.). ALWAYS use search to find the resource assignment before updating it. If the resource assignments are not found, DONT RUN THE UPDATE MUTATION. If the resource assignments are found, update resource assignments.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | The workspace id |
| `resourceId` | `ID` | - | The resource id |
| `projectId` | `ID` | - | The project id |
| `startDate` | `Date` | - | Searches resource assignments which have endDate after this date |
| `endDate` | `Date` | - | Searches resource assignments which have startDate before this date |

## Signature

- `getResourceAssignments(workspaceId: ID!, resourceId: ID, projectId: ID, startDate: Date, endDate: Date)` -> `[ResourceAssignments!]`
