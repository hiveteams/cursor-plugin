# `createDashboardV2`

- Type: `mutation`
- Returns: `Dashboard!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Creates a new dashboard with typed V2 filter input for Buzz/MCP endpoints. This mutation provides full schema introspection for AI assistants.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `title` | `String!` | - | - |
| `privacy` | `DashboardPrivacy!` | - | - |
| `projectIds` | `[ID]!` | - | - |
| `sharingWith` | `[ID!]!` | - | - |
| `teams` | `[ID!]!` | - | - |
| `filter` | `WidgetContainerFilterInputV2` | - | - |
| `shareOnBehalfOfCreator` | `Boolean` | false | - |
| `color` | `String` | "#FFCF55" | - |
| `type` | `DashboardType` | - | - |

## Signature

- `createDashboardV2(workspaceId: ID!, title: String!, privacy: DashboardPrivacy!, projectIds: [ID]!, sharingWith: [ID!]!, teams: [ID!]!, filter: WidgetContainerFilterInputV2, shareOnBehalfOfCreator: Boolean, color: String, type: DashboardType)` -> `Dashboard!`
