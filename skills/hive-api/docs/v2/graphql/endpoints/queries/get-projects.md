# `getProjects`

- Type: `query`
- Returns: `ProjectConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get projects that the user has access to with pagination, filtering and sorting  Access: Requires workspace access  Parameters:   - workspaceId: The ID of the workspace   - first: Number of projects to return (default: pagination limit)   - last: Optional number of projects to return from the end   - before: Optional cursor for pagination   - after: Optional cursor for pagination   - searchParams: Optional search parameters   - specificIds: Optional array of specific project IDs to include   - excludedIds: Optional array of project IDs to exclude   - includeTemplates: Optional flag to include template projects   - archived: Optional flag to include archived projects (default: false)   - templatesOnly: Optional flag to return only template projects (default: false)   - includePublic: Optional flag to include public projects (default: true)   - includePrivate: Optional flag to include private projects (default: false)   - includeReadOnly: Optional flag to include read-only projects   - includeArchived: Optional flag to include archived projects (default: false)   - rootProjectId: Optional root project ID to filter by   - userId: Optional user ID to filter projects by  Returns: ProjectConnection with edges and page info

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | 20 | - |
| `last` | `Int` | - | - |
| `before` | `ID` | - | - |
| `after` | `ID` | - | - |
| `searchParams` | `SearchParams` | - | - |
| `specificIds` | `[ID!]` | - | - |
| `excludedIds` | `[ID!]` | - | - |
| `includeTemplates` | `Boolean` | - | - |
| `archived` | `Boolean` | false | - |
| `templatesOnly` | `Boolean` | false | - |
| `includePublic` | `Boolean` | true | - |
| `includePrivate` | `Boolean` | false | - |
| `includeReadOnly` | `Boolean` | - | - |
| `includeArchived` | `Boolean` | false | - |
| `rootProjectId` | `ID` | - | - |
| `userId` | `ID` | - | - |

## Signature

- `getProjects(workspaceId: ID!, first: Int, last: Int, before: ID, after: ID, searchParams: SearchParams, specificIds: [ID!], excludedIds: [ID!], includeTemplates: Boolean, archived: Boolean, templatesOnly: Boolean, includePublic: Boolean, includePrivate: Boolean, includeReadOnly: Boolean, includeArchived: Boolean, rootProjectId: ID, userId: ID)` -> `ProjectConnection!`
