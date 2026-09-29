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
@app.get("/tasks")
def get_tasks():
    return tasks
@app.get("/tasks/{task_id}")
@app.post("/tasks", status_code=201)
def create_task(task: Task):
    new_id = max(t["id"] for t in tasks) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "done": task.done
    }
    tasks.append(new_task)
    return new_task
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")