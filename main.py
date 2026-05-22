from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="QuickTasker", version="0.1.0")

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# In‑memory store
_tasks: Dict[int, Task] = {}
_next_id = 1

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    global _next_id
    task.id = _next_id
    _tasks[_next_id] = task
    _next_id += 1
    return task

@app.get("/tasks", response_model=Dict[int, Task])
def list_tasks():
    return _tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = _tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated: Task):
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    updated.id = task_id
    _tasks[task_id] = updated
    return updated

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del _tasks[task_id]
    return
