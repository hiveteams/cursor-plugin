# `updateMeetingUserData`

- Type: `mutation`
- Returns: `MeetingUserData`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update meeting user data using diff operations for array fields and direct values for scalars. Array fields (goals, nextSteps, materials, speakerLabels) accept add/remove/update diffs. Scalar fields (customTitle) accept direct values.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `meetingExternalId` | `String!` | - | Calendar event ID from Google/Microsoft (e.g., 'abc123_20240115T140000Z') |
| `workspaceId` | `ID!` | - | Workspace ID where the meeting belongs |
| `goals` | `GoalDiff` | - | Diff operations for goals (add/remove/update) |
| `nextSteps` | `NextStepDiff` | - | Diff operations for next steps (add/remove/update) |
| `materials` | `MaterialDiff` | - | Diff operations for materials (add/remove/update) |
| `speakerLabels` | `SpeakerLabelDiff` | - | Diff operations for speaker labels (add/remove/update) |
| `customTitle` | `String` | - | User-set title override (pass null to clear) |

## Signature

- `updateMeetingUserData(meetingExternalId: String!, workspaceId: ID!, goals: GoalDiff, nextSteps: NextStepDiff, materials: MaterialDiff, speakerLabels: SpeakerLabelDiff, customTitle: String)` -> `MeetingUserData`
