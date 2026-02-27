# Get action attachments

Retrieves all attachments uploaded directly to the action card itself, or inserted using either of the available action attachment POST endpoints. Does not include attachments uploaded from 3rd party file store services, or attachments nested within comments on an action card.

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
    "/actions/{actionId}/attachments": {
      "get": {
        "summary": "Get action attachments",
        "description": "Retrieves all attachments uploaded directly to the action card itself, or inserted using either of the available action attachment POST endpoints. Does not include attachments uploaded from 3rd party file store services, or attachments nested within comments on an action card.",
        "operationId": "get-action-attachments",
        "parameters": [
          {
            "name": "actionId",
            "in": "path",
            "description": "The ID of the action.",
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
                    "value": "[\n    {\n        \"_id\": \"AzwXZkTsdH32nTPur\",\n        \"name\": \"Hello world\",\n        \"workspace\": \"9driAwqZjDQZndHqs\",\n        \"url\": \"https://hostname.com/file/path\",\n        \"createdAt\": \"2050-10-27T22:09:38.137Z\",\n        \"createdBy\": \"AnMyD2YXX4vcdTgxw\",\n        \"modifiedAt\": \"2050-10-27T22:09:38.717Z\",\n        \"modifiedBy\": \"AnMyD2YXX4vcdTgxw\"\n    }\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "_id": {
                        "type": "string",
                        "example": "AzwXZkTsdH32nTPur"
                      },
                      "name": {
                        "type": "string",
                        "example": "Hello world"
                      },
                      "workspace": {
                        "type": "string",
                        "example": "9driAwqZjDQZndHqs"
                      },
                      "url": {
                        "type": "string",
                        "example": "https://hostname.com/file/path"
                      },
                      "createdAt": {
                        "type": "string",
                        "example": "2050-10-27T22:09:38.137Z"
                      },
                      "createdBy": {
                        "type": "string",
                        "example": "AnMyD2YXX4vcdTgxw"
                      },
                      "modifiedAt": {
                        "type": "string",
                        "example": "2050-10-27T22:09:38.717Z"
                      },
                      "modifiedBy": {
                        "type": "string",
                        "example": "AnMyD2YXX4vcdTgxw"
                      }
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
              "code": "var userId = \"USER_ID\";\nvar actionId = \"ACTION_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1\";\nvar endpoint = \"/actions/\" + actionId + '/attachments';\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});"
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