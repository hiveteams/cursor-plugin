# Update resource assignment

Create a new project

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
      "put": {
        "summary": "Update resource assignment",
        "description": "Create a new project",
        "operationId": "update-resource",
        "parameters": [
          {
            "name": "resourceAssignmentId",
            "in": "path",
            "description": "ID of the resourceAssignment",
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
                "properties": {
                  "startDate": {
                    "type": "string",
                    "description": "Start date of the Project",
                    "format": "date"
                  },
                  "endDate": {
                    "type": "string",
                    "description": "End date of the Project",
                    "format": "date"
                  },
                  "projectId": {
                    "type": "string",
                    "description": "ID of the project for the resourcing"
                  },
                  "notes": {
                    "type": "string",
                    "description": "Project description"
                  },
                  "assignmentType": {
                    "type": "string",
                    "description": "Type of resourcing (regular, timeOff or allocation)",
                    "default": "regular"
                  },
                  "allocationType": {
                    "type": "string",
                    "description": "Type of hours breakdown (hoursPerDay or fixedHours)",
                    "default": "hoursPerDay"
                  },
                  "hoursPerDay": {
                    "type": "integer",
                    "description": "Hours worked per day",
                    "format": "int32"
                  },
                  "fixedHours": {
                    "type": "integer",
                    "description": "Total hours across entire resourcing",
                    "format": "int32"
                  },
                  "fixedDisplayType": {
                    "type": "string",
                    "description": "Display type (hours or days)",
                    "default": "hours"
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
                    "value": "{\n  \"message\": \"Resource assignment was updated successfully\",\n  \"resourceAssignment\": {\n    \"id\" : \"123456ABCDE\",\n    \"resourceId\" : \"user1234\",    \n    \"projectId\":\"project1234\",\n    \"startDate\" : ISODate(\"2019-01-01006:00:00.000Z\"),\n    \"endDate\" : ISODate(\"2020-01-01T00:00:00.000Z\"),\n    \"allocationType\" : \"hoursPerDay\",\n    \"assignmentType\" : \"regular\",\n    \"hoursPerDay\" : 8,\n    \"fixedHours\" : 8,\n    \"fixedDisplayType\" : \"hours\",\n    \"notes\":\"This is a note!\"\n  }\n}\n"
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
              "code": "var userId = \"USER_ID\";\nvar resourceId = \"RESOURCE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"resource-assignments/\" + resourceId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n    \"resourceId\" : \"user1234\",\n    \"projectId\":\"project1234\",\n    \"startDate\" : ISODate(\"2019-01-01006:00:00.000Z\"),\n    \"endDate\" : ISODate(\"2020-01-01T00:00:00.000Z\"),\n    \"allocationType\" : \"hoursPerDay\",\n    \"assignmentType\" : \"regular\",\n    \"hoursPerDay\" : 8,\n    \"fixedHours\" : 8,\n    \"fixedDisplayType\" : \"hours\",\n    \"notes\":\"This is a note!\"\n  };\n\n$.ajax({\n  method: \"PUT\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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