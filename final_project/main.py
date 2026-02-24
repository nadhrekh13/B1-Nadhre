from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tasks_helper import load_tasks, save_tasks

app = FastAPI(title="Task Management API", description="A simple task management backend using FastAPI")


class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


@app.get("/")
def root():
    return {"message": "Task Management API is running"}


@app.get("/tasks")
def get_tasks(completed: bool | None = None):
    tasks = load_tasks()
    if completed is not None:
        tasks = [t for t in tasks if t["completed"] == completed]
    return tasks


@app.get("/tasks/stats")
def get_stats():
    tasks = load_tasks()
    total = len(tasks)
    completed_count = sum(1 for t in tasks if t["completed"])
    pending_count = total - completed_count
    completion_percentage = (completed_count / total * 100) if total > 0 else 0.0
    return {
        "total": total,
        "completed": completed_count,
        "pending": pending_count,
        "completion_percentage": completion_percentage,
    }


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    tasks = load_tasks()
    new_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {
        "id": new_id,
        "title": task_data.title,
        "description": task_data.description,
        "completed": False,
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: Task):
    tasks = load_tasks()
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            updated = task_data.model_dump()
            updated["id"] = task_id
            tasks[index] = updated
            save_tasks(tasks)
            return tasks[index]
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted = tasks.pop(index)
            save_tasks(tasks)
            return {"message": "Task deleted", "task": deleted}
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks")
def delete_all_tasks():
    save_tasks([])
    return {"message": "All tasks deleted"}
