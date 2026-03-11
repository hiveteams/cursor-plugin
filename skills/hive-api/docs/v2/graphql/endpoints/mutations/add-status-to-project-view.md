# `addStatusToProjectView`

- Type: `mutation`
- Returns: `ActionView`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

This mutation is used to add a status to a specific project. ALWAYS run the setCustomStatusColor mutation (setting status color) to set the color of the status afterwards.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddStatusToProjectViewInput!` | - | The ID of the action view and status name to add |

## Signature

- `addStatusToProjectView(input: AddStatusToProjectViewInput!)` -> `ActionView`
