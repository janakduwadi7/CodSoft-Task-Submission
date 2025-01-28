# To-Do List application

## Overview

This project is a simple To-Do List application built using Flask. It allows users to create, view, update, and delete tasks. The project also includes an HTML interface to display tasks and a form to add new ones. Additionally, the API can be tested and utilized through Postman or similar tools.

## Features

- **Render Tasks on Webpage**: Displays the list of tasks on the homepage (`index.html`).
- **API Endpoints**: Includes RESTful API endpoints to perform CRUD (Create, Read, Update, Delete) operations.
- **Form Integration**: Users can add tasks through a form on the webpage.
- **Real-Time Update**: Tasks added or updated are dynamically reflected in the system.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, Jinja2 for template rendering
- **Testing Tools**: Postman

## How to Use

### 1. Clone the Repository

Clone this project from GitHub:

```bash
$ git clone https://github.com/your-username/repository-name.git
$ cd repository-name
```

### 2. Install Dependencies

Ensure you have Python installed, then install the required dependencies:

```bash
$ pip install flask
```

### 3. Run the Application

Start the Flask application by running:

```bash
$ python app.py
```

The application will run in development mode, accessible at `http://127.0.0.1:5000`.

### 4. API Endpoints

#### a. Fetch All Tasks

**URL:** `GET /api/tasks`

**Example Response:**

```json
[
  {"id": 1, "task": "Go to gym", "done": false},
  {"id": 2, "task": "Buy groceries", "done": false}
]
```

#### b. Add a New Task

**URL:** `POST /api/tasks`

**Form Data:**

- `id`: (Optional) Task ID (auto-generated if not provided)
- `task`: Task description (required)
- `done`: Completion status (default: `false`)

**Example Request in Postman:**

- **Method:** POST
- **Form Data:**
  ```json
  {
    "task": "Complete Flask Project",
    "done": false
  }
  ```

**Example Response:**

```json
{"message": "Task has been added successfully."}
```

#### c. Update a Task

**URL:** `PUT /api/tasks/<int:task_id>`

**JSON Data:**

- `done`: Completion status (required)

**Example Request in Postman:**

- **Method:** PUT
- **URL:** `http://127.0.0.1:5000/api/tasks/1`
- **JSON Body:**
  ```json
  {
    "done": true
  }
  ```

**Example Response:**

```json
{"message": "Task Updated successfully"}
```

#### d. Delete a Task

**URL:** `DELETE /api/tasks/<int:task_id>`

**Example Request in Postman:**

- **Method:** DELETE
- **URL:** `http://127.0.0.1:5000/api/tasks/1`

**Example Response:**

```json
{"message": "Task Deleted Successfully."}
```

## Frontend Usage

- Navigate to `http://127.0.0.1:5000` to view tasks and add new tasks.
- The page includes:
  - A list of tasks with their completion status (Done/Pending).
  - A form to submit new tasks.

## Special Features

- **Dynamic Templating**: Uses Jinja2 to render tasks dynamically on the homepage.
- **Global Task Management**: Updates tasks in-memory, making changes instantly visible.
- **API Flexibility**: Endpoints are designed to work seamlessly with tools like Postman.

## Future Enhancements

- Add a database for persistent task storage (e.g., PostgreSQL, SQLite).
- Implement user authentication for personalized task management.
- Enhance the frontend design with CSS frameworks like Bootstrap or TailwindCSS.

---

Feel free to explore, modify, and expand upon this project. Contributions are welcome!

