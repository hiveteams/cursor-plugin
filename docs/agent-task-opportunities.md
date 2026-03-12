# Agent Task Opportunities

> A catalog of workflows that an AI agent could simplify, speed up, or fully automate by connecting Hive's API surface to day-to-day engineering and business functions.

---

## How to Read This Document

Each opportunity is framed as a **"When X happens, the agent does Y"** scenario.  
Underneath, you'll find the specific API endpoints that make it possible, plus a plain-English value statement any stakeholder can understand.

---

## 1. Code Review ↔ Stakeholder Coordination

### 1a. Schedule desk-check appointments when a PR is opened

**Trigger:** Engineer opens a PR linking a Hive action (via `updateActionGithubBranchNames`).  
**Agent workflow:**
1. Look up the action and its project (`getActionsByWorkspace`).
2. Identify the product/design owner on the project (`getProjects` → project owners).
3. Create or find the DM group with that stakeholder (`groups` / `insertGroup`).
4. Send a message requesting a desk-check time slot (`insertMessage`).
5. Set the action status to "In Review" (`bulkUpdateActionStatus`).

**Value:** Reviewers hear about the work *the moment it's ready*, not when someone remembers to Slack them.

---

### 1b. Auto-link GitHub branches to Hive actions

**Trigger:** Branch name contains an action ID (e.g. `feature/HIVE-1234-widget-redesign`).  
**Agent workflow:**
1. Parse the branch name for the action ID.
2. Call `updateActionGithubBranchNames` to link the branch.
3. Add a comment on the action summarizing the PR scope (`insertMessage` with `containerType: action`).

**Value:** Zero manual copy-paste between GitHub and Hive. Every action automatically has a breadcrumb trail to its code.

---

### 1c. Approval-gate deployments on design sign-off

**Trigger:** An action reaches "Ready for Approval" status.  
**Agent workflow:**
1. Look up the approval template for design reviews (`getApprovalTemplates`).
2. Apply it to the action (`applyApprovalTemplate`).
3. Request approvals (`requestApprovals`).
4. Check `nextApprovalStage` periodically; once approved, update the action status to "Ready to Deploy" (`bulkUpdateActionStatus`).

**Value:** Deployment can't happen until design has formally signed off. No more "I thought you approved it" conversations.

---

## 2. Meeting → Action Pipeline

### 2a. Turn meeting notes into assigned, prioritized tasks

**Trigger:** A meeting ends and Sidekick records transcript data.  
**Agent workflow:**
1. Pull meeting data (`getMeetingUserData` / `getMeetingUserDataList`).
2. Extract next steps and goals from the meeting record.
3. Create Hive actions for each next step (`bulkInsertActions`), setting assignees, deadlines, and priority levels.
4. Update the meeting record to mark next steps as linked (`updateMeetingUserData`).
5. Send a summary message to the relevant project group chat (`insertMessage`).

**Value:** Meeting action items go from "written on a sticky note" to "assigned with a deadline" in seconds, not days.

---

### 2b. Pre-populate meeting prep with relevant context

**Trigger:** 15 minutes before a scheduled meeting with a stakeholder.  
**Agent workflow:**
1. Look up open actions assigned to meeting participants (`getActionsByWorkspace` filtered by `assignees`).
2. Check for overdue items, pending approvals (`currentRoundAndStage`), and blocked work.
3. Update meeting goals/materials with this context (`updateMeetingUserData` → `goals.add`, `materials.add`).
4. Set a reminder (`createReminder`) for the user to review the prep.

**Value:** Walk into every meeting already knowing what's stuck, what's done, and what to discuss. No more "let me pull that up."

---

### 2c. Post-meeting stakeholder broadcast

**Trigger:** Meeting next steps are finalized.  
**Agent workflow:**
1. Read finalized next steps from meeting data (`getMeetingUserData`).
2. Compose a summary and post it to the workspace news feed (`insertPost`).
3. DM each action owner with their specific next steps (`insertMessage` via `participants`).

**Value:** Everyone who wasn't in the meeting still knows what happened and what they owe, within minutes.

---

## 3. Sprint & Milestone Automation

### 3a. Auto-generate sprint actions from a template

