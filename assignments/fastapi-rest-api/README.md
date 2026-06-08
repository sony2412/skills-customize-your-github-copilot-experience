# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to create a simple REST API using FastAPI, define request and response models with Pydantic, and implement endpoint logic for data operations.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Set up a FastAPI application with a root endpoint and a health check endpoint.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define a root endpoint at `/` that returns a welcome message
- Define a health endpoint at `/health` that returns application status
- Example response for `/health`:
  ```json
  {
    "status": "ok"
  }
  ```

### 🛠️ Define Models and CRUD Endpoints

#### Description
Create Pydantic models and implement create, read, update, and delete operations using an in-memory data store.

#### Requirements
Completed program should:

- Define a `Item` model with `id`, `name`, `description`, and `price`
- Implement endpoints for:
  - `GET /items` to return all items
  - `GET /items/{item_id}` to return a single item
  - `POST /items` to create a new item
  - `PUT /items/{item_id}` to update an existing item
  - `DELETE /items/{item_id}` to remove an item
- Use an in-memory list or dictionary to store items
- Return appropriate status codes for success and missing items

### 🛠️ Validate Requests and Document the API

#### Description
Add request validation and ensure the API is easy to explore using FastAPI's automatic documentation.

#### Requirements
Completed program should:

- Use Pydantic validation for request bodies
- Return clear error responses for invalid input or missing items
- Confirm FastAPI docs are available at `/docs`
- Example valid `POST /items` request body:
  ```json
  {
    "name": "Notebook",
    "description": "A ruled notebook",
    "price": 7.99
  }
  ```
