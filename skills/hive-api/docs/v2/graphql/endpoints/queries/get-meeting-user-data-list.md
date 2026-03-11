# `getMeetingUserDataList`

- Type: `query`
- Returns: `[MeetingUserData!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get all meeting user data records for the current user. Returns meetings where Sidekick has recorded data (transcripts, goals, etc). Sorted by most recently modified first. Use this to list recent meetings with materials, goals, or transcripts.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `limit` | `Int` | - | Maximum number of results to return (default: 50) |

## Signature

- `getMeetingUserDataList(workspaceId: ID!, limit: Int)` -> `[MeetingUserData!]!`
