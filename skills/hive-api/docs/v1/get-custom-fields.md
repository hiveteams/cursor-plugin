# Get custom fields

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
    "/workspaces/{workspaceId}/custom-fields": {
      "get": {
        "summary": "Get custom fields",
        "description": "",
        "operationId": "get-custom-fields",
        "parameters": [
          {
            "name": "workspaceId",
            "in": "path",
            "description": "Workspace ID you wish to see custom fields for",
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
                    "value": "{\n  \"_id\": \"customFieldId\",\n  \"label\": \"Custom Field Nmae\",\n  \"type\": \"text\",\n  \"workspace\": \"workspaceId\",\n  \"deleted\": false,\n  \"modifiedAt\": \"2019-10-22T00:00:00.000Z\",\n  \"modifiedBy\": \"server\",\n  \"attachedToObject\": \"action\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string",
                      "example": "customFieldId"
                    },
                    "label": {
                      "type": "string",
                      "example": "Custom Field Nmae"
                    },
                    "type": {
                      "type": "string",
                      "example": "text"
                    },
                    "workspace": {
                      "type": "string",
                      "example": "workspaceId"
                    },
                    "deleted": {
                      "type": "boolean",
                      "example": false,
                      "default": true
                    },
                    "modifiedAt": {
                      "type": "string",
                      "example": "2019-10-22T00:00:00.000Z"
                    },
                    "modifiedBy": {
                      "type": "string",
                      "example": "server"
                    },
                    "attachedToObject": {
                      "type": "string",
                      "example": "action"
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
              "code": "var userId = \"USER_ID\";\nvar customFieldId = \"CUSTOM_FIELD_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/workspaces/workspaceId/custom-fields\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});"
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