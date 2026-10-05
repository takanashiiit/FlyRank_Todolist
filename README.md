# Todo API

A simple Todo CRUD API built with FastAPI and SQLite.

# Swagger UI

<img width="1840" height="800" alt="image" src="https://github.com/user-attachments/assets/35480baa-3c6d-44ed-9361-cf5c46feae60" />
<img width="1322" height="837" alt="image" src="https://github.com/user-attachments/assets/f7f71412-7f52-4cf1-b190-7828d8380868" />
<img width="882" height="760" alt="image" src="https://github.com/user-attachments/assets/1b6979d2-3495-4f7e-8b29-bc82caedc0d2" />

#### curl -i Output

Request:

```bash
curl.exe -i http://127.0.0.1:8000/tasks
```

Response:

```text
HTTP/1.1 200 OK
date: Thu, 01 Oct 2026 11:04:55 GMT
server: uvicorn
content-length: 198
content-type: application/json

[{"id":1,"title":"Learn FastAPI","done":false},{"id":2,"title":"Build Todo API","done":false},{"id":3,"title":"Submit FlyRank assignment","done":false},{"id":4,"title":"A1 submission","done":false}]
```

## Database

The API uses SQLite to store tasks instead of keeping them only in memory.

SQLite was chosen because it is lightweight and does not require a separate database server, which makes it suitable for this small Todo API.

The database is stored locally as:

`tasks.db`

The `tasks` table contains:

* `id` - integer primary key
* `title` - task title
* `done` - task completion status

The database and table are created automatically when the application starts. Three example tasks are inserted only when the table is empty.

## Example SQL

View all tasks:

```sql
SELECT * FROM tasks;
```

Update a task:

```sql
UPDATE tasks
SET done = 1
WHERE id = 1;
```

Delete a task:

```sql
DELETE FROM tasks
WHERE id = 1;
```

The database was manually inspected using DB Browser for SQLite, and the CRUD operations were tested through Swagger UI. Data was also verified to persist after restarting the application.

## Run

```bash
pip install "fastapi[standard]" sqlmodel
fastapi dev main.py
```

Swagger UI:

`http://127.0.0.1:8000/docs`

## API Endpoints

* `GET /tasks` - Get all tasks
* `GET /tasks/{task_id}` - Get a task by ID
* `POST /tasks` - Create a task
* `PUT /tasks/{task_id}` - Update a task
* `DELETE /tasks/{task_id}` - Delete a task
