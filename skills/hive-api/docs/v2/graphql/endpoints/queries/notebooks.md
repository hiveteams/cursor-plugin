# `notebooks`

- Type: `query`
- Returns: `NotebookConnection`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Gets paginated notebooks for a user across all workspaces. Use this resolver when you want to find notebooks by title or list notebooks in a workspace or project. Supports searching by title, filtering by workspace/project, search type (mine, shared, templates), and pagination.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `first` | `Int` | 20 | Optional number of notebooks to return |
| `last` | `Int` | - | - |
| `before` | `ID` | - | Optional cursor to return notebooks before a specific notebook |
| `after` | `ID` | - | Optional cursor to return notebooks after a specific notebook |
| `sortField` | `String` | "modifiedAt" | Optional field to sort notebooks by |
| `sortOrder` | `Int` | -1 | Optional order to sort notebooks by |
| `searchType` | `NotebookSearchType` | - | Optional notebook search type to restrict notebook results |
| `workspaceId` | `ID` | - | Optional workspaceId to restrict notebook results |
| `projectId` | `ID` | - | Optional projectId to restrict notebook results |
| `archived` | `Boolean` | false | Optional archived flag to get archived notebook results |
| `includedNotebookIds` | `[ID!]` | - | Optional notebook ids to restrict notebook results |
| `searchParams` | `SearchParams` | - | Optional search parameters to find notebooks by title |

## Signature

- `notebooks(first: Int, last: Int, before: ID, after: ID, sortField: String, sortOrder: Int, searchType: NotebookSearchType, workspaceId: ID, projectId: ID, archived: Boolean, includedNotebookIds: [ID!], searchParams: SearchParams)` -> `NotebookConnection`
