# Get resource assignment

Get a resource by id

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
    "/resource-assignments/{resourceAssignmentId}": {
      "get": {
        "summary": "Get resource assignment",
        "description": "Get a resource by id",
        "operationId": "get-resource",
        "parameters": [
          {
            "name": "resourceAssignmentId",
            "in": "path",
            "description": "ID of the resourceAssignment to update",
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
                    "value": "{\n  resourceAssignment:\n  {\n    \"id\" : \"123ABC567XYZ\",\n    \"resourceId\" : \"user1234\",\n    \"projectId\":\"project1234\",\n    \"startDate\" : ISODate(\"2019-01-01006:00:00.000Z\"),\n    \"endDate\" : ISODate(\"2020-01-01T00:00:00.000Z\"),\n    \"allocationType\" : \"hoursPerDay\",\n    \"assignmentType\" : \"regular\",\n    \"hoursPerDay\" : 8,\n    \"fixedHours\" : 8,\n    \"fixedDisplayType\" : \"hours\",\n    \"notes\":\"This is a note!\"\n  }\n}\n"
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
                    "value": "// If resourcing is desabled\n{\n    \"error\": 400,\n    \"message\": \"Resourcing is not enabled in current workspace\"\n}"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
                      "type": "object",
                      "properties": {}
                    },
                    {
                      "type": "object",
                      "properties": {
                        "error": {
                          "type": "integer",
                          "example": 400,
                          "default": 0
                        },
                        "message": {
                          "type": "string",
                          "example": "Resourcing is not enabled in current workspace"
                        }
                      }
                    }
                  ]
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
              "code": "var userId = \"USER_ID\";\nvar resourceId = \"RESOURCE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"resource-assignments/\" + resourceId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url\n}).done(function(data) {\n  console.log(data);\n});"
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