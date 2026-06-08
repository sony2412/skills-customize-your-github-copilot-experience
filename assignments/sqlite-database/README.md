# 📘 Assignment: Persistent Data with SQLite and Python

## 🎯 Objective

Learn how to store and manage application data using SQLite in Python, including creating tables, inserting records, querying data, and updating stored values.

## 📝 Tasks

### 🛠️ Set Up SQLite and Create a Database

#### Description
Initialize a SQLite database file and create a table to store student records.

#### Requirements
Completed program should:

- Connect to a SQLite database file using the `sqlite3` module
- Create a table named `students` with columns `id`, `name`, `grade`, and `email`
- Ensure the database file is created if it does not already exist
- Example table schema:
  ```sql
  CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade REAL,
    email TEXT
  )
  ```

### 🛠️ Insert and Query Records

#### Description
Implement functions to add new student records and retrieve them from the database.

#### Requirements
Completed program should:

- Add at least three student records to the `students` table
- Query all records and return the results
- Query a single student by `id`
- Example output:
  ```
  [(1, 'Ava', 92.5, 'ava@example.com'), (2, 'Noah', 88.0, 'noah@example.com')]
  ```

### 🛠️ Update and Delete Records

#### Description
Add functionality to update existing records and remove records from the database.

#### Requirements
Completed program should:

- Update a student's grade by `id`
- Delete a student record by `id`
- Confirm that changes are persisted by querying after each operation
- Example actions:
  - Update grade for student `id=2` to `90.0`
  - Delete student `id=3`