**Trigger:** Start of a new sprint (recurring date or manual kick-off).  
**Agent workflow:**
1. Find the sprint template (`getWorkflowsForWorkspacePaginated`).
2. Apply it to the target project or duplicate a template action (`copyAction` / `runWorkflow`).
3. Set scheduled dates and deadlines across all created actions.
4. Assign team members based on resource availability (`getResourceAssignments`, `workspacePlaceholders`).

**Value:** Sprint setup goes from a 30-minute ceremony to a one-click operation.

---

### 3b. Milestone progress alerts for leadership

**Trigger:** Daily or weekly cadence.  
**Agent workflow:**
1. Query all milestone-flagged actions (`getActionsByWorkspace` with `milestone: true`).
2. Check completion status, deadlines, and overdue items.
3. Build a dashboard widget showing milestone health (`createDashboardWidget` with bar chart, X-axis by projects, Y-axis by count of actions).
4. Send a summary message to a leadership group chat (`insertMessage`).

**Value:** Execs get a "red/yellow/green" milestone status without having to ask anyone.

---

### 3c. Story-point velocity tracking

**Trigger:** Action is marked "Completed."  
**Agent workflow:**
1. Read the story points on the completed action (`getActionsByWorkspace` → `storyPoints`).
2. Aggregate points completed this sprint vs. target.
3. Update a velocity goal (`createGoal` or update existing via the goals system).
4. Refresh the sprint dashboard widget (`updateDashboardWidget`).

**Value:** Real-time velocity numbers that update themselves. No end-of-sprint spreadsheet rodeo.

---

## 4. Approval Workflow Orchestration

### 4a. Multi-stage approval chains with automatic escalation

**Trigger:** A content piece, design, or deliverable is submitted for review.  
**Agent workflow:**
1. Create an approval round with staged reviewers (`insertApprovalRound`, `insertApprovalStage`).
2. Add approvers at each stage: first the direct lead, then the director (`changeApprovalStageApprover`).
3. Request approvals (`requestApprovals`).
4. Monitor `nextApprovalStage`; if no response within 24 hours, send a nudge DM (`insertMessage`).
5. Once fully approved, update the action status and notify the submitter.

**Value:** Approvals don't die in someone's queue. The agent follows up so people don't have to.

---

### 4b. Budget approval gating for project spend

**Trigger:** A project's budget custom field exceeds a threshold.  
**Agent workflow:**
1. Monitor project custom fields (`getCustomFields`, `getActionsByWorkspace` with `customFieldId`).
2. When spend crosses a defined limit, apply an approval template (`applyApprovalTemplate`).
3. Notify finance stakeholders via group message (`insertMessage`).
4. Block status progression until approval clears (`currentRoundAndStage` polling).

**Value:** Budget overruns get flagged and gated automatically. Finance finds out before the invoice arrives, not after.

---

## 5. Resource & Capacity Management

### 5a. Auto-balance resource assignments when scope changes

**Trigger:** New actions are added to a project mid-sprint.  
**Agent workflow:**
1. Detect new actions in the project (`getActionsByWorkspace` with `createdAtStart` filter).
2. Check current resource allocations (`getResourceAssignments`).
3. Identify under-allocated team members or placeholders (`workspacePlaceholders`).
4. Create or adjust resource assignments (`createResourceAssignment` / `updateResourceAssignment`).
5. Message the PM with the proposed rebalance (`insertMessage`).

**Value:** Resource conflicts surface in real time instead of at the next standup when it's too late.

---

### 5b. Placeholder-to-person conversion on hire

**Trigger:** A new team member is onboarded.  
**Agent workflow:**
1. Find all placeholder assignments for the role being filled (`getResourceAssignments` by `resourceId`).
2. Update each assignment to the new hire's user ID (`updateResourceAssignment`).
3. Reassign actions from the placeholder to the new hire (`bulkUpdateActionsAssignees`).
4. Update the placeholder's name/rate if it stays active for future planning (`updateResourcePlaceholder`).
5. Send a welcome message to the new hire in their project chat (`insertMessage`).

**Value:** New hires walk in Day 1 with a populated task list and calendar. No "what should I be working on?" limbo.

---

### 5c. Time-off impact analysis

