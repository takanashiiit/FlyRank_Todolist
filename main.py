from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Session, create_engine, select
from dotenv import load_dotenv
import os
app = FastAPI()


class Task(BaseModel):
    title: str | None = None
    done: bool = False

class TaskDB(SQLModel, table=True):
    __tablename__ = "tasks"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    done: bool = False


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

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

        raise HTTPException(
            status_code=404,
            detail={"error": "Task not found"}
        )

@app.post("/tasks", status_code=201, description="create a task")
def create_task(task: Task):
    if not task.title or not task.title.strip():
        raise HTTPException(status_code=400, detail="Title is required")
    with Session(engine) as session:
        new_task = TaskDB(
            title=task.title,
            done=task.done
        )

        session.add(new_task)
        session.commit()
        session.refresh(new_task)

        return new_task

@app.put("/tasks/{task_id}", description="update a task")
def update_task(task_id: int, task: Task):
    if not task.title or not task.title.strip():
        raise HTTPException(status_code=400, detail="Title is required")

    with Session(engine) as session:
        existing_task = session.get(TaskDB, task_id)

        if not existing_task:
            raise HTTPException(status_code=404, detail="Task not found")

        existing_task.title = task.title.strip()
        existing_task.done = task.done

        session.add(existing_task)
        session.commit()
        session.refresh(existing_task)

        return existing_task

@app.delete("/tasks/{task_id}", status_code=204, description="delete a task")
def delete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(TaskDB, task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        session.delete(task)
        session.commit()
