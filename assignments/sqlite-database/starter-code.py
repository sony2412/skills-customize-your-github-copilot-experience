import sqlite3
from typing import List, Tuple

DATABASE_FILE = "students.db"

def get_connection():
    return sqlite3.connect(DATABASE_FILE)

def create_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                grade REAL,
                email TEXT
            )
            """
        )
        conn.commit()

def add_student(name: str, grade: float, email: str) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, grade, email) VALUES (?, ?, ?)",
            (name, grade, email),
        )
        conn.commit()
        return cursor.lastrowid

def get_all_students() -> List[Tuple[int, str, float, str]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, grade, email FROM students")
        return cursor.fetchall()

def get_student(student_id: int) -> Tuple[int, str, float, str] | None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, grade, email FROM students WHERE id = ?",
            (student_id,),
        )
        return cursor.fetchone()

def update_student_grade(student_id: int, new_grade: float) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET grade = ? WHERE id = ?",
            (new_grade, student_id),
        )
        conn.commit()
        return cursor.rowcount > 0

def delete_student(student_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        return cursor.rowcount > 0

if __name__ == "__main__":
    create_table()
    print("Database initialized and students table created.")