**Trigger:** Someone requests PTO (time-off resource assignment created).  
**Agent workflow:**
1. Find the person's resource assignments overlapping the PTO dates (`getResourceAssignments`).
2. Identify affected projects and their deadlines.
3. Flag actions at risk of missing deadlines (`getActionsByWorkspace` filtered by assignee and date range).
4. Notify project owners with a risk summary (`insertMessage`).
5. Suggest rescheduling or reassignment options.

**Value:** PTO doesn't silently torpedo a deadline. PMs know the impact before they approve the request.

---

## 6. Cross-Tool Sync (Salesforce ↔ Hive)

### 6a. Create delivery actions when a deal closes

**Trigger:** Salesforce Opportunity moves to "Closed Won" (detected via `salesforceOperation` QUERY).  
**Agent workflow:**
1. Query Salesforce for newly closed deals (`salesforceOperation` → QUERY on Opportunity).
2. Create a delivery project or action set in Hive (`bulkInsertActions`) with customer name, deal value, and timeline.
3. Assign the delivery team and set priority based on deal size (`bulkUpdateActionsAssignees`, `bulkUpdateActionsPriorityLevelId`).
4. Add a label like "New Customer Onboarding" (`bulkUpdateActionLabels`).
5. Update the Salesforce Opportunity with a link to the Hive project (`salesforceOperation` → UPDATE).

**Value:** The handoff from Sales to Delivery happens in the same minute the deal closes. No "wait, when did this close?" lag.

---

### 6b. Sync project status back to Salesforce

**Trigger:** Daily cadence or when a project status changes.  
**Agent workflow:**
1. Query Hive projects linked to Salesforce accounts (`getProjects`, cross-reference custom fields).
2. Read completion percentage, milestone status, and any blockers.
3. Update the corresponding Salesforce Account or Opportunity fields (`salesforceOperation` → UPDATE).

**Value:** The sales team sees delivery status in their own tool without asking the PM. Customer conversations are always informed.

---

### 6c. Customer escalation pipeline

**Trigger:** A support case is created in Salesforce.  
**Agent workflow:**
1. Detect new high-priority cases (`salesforceOperation` → QUERY on Case).
2. Create an urgent action in Hive (`bulkInsertActions` with `urgent: true`).
3. Apply the escalation approval workflow (`applyApprovalTemplate`).
4. Notify the engineering lead via DM (`insertMessage`).
5. Set a reminder to check resolution status in 4 hours (`createReminder`).

**Value:** Customer escalations go from "email lost in inbox" to "tracked, assigned, and monitored" in under a minute.

---

## 7. Stakeholder Reporting & Dashboards

### 7a. One-click executive dashboard generation

**Trigger:** End of week/month, or on-demand from a stakeholder.  
**Agent workflow:**
1. Create a dashboard (`createDashboardV2`) with privacy set to "everyone."
2. Add a bar chart widget showing actions by status across projects (`createDashboardWidget` → `barChart`, X-axis: `statuses`, Y-axis: `countOfActions`).
3. Add a pie chart for workload by assignee (`createDashboardWidget` → `pieChart`, X-axis: `assignees`).
4. Add a project status widget for each key initiative.
5. Add a goals list widget showing OKR progress (`createDashboardWidget` → `goalsList`).
6. Share with the leadership team.

**Value:** Execs get a polished status report without anyone building slides. It updates itself.

---

### 7b. Overdue work spotlight report

**Trigger:** Monday morning, every week.  
**Agent workflow:**
1. Query all overdue actions across projects (`getActionsByWorkspace` with date filters).
2. Group by project and assignee.
3. Create or update a dashboard widget highlighting overdue counts (`createDashboardWidget` with `overdueFilter: includeOnly`).
4. Send a summary to each team lead with their team's overdue items (`insertMessage`).

**Value:** Overdue work doesn't hide. Every Monday, team leads know exactly what's slipping.

---

### 7c. Goal progress auto-updates for OKR reviews

**Trigger:** Continuous or pre-OKR-review cadence.  
**Agent workflow:**
1. Pull all active goals (`getGoals`).
2. For goals tied to action completion, re-count completed vs. total actions.
3. For goals tied to project progress, check project status.
4. Post a progress update comment on each goal (`insertMessage` with `containerType: goal`).
5. Refresh goal dashboard widgets (`updateDashboardWidget`).

**Value:** OKR reviews start with accurate numbers, not a scramble to update spreadsheets the night before.

---

