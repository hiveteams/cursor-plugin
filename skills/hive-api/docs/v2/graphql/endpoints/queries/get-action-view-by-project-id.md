# `getActionViewByProjectId`

- Type: `query`
- Returns: `ActionView`
- Deprecated: yes
- Deprecation reason: Use getWorkspacePhases instead!
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

This query is used to get the action view by project id.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | The ID of the project |

## Signature

- `getActionViewByProjectId(projectId: ID!)` -> `ActionView`
