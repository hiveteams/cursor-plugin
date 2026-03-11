# Create webhook

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
    "/webhooks": {
      "post": {
        "summary": "Create webhook",
        "description": "",
        "operationId": "create-webhook",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "name",
                  "workspaceId",
                  "trigger",
                  "url"
                ],
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "workspaceId": {
                    "type": "string"
                  },
                  "projectIds": {
                    "type": "array",
                    "default": [
                      "[]"
                    ],
                    "items": {
                      "type": "string"
                    }
                  },
                  "trigger": {
                    "type": "string"
                  },
                  "fields": {
                    "type": "array",
                    "default": [
                      "[]"
                    ],
                    "items": {
                      "type": "string"
                    }
                  },
                  "url": {
                    "type": "string"
                  },
                  "additionalHeaders": {
                    "type": "array"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "201",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"message\": \"Webhook created\",\n    \"webhook\": {\n        \"_id\": \"v2Y3CNCDyzeHEeorr\",\n        \"name\": \"Tell me when Projects are inserted\",\n        \"workspaceId\": \"oQkqDmkXzoHwjatAA\",\n        \"trigger\": \"projects::i\",\n        \"url\": \"https://webhook.site/4bfcb247-7370-4b5f-822a-6b6036db808e\",\n        \"projectIds\": [],\n        \"fields\": [],\n        \"filters\": [],\n        \"operator\": \"OR\",\n        \"ownerId\": \"9Mbh6keyT33iNN2xp\",\n        \"deleted\": false,\n        \"createdAt\": \"2023-09-27T15:21:14.839Z\",\n        \"modifiedAt\": \"2023-09-27T15:21:14.839Z\",\n        \"createdBy\": \"9Mbh6keyT33iNN2xp\",\n        \"modifiedBy\": \"9Mbh6keyT33iNN2xp\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "Webhook created"
                    },
                    "webhook": {
                      "type": "object",
                      "properties": {
                        "_id": {
                          "type": "string",
                          "example": "v2Y3CNCDyzeHEeorr"
                        },
                        "name": {
                          "type": "string",
                          "example": "Tell me when Projects are inserted"
                        },
                        "workspaceId": {
                          "type": "string",
                          "example": "oQkqDmkXzoHwjatAA"
                        },
                        "trigger": {
                          "type": "string",
                          "example": "projects::i"
                        },
                        "url": {
                          "type": "string",
                          "example": "https://webhook.site/4bfcb247-7370-4b5f-822a-6b6036db808e"
                        },
                        "projectIds": {
                          "type": "array"
                        },
                        "fields": {
                          "type": "array"
                        },
                        "filters": {
                          "type": "array"
                        },
                        "operator": {
                          "type": "string",
                          "example": "OR"
                        },
                        "ownerId": {
                          "type": "string",
                          "example": "9Mbh6keyT33iNN2xp"
                        },
                        "deleted": {
                          "type": "boolean",
                          "example": false,
                          "default": true
                        },
                        "createdAt": {
                          "type": "string",
                          "example": "2023-09-27T15:21:14.839Z"
                        },
                        "modifiedAt": {
                          "type": "string",
                          "example": "2023-09-27T15:21:14.839Z"
                        },
                        "createdBy": {
                          "type": "string",
                          "example": "9Mbh6keyT33iNN2xp"
                        },
                        "modifiedBy": {
                          "type": "string",
                          "example": "9Mbh6keyT33iNN2xp"
                        }
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
        "deprecated": false
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