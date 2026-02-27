# Get workspaces

Get all workspaces that you're is a member of.

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
    "/workspaces": {
      "get": {
        "summary": "Get workspaces",
        "description": "Get all workspaces that you're is a member of.",
        "operationId": "workspaces-1",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  {\n  \t\"id\": \"1a2b3c4d5e6f7g8h9\",\n\t  \"name\": \"Honey Enterprises\",\n\t  \"members\": [\n\t    '1234abc',\n\t    '5678zyc'\n\t  ],\n\t  \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n\t  \"modifiedAt\": \"2017-05-19T02:25:06.190Z\",\n\t  \"createdBy\": \"1234abcuJzo4k7F9\",\n\t  \"modifiedBy\": \"1234abcuJzo4k7F9\"\n\t}\n]\n\n"
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
              "language": "curl",
              "code": "curl -X GET -H \"api_key: API_KEY\" https://app.hive.com/api/v1/workspaces?user_id=USER_ID"
            }
          ],
          "samples-languages": [
            "curl"
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