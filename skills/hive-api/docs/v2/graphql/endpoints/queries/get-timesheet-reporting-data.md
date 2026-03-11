# `getTimesheetReportingData`

- Type: `query`
- Returns: `JSONObject`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

No usage.  Access: Requires workspace admin access  Errors: Returns [] if not workspace admin, or this feature is disabled

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | associated workspaceId |
| `startDate` | `Date!` | - | start of period for which data should be retrieved. |
| `endDate` | `Date!` | - | end of period for which data should be retrieved. |

## Signature

- `getTimesheetReportingData(workspaceId: ID!, startDate: Date!, endDate: Date!)` -> `JSONObject`
