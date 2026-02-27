# Get actions

Get all actions for a given workspace that the user has access to

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "hive-rest-api",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://app.hive.com/api/v1"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "in": "header",
        "name": "api_key"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/workspaces/{workspaceId}/actions": {
      "get": {
        "summary": "Get actions",
        "description": "Get all actions for a given workspace that the user has access to",
        "operationId": "workspacesworkspaceidactions",
        "parameters": [
          {
            "name": "projectId",
            "in": "query",
            "description": "An optional project ID to get actions from. By default, all actions will be returned regardless of what project they belong to.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "sortBy",
            "in": "query",
            "description": "Sort results by an Action Object field (for example, `sortBy=title asc`)",
            "schema": {
              "type": "string",
              "default": "fieldName asc"
            }
          },
          {
            "name": "workspaceId",
            "in": "path",
            "description": "ID of the workspace",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "limit",
            "in": "query",
            "description": "default = 100; min = 1; max = 100",
            "schema": {
              "type": "string",
              "default": "100"
            }
          },
          {
            "name": "filters",
            "in": "query",
            "description": "Optional fields to filter by. Filters expects a structure like \"filters\\[fieldName\\]=value\". For example, if you wanted to filter to just get actions with the status \"Completed\", you would pass: \"filters\\[status\\]=Completed\". Currently, only the following fields are supported: \"status\", \"parent\", \"archived\", \"milestone\", \"deleted\", \"root\", \"recurringId\", \"teamAssignee\", \"placeholderAssignees\", \"priorityLevelId\", \"followingUserIds\".",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  {\n    \"id\": \"jArt6JZpezAMZimzy\",\n    \"title\": \"Prepare for weekly product meeting\",\n    \"workspace\": \"12345aZjDQZndHqs\",\n    \"assignees\": [],\n    \"projectId\": null,\n    \"createdAt\": \"2015-07-09T20:33:56.465Z\",\n    \"modifiedAt\": \"2016-08-23T07:49:09.621Z\",\n    \"createdBy\": \"1234abcuJzo4k7F9\",\n    \"modifiedBy\": \"1234abcuJzo4k7F9\",\n    \"status\": \"Unstarted\",\n    \"deadline\": null,\n    \"scheduledDate\": null,\n    \"checkedDate\": null,\n    \"parent\": null,\n    \"root\": null,\n    \"archived\":false,\n    \"deleted\":false,\n    \"hasSubactions\": false,\n    \"estimate\": null,\n    \"estimates\": [\n      {\"userId\":\"user12345\",\"time\":7200}\n    ]\n    \"milestone\": false,\n    \"loggedTime\": [\n      {\n        \"userId\":\"user12345\",\n        \"time\": 7200,\n        \"date\":\"2019-01-01T00:00:00.000Z\"\n      }\n    ],\n  \t\"phaseId\":\"abcdefg9876\",\n    \"phaseName\": \"Planning\",\n    \"priority\": {\n  \t  \"name\":\"Urgent\",\n      \"level\": 1,\n      \"color\": \"#f6781a\",\n      \"_id\": \"abc321\"\n     }\n  }\n]"
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false,
        "x-readme": {
          "code-samples": [
            {
              "language": "javascript",
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/actions\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey + \"&sortBy=title asc\";\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});"
            }
          ],
          "samples-languages": [
            "javascript"
          ]
        }
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```