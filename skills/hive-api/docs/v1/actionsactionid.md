# Get action

`estimate` is the amount of time estimated for the action, in seconds. If no estimate is present, the field will be `null`

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
    "/actions/{actionId}": {
      "get": {
        "summary": "Get action",
        "description": "",
        "operationId": "actionsactionid",
        "parameters": [
          {
            "name": "actionId",
            "in": "path",
            "description": "The id of the action",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"id\": \"232b3c4d5e6f7g8h1\",\n  \"title\": \"Action title\",\n  \"workspace\": \"w32bac4d5e6f7g8h2\",\n  \"assignees\": [],\n  \"projectId\": null,\n  \"customFields\": [],\n  \"createdAt\": \"2019-01-01T00:00:00.000Z\",\n  \"modifiedAt\": \"2019-01-01T00:00:00.000Z\",\n  \"createdBy\": \"u32bac4d5e6f7g8h2\",\n  \"modifiedBy\": \"u32bac4d5e6f7g8h2\",\n  \"status\": \"Unstarted\",\n  \"deadline\": null,\n  \"scheduledDate\": null,\n  \"checkedDate\": null,\n  \"parent\": null,\n  \"root\": null,\n  \"archived\":false,\n  \"deleted\":false,\n  \"hasSubactions\": false,\n  \"estimate\": null,\n  \"estimates\":[\n    {\"userId\":user12345,\"time\":7200}\n  ]\n  \"milestone\": false,\n  \"loggedTime\": [\n    {\n      \"userId\":\"user12345\",\n      \"time\": 7200,\n      \"date\":\"2019-01-01T00:00:00.000Z\"\n    }\n  ],\n  \"phaseId\":\"123ab456\",\n  \"phaseName\":\"planning\",\n  \"priority\": {\n  \t  \"name\":\"Urgent\",\n      \"level\": 1,\n      \"color\": \"#f6781a\",\n      \"_id\": \"abc321\"\n  }\n}"
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
              "code": "var userId = \"USER_ID\";\nvar actionId = \"ACTION_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"/actions/\" + actionId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});\n"
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