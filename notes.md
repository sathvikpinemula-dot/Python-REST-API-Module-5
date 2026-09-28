# Python Application Development – Learning Notes

## 1. FastAPI Fundamentals
FastAPI is a Python web framework used to build APIs. It provides routing, request handling, validation and automatic interactive documentation.

Example 1:
`@app.get("/")` handles a GET request.

Example 2:
`@app.post("/students")` handles creation of a student.

## 2. HTTP Methods
- GET: retrieve data
- POST: create data
- PUT: update data
- DELETE: remove data

## 3. Routing and Endpoints
An endpoint combines an HTTP method and URL path. For example, `GET /students/1` retrieves student 1.

## 4. SQLite Database
SQLite is a lightweight relational database stored in a local file. Python's `sqlite3` module can execute SQL statements.

Example:
`SELECT * FROM students`

## 5. CRUD
CRUD means Create, Read, Update and Delete. The project implements all four operations through REST endpoints.

## 6. Schema Validation
Pydantic models validate incoming JSON data. Fields can have minimum and maximum lengths and required values.

## 7. Basic API Authentication
The project uses an API key sent in the `X-API-Key` request header. Protected endpoints reject requests with a missing or incorrect key.

## 8. Testing
FastAPI endpoints are tested with `TestClient` and pytest. Tests verify successful requests and authentication behavior.

## 9. API Documentation
FastAPI automatically provides Swagger UI at `/docs` and ReDoc at `/redoc`.

## 10. Clean Code Practices
- Separate application and test code
- Use meaningful names
- Validate inputs
- Use parameterized SQL queries
- Handle errors with suitable HTTP status codes
- Keep documentation updated
