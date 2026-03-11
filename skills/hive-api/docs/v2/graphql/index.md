# Hive GraphQL v2 Endpoint Reference

Auto-generated from live introspection of `https://prod-gql.hive.com/graphql`.

- Generated at: `2026-03-11T02:52:57+00:00`
- Query operations: **54**
- Mutation operations: **102**
- Subscription operations: **1**

Each operation has its own file under `endpoints/`.

## Queries

Root type: `Query`

Total operations: **54**

| Operation | Args | Returns | Deprecated |
|---|---|---|---|
| [`actionComments`](endpoints/queries/action-comments.md) | `actionId: ID!`, `first: Int`, `after: String`, `last: Int`, `before: String`, `sortField: String`, `sortOrder: Int`, `reverse: Boolean` | `MessageConnection` | no |
| [`approvalRounds`](endpoints/queries/approval-rounds.md) | `actionId: ID!`, `first: Int`, `last: Int`, `before: ID`, `after: ID` | `ApprovalRoundConnection!` | no |
| [`approvalStages`](endpoints/queries/approval-stages.md) | `roundId: ID!`, `first: Int`, `last: Int`, `before: ID`, `after: ID` | `ApprovalStageConnection` | no |
| [`currentRoundAndStage`](endpoints/queries/current-round-and-stage.md) | `actionId: ID!` | `CurrentRoundAndStageReturn` | no |
| [`getAction`](endpoints/queries/get-action.md) | `actionId: ID!` | `Action` | no |
| [`getActionByWorkspace`](endpoints/queries/get-action-by-workspace.md) | `actionId: String!`, `workspaceId: ID!` | `Action` | no |
| [`getActionsByWorkspace`](endpoints/queries/get-actions-by-workspace.md) | `workspaceId: ID!`, `text: String`, `first: Int`, `last: Int`, `before: ID`, `after: ID`, `status: String`, `archived: Boolean`, `projectIds: [ID]`, `excludeProjectIds: [ID]`, `specificIds: [ID!]`, `assignees: [ID!]`, `labels: [ID!]`, `includeChildProjects: Boolean`, `excludeCompletedActions: Boolean`, `excludeSnoozedActions: Boolean`, `createdAtStart: Date`, `createdAtEnd: Date`, `startDate: Date`, `endDate: Date`, `includePrivate: Boolean`, `parent: ID`, `sortField: String`, `sortOrder: Int`, `milestone: Boolean`, `customFieldId: ID`, `customFieldValue: String` | `ActionConnector` | no |
| [`getActionViewByProjectId`](endpoints/queries/get-action-view-by-project-id.md) | `projectId: ID!` | `ActionView` | yes |
| [`getApprovalTemplates`](endpoints/queries/get-approval-templates.md) | `workspaceId: ID!`, `searchParams: SearchParams`, `first: Int`, `last: Int`, `after: ID`, `before: ID`, `sortField: String` | `ApprovalTemplateConnection!` | no |
| [`getBuzzCommands`](endpoints/queries/get-buzz-commands.md) | `workspaceId: ID!`, `specificIds: [ID!]`, `name: String`, `first: Int`, `last: Int`, `after: String`, `before: String`, `sortField: String`, `sortOrder: Int` | `BuzzCommandConnection!` | no |
| [`getCustomFields`](endpoints/queries/get-custom-fields.md) | `workspaceId: ID!`, `actionViewId: ID`, `formId: ID`, `first: Int`, `last: Int`, `before: ID`, `after: ID`, `selector: JSONObject`, `itemType: CustomFieldItemType`, `includeRemoved: Boolean`, `searchParams: SearchParams`, `sortField: String`, `sortOrder: Int`, `includeProjectCustomFields: Boolean` | `CustomFieldConnection` | no |
| [`getDashboards`](endpoints/queries/get-dashboards.md) | `workspaceId: ID!`, `first: Int`, `last: Int`, `after: ID`, `before: ID`, `searchParams: SearchParams`, `sortField: String`, `sortOrder: Int`, `selector: JSONObject`, `excludedIds: [ID]`, `type: DashboardType` | `DashboardConnection` | no |
| [`getDashboardWidgets`](endpoints/queries/get-dashboard-widgets.md) | `dashboardId: ID!` | `[DashboardWidget!]!` | no |
| [`getEmails`](endpoints/queries/get-emails.md) | `from: [String!]`, `to: [String!]`, `cc: [String!]`, `bcc: [String!]`, `subject: String`, `searchQuery: String`, `after: Date`, `before: Date`, `maxResults: Int`, `searchInboxOnly: Boolean`, `searchSentOnly: Boolean`, `nextPageToken: String` | `GetEmailsResponse!` | no |
| [`getGoal`](endpoints/queries/get-goal.md) | `goalId: ID!` | `Goal` | no |
| [`getGoals`](endpoints/queries/get-goals.md) | `workspace: ID!`, `first: Int`, `last: Int`, `after: ID`, `before: ID`, `searchParams: SearchParams`, `sortField: String`, `sortOrder: Int`, `selector: JSONObject`, `ownerIds: [ID]`, `excludedIds: [ID]`, `specificIds: [ID]` | `GoalConnection` | no |
| [`getHistoricalTimesheets`](endpoints/queries/get-historical-timesheets.md) | `workspaceId: ID!`, `userId: ID!`, `startDate: Date!`, `endDate: Date!` | `[Timesheet!]!` | no |
| [`getLabels`](endpoints/queries/get-labels.md) | `searchParams: LabelParams!`, `workspaceId: ID!`, `first: Int`, `after: ID` | `LabelWithChildrenConnection` | no |
| [`getMeetingUserData`](endpoints/queries/get-meeting-user-data.md) | `meetingExternalId: String!`, `workspaceId: ID!` | `MeetingUserData` | no |
| [`getMeetingUserDataList`](endpoints/queries/get-meeting-user-data-list.md) | `workspaceId: ID!`, `limit: Int` | `[MeetingUserData!]!` | no |
| [`getMessages`](endpoints/queries/get-messages.md) | `workspaceId: ID!`, `groupId: ID`, `text: String`, `first: Int` | `MessageConnection!` | no |
| [`getMyTimesheets`](endpoints/queries/get-my-timesheets.md) | `workspaceId: ID!`, `startDate: Date!`, `endDate: Date!`, `userId: ID`, `rootTimesheetCreatedAt: Date`, `includeEstimatedActions: Boolean` | `[Timesheet!]!` | no |
| [`getNote`](endpoints/queries/get-note.md) | `noteId: ID!` | `Note` | no |
| [`getNotes`](endpoints/queries/get-notes.md) | `first: Int`, `last: Int`, `before: ID`, `after: ID`, `sortField: String`, `sortOrder: Int`, `workspaceId: ID`, `specificIds: [ID]`, `excludedIds: [ID]` | `NoteConnection!` | no |
| [`getPriorityLevels`](endpoints/queries/get-priority-levels.md) | `workspaceId: ID!`, `formId: ID`, `actionId: ID`, `specificIds: [ID]`, `excludedIds: [ID]` | `[PriorityLevel!]!` | no |
| [`getProjectIds`](endpoints/queries/get-project-ids.md) | `workspaceId: ID!`, `specificIds: [ID]`, `excludedIds: [ID]`, `includeTemplates: Boolean`, `includeReadOnly: Boolean`, `publicOnly: Boolean` | `[String]!` | no |
| [`getProjects`](endpoints/queries/get-projects.md) | `workspaceId: ID!`, `first: Int`, `last: Int`, `before: ID`, `after: ID`, `searchParams: SearchParams`, `specificIds: [ID!]`, `excludedIds: [ID!]`, `includeTemplates: Boolean`, `archived: Boolean`, `templatesOnly: Boolean`, `includePublic: Boolean`, `includePrivate: Boolean`, `includeReadOnly: Boolean`, `includeArchived: Boolean`, `rootProjectId: ID`, `userId: ID` | `ProjectConnection!` | no |
| [`getRecentlyVisitedProjectIds`](endpoints/queries/get-recently-visited-project-ids.md) | `workspaceId: ID!` | `[ID]!` | yes |
| [`getReminders`](endpoints/queries/get-reminders.md) | `workspaceId: ID!`, `first: Int`, `after: String`, `last: Int`, `before: String` | `ReminderConnection!` | no |
| [`getResourceAssignment`](endpoints/queries/get-resource-assignment.md) | `id: ID!` | `ResourceAssignments` | no |
| [`getResourceAssignments`](endpoints/queries/get-resource-assignments.md) | `workspaceId: ID!`, `resourceId: ID`, `projectId: ID`, `startDate: Date`, `endDate: Date` | `[ResourceAssignments!]` | no |
| [`getTimeCategories`](endpoints/queries/get-time-categories.md) | `workspaceId: ID!`, `projectId: ID`, `specificIds: [ID!]`, `includeSubmitted: Boolean`, `onlyBillable: Boolean` | `[TimeCategory!]!` | no |
| [`getTimers`](endpoints/queries/get-timers.md) | `workspaceId: ID!`, `status: TimerStatus`, `actionId: ID`, `first: Int`, `after: String`, `last: Int`, `before: String` | `TimerConnection!` | no |
| [`getTimesheetApprovals`](endpoints/queries/get-timesheet-approvals.md) | `workspaceId: ID!`, `first: Int`, `after: ID` | `TimesheetConnection!` | no |
| [`getTimesheetComments`](endpoints/queries/get-timesheet-comments.md) | `timesheetId: ID!` | `TimesheetComments` | no |
| [`getTimesheetEstimatedTime`](endpoints/queries/get-timesheet-estimated-time.md) | `workspaceId: ID!`, `containerIds: [ID]!`, `containerType: TimesheetContainer!`, `userIds: [ID!]!`, `startDate: Date!`, `endDate: Date!` | `[TimesheetEstimatedTimeEntry!]!` | no |
| [`getTimesheetReportingCsvExportData`](endpoints/queries/get-timesheet-reporting-csv-export-data.md) | `workspaceId: ID!`, `startDate: Date!`, `endDate: Date!`, `groupBy: TimesheetReportingGroupByEnum`, `columns: [TimesheetReportingColumnsEnum!]`, `selectedFilters: TimesheetsReportingFiltersInput` | `String` | no |
| [`getTimesheetReportingData`](endpoints/queries/get-timesheet-reporting-data.md) | `workspaceId: ID!`, `startDate: Date!`, `endDate: Date!` | `JSONObject` | no |
| [`getTimesheets`](endpoints/queries/get-timesheets.md) | `workspaceId: ID!`, `startDate: Date!`, `endDate: Date!`, `status: TimesheetStatus`, `first: Int`, `after: ID` | `TimesheetConnection!` | no |
| [`getTimesheetsToApprove`](endpoints/queries/get-timesheets-to-approve.md) | `workspaceId: ID!`, `startDate: Date!`, `endDate: Date!`, `grouping: TimesheetGrouping!`, `statuses: [TimesheetStatus!]` | `[GroupedTimesheet!]!` | no |
| [`getTimesheetTrackedTime`](endpoints/queries/get-timesheet-tracked-time.md) | `workspaceId: ID!`, `containerIds: [ID]!`, `containerType: TimesheetContainer!`, `userIds: [ID!]!`, `startDate: Date!`, `endDate: Date!` | `[TimesheetTrackedTimeEntry!]!` | no |
| [`getTimeTrackingData`](endpoints/queries/get-time-tracking-data.md) | `workspaceId: ID!`, `startDate: Date`, `endDate: Date` | `TimeTrackingData!` | no |
| [`getUserTimeEntries`](endpoints/queries/get-user-time-entries.md) | `userId: ID!`, `workspaceId: ID!`, `startDate: Date!`, `endDate: Date!`, `status: TimesheetStatus`, `containerId: ID`, `containerType: TimesheetContainer`, `categoryId: ID`, `first: Int`, `last: Int`, `before: ID`, `after: ID`, `sortOrder: Int`, `filterBy: TimeEntriesFilter` | `TimeEntryConnection` | no |
| [`getUserTimesheets`](endpoints/queries/get-user-timesheets.md) | `workspaceId: ID!`, `userId: ID!`, `startDate: Date!`, `endDate: Date!` | `[Timesheet!]!` | no |
| [`getWorkflowsForWorkspacePaginated`](endpoints/queries/get-workflows-for-workspace-paginated.md) | `workspaceId: ID!`, `first: Int`, `last: Int`, `before: ID`, `after: ID`, `searchParams: SearchParams` | `WorkflowConnection!` | no |
| [`getWorkspace`](endpoints/queries/get-workspace.md) | `workspaceId: ID!` | `Workspace` | no |
| [`getWorkspaceForms`](endpoints/queries/get-workspace-forms.md) | `workspaceId: ID!`, `first: Int`, `after: Int`, `sortModel: [SortModel!]`, `filterModel: [FilterModel!]`, `searchParams: SearchParams` | `FormConnector!` | no |
| [`goalsEasySearch`](endpoints/queries/goals-easy-search.md) | `text: String!`, `workspaceId: ID!`, `assignees: [ID]`, `limit: Int!` | `GoalConnection` | no |
| [`groups`](endpoints/queries/groups.md) | `workspace: ID!`, `oneToOne: Boolean`, `type: String`, `first: Int`, `after: String`, `last: Int`, `before: String`, `sortField: String`, `sortOrder: Int`, `searchParams: SearchParams`, `showHiddenGroups: Boolean!`, `members: [ID!]` | `GroupConnection` | no |
| [`isAdminOrManagerOrProjectCreator`](endpoints/queries/is-admin-or-manager-or-project-creator.md) | `workspaceId: ID!` | `Boolean!` | no |
| [`messagesEasySearch`](endpoints/queries/messages-easy-search.md) | `text: String!`, `workspaceId: ID!`, `users: [ID!]`, `groups: [ID!]`, `limit: Int!`, `includeTotalCount: Boolean` | `MessageConnection!` | no |
| [`nextApprovalStage`](endpoints/queries/next-approval-stage.md) | `actionId: ID!` | `ApprovalStage` | no |
| [`notebooks`](endpoints/queries/notebooks.md) | `first: Int`, `last: Int`, `before: ID`, `after: ID`, `sortField: String`, `sortOrder: Int`, `searchType: NotebookSearchType`, `workspaceId: ID`, `projectId: ID`, `archived: Boolean`, `includedNotebookIds: [ID!]`, `searchParams: SearchParams` | `NotebookConnection` | no |
| [`workspacePlaceholders`](endpoints/queries/workspace-placeholders.md) | `workspaceId: ID!`, `specificIds: [ID!]` | `[ResourcePlaceholder!]!` | no |

