#!/usr/bin/env python3
"""
beforeMCPExecution hook that gates Hive MCP tool calls.

When the Hive MCP server is invoked:
- If the workspace profile (.cursor/hive-profile.json) is populated,
  allows the call and injects the activeWorkspaceId via agent_message.
- If the profile is empty, denies the call (except getUsersWorkspaces)
  and instructs the agent to run first-time setup.

Non-Hive MCP calls pass through untouched.
"""
import json
import os
import sys

PROFILE_SETUP_INSTRUCTIONS = """The Hive workspace profile is not configured yet. Before making any other Hive MCP calls, you must set it up:

1. Call the `getUsersWorkspaces` tool from the Hive MCP server (no parameters needed).
2. The response contains `acceptedWorkspaces` (array with `_id` and `name`) and `primaryWorkspace` (the user's primary workspace ID).
3. Save the result to `.cursor/hive-profile.json`:
   {
     "workspaces": [{ "id": "<_id>", "name": "<name>" }, ...],
     "primaryWorkspaceId": "<primaryWorkspace>",
     "activeWorkspaceId": "<selected workspace>"
   }
4. If the user has ONE workspace, set activeWorkspaceId automatically and confirm.
5. If MULTIPLE workspaces, present the list and ask:
   "You have access to multiple Hive workspaces:
    1. WorkspaceName1
    2. WorkspaceName2
    Which should I use by default? (Your primary workspace is PrimaryName.)"
   Default to primaryWorkspaceId if the user has no preference.
6. After saving, retry the original Hive MCP call with the activeWorkspaceId."""

POST_SETUP_INSTRUCTIONS = """You just called getUsersWorkspaces. Save the workspace data to .cursor/hive-profile.json now:
- Map acceptedWorkspaces to { "id": w._id, "name": w.name } entries in the "workspaces" array.
- Set "primaryWorkspaceId" from the primaryWorkspace field.
- If one workspace: set "activeWorkspaceId" automatically.
- If multiple: ask the user which to use (default to primary).
Then retry the original Hive MCP call using the activeWorkspaceId."""


def main():
    payload = json.load(sys.stdin)

    url = payload.get("url", "")
    if "hive" not in url.lower():
        json.dump({"permission": "allow"}, sys.stdout)
        return

    tool_name = payload.get("tool_name", "")
    project_dir = os.environ.get("CURSOR_PROJECT_DIR", ".")
    profile_path = os.path.join(project_dir, ".cursor", "hive-profile.json")

    try:
        with open(profile_path) as f:
            profile = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        profile = {"workspaces": [], "primaryWorkspaceId": None, "activeWorkspaceId": None}

    active_workspace = profile.get("activeWorkspaceId")
    workspaces = profile.get("workspaces") or []

    if active_workspace and workspaces:
        workspace_name = next(
            (w["name"] for w in workspaces if w.get("id") == active_workspace),
            active_workspace,
        )
        json.dump({
            "permission": "allow",
            "agent_message": (
                f"Active Hive workspace: \"{workspace_name}\" (ID: {active_workspace}). "
                f"Use this as the workspaceId/workspace parameter for this call. "
                f"If the user asks to switch workspaces, update activeWorkspaceId in .cursor/hive-profile.json."
            ),
        }, sys.stdout)
    elif tool_name == "getUsersWorkspaces":
        json.dump({
            "permission": "allow",
            "agent_message": POST_SETUP_INSTRUCTIONS,
        }, sys.stdout)
    else:
        json.dump({
            "permission": "deny",
            "user_message": "Setting up your Hive workspace profile first...",
            "agent_message": PROFILE_SETUP_INSTRUCTIONS,
        }, sys.stdout)


if __name__ == "__main__":
    main()
