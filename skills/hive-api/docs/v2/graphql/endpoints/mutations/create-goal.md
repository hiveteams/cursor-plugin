# `createGoal`

- Type: `mutation`
- Returns: `Goal`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Create a new goal with comprehensive validation rules  IMPORTANT VALIDATION RULES:  Display Type Rules: - progress: Only works with measurementType null, number, or actions - number: Only works with measurementType null, number, actions, or overdue - status: Only works with measurementType status  Measurement Type + Unit Combinations: - measurementType actions/overdue: Must use measurementUnit actions OR projects - measurementType number: Must use measurementUnit currency, custom, OR percentage - measurementType status: Must use measurementUnit subGoals  Measurement Unit + Value + Symbol Rules: - measurementUnit currency: measurementUnitValue must be one of the supported currency codes (e.g., USD/EUR/JPY/GBP/AUD), symbol $/€/¥/£/AU$   This list is not exhaustive. For additional currencies, specify the ISO 4217 currency code as measurementUnitValue and provide the appropriate symbol. Refer to the application's documentation or configuration for the full list of supported currencies and symbols. - measurementUnit percentage: measurementUnitValue must be 'percentage', symbol '%' - measurementUnit actions: measurementUnitValue must be 'actions' - measurementUnit projects: measurementUnitValue must be 'projects' - measurementUnit subGoals: measurementUnitValue must be the empty string ("") - measurementUnit custom: measurementUnitValue can be any string  Action/Project ID Rules: - actionIds: Requires measurementType actions/overdue + measurementUnit actions + measurementUnitValue 'actions' - projectIds: Requires measurementType actions/overdue + measurementUnit projects + measurementUnitValue 'projects'  Date Rules: - Cannot be both ongoingDate AND recurringDate - Cannot combine ongoingDate with startDate/endDate - Cannot combine recurringDate with startDate/endDate - If startDate provided, endDate is required - startDate must be before endDate

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID` | - | - |
| `workspace` | `ID!` | - | The workspace ID where this goal will be created |
| `owners` | `[ID!]!` | - | User IDs who own this goal (must contain at least one element; empty arrays are not allowed and will be rejected at runtime) |
| `teamOwners` | `[ID!]!` | - | Team IDs who own this goal |
| `name` | `String!` | - | Goal name (cannot be empty string) |
| `parentId` | `ID` | - | Parent goal ID if this is a sub-goal |
| `description` | `String!` | - | Goal description in HTML format |
| `initialValue` | `Float!` | - | Initial numeric value for the goal |
| `currentValue` | `Float!` | - | Current numeric value for the goal |
| `goalValue` | `Float!` | - | Target numeric value for the goal |
| `startDate` | `Date` | - | Start date (requires endDate if provided) |
| `endDate` | `Date` | - | End date (required if startDate provided, must be after startDate) |
| `ongoingDate` | `Boolean` | false | Whether goal is ongoing (cannot combine with recurringDate or start/endDate) |
| `recurringDate` | `GoalRecurringDateInput` | null | Recurring schedule (cannot combine with ongoingDate or start/endDate) |
| `measurementType` | `MeasurementType` | null | How goal value is measured (null, number, actions, status, overdue) |
| `measurementUnit` | `MeasurementUnit` | null | Unit for measurement (currency, percentage, custom, actions, projects, subGoals) |
| `measurementUnitValue` | `String!` | - | Specific value for the unit (e.g., 'USD', 'percentage', 'actions', 'projects', '' for subGoals) |
| `measurementUnitSymbol` | `String!` | - | Symbol for the unit (e.g., '$', '%', '€', '¥', '£', 'AU$') |
| `displayType` | `DisplayType!` | - | How goal is displayed (number, progress, status) |
| `actionIds` | `[ID!]` | [] | Action IDs to track (requires measurementType actions/overdue + measurementUnit actions + measurementUnitValue 'actions') |
| `includeSubActions` | `Boolean` | - | Whether to include sub-actions in tracking |
| `projectIds` | `[ID!]` | [] | Project IDs to track (requires measurementType actions/overdue + measurementUnit projects + measurementUnitValue 'projects') |
| `sharingType` | `SharingTypes` | - | Who can access this goal (me, custom, everyone) |
| `sharingWith` | `[ID!]` | [] | User IDs to share with (only valid when sharingType is custom) |
| `isAutomated` | `Boolean` | false | Whether this goal was created automatically |

## Signature

- `createGoal(_id: ID, workspace: ID!, owners: [ID!]!, teamOwners: [ID!]!, name: String!, parentId: ID, description: String!, initialValue: Float!, currentValue: Float!, goalValue: Float!, startDate: Date, endDate: Date, ongoingDate: Boolean, recurringDate: GoalRecurringDateInput, measurementType: MeasurementType, measurementUnit: MeasurementUnit, measurementUnitValue: String!, measurementUnitSymbol: String!, displayType: DisplayType!, actionIds: [ID!], includeSubActions: Boolean, projectIds: [ID!], sharingType: SharingTypes, sharingWith: [ID!], isAutomated: Boolean)` -> `Goal`
