# `createResourceAssignment`

- Type: `mutation`
- Returns: `ResourceAssignments`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Create a resource assignment.  IMPORTANT: ALWAYS pass 'fixedDisplayType' and 'allocationType' together. Use assignmentType: 'regular' by default. Use other assignment types only if the user explicitly mentioned another type.  Possible valid combinations ('allocationType' + 'fixedDisplayType'): • 'hoursPerDay' + 'hours' - when you want to allocate hours per day • 'fixedHours' + 'hours' - when you want to allocate total hours • 'fixedHours' + 'days' - when you want to allocate in days (default work day = 8 hours) • 'fixedHours' + 'percentages' - when you want to allocate in percentages (percentage of the default default work day hours, e,g, 50% = 4 hours)  IMPORTANT: ALWAYS pass 'allocationValue' when allocating by percentage. IMPORTANT: ALWAYS pass 'fixedHours' when allocating by hours or days. IMPORTANT: ALWAYS pass 'hoursPerDay' when allocating by hours per day.  Examples: • Duration: 1 day, allocationType = hoursPerDay, fixedDisplayType = hours, allocationValue = 8, hoursPerDay = 8 • Duration: 5 days, allocationType = hoursPerDay, fixedDisplayType = hours, allocationValue = 8, hoursPerDay = 8 • Duration: 1 day, allocationType = fixedHours, fixedDisplayType = hours, allocationValue = 40, fixedHours = 40 • Duration: 5 days, allocationType = fixedHours, fixedDisplayType = hours, allocationValue = 40, fixedHours = 40 • Duration: 1 day, allocationType = fixedHours, fixedDisplayType = percentages, allocationValue = 50 (percents), fixedHours = 8 (default work day hours) * 1 (days) * 0.5 = 4 • Duration: 5 days, allocationType = fixedHours, fixedDisplayType = percentages, allocationValue = 50 (percents), fixedHours = 8 (default work day hours) * 5 (days) * 0.5 = 20 • Duration: 1 day, allocationType = fixedHours, fixedDisplayType = days, allocationValue = 2 (days), fixedHours = 8 (default work day hours) * 2 = 16 • Duration: 5 days, allocationType = fixedHours, fixedDisplayType = days, allocationValue = 2 (days), fixedHours = 8 (default work day hours) * 2 = 16

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `resourceAssignment` | `CreateResourceAssignmentInput!` | - | The resource assignment to create |

## Signature

- `createResourceAssignment(resourceAssignment: CreateResourceAssignmentInput!)` -> `ResourceAssignments`
