from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = [
    {"id": 1, "title": "Learn fastAPI", "done": False},
    {"id": 2, "title": "Build todo API", "done": False},
    {"id": 3, "title": "submit flyrank a1 assignment", "done": False}
]

@app.get("/")
def home():
    return {"message": "Hello"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")