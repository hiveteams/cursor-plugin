---
name: hive-open-pr
description: Creates a GitHub pull request and attaches it to a Hive action when GitHub tooling is already available in the user's Cursor environment. Automatically links the branch to the Hive action in context, or asks which action to use. Use when the user wants to open a PR, create a pull request, submit changes for review, or push a branch for merging.
---

# Open PR

Create a GitHub pull request and attach the branch to the relevant Hive action.

## Required data sources

- Use local git for branch, remote, and diff information.
- Use the GitHub MCP server when it is configured in the user's environment, or the `gh` CLI, to open the PR.
- Use the Hive MCP server (`updateActionGithubBranchNames`) to link the branch to a Hive action.

## Workflow

1. Gather branch and repo context.
   - Run `git branch --show-current` to get the current branch name.
   - Run `git remote get-url origin` to extract the repo owner and name.
   - Run `git status` and `git log` to understand staged/unstaged changes and recent commit history on this branch.
   - Determine the base branch (typically `beta` or `main`/`master`). Check which exists with `git branch -r`.
   - If there are uncommitted changes, ask the user whether to commit first.

2. Push the branch if needed.
   - Check if the branch has an upstream with `git status -sb`.
   - If not pushed, push with `git push -u origin HEAD`.

3. Create the pull request.
   - Use the available GitHub integration in the environment.
   - Derive the title from the commit history or branch name.
   - Build a concise body summarizing the changes (use `git diff <base>...HEAD`).
   - Set `base` to the target branch identified in step 1.
   - Present the PR URL to the user.

4. Identify the Hive action to attach to.
   - Check the conversation context for a Hive action URL, action ID, or action title the user has been working on.
   - If a Hive action is clearly in context, use it.
   - **If there is any ambiguity or no action is in context, ask the user which Hive action to attach the PR to.** Accept a URL, action ID, or title to search for.

5. Resolve the Hive action ID.
   - If given a URL, extract the action ID from the path.
   - If given a title or search term, resolve the workspace first:
     - Read `hive-profile.json`.
    - If `activeWorkspaceId` is a non-empty string, use it. Otherwise call `getUsersWorkspaces` and use the active or primary workspace.
   - Call `getActions` with `specificIds` (for an ID) or `text` (for a title search) to confirm the action exists.
   - If a text search returns multiple results, ask the user to pick one.

6. Attach the branch to the Hive action.
   - Call `updateActionGithubBranchNames` with:
     - `actionId`: the resolved action ID
     - `githubBranchNames`: the existing branch names from the action (if any) plus the new entry in `"Repo:branch-name"` format (e.g. `"hiveteams/web-app:my-feature-branch"`)
   - Use the repo owner/name from step 1 and the branch name to build the string.
   - Preserve any branch names already attached to the action — append, don't replace.

7. Confirm to the user.
   - Show the PR URL and confirm the branch was linked to the Hive action.

## Notes

- Never commit directly to a target branch. Always create a PR.
- If the user provides a Hive action up front (e.g. "open a PR for ACTION_ID"), skip the disambiguation step.
