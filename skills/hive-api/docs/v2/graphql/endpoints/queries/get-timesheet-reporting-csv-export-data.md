# `getTimesheetReportingCsvExportData`

- Type: `query`
- Returns: `String`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for csv export in Reporting in "Timesheets" app.  Access: It requires user access.  Errors: Returns [] if not logged in, or doesn't have access to reporting, or this feature is disabled

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | associated workspace |
| `startDate` | `Date!` | - | start of period for which data should be retrieved. |
| `endDate` | `Date!` | - | end of period for which data should be retrieved. |
| `groupBy` | `TimesheetReportingGroupByEnum` | MONTH | group by period |
| `columns` | `[TimesheetReportingColumnsEnum!]` | [hours, estimate, billable, utilization, utilizationTarget, budget, remainingBudget] | fields for result |
| `selectedFilters` | `TimesheetsReportingFiltersInput` | - | filters |

## Signature

- `getTimesheetReportingCsvExportData(workspaceId: ID!, startDate: Date!, endDate: Date!, groupBy: TimesheetReportingGroupByEnum, columns: [TimesheetReportingColumnsEnum!], selectedFilters: TimesheetsReportingFiltersInput)` -> `String`