## 8. Project Lifecycle Automation

### 8a. New project kickoff from a single sentence

**Trigger:** PM says "spin up a project for X."  
**Agent workflow:**
1. Find the appropriate project template (`getProjects` with `templatesOnly: true`).
2. Create a new project from an action or template (`convertActionToProject` / `applyProjectTemplate`).
3. Add statuses with appropriate colors (`addStatusToProjectView`, `setCustomStatusColor`).
4. Enable relevant custom fields (`addActionCustomFields`, `updateProjectsCustomFields`).
5. Add the PM and team as project members (`updateMembersPermissions`).
6. Set the project owner (`addProjectOwner`).
7. Post a kickoff message to the team (`insertMessage`).

**Value:** A fully configured project with statuses, fields, members, and a kickoff message in 30 seconds instead of 30 minutes.

---

### 8b. Archive stale projects with a grace period

**Trigger:** Weekly scan.  
**Agent workflow:**
1. Find projects with no activity in 30+ days (`getProjects`, cross-reference with action modified dates).
2. Send a warning message to project owners (`insertMessage`): "This project will be archived in 7 days if no action is taken."
3. If no response after 7 days, archive the project (`updateProjectArchived`).

**Value:** The workspace stays clean without someone doing manual spring cleaning. Nothing gets archived without fair warning.

---

### 8c. Action-to-project promotion when complexity grows

**Trigger:** An action accumulates more than N sub-actions.  
**Agent workflow:**
1. Detect actions with a high sub-action count (`getActionsByWorkspace` with `parent` filter).
2. Notify the owner: "This action has grown complex. Want to convert it to a project?"
3. On approval, convert it (`convertActionToProject`), preserving sub-actions as project actions.
4. Apply a template and set up statuses.

**Value:** Work that outgrows a task card gets proper project structure before it becomes unmanageable.

---

## 9. Communication & Notifications

### 9a. Smart digest: daily summary of what matters to you

**Trigger:** Start of each workday.  
**Agent workflow:**
1. Find the user's assigned actions due this week (`getActionsByWorkspace` by assignee, date range).
2. Check for pending approvals awaiting the user (`nextApprovalStage`).
3. Pull unread messages from key project groups (`getMessages`).
4. Check reminders (`getReminders`).
5. Compose and DM a prioritized daily digest (`insertMessage`).

**Value:** One message tells you exactly what to focus on today. No more opening 6 tabs to figure out your priorities.

---

### 9b. Blockers detected → stakeholders notified

**Trigger:** An action sits in "Blocked" status for more than 24 hours.  
**Agent workflow:**
1. Scan for actions in "Blocked" status (`getActionsByWorkspace` with `status: "Blocked"`).
2. Look up the project owner and the action assignee.
3. Send a message to both: "This has been blocked for 24h. Can we unblock?" (`insertMessage`).
4. If still blocked after 48h, escalate to the project owner's manager.

**Value:** Blocked work gets unstuck faster because the right people hear about it at the right time.

---

### 9c. Workspace news posts for major milestones

**Trigger:** A milestone action is completed.  
**Agent workflow:**
1. Detect milestone completion (`getActionsByWorkspace` with `milestone: true`, `excludeCompletedActions: false`).
2. Compose a celebratory news post with project context (`insertPost`).
3. @-mention the team that delivered it.

**Value:** Wins get celebrated visibly. The whole org knows when big things ship, not just the team that built it.

---

## 10. Email ↔ Task Bridge

### 10a. Turn client emails into tracked actions

**Trigger:** Email arrives from a known client domain.  
**Agent workflow:**
1. Search inbox for new emails from the client (`getEmails` with `from` filter).
2. Parse the email for action items or requests.
3. Create Hive actions with the email content as the description (`bulkInsertActions`).
4. Attach the email thread to the action.
5. Assign to the account manager and label as "Client Request" (`bulkUpdateActionsAssignees`, `bulkUpdateActionLabels`).

**Value:** Client requests never fall through the cracks. Every email becomes a trackable, assignable task.

---

### 10b. Email follow-up reminders for unanswered outreach

**Trigger:** 48 hours after sending an email with no reply.  
**Agent workflow:**
1. Search sent emails from the last week (`getEmails` with `searchSentOnly: true`).
2. Cross-reference with inbox for replies.
3. For unanswered emails, create a follow-up reminder (`createReminder`).
4. Optionally, create a follow-up action assigned to the sender (`bulkInsertActions`).

