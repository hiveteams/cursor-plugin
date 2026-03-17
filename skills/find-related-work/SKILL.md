---
name: find-related-work
description: Finds work related to a Hive ticket by searching Hive actions and git history for similar code changes. Accepts a Hive action URL or action ID as input. Use when the user asks for related work, prior art, similar tickets, related commits, or implementation context for a ticket.
---

# Find Related Work

Use this skill to gather prior art for a Hive ticket from both Hive and git history.

## Required data sources

- Use the Hive MCP server for Hive actions.
- Use GitHub tooling only when it already exists in the user's Cursor environment and the Hive action has attached branch names that warrant PR diff lookup.
- Use local git history for commit search, pickaxe, and branch lookup.

## Input

Accept one argument:

- A Hive action URL, such as `https://app.hive.com/workspace/.../action/ACTION_ID`
- A raw Hive action ID

If the input is a URL, extract the action ID from the URL path before continuing.

## Workflow

1. Resolve the workspace and fetch the source action.
   - First read `hive-profile.json`.
   - If `activeWorkspaceId` is present, use it as the workspace ID.
   - Otherwise call `getUsersWorkspaces` and use the active workspace if available, or the primary workspace as fallback.
   - Call Hive `getActions` with:
   - `workspaceId`
   - `specificIds: [actionId]`
   - `includePrivate: true`
   - Use the returned action as the source ticket. Capture its title, description, labels, project, assignees, and `githubBranchNames`.
   - If the action cannot be found, say so directly and stop.

2. Build search terms for related work.
   - Start with the most specific nouns and phrases from the action title.
   - Add distinctive terms from the description only when they look implementation-specific.
   - Prefer product names, feature names, API names, config keys, and acronyms.
   - Avoid generic terms such as `bug`, `fix`, `update`, `data`, `error`, `api`, or `ui`.
   - Keep a short list of high-value keywords rather than a long noisy list.

3. Search Hive for related actions.
   - Use `getActions` to search by `text` for the strongest keywords or phrases.
   - Prefer a few targeted searches over one broad search.
   - Use the source action's `projectIds` when available.
   - Use the source action's `labels` when available.
   - Exclude the source action from the final results.
   - Rank candidate actions higher when they share the same project, labels, branch names, or distinctive terms.

4. Gather code change context before searching history.
   - Run `git diff` and `git diff --cached` in the current repo to see if there is a local change related to the ticket.
   - If the source action has `githubBranchNames`, try to fetch attached PR diffs:
   - Identify the current repository owner and name from the local git remote when possible.
   - For each branch name, use the available GitHub integration to find matching PRs.
   - For the most relevant PRs, fetch a diff only if the environment supports it.
   - Use local diffs first when they exist. Use PR diffs as additional context or as the primary diff source when there is no local diff.
   - If no local or PR diffs are available, continue with keyword-only history search.

5. Extract high-value code tokens from the diffs.
   - Look for identifiers that are likely to be stable across commits:
   - Function names
   - Class names
   - Type names
   - Constants
   - Config keys
   - Domain-specific variable names
   - Prefer tokens that are specific to the feature or system.
   - Ignore generic identifiers such as `result`, `item`, `value`, `data`, `props`, `error`, or `handler`.
   - If the diff includes file paths, use those as supporting context but do not treat a full path as the primary token.
   - Keep a ranked list of the best tokens.

6. Search git history in two passes.
   - Pass A: commit message grep
   - Run `git log --all --oneline --grep="<keyword>"` once for each keyword.
   - Deduplicate the combined results across all keyword searches.
   - Rank hits higher when multiple keywords point to the same commit.
   - Pass B: pickaxe token search
   - For each high-value token, run `git log -S"<token>" --all --oneline`.
   - Use pickaxe results to find commits that introduced or removed the token.
   - For the strongest hits, inspect nearby context with `git show <hash> --stat`.
   - When needed, inspect the patch with `git show <hash> -p` and look at the surrounding identifiers near the token to understand whether the change is truly related.

7. Link commits back to Hive actions when possible.
   - For promising commits from grep or pickaxe, run `git branch --contains <hash>`.
   - Compare those branch names to any `githubBranchNames` found on related Hive actions.
   - Start with the source action and the related actions already found in step 3.
   - If needed, run additional Hive searches to find actions whose `githubBranchNames` match one of the branch names.
   - When a commit can be connected to a branch name that appears in `actionDoc.githubBranchNames`, include that Hive action in the result.

8. Repeat per repo when multiple repos are in scope.
   - If the user is actively working in more than one repo, repeat the git workflow in each repo.
   - Label commit findings by repo so the user can tell where each result came from.

## Output format

Use this template:

```markdown
## Related work for [Action title]

### Source action
- [Action title] - [status]
- Key terms: [keyword 1], [keyword 2], [keyword 3]

### Related Hive actions
- [Action title] - [status] - [why it is related]

### Related git commits from keyword search
- `[hash]` [commit subject] - [repo if needed]

### Related git commits from token search
- Token: `[token]`
- `[hash]` [commit subject] - [why the token match matters]

### Commit to action links
- `[hash]` -> `[branch-name]` -> [Hive action title]
```

## Notes

- Keep the final answer concise and evidence-based.
- Prefer a smaller set of strong matches over a long weak list.
- Say when the result is based only on keyword matches and no diff-derived tokens were available.
- Do not claim a commit is related unless the message, token history, or nearby patch context supports it.
