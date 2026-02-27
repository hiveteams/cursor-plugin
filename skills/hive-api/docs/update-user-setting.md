# Update user setting

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
      "put": {
        "summary": "Update user setting",
        "description": "Get a single user tag for a given workspace and user",
        "operationId": "update-user-setting",
        "parameters": [
          {
            "name": "workspaceId",
            "in": "path",
            "description": "Workspace ID",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "userId",
            "in": "path",
            "description": "User ID",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "firstDayOfWork": {
                    "type": "string",
                    "description": "First day of work"
                  },
                  "lastDayOfWork": {
                    "type": "string",
                    "description": "Last day of work"
                  },
                  "billRate": {
                    "type": "number",
                    "description": "Bill rate",
                    "format": "float"
                  },
                  "costRate": {
                    "type": "number",
                    "description": "Cost rate",
                    "format": "float"
                  },
                  "managers": {
                    "type": "array",
                    "description": "Array of User IDs representing the User's manager(s)",
                    "default": "",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"workspaceId\": \"12345aZjDQZndHqs\",\n  \"_id\": \"qFR6a524nFARukmvF\",\n  \"userId\": \"123123123\",\n  \"firstDayOfWork\": \"2018-01-23T00:00:00.000Z\",\n  \"lastDayOfWork\": \"2019-01-23T00:00:00.000Z\",\n  \"billRate\": 100,\n  \"costRate\": 70\n}\n"
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
                      "example": 100,
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/user-settings/\" + userId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  billRate: 100\n};\n\n$.ajax({\n  method: \"PUT\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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