**Value:** Important outreach doesn't silently die. The agent remembers to follow up even when you're heads-down on something else.

---

## 11. Label & Priority Intelligence

### 11a. Auto-label actions based on content analysis

**Trigger:** New action is created.  
**Agent workflow:**
1. Read the action title and description.
2. Look up existing labels (`getLabels`).
3. Match keywords to labels (e.g., "bug" → Bug label, "design" → Design label).
4. Apply matching labels (`bulkUpdateActionLabels`).
5. Suggest a priority level based on keywords like "urgent," "blocker," "nice-to-have" (`bulkUpdateActionsPriorityLevelId`).

**Value:** Consistent tagging without relying on everyone to remember. Reports and filters actually work because data is clean.

---

### 11b. Priority re-ranking based on deadline proximity

**Trigger:** Daily scan.  
**Agent workflow:**
1. Pull all open actions with deadlines (`getActionsByWorkspace` sorted by deadline).
2. Compare current priority to deadline urgency.
3. Bump priority for items due within 48 hours that are still low-priority (`bulkUpdateActionsPriorityLevelId`).
4. Notify assignees of the priority change (`insertMessage`).

**Value:** Priority levels stay honest. Something due tomorrow doesn't sit at "Low" because someone forgot to update it.

---

## 12. Recurring Work & Compliance

### 12a. Automated compliance checklist generation

**Trigger:** Start of each quarter or regulatory cycle.  
**Agent workflow:**
1. Duplicate the compliance checklist template action (`copyAction`).
2. Set it as recurring (`insertRecurringAction`).
3. Assign to the compliance officer, set deadlines.
4. Apply the approval template for sign-off (`applyApprovalTemplate`).
5. Create a reminder 1 week before the deadline (`createReminder`).

**Value:** Compliance tasks generate themselves on schedule. Nobody has to remember it's audit season.

---

### 12b. Stop recurring actions that are no longer relevant

**Trigger:** A project is archived or completed.  
**Agent workflow:**
1. Detect project archival (`getProjects` with `includeArchived: true`).
2. Find all recurring actions tied to that project (`getActionsByWorkspace`).
3. Unset their recurring schedule (`unsetRecurringActions`).
4. Notify the action owners that the recurrence has been stopped (`insertMessage`).

**Value:** Ghost tasks stop haunting people's action lists. When a project ends, its recurring work ends too.

---

## 13. Form & Intake Automation

### 13a. Triage incoming form submissions

**Trigger:** New form submission creates an action.  
**Agent workflow:**
1. Monitor for new actions created via forms (`getWorkspaceForms`, `getActionsByWorkspace` with `createdAtStart`).
2. Read custom field values to determine type and urgency (`getCustomFields`, action custom field values).
3. Route to the correct project (`updateActionProject`).
4. Assign to the appropriate team member (`bulkUpdateActionsAssignees`).
5. Set priority and labels (`bulkUpdateActionsPriorityLevelId`, `bulkUpdateActionLabels`).
6. Send an acknowledgment message to the submitter.

**Value:** Intake requests get routed and prioritized in seconds, not stuck in a triage queue for days.

---

## 14. Snooze & Focus Management

### 14a. Smart snooze based on dependencies

**Trigger:** An action's dependency (parent or related action) isn't complete yet.  
**Agent workflow:**
1. Identify actions that can't start until a predecessor finishes.
2. Snooze the dependent action until the predecessor's deadline (`updateActionSnoozeDate`).
3. When the predecessor completes, un-snooze and notify (`updateActionSnoozeDate` with null).

**Value:** People only see work they can actually do right now. No noise from tasks that are blocked by something upstream.

---

## 15. Custom Field & Data Hygiene

### 15a. Enforce required fields before status transitions

**Trigger:** An action's status is changed.  
**Agent workflow:**
1. Check if required custom fields are populated (`getCustomFields`, action data).
2. If missing, block the transition by reverting status and notifying the assignee.
3. Alternatively, prompt the assignee to fill in the missing data (`insertMessage`).

**Value:** Data quality stays high without manual audits. Reports are trustworthy because the underlying data is complete.

---

