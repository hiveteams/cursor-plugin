# `updateGoal`

- Type: `mutation`
- Returns: `Goal`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update an existing goal - follows the same validation rules as createGoal  See createGoal mutation for complete validation rule documentation. Key validation reminders: - actionIds require: measurementType actions/overdue + measurementUnit actions + measurementUnitValue 'actions'   - projectIds require: measurementType actions/overdue + measurementUnit projects + measurementUnitValue 'projects' - Date combinations: Cannot mix ongoingDate + recurringDate, or ongoingDate/recurringDate + startDate/endDate - measurementUnit + measurementUnitValue + measurementUnitSymbol must match allowed combinations

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID!` | - | Goal ID to update |
| `name` | `String` | - | Goal name (cannot be empty string if provided) |
| `initialValue` | `Float` | - | Initial numeric value |
| `currentValue` | `Float` | - | Current numeric value |
| `goalValue` | `Float` | - | Target numeric value |
| `actionIds` | `[ID!]` | - | Action IDs to track (requires measurementType actions/overdue + measurementUnit actions + measurementUnitValue 'actions') |
| `includeSubActions` | `Boolean` | - | Whether to include sub-actions in tracking |
| `projectIds` | `[ID!]` | - | Project IDs to track (requires measurementType actions/overdue + measurementUnit projects + measurementUnitValue 'projects') |
| `parentId` | `ID` | - | Parent goal ID |
| `description` | `String` | - | Goal description in HTML format |
| `owners` | `[ID!]` | - | User IDs who own this goal |
| `teamOwners` | `[ID!]` | - | Team IDs who own this goal |
| `startDate` | `Date` | - | Start date (requires endDate, cannot combine with ongoingDate/recurringDate) |
| `endDate` | `Date` | - | End date (must be after startDate, cannot combine with ongoingDate/recurringDate) |
| `ongoingDate` | `Boolean` | - | Whether goal is ongoing (cannot combine with recurringDate or dates) |
| `recurringDate` | `GoalRecurringDateInput` | - | Recurring schedule (cannot combine with ongoingDate or dates) |
| `includeSubGoals` | `Boolean` | - | Whether to include sub-goals |
| `status` | `GoalStatusType` | - | Goal status |
| `statusDetails` | `String` | - | Status details/notes |
| `measurementType` | `MeasurementType` | - | How goal value is measured - affects which measurementUnit values are valid |
| `measurementUnit` | `MeasurementUnit` | - | Unit for measurement - must match measurementType rules |
| `measurementUnitValue` | `String` | - | Specific value for unit - must match measurementUnit (e.g., 'USD', 'actions', 'projects') |
| `measurementUnitSymbol` | `String` | - | Symbol for unit - must match measurementUnitValue (e.g., '$', '%') |
| `displayType` | `DisplayType` | - | How goal is displayed - must match measurementType rules |
| `statusUpdateMode` | `GoalStatusUpdateMode` | - | Status update mode |
| `statusUpdateRange` | `[GoalStatusUpdateRangeInput!]` | - | Status update range rules |
| `rankInput` | `RankInput` | - | Ranking input for goal positioning |
| `recurringUpdateReminder` | `RecurrenceDefinitionInput` | - | Recurring update reminder settings |
| `sharingType` | `SharingTypes` | - | Who can access this goal |
| `sharingWith` | `[ID!]` | - | User IDs to share with (only valid when sharingType is custom) |
| `isAutomated` | `Boolean` | - | Whether this goal was created/updated automatically |

## Signature

- `updateGoal(_id: ID!, name: String, initialValue: Float, currentValue: Float, goalValue: Float, actionIds: [ID!], includeSubActions: Boolean, projectIds: [ID!], parentId: ID, description: String, owners: [ID!], teamOwners: [ID!], startDate: Date, endDate: Date, ongoingDate: Boolean, recurringDate: GoalRecurringDateInput, includeSubGoals: Boolean, status: GoalStatusType, statusDetails: String, measurementType: MeasurementType, measurementUnit: MeasurementUnit, measurementUnitValue: String, measurementUnitSymbol: String, displayType: DisplayType, statusUpdateMode: GoalStatusUpdateMode, statusUpdateRange: [GoalStatusUpdateRangeInput!], rankInput: RankInput, recurringUpdateReminder: RecurrenceDefinitionInput, sharingType: SharingTypes, sharingWith: [ID!], isAutomated: Boolean)` -> `Goal`
