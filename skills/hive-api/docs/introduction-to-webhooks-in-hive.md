# Introduction to Webhooks in Hive

Webhooks are useful for getting real-time updates from Hive when records, like Actions or Projects, are inserted or updated. When you register a Webhook in your Hive Workspace, Hive will listen for events which match your registered Webhook's trigger and field information, and send HTTP POST requests to a URL which you specify in Webhook registration with a payload that contains data relevant to the operation.

## Example Webhook registries

### Get notified when a new Project is created in Hive

If you wanted to be notified any time a new Project is created in Hive, you could register a Webhook with a "trigger" set to "projects::i" and receive information about the new Project at a URL you specify. The Webhook would look something like:

```
{
    "name": "Tell me when Projects are inserted",
    "workspaceId": "oQkqDmkXzoHwjatAA",
    "trigger": "projects::i",
    "url": "https://webhook.site/4bfcb247-7370-4b5f-822a-6b6036db808e"
}
```

### Get notified when a Project has its end date updated

If you only cared about certain field updates to a record in Hive, you can control that with the "fields" field. The Webhook would look something like:

```
{
    "name": "Tell me when any Project end date is updated",
    "workspaceId": "oQkqDmkXzoHwjatAA",
    "trigger": "projects::u",
    "fields": ["endDate"],
    "url": "https://webhook.site/4bfcb247-7370-4b5f-822a-6b6036db808e"
}
```

### Get notified when an Action which belongs to a specific Project is updated

Another example might be watching specific updates to Actions which exist in specific project(s). If you have a project with ID "v2Y3CNCDyzeHEeorr" and want a Webhook to fire when an action in that project has any field updated, the Webhook would look something like:

```
{
    "name": "Tell me when Actions in a specific Project are updated",
    "workspaceId": "oQkqDmkXzoHwjatAA",
    "trigger": "actions::u",
    "projectIds": ["v2Y3CNCDyzeHEeorr"],
    "fields": [],
    "url": "https://webhook.site/4bfcb247-7370-4b5f-822a-6b6036db808e"
}
```

You could further refine this to only fire when an Action's title or description are updated by changing the "fields" value from an empty array to an array which includes the name of the fields you want to listen on, like:

```
{
    "name": "Tell me when Actions in a specific Project are updated (title or description only)",
    "workspaceId": "oQkqDmkXzoHwjatAA",
    "trigger": "actions::u",
    "projectIds": ["v2Y3CNCDyzeHEeorr"],
    "fields": ["title", "description"],
    "url": "https://webhook.site/4bfcb247-7370-4b5f-822a-6b6036db808e"
}
```

## Webhook Payloads

Webhook payloads follow a format where the top-level fields include information on the Webhook itself, and one top-level key set to match the name of the respective record type inserted/updated holds full information on the record in its current state.

An example payload structure for Webhooks where the record type is an Action will have an "action" key:

```
{
  "trigger": "actions::u",
  "ownerId": "9Mbh6keyT33iNN2xp",
  "webhookId": "zhMJzqMTa8GKz3yqH",
  "action": {
    /** Full record details here **/
  }
}
```

An example payload structure for Webhooks where the record type is a Project will have an "project" key:

```
{
  "trigger": "projects::i",
  "ownerId": "9Mbh6keyT33iNN2xp",
  "webhookId": "zhMJzqMTa8GKz3yqH",
  "project": {
    /** Full record details here **/
  }
}
```