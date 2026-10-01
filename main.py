from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Session, create_engine, select

app = FastAPI()


class Task(BaseModel):
    title: str
    done: bool = False


class TaskDB(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    done: bool = False


DATABASE_URL = "sqlite:///tasks.db"

engine = create_engine(DATABASE_URL)


def create_db_and_seed():
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        existing_tasks = session.exec(select(TaskDB)).all()

        if not existing_tasks:
            tasks = [
                TaskDB(title="Learn FastAPI", done=False),
                TaskDB(title="Build Todo API", done=False),
                TaskDB(title="Submit FlyRank assignment", done=False)
            ]

            session.add_all(tasks)
            session.commit()


@app.on_event("startup")
def startup():
    create_db_and_seed()

tasks = [
    {"id": 1, "title": "Learn FastAPII", "done": False},
    {"id": 2, "title": "Build Todo API", "done": False},
    {"id": 3, "title": "Submit FlyRank assignment", "done": False}
]

@app.get("/")
def home():
    return {"message": "Hello"}

@app.get("/tasks", description="Get all tasks")
def get_tasks():
    with Session(engine) as session:
        tasks = session.exec(select(TaskDB)).all()
        return tasks

@app.get("/tasks/{task_id}", description="get a task by id")
def get_task(task_id: int):
    with Session(engine) as session:
        task = session.get(TaskDB, task_id)

        if task:
            return task

        raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", status_code=201, description="create a task")
def create_task(task: Task):
    with Session(engine) as session:
        new_task = TaskDB(
            title=task.title,
            done=task.done
        )

        session.add(new_task)
        session.commit()
        session.refresh(new_task)

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
from sqlmodel import Session, select

with Session(engine) as session:
    tasks = session.exec(select(TaskDB)).all()
    print(tasks)