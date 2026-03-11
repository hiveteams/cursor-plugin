# Agent Task Opportunities

> 28 queries, 53 mutations, and a whole lot of time we can give back to people.

This document maps every Hive API surface to concrete agent automations that bridge the gap between **engineering execution** and **business visibility**. Each opportunity is tagged with the primary API operations it would use, the business function it serves, and a rough complexity estimate.

---

## Table of Contents

1. [Engineering ↔ Stakeholder Handoffs](#1-engineering--stakeholder-handoffs)
2. [Sprint & Delivery Ops](#2-sprint--delivery-ops)
3. [Approval & Review Workflows](#3-approval--review-workflows)
4. [Reporting & Dashboards on Demand](#4-reporting--dashboards-on-demand)
5. [Meeting Prep & Follow-up](#5-meeting-prep--follow-up)
6. [Email-to-Action Pipeline](#6-email-to-action-pipeline)
7. [Resource & Capacity Planning](#7-resource--capacity-planning)
8. [Salesforce ↔ Project Management Bridge](#8-salesforce--project-management-bridge)
9. [Goal Tracking & OKR Automation](#9-goal-tracking--okr-automation)
10. [Project Scaffolding & Templates](#10-project-scaffolding--templates)
11. [Communication & Notification Bots](#11-communication--notification-bots)
12. [Housekeeping & Hygiene](#12-housekeeping--hygiene)

---

## 1. Engineering ↔ Stakeholder Handoffs

These are the "I opened a PR, now what?" automations. They close the loop between code changes and the people who need to see them.

### 1.1 — PR-Triggered Desk Check Scheduling
**When I open a PR, schedule a desk check with the product or design stakeholder.**

Create an action assigned to the relevant reviewer with a deadline, link the GitHub branch, and DM them a heads-up.

| | |
|---|---|
| **API ops** | `bulkInsertActions`, `updateActionGithubBranchNames`, `insertMessage`, `groups` |
| **Business value** | Eliminates the Slack-tag-and-pray approach to getting stakeholder eyes on a feature. Reviewers get a tracked task, not a message they can lose. |
| **Complexity** | Medium |

### 1.2 — Branch-to-Task Linking on Push
**When an engineer pushes a branch, automatically link it to the matching Hive action.**

Parse the branch name (e.g., `feat/HIVE-1234-new-widget`) and call `updateActionGithubBranchNames` so the PM can click straight from the task to the code.

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (search by ID), `updateActionGithubBranchNames` |
| **Business value** | PMs stop asking "where's the code for this?" — the link is right on the card. |
| **Complexity** | Low |

### 1.3 — Auto-Status Update on Merge
**When a PR merges, move the linked Hive action to "Ready for QA" or "In Review."**

Look up the action via the branch name, find the right status in the project, and update it.

| | |
|---|---|
| **API ops** | `getActionsByWorkspace`, `bulkUpdateActionStatus` |
| **Business value** | The board reflects reality in real time. No more "oh I forgot to move the card." |
| **Complexity** | Low |

### 1.4 — Deploy-Triggered Stakeholder Notification
**When a deploy completes, DM the stakeholders on every action that shipped.**

Query actions completed in the deploy window, find the assignees' DM groups, and send a formatted message with what went live.

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (by date range + status), `groups` (find DMs), `insertMessage` |
| **Business value** | Stakeholders know what shipped without attending standup or reading release notes. |
| **Complexity** | Medium |

---

## 2. Sprint & Delivery Ops

### 2.1 — Daily Standup Report Generator
**Every morning, generate a summary of what's in progress, what's blocked, and what's overdue — posted to the team chat.**

Query actions by status, check for overdue deadlines, and compose a Buzz message.

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (filter by status, assignees, dates), `getLabels`, `insertMessage` |
| **Business value** | Async standups that write themselves. The team gets signal without the ceremony. |
| **Complexity** | Medium |

### 2.2 — Sprint Velocity Snapshot Dashboard
**At sprint end, auto-generate a dashboard showing completed vs. planned story points, broken down by assignee.**

Create a dashboard with bar charts for story points by assignee, completed actions count, and overdue counts.

| | |
|---|---|
| **API ops** | `createDashboardV2`, `createDashboardWidget` (barChart, XAxis=assignees, YAxis=agileStoryPoints) |
| **Business value** | Leadership gets a polished velocity report without anyone in engineering spending 45 minutes building it in a spreadsheet. |
| **Complexity** | Medium |

### 2.3 — Overdue Action Escalation
**When a task is overdue by more than 2 days, bump its priority to "Urgent" and notify the assignee's manager.**

Query overdue actions, update their priority, and send a DM to the project owner.

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (date filters), `getPriorityLevels`, `bulkUpdateActionsPriorityLevelId`, `insertMessage` |
| **Business value** | Blockers don't silently age. The right people find out before the sprint review, not during it. |
| **Complexity** | Medium |

### 2.4 — End-of-Day "What I Shipped" Summary
**At 5 PM, send each engineer a DM with the actions they completed today and the ones still open.**

Filter actions by assignee and completed date range, format it nicely, DM them.

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (assignees, completedDate range), `groups`, `insertMessage` |
| **Business value** | Engineers get a personal highlight reel. Makes it easy to fill out timesheets, update standups, or just feel good about what got done. |
| **Complexity** | Low |

### 2.5 — Milestone Progress News Post
**When a milestone action is completed, publish a news post celebrating the achievement.**

Watch for milestone-flagged actions getting completed, then post an announcement.

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (milestone=true, status="Completed"), `insertPost` |
| **Business value** | The whole org sees meaningful progress without anyone having to write the update. Morale multiplier. |
| **Complexity** | Low |

---

## 3. Approval & Review Workflows

### 3.1 — Smart Approval Routing
**When a design deliverable is uploaded, apply the right approval template and request sign-off from the correct stakeholders.**

Look up approval templates, apply the matching one, then request approvals — all in one step.

| | |
|---|---|
| **API ops** | `getApprovalTemplates`, `applyApprovalTemplate`, `requestApprovals` |
| **Business value** | Creative teams stop manually setting up 5-stage approval chains every time. The process is consistent and instant. |
| **Complexity** | Low |

### 3.2 — Approval Nag Bot
**If an approval has been pending for more than 24 hours, DM the approver with a polite reminder.**

Check the next pending approval stage, see who hasn't approved yet, and message them.

| | |
|---|---|
| **API ops** | `nextApprovalStage`, `currentRoundAndStage`, `groups`, `insertMessage` |
| **Business value** | Approvals don't rot in someone's queue. Reduces average approval time without anyone having to be the "hey, did you see this?" person. |
| **Complexity** | Medium |

### 3.3 — Post-Approval Auto-Status Progression
**When all approvers sign off, automatically move the action to the next status (e.g., "Approved → Ready for Dev").**

Poll `currentRoundAndStage` for fully-approved states, then update the action status.

| | |
|---|---|
| **API ops** | `currentRoundAndStage`, `bulkUpdateActionStatus` |
| **Business value** | Zero lag between "approved" and "in the next stage." The workflow is self-propelling. |
| **Complexity** | Medium |

### 3.4 — Multi-Stage Approval Builder from Natural Language
**"I need legal, then finance, then the VP to sign off on this." → Agent builds the approval round with 3 stages.**

Create the round, insert 3 stages, assign the approvers, and request approvals.

| | |
|---|---|
| **API ops** | `insertApprovalRound`, `insertApprovalStage`, `changeApprovalStageApprover`, `requestApprovals` |
| **Business value** | Non-technical stakeholders can set up complex approval chains by describing them in plain English. |
| **Complexity** | Medium |

---

## 4. Reporting & Dashboards on Demand

### 4.1 — "How's the project going?" Instant Dashboard
**A VP asks how Project X is going. Agent creates a dashboard with status breakdown, overdue count, and timeline view — shared with the VP.**

Build a dashboard with pie chart (statuses), numbers widget (overdue), and actions list.

| | |
|---|---|
| **API ops** | `getProjects`, `createDashboardV2`, `createDashboardWidget` (pieChart, numbers, actionsList, projectStatus) |
| **Business value** | Executives get a live, interactive view instead of a stale slide deck. Built in seconds, not hours. |
| **Complexity** | Medium |

### 4.2 — Weekly Team Workload Report
**Every Monday, generate a bar chart showing action count by assignee across all active projects.**

| | |
|---|---|
| **API ops** | `createDashboardV2`, `createDashboardWidget` (barChart, XAxis=assignees, YAxis=countOfActions), `insertMessage` |
| **Business value** | Managers spot overloaded team members before burnout, not after. |
| **Complexity** | Medium |

### 4.3 — Custom Stakeholder Portfolio View
**Build a project portfolio dashboard filtered to only the projects a specific exec owns, with budget overview and status widgets.**

| | |
|---|---|
| **API ops** | `getProjects` (filter by owner), `createDashboardV2` (filter by projects), `createDashboardWidget` (projectsList, budgetOverview, projectStatus) |
| **Business value** | Each leader gets their own command center without IT building it. |
| **Complexity** | Medium |

### 4.4 — Completion Trend Line for Board Meetings
**Generate a line chart showing actions completed per week over the last quarter, grouped by project.**

| | |
|---|---|
| **API ops** | `createDashboardWidget` (line, XAxis=completedDate, YAxis=countOfActions, timeUnitsType, completedDateRange) |
| **Business value** | Board-ready throughput visualization that refreshes itself. |
| **Complexity** | Low |

### 4.5 — Label-Based Initiative Tracker
**"Show me everything tagged 'Q2 Launch'." → Agent builds a filtered dashboard scoped to that label.**

| | |
|---|---|
| **API ops** | `getLabels`, `createDashboardV2` (filter by labels), `createDashboardWidget` |
| **Business value** | Cross-project initiative tracking without complex project restructuring. |
| **Complexity** | Low |

---

## 5. Meeting Prep & Follow-up

### 5.1 — Pre-Meeting Briefing Document
**30 minutes before a meeting, compile open actions, blockers, and recent comments relevant to the attendees and post them to the meeting's materials.**

| | |
|---|---|
| **API ops** | `getMeetingUserData`, `getActionsByWorkspace` (by assignees), `actionComments`, `updateMeetingUserData` (add materials and goals) |
| **Business value** | Everyone walks into the meeting already up to speed. Meetings get shorter. |
| **Complexity** | High |

### 5.2 — Post-Meeting Action Item Generator
**After a meeting, parse the next steps and create Hive actions for each one, assigned to the right people with deadlines.**

| | |
|---|---|
| **API ops** | `getMeetingUserData` (read nextSteps), `bulkInsertActions` (create actions with assignees and deadlines), `updateMeetingUserData` (mark next steps as done) |
| **Business value** | Meeting action items actually get tracked instead of dying in someone's notebook. Accountability is automatic. |
| **Complexity** | Medium |

### 5.3 — Meeting Goal Completion Tracker
**Before a recurring meeting, check whether the goals from last time were completed and update the meeting data accordingly.**

| | |
|---|---|
| **API ops** | `getMeetingUserDataList`, `getMeetingUserData`, `getActionsByWorkspace`, `updateMeetingUserData` (update goal completion status) |
| **Business value** | Recurring meetings start with a scorecard, not "so, where were we?" |
| **Complexity** | Medium |

---

## 6. Email-to-Action Pipeline

### 6.1 — Client Email → Task Creation
**When a client emails a request, agent creates an action with the email content as the description, assigns it to the account manager, and labels it "Client Request."**

| | |
|---|---|
| **API ops** | `getEmails` (filter by sender), `bulkInsertActions` (with description, labels, assignees), `getLabels` |
| **Business value** | Client requests never get lost in an inbox. They're immediately visible on the project board. |
| **Complexity** | Medium |

### 6.2 — Email Follow-up Reminder
**If a sent email hasn't received a reply in 3 days, create a reminder to follow up.**

| | |
|---|---|
| **API ops** | `getEmails` (searchSentOnly, date filter), `createReminder` |
| **Business value** | Sales and account management never let a warm lead or open question go cold. |
| **Complexity** | Medium |

### 6.3 — Email Digest → Stakeholder DM
**Summarize unread emails from key accounts and DM the summary to the account owner every morning.**

| | |
|---|---|
| **API ops** | `getEmails`, `groups`, `insertMessage` |
| **Business value** | Account managers start the day knowing exactly what clients need without triaging their inbox first. |
| **Complexity** | Medium |

---

## 7. Resource & Capacity Planning

### 7.1 — Auto-Allocate Engineers to Sprint Work
**When sprint planning is done, create resource assignments for each engineer based on their assigned actions and estimated story points.**

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (by assignees, sprint dates), `createResourceAssignment` |
| **Business value** | Resource allocation happens in one click after planning, not in a 30-minute spreadsheet exercise. |
| **Complexity** | High |

### 7.2 — Utilization Alert
**When a team member's resource assignments exceed capacity for a given week, DM their manager.**

| | |
|---|---|
| **API ops** | `getResourceAssignments` (by date range + resource), `groups`, `insertMessage` |
| **Business value** | Overallocation is caught before it becomes missed deadlines. |
| **Complexity** | Medium |

### 7.3 — Placeholder-to-Hire Pipeline
**When headcount is approved, create a resource placeholder with bill/cost rates, assign it to upcoming projects, and notify hiring managers.**

| | |
|---|---|
| **API ops** | `createResourcePlaceholder`, `createResourceAssignment`, `insertMessage` |
| **Business value** | Resource planning doesn't wait for the hire to start. Projects are modeled with realistic staffing from day one. |
| **Complexity** | Medium |

### 7.4 — Bench Time Reporter
**Weekly report showing team members with less than 60% allocation, posted to the leadership channel.**

| | |
|---|---|
| **API ops** | `getResourceAssignments` (by date range), `workspacePlaceholders`, `createDashboardWidget` (barChart, resourcingUtilization) |
| **Business value** | Leadership sees available capacity at a glance for rebalancing or new project staffing. |
| **Complexity** | High |

---

## 8. Salesforce ↔ Project Management Bridge

### 8.1 — Won Opportunity → Project Kickoff
**When a Salesforce Opportunity is marked "Closed Won," auto-create a Hive project from a template, add the account team as members, and create the onboarding actions.**

| | |
|---|---|
| **API ops** | `salesforceOperation` (QUERY Opportunities), `getProjects` (find template), `applyProjectTemplate`, `updateMembersPermissions`, `bulkInsertActions` |
| **Business value** | Zero lag between "we closed the deal" and "the delivery team is ramped up." No more "wait, who's doing onboarding?" |
| **Complexity** | High |

### 8.2 — Salesforce Contact → Approval Routing
**When a deliverable needs client approval, look up the client contact in Salesforce and add them as an external approver.**

| | |
|---|---|
| **API ops** | `salesforceOperation` (QUERY Contacts), `insertApprovalRound`, `insertApprovalStage`, `changeApprovalStageApprover` (type: external) |
| **Business value** | Client approvals are routed to the right person automatically. No more "who signs off on their side?" |
| **Complexity** | High |

### 8.3 — CRM Activity Sync
**When actions are completed on a client project, log them as Activities on the Salesforce Account so the sales team sees delivery progress.**

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (completed, by project), `salesforceOperation` (INSERT Task/Activity) |
| **Business value** | Sales and CS see delivery progress without asking engineering. Upsell conversations are grounded in real data. |
| **Complexity** | Medium |

### 8.4 — Lead Conversion with Project Scaffolding
**Convert a Salesforce lead and simultaneously scaffold the Hive project for the new customer.**

| | |
|---|---|
| **API ops** | `salesforceOperation` (CONVERT_LEAD), `bulkInsertActions`, `applyProjectTemplate` |
| **Business value** | The handoff from sales to delivery is a single agent action, not a week of setup. |
| **Complexity** | High |

---

## 9. Goal Tracking & OKR Automation

### 9.1 — Auto-Create Quarterly OKRs from Template
**At quarter start, generate the standard OKR structure: company goals → team goals → individual goals, with ownership and measurement types pre-configured.**

| | |
|---|---|
| **API ops** | `createGoal` (parent/child hierarchy, measurementType, displayType) |
| **Business value** | OKR setup goes from a 2-week process to a 2-minute one. Every team starts the quarter on the same page. |
| **Complexity** | Medium |

### 9.2 — Goal Progress Auto-Update
**Link goals to projects, and as actions complete, the goal progress updates automatically. Post a weekly summary to the goals chat.**

| | |
|---|---|
| **API ops** | `getGoals`, `getActionsByWorkspace` (by projectIds, completed), `insertMessage` |
| **Business value** | Goals aren't aspirational documents that rot in a drawer. They're live dashboards. |
| **Complexity** | Medium |

### 9.3 — At-Risk Goal Escalation
**When a goal is behind schedule (current value < expected trajectory), alert the goal owners and their managers.**

| | |
|---|---|
| **API ops** | `getGoals` (selector: status='atRisk'), `groups`, `insertMessage` |
| **Business value** | Course corrections happen mid-quarter, not in the post-mortem. |
| **Complexity** | Low |

### 9.4 — Goal Achievement News Blast
**When a goal hits its target value, post a company-wide announcement celebrating the milestone.**

| | |
|---|---|
| **API ops** | `getGoals`, `insertPost` |
| **Business value** | Wins get celebrated publicly and in real time. Culture impact is real. |
| **Complexity** | Low |

---

## 10. Project Scaffolding & Templates

### 10.1 — "New Feature" One-Liner
**Engineer says "spin up a project for the new payments integration." Agent creates the project from a template, adds standard statuses, sets up labels, and adds the team.**

| | |
|---|---|
| **API ops** | `getProjects` (find template), `applyProjectTemplate`, `addStatusToProjectView`, `setCustomStatusColor`, `updateMembersPermissions`, `addProjectOwner` |
| **Business value** | Project setup is consistent and instant. No more "I set up the board wrong" or "we forgot to add the QA status." |
| **Complexity** | Medium |

### 10.2 — Action-to-Project Promotion
**When a task grows beyond a single action (too many sub-tasks), convert it to a full project with proper structure.**

| | |
|---|---|
| **API ops** | `convertActionToProject`, `applyProjectTemplate`, `updateMembersPermissions` |
| **Business value** | Organic project growth is handled gracefully. The task that outgrew its home gets a proper one. |
| **Complexity** | Low |

### 10.3 — Recurring Project Cloning
**Every month, clone the "Monthly Operations" project with fresh actions, dates shifted forward, and the same team assigned.**

| | |
|---|---|
| **API ops** | `getProjects`, `copyAction` (for each action), `bulkInsertActions`, `insertRecurringAction` |
| **Business value** | Ops teams don't rebuild their project board every month. It just appears, ready to go. |
| **Complexity** | High |

### 10.4 — Template Application with Custom Fields
**Apply a project template AND enable the right custom fields for that project type (e.g., "Client Project" gets Budget, Client Contact, Contract End Date fields).**

| | |
|---|---|
| **API ops** | `applyProjectTemplate`, `getCustomFields`, `addActionCustomFields`, `updateProjectsCustomFields` |
| **Business value** | Projects are born fully configured. No one has to remember "oh, we need to turn on the budget field for client projects." |
| **Complexity** | Medium |

---

## 11. Communication & Notification Bots

### 11.1 — New Team Member Onboarding DM
**When a new member is added to a project, DM them with a welcome message, links to key notebooks, and their assigned onboarding actions.**

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (by assignee + project), `notebooks` (by project), `groups`, `insertMessage` |
| **Business value** | New team members ramp up faster. They know where things are from minute one. |
| **Complexity** | Medium |

### 11.2 — Cross-Team Dependency Alert
**When a task in Project A is blocked by a task in Project B, notify Project B's owner and create a linked action.**

| | |
|---|---|
| **API ops** | `getActionsByWorkspace`, `getProjects`, `bulkInsertActions`, `insertMessage` |
| **Business value** | Cross-team dependencies don't silently block. The other team knows before it's a crisis. |
| **Complexity** | High |

### 11.3 — Friday Wins Roundup
**Every Friday at 4 PM, post a news update summarizing all actions completed this week, grouped by project, with shout-outs to top contributors.**

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (completedDate this week, all projects), `insertPost` |
| **Business value** | The whole company sees momentum. It's a morale engine that runs itself. |
| **Complexity** | Medium |

### 11.4 — Smart Reminder System
**"Remind me to check on the API migration every Tuesday at 10am." → Agent creates a recurring reminder tied to the relevant action or chat thread.**

| | |
|---|---|
| **API ops** | `createReminder`, `getActionsByWorkspace` (find the related action) |
| **Business value** | Personal productivity assistant that lives inside the project management tool, not a separate app. |
| **Complexity** | Low |

---

## 12. Housekeeping & Hygiene

### 12.1 — Stale Action Cleanup
**Weekly scan for actions with no updates in 30+ days. Snooze or archive them, and DM the assignee asking if they're still relevant.**

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (date filters, sort by modifiedAt), `updateActionSnoozeDate` or `bulkArchiveActions`, `insertMessage` |
| **Business value** | Boards stay clean. Old tasks don't create noise that makes people ignore the real work. |
| **Complexity** | Medium |

### 12.2 — Unassigned Action Alert
**Daily check for actions in active projects that have no assignee. Post a summary to the project owner's DM.**

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (assignees: empty/null), `getProjects`, `groups`, `insertMessage` |
| **Business value** | Nothing falls through the cracks because nobody owns it. |
| **Complexity** | Low |

### 12.3 — Completed Project Archival
**When all actions in a project are completed, archive the project and notify the owner.**

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (by project, excludeCompletedActions=true → if empty, all done), `updateProjectArchived`, `insertMessage` |
| **Business value** | The project list stays focused on active work. Finished work moves to the archive automatically. |
| **Complexity** | Low |

### 12.4 — Priority Rebalancer
**When more than 5 actions are marked "Urgent" for a single person, DM them and their manager suggesting a re-prioritization, with a list of what's currently urgent.**

| | |
|---|---|
| **API ops** | `getActionsByWorkspace` (by assignee), `getPriorityLevels`, `groups`, `insertMessage` |
| **Business value** | When everything is urgent, nothing is. This automation forces the prioritization conversation before it's too late. |
| **Complexity** | Medium |

### 12.5 — Form Submission → Intake Triage
**When a form submission creates an action, auto-label it, set priority based on form fields, assign it to the intake team, and notify the requester.**

| | |
|---|---|
| **API ops** | `getWorkspaceForms`, `getActionsByWorkspace`, `bulkUpdateActionLabels`, `bulkUpdateActionsPriorityLevelId`, `bulkUpdateActionsAssignees`, `insertMessage` |
| **Business value** | Intake requests are triaged instantly, not sitting in a queue until someone manually sorts them. |
| **Complexity** | Medium |

---

## Capability Quick-Reference Matrix

| API Operation | Opportunities That Use It |
|---|---|
| `getActionsByWorkspace` | 1.2, 1.3, 1.4, 2.1, 2.3, 2.4, 4.5, 5.1, 5.2, 5.3, 6.1, 7.1, 8.3, 9.2, 11.1, 11.2, 11.3, 12.1, 12.2, 12.3, 12.4, 12.5 |
| `bulkInsertActions` | 1.1, 5.2, 6.1, 8.1, 8.4, 10.3, 11.2 |
| `insertMessage` | 1.1, 1.4, 2.1, 2.3, 2.4, 3.2, 6.3, 7.2, 7.3, 9.2, 9.3, 11.1, 11.2, 11.3, 12.1, 12.2, 12.3, 12.4, 12.5 |
| `groups` | 1.1, 1.4, 2.4, 3.2, 6.3, 7.2, 9.3, 11.1, 12.2, 12.4 |
| `bulkUpdateActionStatus` | 1.3, 3.3, 2.1 |
| `createDashboardV2` | 2.2, 4.1, 4.2, 4.3 |
| `createDashboardWidget` | 2.2, 4.1, 4.2, 4.3, 4.4, 4.5, 7.4 |
| `getProjects` | 4.1, 4.3, 10.1, 10.3, 11.2, 12.3 |
| `insertPost` | 2.5, 9.4, 11.3 |
| `salesforceOperation` | 8.1, 8.2, 8.3, 8.4 |
| `createGoal` | 9.1 |
| `getGoals` | 9.2, 9.3, 9.4 |
| `applyApprovalTemplate` | 3.1 |
| `requestApprovals` | 3.1, 3.4 |
| `nextApprovalStage` | 3.2 |
| `currentRoundAndStage` | 3.2, 3.3 |
| `createReminder` | 6.2, 11.4 |
| `getEmails` | 6.1, 6.2, 6.3 |
| `getMeetingUserData` | 5.1, 5.2, 5.3 |
| `updateMeetingUserData` | 5.1, 5.2, 5.3 |
| `createResourceAssignment` | 7.1, 7.3 |
| `getResourceAssignments` | 7.2, 7.4 |
| `applyProjectTemplate` | 8.1, 10.1, 10.2, 10.4 |
| `convertActionToProject` | 10.2 |
| `updateActionGithubBranchNames` | 1.1, 1.2 |
| `bulkUpdateActionLabels` | 6.1, 12.5 |
| `bulkUpdateActionsPriorityLevelId` | 2.3, 12.5 |
| `bulkUpdateActionsAssignees` | 12.5 |
| `updateActionSnoozeDate` | 12.1 |
| `bulkArchiveActions` | 12.1 |
| `updateProjectArchived` | 12.3 |
| `updateMembersPermissions` | 8.1, 10.1, 10.2 |
| `createResourcePlaceholder` | 7.3 |
| `getCustomFields` | 10.4, 12.5 |
| `notebooks` | 11.1 |
| `actionComments` | 5.1 |
| `getPriorityLevels` | 2.3, 12.4, 12.5 |
| `getLabels` | 2.1, 4.5, 6.1 |
| `getMeetingUserDataList` | 5.3 |
| `getWorkspaceForms` | 12.5 |
| `addStatusToProjectView` | 10.1 |
| `setCustomStatusColor` | 10.1 |
| `addProjectOwner` | 10.1 |
| `insertApprovalRound` | 3.4, 8.2 |
| `insertApprovalStage` | 3.4, 8.2 |
| `changeApprovalStageApprover` | 3.4, 8.2 |
| `copyAction` | 10.3 |
| `insertRecurringAction` | 10.3 |
| `addActionCustomFields` | 10.4 |
| `updateProjectsCustomFields` | 10.4 |
| `workspacePlaceholders` | 7.4 |
| `getApprovalTemplates` | 3.1 |

---

## What's Not Covered (and Why)

A few API operations aren't featured above because they're configuration primitives rather than business workflows:

- **`bulkUpsertCustomFields`** — Schema changes, not daily automation
- **`disableActionCustomFields` / `disableProjectsCustomFields`** — Cleanup ops, rarely triggered by a business event
- **`setActionColor`** — Visual preference, not a workflow
- **`setStoryPoints`** — Usually set during estimation, could be part of 2.2 but adds complexity
- **`unsetRecurringActions`** — Edge case cleanup
- **`removeProjectOwner`** — Rarely automated
- **`updateProjectDescription`** — Usually a one-time setup
- **`updateResourcePlaceholder`** — Admin maintenance
- **`runWorkflow`** — Meta-automation (running templates), could wrap any of the above

These could still be composed into larger automations, but they're not the headline acts.
