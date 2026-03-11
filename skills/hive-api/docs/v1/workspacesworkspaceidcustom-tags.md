# Get custom tags

Get all project or user custom tags

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
    "/workspaces/{workspaceId}/custom-tags": {
      "get": {
        "summary": "Get custom tags",
        "description": "Get all project or user custom tags",
        "operationId": "workspacesworkspaceidcustom-tags",
        "parameters": [
          {
            "name": "type",
            "in": "query",
            "description": "Type of custom tags you are trying to access. Can be either \"user\" or \"project\"",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "workspaceId",
            "in": "path",
            "description": "Workspace ID",
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
                    "value": "[\n  {\n    \"_id\": \"qFR6a524nFARukmvF\",\n    \"workspace\": \"12345aZjDQZndHqs\",\n    \"name\": \"Custom Tag 1\",\n    \"type\": \"user\",\n    \"options\": [\"Option 1\", \"Option 2\"],\n    \"isMulti\": false\n    \"createdBy\": \"12345gfuJzo4k7F9\",\n    \"modifiedBy\": \"12345xgfuJzo4k7F9\",\n    \"createdAt\": \"2018-01-23T22:14:24.862Z\",\n    \"modifiedAt\": \"2018-01-23T22:14:24.862Z\"\n\t},\n  {\n    \"_id\": \"lkdjfwjdoi2342w3\",\n    \"workspace\": \"12345aZjDQZndHqs\",\n    \"name\": \"Custom Tag 2\",\n    \"type\": \"user\",\n    \"options\": [\"Option 1\", \"Option 2\"],\n    \"isMulti\": false\n    \"createdBy\": \"12345gfuJzo4k7F9\",\n    \"modifiedBy\": \"12345xgfuJzo4k7F9\",\n    \"createdAt\": \"2018-01-23T22:14:24.862Z\",\n    \"modifiedAt\": \"2018-01-23T22:14:24.862Z\"\n\t}\n]\n\n"
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar tagType = \"user\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/custom-tags\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey + \"&type=\" + tagType;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url\n}).done(function(data) {\n  console.log(data);\n});"
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