### 15b. Bulk data cleanup campaigns

**Trigger:** On-demand or scheduled.  
**Agent workflow:**
1. Scan for actions with missing labels, empty descriptions, or no assignees (`getActionsByWorkspace`).
2. Generate a report of hygiene issues.
3. Send personalized cleanup requests to each owner (`insertMessage`).
4. Track cleanup progress via a dashboard widget (`createDashboardWidget`).

**Value:** Data rot gets addressed proactively. The workspace stays useful instead of becoming a graveyard of half-filled-out cards.

---

---

# Part 2: Business Jobs-to-Be-Done

> The first 15 sections above lean toward the engineering-PM interface. The 10 below are pure business repeatable motions -- the kind of work that eats Tuesday afternoons and produces no competitive advantage. Every one is a recurring "job" someone does today by hand.

---

## 16. Client QBR Prep (Quarterly Business Review)

**The job:** Every quarter, an account manager spends 3-5 hours pulling together project status, milestone completions, goal progress, and open items to present to a client.

**Agent workflow:**
1. Pull all projects tagged to the client account (`getProjects`, filter by client label or custom field).
2. For each project, gather completed milestones this quarter (`getActionsByWorkspace` with `milestone: true`, `excludeCompletedActions: false`, date range).
3. Pull goal progress for client-linked goals (`getGoals` filtered by `ownerIds` or `specificIds`).
4. Read open/overdue action counts per project for a risk snapshot.
5. Build a QBR dashboard with charts: milestones delivered, actions completed over time, goal attainment (`createDashboardV2`, `createDashboardWidget` with `completedDateRange`).
6. Compose a narrative summary and post it to the client's project group (`insertMessage`) or create a notebook (`notebooks` query to find existing, or create via notes).
7. Set a reminder for the account manager to review the package 2 days before the meeting (`createReminder`).

**Value:** QBR prep goes from a 4-hour data scavenger hunt to a 15-minute review of an agent-generated package. Account managers can run 3x the book of business without dropping the ball.

---

## 17. Capacity Forecast for New Business

**The job:** Before committing to a new client engagement or internal initiative, a resource manager needs to answer: "Can we actually staff this with who we have, and when?"

**Agent workflow:**
1. Query all current resource assignments across the workspace (`getResourceAssignments` with date range for the proposed engagement window).
2. Pull placeholder assignments to see planned-but-unfilled roles (`workspacePlaceholders`, `getResourceAssignments` by placeholder `resourceId`).
3. Calculate available hours per person by subtracting allocated hours from standard capacity.
4. Cross-reference the proposed project template to estimate required hours (`getProjects` with `templatesOnly: true`, count actions and story points).
5. Produce a gap analysis: which roles are available, which are overbooked, and when the first feasible start date would be.
6. Send the summary to the sales lead and resource manager (`insertMessage`).
7. If the answer is "yes, but we need a hire," create a placeholder for the missing role (`createResourcePlaceholder`) and draft resource assignments against it (`createResourceAssignment`).

**Value:** The answer to "can we take this on?" stops being a guess and starts being a data-backed recommendation. Sales doesn't oversell; delivery doesn't get blindsided.

---

## 18. Written Standup Generation

**The job:** Every morning, each team member is expected to post a standup update: what they did yesterday, what they're doing today, and what's blocking them. Most people either skip it or phone it in.

**Agent workflow:**
1. Find all actions the user completed yesterday (`getActionsByWorkspace` by assignee, `status: "Completed"`, date range = yesterday).
2. Find all actions currently in progress (`getActionsByWorkspace` by assignee, `status: "In Progress"`).
3. Check for any blocked items (`status: "Blocked"`).
4. Check for any pending approvals the user is waiting on (`currentRoundAndStage` across their actions).
5. Compose a standup message summarizing: Done / Doing / Blocked.
6. Post it to the team standup group chat (`insertMessage` to the project or standup `group`).

**Value:** Standups actually happen, and they're accurate. Managers get visibility without the daily "did everyone post?" nag. Engineers save 5-10 minutes every morning -- that's 40+ hours/year per person.

---

## 19. Cross-Project Dependency Mapping

**The job:** When multiple teams are working on related initiatives, someone (usually a program manager) has to manually identify which team's work blocks another team's work and maintain that picture as things change.