## Mutations

Root type: `Mutation`

Total operations: **102**

| Operation | Args | Returns | Deprecated |
|---|---|---|---|
| [`addActionCustomFields`](endpoints/mutations/add-action-custom-fields.md) | `ids: [ID!]!`, `projectIds: [ID!]!`, `workspaceId: ID!` | `[Project!]!` | no |
| [`addCreatorComment`](endpoints/mutations/add-creator-comment.md) | `timesheetId: ID!`, `text: String!` | `Timesheet` | no |
| [`addPostReaction`](endpoints/mutations/add-post-reaction.md) | `postId: ID!`, `emoji: String!` | `Post!` | no |
| [`addProjectOwner`](endpoints/mutations/add-project-owner.md) | `projectId: ID!`, `ownerId: ID!`, `workspaceId: ID!` | `Project` | no |
| [`addStatusToProjectView`](endpoints/mutations/add-status-to-project-view.md) | `input: AddStatusToProjectViewInput!` | `ActionView` | no |
| [`applyApprovalTemplate`](endpoints/mutations/apply-approval-template.md) | `actionId: ID!`, `templateId: ID!`, `roundId: ID` | `Boolean!` | no |
| [`applyProjectTemplate`](endpoints/mutations/apply-project-template.md) | `templateProjectId: ID!`, `targetProjectId: ID!`, `importWith: ApplyProjectTemplateImportWithInput`, `overrideLabels: Boolean` | `Project` | no |
| [`bulkArchiveActions`](endpoints/mutations/bulk-archive-actions.md) | `actionIds: [ID!]!`, `workspaceId: ID!` | `[Action!]!` | no |
| [`bulkInsertActions`](endpoints/mutations/bulk-insert-actions.md) | `actions: [BulkInsertActionInput!]!`, `sortByDates: Boolean` | `[ID!]` | no |
| [`bulkUpdateActionCustomFields`](endpoints/mutations/bulk-update-action-custom-fields.md) | `actionIds: [ID!]!`, `workspaceId: ID!`, `fieldId: ID!`, `value: String`, `selectedValues: [String]`, `dateValue: Date`, `numberValue: Float` | `[Action!]!` | no |
| [`bulkUpdateActionDescription`](endpoints/mutations/bulk-update-action-description.md) | `actionIds: [ID!]!`, `workspaceId: ID!`, `description: String!`, `isCollabUpdate: Boolean`, `forcePersistCollab: Boolean` | `Boolean` | no |
| [`bulkUpdateActionLabels`](endpoints/mutations/bulk-update-action-labels.md) | `actionIds: [ID!]!`, `workspaceId: ID!`, `labelIds: [ID!]!`, `operation: BatchOperation!`, `shouldUpdateChildren: Boolean`, `shouldUpdateRecurring: Boolean`, `isAutomated: Boolean` | `Boolean` | no |
| [`bulkUpdateActionsAssignees`](endpoints/mutations/bulk-update-actions-assignees.md) | `actionIds: [ID!]!`, `workspaceId: ID!`, `assigneesToSet: [ID!]`, `assigneesToAdd: [ID!]`, `assigneesToPull: [ID!]`, `teamAssignee: ID`, `placeholderAssigneesToSet: [ID!]`, `placeholderAssigneesToAdd: [ID!]`, `placeholderAssigneesToPull: [ID!]`, `privacy: ActionPrivacy`, `shouldUpdateChildren: Boolean`, `shouldUpdateRecurring: Boolean`, `updatePlaceholderAssignees: Boolean`, `currentAssigneeId: ID` | `Boolean` | no |
| [`bulkUpdateActionsPriorityLevelId`](endpoints/mutations/bulk-update-actions-priority-level-id.md) | `actionIds: [ID!]!`, `workspaceId: ID!`, `priorityLevelId: ID`, `shouldUpdateRecurring: Boolean`, `rank: Float` | `Boolean` | no |
| [`bulkUpdateActionStatus`](endpoints/mutations/bulk-update-action-status.md) | `actionIds: [ID!]!`, `workspaceId: ID!`, `status: String!`, `rankInput: RankInput`, `shouldUpdateChildren: Boolean` | `Boolean` | no |
| [`bulkUpdateActionsTitle`](endpoints/mutations/bulk-update-actions-title.md) | `actionIds: [ID!]!`, `workspaceId: ID!`, `title: String!`, `shouldUpdateRecurring: Boolean`, `allowEmpty: Boolean` | `Boolean` | no |
| [`bulkUpdateActionsTitles`](endpoints/mutations/bulk-update-actions-titles.md) | `actionTitleUpdates: [ActionTitleUpdateInput!]!`, `workspaceId: ID!` | `Boolean` | no |
| [`bulkUpdateActionsType`](endpoints/mutations/bulk-update-actions-type.md) | `workspaceId: ID!`, `actionIds: [ID!]!`, `type: ActionTypeEnum`, `rank: Float` | `Boolean` | no |
| [`bulkUpdateTimesheetStatus`](endpoints/mutations/bulk-update-timesheet-status.md) | `workspaceId: ID!`, `timesheets: [UpdateStatusTimesheetInput!]!` | `[Timesheet!]!` | no |
| [`bulkUpsertCustomFields`](endpoints/mutations/bulk-upsert-custom-fields.md) | `workspaceId: ID!`, `customFields: [CustomFieldToInsertInput!]!` | `CustomFieldUpsertResult` | no |
| [`changeApprovalStageApprover`](endpoints/mutations/change-approval-stage-approver.md) | `actionId: ID!`, `stageId: ID!`, `type: ApprovalType!`, `index: Int!`, `approvalItemId: ID!` | `ApprovalStage` | no |
| [`convertActionToProject`](endpoints/mutations/convert-action-to-project.md) | `actionId: ID!`, `projectName: String`, `parentProjectId: ID`, `deleteOriginalAction: Boolean`, `applyTemplateId: ID`, `sharingType: SharingTypes`, `members: [ID!]`, `teams: [ID!]`, `viewType: ActionViewType` | `Project` | no |
| [`copyAction`](endpoints/mutations/copy-action.md) | `actionId: ID!`, `shouldAddCopySign: Boolean!`, `assigneeForSubaction: [String!]`, `isPlaceholdersAssignee: Boolean!`, `lowestRank: Boolean`, `projectId: ID` | `Action` | no |
| [`createBuzzCommand`](endpoints/mutations/create-buzz-command.md) | `input: CreateBuzzCommandInput!` | `BuzzCommand!` | no |
| [`createDashboardV2`](endpoints/mutations/create-dashboard-v2.md) | `workspaceId: ID!`, `title: String!`, `privacy: DashboardPrivacy!`, `projectIds: [ID]!`, `sharingWith: [ID!]!`, `teams: [ID!]!`, `filter: WidgetContainerFilterInputV2`, `shareOnBehalfOfCreator: Boolean`, `color: String`, `type: DashboardType` | `Dashboard!` | no |
| [`createDashboardWidget`](endpoints/mutations/create-dashboard-widget.md) | `dashboardId: ID`, `containerId: ID`, `containerType: WidgetContainerType`, `type: DashboardWidgetType!`, `title: String!`, `titleColor: String`, `titleSize: TextSize`, `fileIds: [ID!]`, `chartType: ChartType`, `sort: String`, `url: String`, `projectId: String`, `goalId: String`, `noteId: String`, `showTitles: Boolean`, `showLegend: Boolean`, `ignoreContainerFilter: Boolean`, `legendPosition: LegendPosition`, `showValueLabels: Boolean`, `showRowTotals: Boolean`, `showColumnTotals: Boolean`, `chartValuesState: [ChartValueStateInput!]`, `showFlattenedData: Boolean`, `showLinkedToProject: Boolean`, `truncateLongNumbers: Boolean`, `displayGroupsAs: DisplayGroupsAs`, `timeUnitsType: TimeUnit`, `projectTreeLevelsToShow: [Int!]`, `isProjectTreeLevelActive: Boolean`, `reportOn: DashboardWidgetReportOn`, `XAxis: DashboardWidgetXAxis`, `XAxisCustomFieldId: String`, `XAxisTitle: String`, `YAxis: DashboardWidgetYAxis`, `YAxisCustomFieldId: String`, `YAxisTitle: String`, `YAxisGroupBy: DashboardWidgetYAxis`, `groupByCustomFieldId: String`, `chartValueColors: [ChartValueColorInput!]`, `groupOthers: DashboardWidgetGroupOthersInput`, `sectionHeaderText: String`, `sectionHeaderTextAlignment: TextAlignment`, `sectionHeaderLinePosition: SectionHeaderLinePosition`, `isHidden: Boolean`, `projectDetailsFields: [String!]`, `contentTextAlignment: TextAlignment`, `contentTextSize: TextSize`, `contentTextColorPrimary: String`, `contentTextColorSecondary: String`, `workspaceId: String`, `overdueFilter: IncludeFilterType`, `recurringFilter: IncludeFilterType`, `completedDateRange: DateRangeFilterInput`, `createdDateRange: DateRangeFilterInput`, `dueDatesRange: DateRangeFilterInput`, `projectDateRange: DateRangeFilterInput`, `projectStatusDateRange: DateRangeFilterInput`, `dateRange: DateRangeFilterInput`, `colorThemeId: String`, `segmentColorOverrides: [SegmentColorOverrideInput!]`, `projectBudgetCategoryIds: [String]`, `projectBudgetDateRange: [Date!]` | `DashboardWidget!` | no |
| [`createForm`](endpoints/mutations/create-form.md) | `_id: String`, `workspace: String!`, `isDraft: Boolean`, `title: String!`, `externalTitle: String`, `externalLogo: String`, `target: [FormTarget!]!`, `description: String`, `confirmMessage: String`, `projectId: String`, `parentActionId: String`, `template: String`, `projectTemplate: String`, `assignees: [String!]`, `projectOwner: String`, `members: [String!]!`, `teams: [String!]`, `sharingType: String!`, `jsonFormData: FormJSONDataInput!`, `setFormNameToTitle: Boolean`, `setDateAndUserNameToTitle: Boolean`, `setCardNumberToTitle: Boolean`, `setTemplateNameToTitle: Boolean`, `authRequired: Boolean`, `allowProgressionTracking: Boolean`, `allowAccessToWhitelistedDomains: Boolean`, `allowedEmailDomains: [String!]`, `onlyCreatorEditable: Boolean`, `mapToProjectId: String`, `actionsData: [ActionDataInput!]`, `receivers: String`, `emailDynamicFields: [String!]`, `archived: Boolean`, `shortcuttedAt: Date`, `draftFormId: String`, `publishedFormId: String` | `Form!` | no |
| [`createGoal`](endpoints/mutations/create-goal.md) | `_id: ID`, `workspace: ID!`, `owners: [ID!]!`, `teamOwners: [ID!]!`, `name: String!`, `parentId: ID`, `description: String!`, `initialValue: Float!`, `currentValue: Float!`, `goalValue: Float!`, `startDate: Date`, `endDate: Date`, `ongoingDate: Boolean`, `recurringDate: GoalRecurringDateInput`, `measurementType: MeasurementType`, `measurementUnit: MeasurementUnit`, `measurementUnitValue: String!`, `measurementUnitSymbol: String!`, `displayType: DisplayType!`, `actionIds: [ID!]`, `includeSubActions: Boolean`, `projectIds: [ID!]`, `sharingType: SharingTypes`, `sharingWith: [ID!]`, `isAutomated: Boolean` | `Goal` | no |
| [`createProject`](endpoints/mutations/create-project.md) | `workspace: ID!`, `name: String`, `archived: Boolean`, `actionDateSync: Boolean`, `attachments: [AttachmentObject!]`, `autoCompleteParent: Boolean`, `automationWorkflows: [String!]`, `color: String`, `copyActionStatuses: Boolean`, `copyApprovals: Boolean`, `copyAssignees: Boolean`, `copyAppWorkflows: Boolean`, `copyActionDates: Boolean`, `copyProjectChildren: Boolean`, `copyFrom: String`, `description: String`, `startDate: Date`, `endDate: Date`, `ganttGroupBy: String`, `hiddenApps: [String!]`, `hideActionsForExternal: Boolean`, `hideActionsForExternalByDefault: Boolean`, `isDraftMode: Boolean`, `labels: [ID!]`, `members: [ID!]`, `parentProject: String`, `destination: String`, `permissions: InputProjectPermissions`, `phases: [PhaseInput!]`, `pinActionView: Boolean`, `resourcePlaceholderIds: [ID!]`, `sharingType: SharingTypes`, `showKanbanViewSubactions: String`, `showCompletedSubactionsByDefault: Boolean`, `showRootActionCustomFields: Boolean`, `sortType: SortType`, `teams: [ID!]`, `viewType: String`, `template: Boolean`, `copyUserPermissions: Boolean`, `customFieldsToCreate: [CustomFieldInput!]`, `notifyProjectMembers: Boolean`, `projCustomFields: [CustomFieldItemInput!]`, `isAutomated: Boolean`, `ganttAutoScheduling: GanttAutoSchedulingEnum`, `projectStatuses: [String!]`, `harvestProjectId: String` | `Project` | no |
| [`createReminder`](endpoints/mutations/create-reminder.md) | `text: String!`, `userIds: [ID!]!`, `recurrenceDefinition: RecurrenceDefinitionInput!`, `workspaceId: ID!`, `originType: ReminderOriginType!`, `originId: ID!` | `Reminder!` | no |
| [`createResourceAssignment`](endpoints/mutations/create-resource-assignment.md) | `resourceAssignment: CreateResourceAssignmentInput!` | `ResourceAssignments` | no |
| [`createResourcePlaceholder`](endpoints/mutations/create-resource-placeholder.md) | `name: String!`, `workspaceId: ID!`, `billRate: Float`, `costRate: Float`, `roleTagId: ID` | `ResourcePlaceholder!` | no |
| [`createScheduledMailMessage`](endpoints/mutations/create-scheduled-mail-message.md) | `scheduledSendTime: Date!`, `email: String!`, `body: String!`, `subject: String!`, `snippet: String!`, `threadId: ID`, `messageId: ID`, `inReplyTo: ID`, `references: [ID!]!`, `actionId: ID`, `parentThreadId: ID` | `ResidentMailMessage!` | no |
| [`createTimeEntries`](endpoints/mutations/create-time-entries.md) | `workspaceId: ID!`, `entries: [CreateTimeEntryInput!]!`, `status: TimesheetStatus` | `CreateTimeEntriesResult!` | no |
| [`createTimer`](endpoints/mutations/create-timer.md) | `workspaceId: ID!`, `actionId: ID`, `timerStatus: TimerStatus` | `Timer!` | no |
| [`deleteBuzzCommand`](endpoints/mutations/delete-buzz-command.md) | `_id: ID!` | `Boolean!` | no |
| [`deleteCustomField`](endpoints/mutations/delete-custom-field.md) | `customFieldId: ID!`, `shouldRemoveExistingValues: Boolean!` | `CustomField` | no |
| [`deleteGoal`](endpoints/mutations/delete-goal.md) | `_id: ID!` | `Boolean` | no |
| [`deleteTimeCategory`](endpoints/mutations/delete-time-category.md) | `_id: ID!` | `TimeCategory!` | no |
| [`deleteTimer`](endpoints/mutations/delete-timer.md) | `timerId: ID!` | `Boolean!` | no |
| [`deleteTimesheet`](endpoints/mutations/delete-timesheet.md) | `_id: ID!`, `workspaceId: ID!` | `Timesheet` | no |
| [`deleteTimesheetComment`](endpoints/mutations/delete-timesheet-comment.md) | `timesheetId: ID!`, `isManager: Boolean` | `Timesheet` | no |
| [`disableActionCustomFields`](endpoints/mutations/disable-action-custom-fields.md) | `customFieldIds: [ID!]!`, `projectIds: [ID!]!`, `workspaceId: ID!`, `removeFromActions: Boolean` | `[Project!]!` | no |
| [`disableProjectsCustomFields`](endpoints/mutations/disable-projects-custom-fields.md) | `customFieldIds: [ID!]!`, `projectIds: [ID!]!`, `workspaceId: ID!` | `[Project!]!` | no |
| [`insertAction`](endpoints/mutations/insert-action.md) | `_id: ID`, `title: String!`, `description: String`, `status: String`, `assignees: [ID!]`, `placeholderAssignees: [ID!]`, `teamAssignee: ID`, `labels: [ID!]`, `projectId: ID`, `phaseId: ID`, `priorityLevelId: ID`, `deadline: Date`, `scheduledDate: Date`, `newAction: Boolean`, `noteIds: [ID]`, `sectionIds: [ID!]`, `privacy: String`, `urgent: Boolean`, `parentId: ID`, `workspace: ID`, `actionViewId: ID`, `isRisk: Boolean`, `estimates: [TimeTrackingEstimateItemInput!]`, `insertOrder: InsertOrder`, `attachments: [ActionAttachmentInput!]`, `rank: Float`, `isAutomated: Boolean`, `preserveUTC: Boolean`, `type: ActionTypeEnum`, `timeCategoryId: ID`, `githubBranchNames: [String!]`, `gitlabBranchNames: [String!]`, `showInOtherProjects: [ID!]` | `Action` | no |
| [`insertActionLink`](endpoints/mutations/insert-action-link.md) | `source: ID!`, `target: ID!`, `lag: Int`, `type: DependencyType` | `ActionLink!` | no |
| [`insertApprovalRound`](endpoints/mutations/insert-approval-round.md) | `actionId: ID!`, `roundId: ID!`, `stageId: ID!` | `ApprovalRound` | no |
| [`insertApprovalStage`](endpoints/mutations/insert-approval-stage.md) | `actionId: ID!`, `roundId: ID!`, `stageId: ID` | `ApprovalStage` | no |
| [`insertGroup`](endpoints/mutations/insert-group.md) | `workspace: String!`, `members: [String!]!`, `teams: [String!]`, `name: String`, `oneToOne: Boolean`, `type: String`, `projectId: String` | `Group` | no |
| [`insertMessage`](endpoints/mutations/insert-message.md) | `_id: ID`, `workspaceId: ID`, `containerId: ID`, `containerType: ContainerType`, `participants: [ID!]`, `mentions: [String]`, `automated: Boolean`, `body: String!`, `attachments: [Attachment]`, `color: String`, `isNoteJsonComment: Boolean`, `isPrivate: Boolean`, `userMentionsByGroup: [ID!]` | `Message!` | no |
| [`insertPost`](endpoints/mutations/insert-post.md) | `_id: ID`, `body: String!`, `workspaceId: ID!`, `fileId: ID`, `category: String` | `Post!` | no |
| [`insertRecurringAction`](endpoints/mutations/insert-recurring-action.md) | `actionId: ID!`, `type: String`, `dayType: String`, `startDate: Date`, `endDate: Date`, `interval: Int`, `endingType: String`, `endingAfter: Int`, `days: [String]`, `showOnDueDate: Boolean`, `recurringId: ID` | `RecurringAction` | no |
| [`insertTimeCategory`](endpoints/mutations/insert-time-category.md) | `_id: ID!`, `name: String!`, `workspaceId: ID!`, `projectId: ID`, `billable: Boolean` | `TimeCategory!` | no |
| [`recoverTimesheet`](endpoints/mutations/recover-timesheet.md) | `_id: ID!`, `workspaceId: ID!` | `Timesheet` | no |
| [`recurringRequestActionUpdate`](endpoints/mutations/recurring-request-action-update.md) | - | `Boolean!` | no |
| [`recurringRequestGoalUpdate`](endpoints/mutations/recurring-request-goal-update.md) | - | `Boolean!` | no |
| [`regenerateShareToken`](endpoints/mutations/regenerate-share-token.md) | `_id: ID!` | `Dashboard!` | no |
| [`removePost`](endpoints/mutations/remove-post.md) | `postId: ID!` | `Boolean!` | no |
| [`removePostReaction`](endpoints/mutations/remove-post-reaction.md) | `postId: ID!`, `emoji: String!` | `Post!` | no |
| [`removeProjectOwner`](endpoints/mutations/remove-project-owner.md) | `projectId: ID!`, `ownerId: ID!`, `workspaceId: ID!` | `Project` | no |
| [`requestActionUpdate`](endpoints/mutations/request-action-update.md) | `_id: ID!` | `Boolean` | no |
| [`requestApprovals`](endpoints/mutations/request-approvals.md) | `roundId: ID!` | `ApprovalRound` | no |
| [`requestGoalUpdate`](endpoints/mutations/request-goal-update.md) | `_id: ID!` | `Boolean` | no |
| [`restoreDeletedProject`](endpoints/mutations/restore-deleted-project.md) | `projectId: ID!` | `Project` | no |
| [`runWorkflow`](endpoints/mutations/run-workflow.md) | `workflowId: ID!`, `actionId: ID!` | `Boolean` | no |
| [`salesforceOperation`](endpoints/mutations/salesforce-operation.md) | `input: SalesforceOperationInput!` | `SalesforceOperationResult!` | no |
| [`setActionColor`](endpoints/mutations/set-action-color.md) | `actionId: ID!`, `actionColor: String!` | `Action` | no |
| [`setActionEstimatedTime`](endpoints/mutations/set-action-estimated-time.md) | `actionId: ID!`, `estimate: Int`, `estimates: [TimeTrackingEstimateItemInput!]` | `Action` | no |
| [`setCustomStatusColor`](endpoints/mutations/set-custom-status-color.md) | `workspaceId: ID!`, `status: String!`, `color: String` | `Workspace` | no |
| [`setStoryPoints`](endpoints/mutations/set-story-points.md) | `actionId: ID!`, `storyPoints: Int!` | `Action` | no |
| [`setTimesheetLock`](endpoints/mutations/set-timesheet-lock.md) | `timesheetId: ID!`, `locked: Boolean!` | `Timesheet` | no |
| [`setTimeTrackingItemToAction`](endpoints/mutations/set-time-tracking-item-to-action.md) | `actionId: ID!`, `time: TimeInput!`, `date: Date!`, `description: String`, `categoryId: ID`, `id: ID`, `userId: ID`, `replaceForDate: Boolean` | `Action` | no |
| [`submitTimesheets`](endpoints/mutations/submit-timesheets.md) | `workspaceId: ID!`, `userId: ID!`, `startDate: Date!`, `endDate: Date!`, `timesheets: [TimesheetInput!]!`, `isEditMode: Boolean`, `includeEstimatedActions: Boolean` | `[Timesheet!]!` | no |
| [`unsetRecurringActions`](endpoints/mutations/unset-recurring-actions.md) | `actionIds: [ID!]!`, `workspaceId: ID!` | `Boolean` | no |
| [`updateActionAssignees`](endpoints/mutations/update-action-assignees.md) | `actionId: ID!`, `assignees: [String!]`, `placeholderAssignees: [ID!]`, `teamAssignee: ID`, `rankInput: RankInput`, `shouldUpdateChildren: Boolean`, `externalAssigneeName: String`, `isAutomated: Boolean` | `Action` | yes |
| [`updateActionCustomField`](endpoints/mutations/update-action-custom-field.md) | `actionId: ID!`, `fieldId: ID!`, `value: String`, `selectedValues: [String]`, `dateValue: Date`, `numberValue: Float` | `Action` | no |
| [`updateActionGithubBranchNames`](endpoints/mutations/update-action-github-branch-names.md) | `actionId: ID!`, `githubBranchNames: [String!]!` | `Action` | no |
| [`updateActionGitlabBranchNames`](endpoints/mutations/update-action-gitlab-branch-names.md) | `actionId: ID!`, `gitlabBranchNames: [String!]!` | `Action` | no |
| [`updateActionLabels`](endpoints/mutations/update-action-labels.md) | `actionId: ID!`, `labels: [String!]`, `rankInput: RankInput`, `shouldUpdateChildren: Boolean`, `isAutomated: Boolean` | `Action` | no |
| [`updateActionLink`](endpoints/mutations/update-action-link.md) | `source: ID!`, `target: ID!`, `lag: Int`, `type: DependencyType` | `ActionLink!` | no |
| [`updateActionProject`](endpoints/mutations/update-action-project.md) | `actionId: ID!`, `projectId: ID`, `rank: Float` | `Action` | no |
| [`updateActionsMilestone`](endpoints/mutations/update-actions-milestone.md) | `actionIds: [ID!]!`, `workspaceId: ID!`, `value: Boolean!` | `Boolean` | no |
| [`updateActionSnoozeDate`](endpoints/mutations/update-action-snooze-date.md) | `actionId: ID!`, `snoozeDate: Date` | `Action` | no |
| [`updateBuzzCommand`](endpoints/mutations/update-buzz-command.md) | `_id: ID!`, `input: UpdateBuzzCommandInput!` | `BuzzCommand!` | no |
| [`updateDashboardV2`](endpoints/mutations/update-dashboard-v2.md) | `_id: ID!`, `title: String`, `privacy: DashboardPrivacy`, `projectIds: [ID]`, `sharingWith: [ID!]`, `teams: [ID!]`, `layout: [InputDashboardLayout!]`, `filter: WidgetContainerFilterInputV2`, `shareOnBehalfOfCreator: Boolean`, `shareOnBehalfOfCreatorSettings: ShareOnBehalfOfCreatorSettingsInput`, `pinToUser: Boolean`, `color: String`, `allowedEmailDomains: [String!]`, `allowAccessToWhitelistedDomains: Boolean`, `backgroundColor: DashboardBackgroundColor`, `backgroundImageUrl: String`, `backgroundImageCropType: DashboardBackgroundImageCropType`, `displayTipsAndTricksFooter: Boolean`, `headerTextColor: DashboardHeaderTextColor`, `type: DashboardType` | `Dashboard` | no |
| [`updateDashboardWidget`](endpoints/mutations/update-dashboard-widget.md) | `_id: ID!`, `title: String`, `titleColor: String`, `titleSize: TextSize`, `url: String`, `sort: String`, `type: DashboardWidgetType`, `chartType: ChartType`, `slateJson: JSONObject`, `XAxis: DashboardWidgetXAxis`, `XAxisCustomFieldId: String`, `XAxisTitle: String`, `YAxis: DashboardWidgetYAxis`, `YAxisCustomFieldId: String`, `YAxisTitle: String`, `YAxisGroupBy: DashboardWidgetYAxis`, `groupByCustomFieldId: String`, `fileIds: [ID!]`, `noteId: String`, `portfolioViewId: String`, `hideHeader: Boolean`, `goalId: String`, `showTitles: Boolean`, `showLegend: Boolean`, `ignoreContainerFilter: Boolean`, `legendPosition: LegendPosition`, `showValueLabels: Boolean`, `showRowTotals: Boolean`, `showColumnTotals: Boolean`, `showFlattenedData: Boolean`, `showLinkedToProject: Boolean`, `truncateLongNumbers: Boolean`, `displayGroupsAs: DisplayGroupsAs`, `displayGoalsBy: DisplayGoalsBy`, `timeUnitsType: TimeUnit`, `projectTreeLevelsToShow: [Int!]`, `isProjectTreeLevelActive: Boolean`, `reportOn: DashboardWidgetReportOn`, `chartValueColors: [ChartValueColorInput!]`, `groupOthers: DashboardWidgetGroupOthersInput`, `projectId: String`, `buttonLabel: String`, `sectionHeaderText: String`, `sectionHeaderTextAlignment: TextAlignment`, `sectionHeaderLinePosition: SectionHeaderLinePosition`, `isHidden: Boolean`, `projectDetailsFields: [String!]`, `contentTextAlignment: TextAlignment`, `contentTextSize: TextSize`, `contentTextColorPrimary: String`, `contentTextColorSecondary: String`, `workspaceId: String`, `containerId: ID`, `colorThemeId: String`, `segmentColorOverrides: [SegmentColorOverrideInput!]`, `projectBudgetCategoryIds: [String]`, `projectBudgetDateRange: [Date!]`, `chartValuesState: [ChartValueStateInput!]` | `DashboardWidget` | no |
| [`updateGoal`](endpoints/mutations/update-goal.md) | `_id: ID!`, `name: String`, `initialValue: Float`, `currentValue: Float`, `goalValue: Float`, `actionIds: [ID!]`, `includeSubActions: Boolean`, `projectIds: [ID!]`, `parentId: ID`, `description: String`, `owners: [ID!]`, `teamOwners: [ID!]`, `startDate: Date`, `endDate: Date`, `ongoingDate: Boolean`, `recurringDate: GoalRecurringDateInput`, `includeSubGoals: Boolean`, `status: GoalStatusType`, `statusDetails: String`, `measurementType: MeasurementType`, `measurementUnit: MeasurementUnit`, `measurementUnitValue: String`, `measurementUnitSymbol: String`, `displayType: DisplayType`, `statusUpdateMode: GoalStatusUpdateMode`, `statusUpdateRange: [GoalStatusUpdateRangeInput!]`, `rankInput: RankInput`, `recurringUpdateReminder: RecurrenceDefinitionInput`, `sharingType: SharingTypes`, `sharingWith: [ID!]`, `isAutomated: Boolean` | `Goal` | no |
| [`updateMeetingUserData`](endpoints/mutations/update-meeting-user-data.md) | `meetingExternalId: String!`, `workspaceId: ID!`, `goals: GoalDiff`, `nextSteps: NextStepDiff`, `materials: MaterialDiff`, `speakerLabels: SpeakerLabelDiff`, `customTitle: String` | `MeetingUserData` | no |
| [`updateMembersPermissions`](endpoints/mutations/update-members-permissions.md) | `projectId: ID!`, `memberIds: [ID!]`, `teamIds: [ID!]`, `permission: String!`, `sharingType: String!`, `isAutomated: Boolean` | `Project` | no |
| [`updatePost`](endpoints/mutations/update-post.md) | `postId: ID!`, `body: String!` | `Post!` | no |
| [`updateProjectArchived`](endpoints/mutations/update-project-archived.md) | `projectId: ID!`, `archived: Boolean!`, `includeChildren: Boolean` | `Project` | no |
| [`updateProjectDescription`](endpoints/mutations/update-project-description.md) | `projectId: ID!`, `description: String!` | `Project` | no |
| [`updateProjectOwner`](endpoints/mutations/update-project-owner.md) | `projectId: ID!`, `ownerId: ID!`, `workspaceId: ID!` | `Project` | yes |
| [`updateProjectsCustomFields`](endpoints/mutations/update-projects-custom-fields.md) | `projectIds: [ID!]!`, `workspaceId: ID!`, `fields: [CustomFieldItemInput!]!` | `[Project!]!` | no |
| [`updateResourceAssignment`](endpoints/mutations/update-resource-assignment.md) | `id: ID!`, `workspaceId: ID!`, `resourceAssignment: UpdateResourceAssignmentInput!` | `ResourceAssignments` | no |
| [`updateResourcePlaceholder`](endpoints/mutations/update-resource-placeholder.md) | `id: ID!`, `name: String`, `billRate: Float`, `costRate: Float`, `roleTagId: ID` | `ResourcePlaceholder!` | no |
| [`updateTimeCategory`](endpoints/mutations/update-time-category.md) | `_id: ID!`, `name: String!`, `billable: Boolean` | `TimeCategory` | no |
| [`updateTimeEntry`](endpoints/mutations/update-time-entry.md) | `timesheetId: ID!`, `date: Date!`, `loggedTime: Int!`, `snapshot: [TimeEntrySnapshotItemInput!]` | `TimeEntry` | no |
| [`updateTimeEntryComment`](endpoints/mutations/update-time-entry-comment.md) | `timeEntryId: ID!`, `text: String!`, `operation: DataOperation!` | `TimeEntry` | no |
| [`updateTimer`](endpoints/mutations/update-timer.md) | `timerId: ID!`, `actionId: ID` | `Timer!` | no |
| [`updateTimerStatus`](endpoints/mutations/update-timer-status.md) | `timerId: ID!`, `operation: TimerOperation!`, `timezone: String` | `Timer!` | no |
| [`updateTimesheetComment`](endpoints/mutations/update-timesheet-comment.md) | `timesheetId: ID!`, `text: String!`, `isManager: Boolean` | `Timesheet` | no |

## Subscriptions

Root type: `Subscription`

Total operations: **1**

| Operation | Args | Returns | Deprecated |
|---|---|---|---|
| [`dummy`](endpoints/subscriptions/dummy.md) | - | `Boolean` | no |
