from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    done: bool = False

tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build Todo API", "done": False},
    {"id": 3, "title": "Submit FlyRank assignment", "done": False}
]

@app.get("/")
def home():
    return {"message": "Hello"}

@app.get("/tasks",description="Get all tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", description="get a task by id")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", status_code=201,description="create a task")
def create_task(task: Task):
    new_id = max(t["id"] for t in tasks) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "done": task.done
    }

    tasks.append(new_task)
    return new_task
@app.put("/tasks/{task_id}",description="update a task")
def update_task(task_id: int, task: Task):
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = task.title
            t["done"] = task.done
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204,description="delete a task")
def delete_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return

    raise HTTPException(status_code=404, detail="Task not found")