# `createDashboardWidget`

- Type: `mutation`
- Returns: `DashboardWidget!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Creates a new dashboard widget with specified configuration. Common configurations by widget type:   1. Chart Widgets (Bar/Line/Pie): - Set chartType, XAxis, YAxis - Configure grouping and aggregation - Set up color schemes - Use these types of widgets when asked to show something broken down by project, assignee, etc.  2. List Widgets (Actions/Projects): - Define filters (status, assignee, etc.) - Set up sorting and grouping - Configure display options - When user asks to create a widget for all actions assigned to them, create a widget with type 'myActionsList' - Use these types of widgets when asked to show something in a list format, like actions, projects, etc.  3. Status Widgets: - Specify project or goal - Configure metrics to display - Set up refresh intervals  4. Custom Widgets: - Set up embedded content - Configure interactive elements - Define data sources      When asked to show something over time, use binBy and binByDateRange parameters.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `dashboardId` | `ID` | - | - |
| `containerId` | `ID` | - | - |
| `containerType` | `WidgetContainerType` | - | Type of container this widget belongs |
| `type` | `DashboardWidgetType!` | - | The type of dashboard widget to create |
| `title` | `String!` | - | Title text to display for the widget |
| `titleColor` | `String` | - | Hex color code for the widget title |
| `titleSize` | `TextSize` | - | Size of the title text |
| `fileIds` | `[ID!]` | - | Array of file IDs associated with this widget |
| `chartType` | `ChartType` | - | Type of chart to display |
| `sort` | `String` | - | Sort order for widget data |
| `url` | `String` | - | URL for embedded content widgets |
| `projectId` | `String` | - | ID of associated project |
| `goalId` | `String` | - | ID of associated goal |
| `noteId` | `String` | - | ID of associated note |
| `showTitles` | `Boolean` | - | Whether to show titles in the widget |
| `showLegend` | `Boolean` | - | Whether to show chart legend |
| `ignoreContainerFilter` | `Boolean` | - | If true, widget ignores container-level filters |
| `legendPosition` | `LegendPosition` | - | Position of the chart legend |
| `showValueLabels` | `Boolean` | - | Whether to show data point values |
| `showRowTotals` | `Boolean` | - | Whether to show row totals |
| `showColumnTotals` | `Boolean` | - | Whether to show column totals |
| `chartValuesState` | `[ChartValueStateInput!]` | - | Used to store the state of the chart values (colors, order, etc.) |
| `showFlattenedData` | `Boolean` | - | Whether to show pivot table in a data mode (flattened) |
| `showLinkedToProject` | `Boolean` | - | Whether to show links to related projects |
| `truncateLongNumbers` | `Boolean` | - | Whether to truncate long numbers |
| `displayGroupsAs` | `DisplayGroupsAs` | - | How to display grouped data |
| `timeUnitsType` | `TimeUnit` | - | Time unit for temporal data |
| `projectTreeLevelsToShow` | `[Int!]` | - | Which levels of project tree to display |
| `isProjectTreeLevelActive` | `Boolean` | - | Whether project tree level is active |
| `reportOn` | `DashboardWidgetReportOn` | - | What type of data to report on |
| `XAxis` | `DashboardWidgetXAxis` | - | Field to use for X-axis |
| `XAxisCustomFieldId` | `String` | - | Custom field ID for X-axis |
| `XAxisTitle` | `String` | - | Title for X-axis |
| `YAxis` | `DashboardWidgetYAxis` | - | Field to use for Y-axis |
| `YAxisCustomFieldId` | `String` | - | Custom field ID for Y-axis |
| `YAxisTitle` | `String` | - | Title for Y-axis |
| `YAxisGroupBy` | `DashboardWidgetYAxis` | - | Field to group Y-axis values by |
| `groupByCustomFieldId` | `String` | - | Custom field ID for grouping |
| `chartValueColors` | `[ChartValueColorInput!]` | - | Color configuration for chart values |
| `groupOthers` | `DashboardWidgetGroupOthersInput` | - | Configuration for grouping "other" values |
| `sectionHeaderText` | `String` | - | Text for section header |
| `sectionHeaderTextAlignment` | `TextAlignment` | - | Alignment of section header text |
| `sectionHeaderLinePosition` | `SectionHeaderLinePosition` | - | Position of section header line |
| `isHidden` | `Boolean` | - | Whether widget is hidden |
| `projectDetailsFields` | `[String!]` | - | Fields to show in project details |
| `contentTextAlignment` | `TextAlignment` | - | Alignment of content text |
| `contentTextSize` | `TextSize` | - | Size of content text |
| `contentTextColorPrimary` | `String` | - | Primary color for content text |
| `contentTextColorSecondary` | `String` | - | Secondary color for content text |
| `workspaceId` | `String` | - | ID of workspace this widget belongs to |
| `overdueFilter` | `IncludeFilterType` | - | Filter for overdue actions. Used to include or exclude overdue actions. Example: {overdueFilter: 'includeOnly'} |
| `recurringFilter` | `IncludeFilterType` | - | Filter for recurring actions. Used to include or exclude recurring actions. Example: {recurringFilter: 'includeOnly'} |
| `completedDateRange` | `DateRangeFilterInput` | - | Date range filter for completed actions. Example: filter to last 3 months - { selectedOption: 'lastNMonths', amount: 3, timeUnit: 'month', timeDirection: 'last' } |
| `createdDateRange` | `DateRangeFilterInput` | - | Date range filter for created actions |
| `dueDatesRange` | `DateRangeFilterInput` | - | Date range filter for due dates |
| `projectDateRange` | `DateRangeFilterInput` | - | Date range filter for project dates |
| `projectStatusDateRange` | `DateRangeFilterInput` | - | Date range filter for project status dates |
| `dateRange` | `DateRangeFilterInput` | - | General date range filter |
| `colorThemeId` | `String` | - | - |
| `segmentColorOverrides` | `[SegmentColorOverrideInput!]` | - | - |
| `projectBudgetCategoryIds` | `[String]` | - | - |
| `projectBudgetDateRange` | `[Date!]` | - | - |

## Signature

- `createDashboardWidget(dashboardId: ID, containerId: ID, containerType: WidgetContainerType, type: DashboardWidgetType!, title: String!, titleColor: String, titleSize: TextSize, fileIds: [ID!], chartType: ChartType, sort: String, url: String, projectId: String, goalId: String, noteId: String, showTitles: Boolean, showLegend: Boolean, ignoreContainerFilter: Boolean, legendPosition: LegendPosition, showValueLabels: Boolean, showRowTotals: Boolean, showColumnTotals: Boolean, chartValuesState: [ChartValueStateInput!], showFlattenedData: Boolean, showLinkedToProject: Boolean, truncateLongNumbers: Boolean, displayGroupsAs: DisplayGroupsAs, timeUnitsType: TimeUnit, projectTreeLevelsToShow: [Int!], isProjectTreeLevelActive: Boolean, reportOn: DashboardWidgetReportOn, XAxis: DashboardWidgetXAxis, XAxisCustomFieldId: String, XAxisTitle: String, YAxis: DashboardWidgetYAxis, YAxisCustomFieldId: String, YAxisTitle: String, YAxisGroupBy: DashboardWidgetYAxis, groupByCustomFieldId: String, chartValueColors: [ChartValueColorInput!], groupOthers: DashboardWidgetGroupOthersInput, sectionHeaderText: String, sectionHeaderTextAlignment: TextAlignment, sectionHeaderLinePosition: SectionHeaderLinePosition, isHidden: Boolean, projectDetailsFields: [String!], contentTextAlignment: TextAlignment, contentTextSize: TextSize, contentTextColorPrimary: String, contentTextColorSecondary: String, workspaceId: String, overdueFilter: IncludeFilterType, recurringFilter: IncludeFilterType, completedDateRange: DateRangeFilterInput, createdDateRange: DateRangeFilterInput, dueDatesRange: DateRangeFilterInput, projectDateRange: DateRangeFilterInput, projectStatusDateRange: DateRangeFilterInput, dateRange: DateRangeFilterInput, colorThemeId: String, segmentColorOverrides: [SegmentColorOverrideInput!], projectBudgetCategoryIds: [String], projectBudgetDateRange: [Date!])` -> `DashboardWidget!`
