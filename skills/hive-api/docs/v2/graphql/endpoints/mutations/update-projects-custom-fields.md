# `updateProjectsCustomFields`

- Type: `mutation`
- Returns: `[Project!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Enables custom fields for specific projects.  This should be used to enable only project itemType custom fields.  Parameters:   - projectIds: Required. The IDs of the projects to add the custom fields to   - workspaceId: Required. The ID of the workspace to add the custom fields to   - fields: Required. The custom fields to add to the projects

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectIds` | `[ID!]!` | - | projects ids associated with custom field |
| `workspaceId` | `ID!` | - | workspace associated with projectIds |
| `fields` | `[CustomFieldItemInput!]!` | - | custom field to update |

## Signature

- `updateProjectsCustomFields(projectIds: [ID!]!, workspaceId: ID!, fields: [CustomFieldItemInput!]!)` -> `[Project!]!`
