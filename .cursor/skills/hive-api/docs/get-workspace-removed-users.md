# Get workspace removed users

Get all removed users entries for a given workspace that the user has access to

Returns an array of removed user entries. Note that if a user was added and removed multiple times, there may be duplicate entries of the user's removal in the response results.

The results here extend the standard User Object with 2 additional fields:

| Field     | Type   | Description                          |
| :-------- | :----- | :----------------------------------- |
| removedBy | String | ID of the user who removed this user |
| removedAt | Date   | Date the user was removed            |

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
    "/workspaces/{workspaceId}/removed-users": {
      "get": {
        "summary": "Get workspace removed users",
        "description": "Get all removed users entries for a given workspace that the user has access to",
        "operationId": "get-workspace-removed-users",
        "parameters": [
          {
            "name": "workspaceId",
            "in": "path",
            "description": "ID of the workspace",
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
                    "value": "[\n  {\n    \"id\": \"22YK3N5uGpzMdw7fm\",\n    \"profile\": {\n      \"firstName\": \"Removed\",\n      \"lastName\": \"User\"\n    },\n    \"fullName\": \"Removed User\",\n    \"email\": \"john.doe@hive.com\",\n\t\t\"removedAt\": \"2025-07-22T22:21:56.087Z\",\n    \"removedBy\": \"VuK8n8uHpzudw7Ez\"\n  },\n]\n"
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
                    "value": "[\n  {\n    \"error\": 400,\n    \"message\": \"Workspace not found.\"\n\t},\n\t{\n    \"error\": 400,\n    \"message\": \"Invalid API Key.\"\n\t}\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "error": {
                        "type": "integer",
                        "example": 400,
                        "default": 0
                      },
                      "message": {
                        "type": "string",
                        "example": "Workspace not found."
                      }
                    }
                  }
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/removed-users\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});\n"
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