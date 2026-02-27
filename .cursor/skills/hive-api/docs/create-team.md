# Create team

Create new team

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
    "/teams": {
      "post": {
        "summary": "Create team",
        "description": "Create new team",
        "operationId": "create-team",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "workspace",
                  "members",
                  "name"
                ],
                "properties": {
                  "workspace": {
                    "type": "string",
                    "description": "Workspace id"
                  },
                  "members": {
                    "type": "array",
                    "description": "Array of user ids. Each user should be workspace members.",
                    "items": {
                      "type": "string"
                    }
                  },
                  "name": {
                    "type": "string",
                    "description": "Team name. Not empty string"
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
                    "value": "{\n    \"_id\": \"B5hrsBi54cTFCwxXb\",\n    \"name\": \"Awesome team\",\n    \"members\": [\n        \"PtZNLxgfuJzo4k7F9\",\n        \"NcL3Tjeh9dtcztoxs\"\n    ],\n    \"workspace\": \"yL4w4D8R4QBEQpn2v\",\n    \"deleted\": false,\n    \"userId\": \"ekYxhtbfKPfb4X49r\",\n    \"createdBy\": \"ekYxhtbfKPfb4X49r\",\n    \"createdAt\": \"2022-06-22T09:58:14.678Z\",\n    \"modifiedAt\": \"2022-06-22T09:58:14.677Z\",\n    \"isExternal\": false\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string",
                      "example": "B5hrsBi54cTFCwxXb"
                    },
                    "name": {
                      "type": "string",
                      "example": "Awesome team"
                    },
                    "members": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "PtZNLxgfuJzo4k7F9"
                      }
                    },
                    "workspace": {
                      "type": "string",
                      "example": "yL4w4D8R4QBEQpn2v"
                    },
                    "deleted": {
                      "type": "boolean",
                      "example": false,
                      "default": true
                    },
                    "userId": {
                      "type": "string",
                      "example": "ekYxhtbfKPfb4X49r"
                    },
                    "createdBy": {
                      "type": "string",
                      "example": "ekYxhtbfKPfb4X49r"
                    },
                    "createdAt": {
                      "type": "string",
                      "example": "2022-06-22T09:58:14.678Z"
                    },
                    "modifiedAt": {
                      "type": "string",
                      "example": "2022-06-22T09:58:14.677Z"
                    },
                    "isExternal": {
                      "type": "boolean",
                      "example": false,
                      "default": true
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
              "code": "var userId = \"USER_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1\";\nvar endpoint = \"/teams\";\nvar qs = \"?user_id=\" + userId;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  workspace: \"yL4w4D8R4QBEQpn2v\",\n  members: [\"PtZNLxgfuJzo4k7F9\", \"NcL3Tjeh9dtcztoxs\"],\n  name: \"Awesome team\"\n};\n\n$.ajax({\n  method: \"POST\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\",\n  headers: { 'api_key': apiKey }\n}).done(function(data) {\n  console.log(data);\n});"
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