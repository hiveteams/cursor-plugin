# Create custom field

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
      "post": {
        "summary": "Create custom field",
        "description": "",
        "operationId": "create-custom-field",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "label"
                ],
                "properties": {
                  "label": {
                    "type": "string",
                    "description": "Label for this new custom field"
                  },
                  "type": {
                    "type": "string",
                    "description": "Type of custom field",
                    "enum": [
                      "\"user\"",
                      "\"select\"",
                      "\"text\"",
                      "\"date\"",
                      "\"project\"",
                      "\"formula\"",
                      "\"number\""
                    ]
                  },
                  "defaultValue": {
                    "type": "string",
                    "description": "Default value for this custom field"
                  },
                  "dropdownValues": {
                    "type": "array",
                    "description": "Set of dropdown values for \"select\" custom fields",
                    "items": {
                      "type": "string"
                    }
                  },
                  "allowMultiSelect": {
                    "type": "boolean",
                    "description": "Boolean for whether this \"select\" custom field should allow multi select"
                  },
                  "itemType": {
                    "type": "string",
                    "description": "Also referred to as attachedToObject elsewhere in the api. Which object this custom field should be attached to",
                    "enum": [
                      "\"action\"",
                      "\"project\""
                    ]
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
                    "value": "{\n  \"_id\": \"customFieldId\",\n  \"label\": \"New Custom Field\",\n  \"type\": \"select\",\n  \"workspace\": \"workspaceId\",\n  \"deleted\": false,\n  \"modifiedAt\": \"2019-10-22T00:00:00.000Z\",\n  \"modifiedBy\": \"server\",\n  \"attachedToObject\": \"action\"\n}\n"
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
                      "example": "New Custom Field"
                    },
                    "type": {
                      "type": "string",
                      "example": "select"
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
              "code": "var userId = \"USER_ID\";\nvar customFieldId = \"CUSTOM_FIELD_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/workspaces/workspaceId/custom-fields\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  label: \"New Custom Field\",\n  type: \"select\",\n  itemType: \"action\"\n  dropdownValues: [\"Option 1\", \"Option 2\"],\n  allowMultiSelect: true\n};\n\n$.ajax({\n  method: \"POST\",\n  url: url,\n  data: JSON.stringify(data),\n}).done(function(data) {\n  console.log(data);\n});"
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