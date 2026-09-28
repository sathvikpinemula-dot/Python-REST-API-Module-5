from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel, Field
import sqlite3
from typing import Optional

DB_NAME = "app.db"
API_KEY = "codomax-demo-key"

app = FastAPI(
    title="Student REST API",
    description="A documented FastAPI REST API with SQLite CRUD operations and basic API-key authentication.",
    version="1.0.0"
)

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            course TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., min_length=5, max_length=150)
    course: str = Field(..., min_length=2, max_length=100)

class Student(StudentCreate):
    id: int

def verify_api_key(x_api_key: Optional[str] = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return True

@app.get("/")
def home():
    return {"message": "Student REST API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/students", response_model=list[Student], dependencies=[Depends(verify_api_key)])
def get_students():
    conn = get_db()
    rows = conn.execute("SELECT * FROM students ORDER BY id").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/students/{student_id}", response_model=Student, dependencies=[Depends(verify_api_key)])
def get_student(student_id: int):
    conn = get_db()
    row = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Student not found")
    return dict(row)

@app.post("/students", response_model=Student, status_code=201, dependencies=[Depends(verify_api_key)])
def create_student(student: StudentCreate):
    conn = get_db()
    try:
        cursor = conn.execute(
            "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
            (student.name, student.email, student.course)
        )
        conn.commit()
        student_id = cursor.lastrowid
        row = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
        return dict(row)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Email already exists")
    finally:
        conn.close()

@app.put("/students/{student_id}", response_model=Student, dependencies=[Depends(verify_api_key)])
def update_student(student_id: int, student: StudentCreate):
    conn = get_db()
    existing = conn.execute("SELECT id FROM students WHERE id = ?", (student_id,)).fetchone()
    if not existing:
        conn.close()
        raise HTTPException(status_code=404, detail="Student not found")
    try:
        conn.execute(
            "UPDATE students SET name = ?, email = ?, course = ? WHERE id = ?",
            (student.name, student.email, student.course, student_id)
        )
        conn.commit()
        row = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
        return dict(row)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Email already exists")
    finally:
        conn.close()

@app.delete("/students/{student_id}", dependencies=[Depends(verify_api_key)])
def delete_student(student_id: int):
    conn = get_db()
    cursor = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