**Agent workflow:**
1. Query all active projects in the workspace (`getProjects`).
2. For each project, pull open actions and their sub-actions (`getActionsByWorkspace` with `parent` to map hierarchies).
3. Read custom fields that track cross-project dependencies (e.g., a "Depends On" project or action custom field — `getCustomFields`, `getActionsByWorkspace` with `customFieldId`).
4. Identify actions in Project A that reference actions in Project B.
5. Check status alignment: if a dependency in Project B is behind schedule, flag the downstream action in Project A.
6. Build a dashboard widget visualizing cross-project dependencies and their health (`createDashboardWidget`).
7. Notify both project owners when a dependency is at risk (`insertMessage`).

**Value:** The program manager's mental model of "what depends on what" becomes a living, auto-updating map. Cross-team surprises drop dramatically.

---

## 20. Client-Facing Status Email Drafting

**The job:** Account managers and project leads send weekly or biweekly status emails to clients. They spend 20-30 minutes per client gathering data and writing a professional update.

**Agent workflow:**
1. Pull the client's projects and their current status (`getProjects`, `getActionsByWorkspace`).
2. Identify milestones completed since the last update (`getActionsByWorkspace` with `milestone: true`, date-filtered).
3. Count actions completed, in progress, and overdue.
4. Check for any open risks or blockers (`status: "Blocked"`).
5. Review recent action comments for notable updates (`actionComments`).
6. Check the most recent emails sent to the client for continuity (`getEmails` with `to` filter).
7. Compose a polished status summary and post it as a draft note (`insertMessage` to the account manager's DM with themselves, or to a drafts group).
8. Set a reminder to review and send by end of day (`createReminder`).

**Value:** A 25-minute writing task becomes a 3-minute review-and-send. Clients get consistent, professional updates on schedule, which directly impacts retention and trust.

---

## 21. Portfolio Health Scoring

**The job:** A VP or department head manages 15-30 active projects and needs to quickly identify which ones need attention. Today this means opening each project, eyeballing it, and building a mental ranking.

**Agent workflow:**
1. Pull all active projects (`getProjects`, excluding archived and templates).
2. For each project, compute health signals:
   - Overdue action ratio (`getActionsByWorkspace` with date filters).
   - Days since last status update (action `modifiedAt` recency).
   - Open blocker count (`status: "Blocked"`).
   - Approval bottlenecks (`currentRoundAndStage` across project actions).
   - Resource allocation vs. plan (`getResourceAssignments`).
3. Score each project as Green / Yellow / Red based on thresholds.
4. Build a portfolio dashboard with a summary widget per project (`createDashboardV2`, `createDashboardWidget` for each).
5. Send a weekly portfolio health digest to the leadership group (`insertMessage`).
6. For any Red projects, automatically DM the project owner asking for a risk mitigation update (`insertMessage`).

**Value:** A VP can scan 30 projects in 60 seconds instead of 60 minutes. Attention goes to the fires, not to the projects that are humming along fine.

---

## 22. Vendor / Contractor Onboarding Checklist

**The job:** When a new contractor or vendor starts, someone has to create accounts, share project access, set up introductions, assign initial work, and make sure nothing falls through the cracks. This happens dozens of times a year at a growing company.

**Agent workflow:**
1. Duplicate the contractor onboarding template action (`copyAction` from the onboarding template).
2. Set the new contractor as the assignee on the parent action (`bulkUpdateActionsAssignees`).
3. Create sub-actions for each onboarding step (NDA, access provisioning, intro meetings, first assignment) — these come from the template.
4. Assign internal owners to each sub-action (IT for access, PM for intro meeting, etc.).
5. Set deadlines relative to the start date.
6. Add the contractor to relevant project groups (`updateMembersPermissions`).
7. Send an introduction message to the project chat (`insertMessage`): "Welcome [Name], here's your onboarding checklist."
8. Create a resource assignment for the contractor's allocation (`createResourceAssignment`).
9. Set a 30-day reminder to check in on onboarding completion (`createReminder`).

**Value:** Every contractor onboarding is consistent, nothing gets skipped, and the PM doesn't have to remember 12 manual steps. Time-to-productivity drops from 2 weeks to 2 days.

---

## 23. Risk Register Maintenance

**The job:** A program manager is supposed to maintain a living risk register -- a list of things that could go wrong, their likelihood, impact, and mitigation status. In practice, it gets updated right before a steering committee meeting and is stale the rest of the time.

**Agent workflow:**
1. Scan all projects for risk indicators (`getActionsByWorkspace` across projects):
   - Actions overdue by more than 3 days.
   - Actions in "Blocked" for more than 48 hours.
   - Milestones with no progress in the last 2 weeks.
   - Resource assignments where allocation exceeds 100% (`getResourceAssignments`).
   - Approval stages stuck awaiting response for 3+ days (`nextApprovalStage`, `currentRoundAndStage`).
2. For each detected risk, check if a matching risk action already exists in the Risk Register project.
3. If not, create a new risk action (`bulkInsertActions`) with title, description, affected project, and severity label (`bulkUpdateActionLabels`).
4. If it already exists, update the description with the latest data (`bulkUpdateActionDescription`).
5. Set a custom field for "Risk Score" based on severity and age (`bulkUpdateActionCustomFields`).
6. Refresh the risk register dashboard (`updateDashboardWidget`).
7. Before each steering committee meeting, send a risk summary to the leadership group (`insertMessage`).

**Value:** The risk register updates itself continuously. Steering committees discuss real, current risks instead of stale guesses. Nothing festers unnoticed.

---

## 24. Proposal Effort Estimation from Historical Data

**The job:** When scoping a new project or responding to an RFP, a delivery lead needs to estimate hours, cost, and timeline. Today they either guess or dig through old projects to find comparable work.

**Agent workflow:**
1. Find completed projects similar to the proposed work (`getProjects`, filter by labels or name search via `searchParams`).
2. For each comparable project, count total actions, completed story points, and duration from first action to last completion (`getActionsByWorkspace` with `excludeCompletedActions: false`).
3. Pull resource assignments from those projects to understand actual hours spent (`getResourceAssignments`).
4. Pull placeholder rates for cost modeling (`workspacePlaceholders` → `billRate`, `costRate`).
5. Compute averages: typical action count, total story points, elapsed weeks, and blended cost per point.
6. Generate an effort estimate for the new proposal with ranges (optimistic / expected / pessimistic).
7. Post the estimate to the sales or pre-sales group chat (`insertMessage`) and attach it as a note on the opportunity action.

**Value:** Proposals are grounded in real delivery data, not gut feel. Bids are more accurate, margins are more predictable, and the sales team gets their numbers in hours instead of days.

---

## 25. End-of-Quarter Goal Reconciliation

**The job:** At the end of every quarter, every goal owner has to reconcile their OKRs: update final numbers, write a retrospective, determine carry-forward items, and set up next quarter's goals. This is a week-long organizational tax.

**Agent workflow:**
1. Pull all goals ending this quarter (`getGoals` with date filters).
2. For each goal, compute final attainment:
   - For action-based goals: count completed vs. total linked actions (`getActionsByWorkspace`).
   - For number-based goals: read the latest `currentValue` vs. `goalValue`.
3. Tag each goal as Hit / Missed / Partial based on attainment thresholds.
4. For missed goals, identify incomplete actions and decide: carry forward or archive (`bulkArchiveActions` for abandoned items).
5. For carry-forward items, create next quarter's goal (`createGoal`) with updated targets and dates.
6. Compose a retrospective summary for each goal and post it as a comment (`insertMessage` with `containerType: goal`).
7. Build a quarter-end dashboard showing attainment by team and department (`createDashboardV2`, `createDashboardWidget` with pie chart by goal status).
8. Send the full reconciliation report to leadership (`insertMessage` to leadership group).

**Value:** Goal close-out shrinks from a painful week to an afternoon of reviewing agent-generated summaries. Next quarter's goals are pre-seeded and ready to go on Day 1.

---

## Summary: The 30-Second Pitch

Every one of these opportunities follows the same pattern:

1. **Detect** something that happened (a PR, a meeting, a status change, a deadline).
2. **Decide** what needs to happen next (assign, notify, approve, escalate).
3. **Do** it automatically using Hive's API surface.

The result: engineers spend less time on project-management busywork, PMs spend less time chasing updates, and leadership gets accurate information without asking for it. The agent doesn't replace anyone's judgment -- it replaces the *overhead* of acting on that judgment.
