# `getMeetingUserData`

- Type: `query`
- Returns: `MeetingUserData`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get user data for a specific meeting

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `meetingExternalId` | `String!` | - | - |
| `workspaceId` | `ID!` | - | - |

## Signature

- `getMeetingUserData(meetingExternalId: String!, workspaceId: ID!)` -> `MeetingUserData`
