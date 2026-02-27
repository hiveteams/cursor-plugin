# Update user role tag

Update user role tag

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
    "/workspaces/{workspaceId}/users/{userId}/role-tags/{roleTagId}": {
      "put": {
        "summary": "Update user role tag",
        "description": "Update user role tag",
        "operationId": "usersuseridrole-tags-1",
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
          },
          {
            "name": "roleTagId",
            "in": "path",
            "description": "Role tag ID to set on the user",
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
                    "value": "{\n  \"_id\": \"qFR6a524nFARukmvF\",\n  \"workspace\": \"12345aZjDQZndHqs\",\n  \"name\": \"Role Tag 1\",\n  \"createdBy\": \"12345gfuJzo4k7F9\",\n  \"modifiedBy\": \"12345xgfuJzo4k7F9\",\n  \"createdAt\": \"2018-01-23T22:14:24.862Z\",\n  \"modifiedAt\": \"2018-01-23T22:14:24.862Z\"\n},\n"
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar roleTagId = \"ROLE_TAG_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint =\n  \"workspaces/\" + workspaceId + \"/users/\" + userId + \"/role-tags/\" + roleTagId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  method: \"PUT\",\n  url: url\n}).done(function(data) {\n  console.log(data);\n});"
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