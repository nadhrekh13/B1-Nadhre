# Task Management API

A RESTful task management backend built with FastAPI that stores tasks in a JSON Lines file.

## Setup

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

2. Run the server from inside the `final_project` folder:
   ```bash
   uvicorn main:app --reload
   ```

3. Open the interactive API docs in your browser:
   ```
   http://127.0.0.1:8000/docs
   ```

## Project Structure

```
final_project/
├── main.py           # FastAPI application with all endpoints
├── tasks_helper.py   # Helper functions for loading/saving tasks
├── tasks.txt         # Data storage (JSON Lines format)
└── README.md         # This file
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Root check – confirms the API is running |
| GET | `/tasks` | Returns all tasks; supports `?completed=true/false` filter |
| GET | `/tasks/stats` | Returns statistics (total, completed, pending, completion %) |
| GET | `/tasks/{task_id}` | Returns a single task by ID |
| POST | `/tasks` | Creates a new task (auto-generates ID) |
| PUT | `/tasks/{task_id}` | Replaces an entire task by ID |
| DELETE | `/tasks/{task_id}` | Deletes a single task by ID |
| DELETE | `/tasks` | Deletes all tasks |

## Data Models

### TaskCreate (request body for POST)
```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread"
}
```

### Task (full representation)
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
```

## Error Handling

- `404 Not Found` – returned with `{"detail": "Task not found"}` when a task ID does not exist.
