
# Python-REST-API-Module-5
=======
# Student REST API – Python Application Development

A beginner-friendly FastAPI project demonstrating web framework fundamentals, routing, REST endpoints, SQLite database storage, CRUD operations, API-key authentication, Pydantic schema validation, automatic API documentation, and endpoint testing.

## Features

- FastAPI application and routing
- GET, POST, PUT and DELETE endpoints
- SQLite database
- CRUD operations for student records
- Pydantic request/response validation
- Basic API-key authentication
- Automated endpoint tests
- Swagger UI and ReDoc documentation

## Project Structure

```text
Python_REST_API_Module_5/
├── app/
│   └── main.py
├── tests/
│   └── test_api.py
├── README.md
├── notes.md
├── requirements.txt
└── .gitignore
```

## Setup

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Open:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

Use this API key in Swagger's header field:

```text
X-API-Key: codomax-demo-key
```

## Example request

POST `/students`

```json
{
  "name": "Sathvik",
  "email": "sathvik@example.com",
  "course": "Python"
}
```

## Test

```bash
pytest
```

## Learning outcome

This project demonstrates how a Python web API can receive validated JSON requests, store data in SQLite, perform CRUD operations, protect endpoints with basic authentication, and expose interactive documentation.(Completed Python Application Development Module)
