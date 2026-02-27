# Get groups

Get all chat groups for a given workspace

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
    "/workspaces/{workspaceId}/groups": {
      "get": {
        "summary": "Get groups",
        "description": "Get all chat groups for a given workspace",
        "operationId": "testinput",
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
                    "value": "[\n    {\n      \"id\": \"8MRZ6oYzRMJ4eJYnR\",\n      \"name\": \"Everyone\",\n      \"members\": [\n        '1234abcuJzo4k7F9',\n        '6789abcuJzo4k7F9'\n       ],\n      \"workspace\": \"12345aZjDQZndHqs\",\n      \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n      \"createdBy\": \"1234abcuJzo4k7F9\",\n      \"modifiedBy\": \"1234abcuJzo4k7F9\"\n    },\n    {\n      \"id\": \"8S8pMXXJwCeExYWzq\",\n      \"name\": \"Bee Hive Gossip\",\n      \"members\": [\n        '1234abcuJzo4k7F9',\n        '6789abcuJzo4k7F9'\n       ],\n      \"workspace\": \"12345aZjDQZndHqs\",\n      \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n      \"createdBy\": \"1234abcuJzo4k7F9\",\n      \"modifiedBy\": \"1234abcuJzo4k7F9\"    \n    },\n    {\n      \"id\": \"8yxNHYsvqYCDFP19J\",\n      \"name\": \"Maria von Trapp\",\n      \"members\": [\n        '1234abcuJzo4k7F9',\n        '6789abcuJzo4k7F9'\n       ],\n      \"workspace\": \"12345aZjDQZndHqs\",\n      \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n      \"createdBy\": \"1234abcuJzo4k7F9\",\n      \"modifiedBy\": \"1234abcuJzo4k7F9\"    \n    }\n  ]\n  "
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\"\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/groups\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});"
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