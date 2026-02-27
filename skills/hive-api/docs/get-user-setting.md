# Get user setting by userId

Get a single user tag for a given workspace and user

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
    "/workspaces/{workspaceId}/user-settings/{userId}": {
      "get": {
        "summary": "Get user setting by userId",
        "description": "Get a single user tag for a given workspace and user",
        "operationId": "get-user-setting",
        "parameters": [
          {
            "name": "workspaceId",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "userId",
            "in": "path",
            "description": "User ID",
            "required": true,
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
                    "value": "{\n  \"workspaceId\": \"12345aZjDQZndHqs\",\n  \"_id\": \"qFR6a524nFARukmvF\",\n  \"userId\": \"123123123\",\n  \"firstDayOfWork\": \"2018-01-23T00:00:00.000Z\",\n  \"lastDayOfWork\": \"2019-01-23T00:00:00.000Z\",\n  \"billRate\": 80,\n  \"costRate\": 70\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "workspaceId": {
                      "type": "string",
                      "example": "12345aZjDQZndHqs"
                    },
                    "_id": {
                      "type": "string",
                      "example": "qFR6a524nFARukmvF"
                    },
                    "userId": {
                      "type": "string",
                      "example": "123123123"
                    },
                    "firstDayOfWork": {
                      "type": "string",
                      "example": "2018-01-23T00:00:00.000Z"
                    },
                    "lastDayOfWork": {
                      "type": "string",
                      "example": "2019-01-23T00:00:00.000Z"
                    },
                    "billRate": {
                      "type": "integer",
                      "example": 80,
                      "default": 0
                    },
                    "costRate": {
                      "type": "integer",
                      "example": 70,
                      "default": 0
                    }
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/user-settings/\" + userId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url\n}).done(function(data) {\n  console.log(data);\n});"
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