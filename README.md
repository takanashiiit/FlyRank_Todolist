# Todo API

A simple Todo CRUD API built with FastAPI.

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
HTTP/1.1 200 OK
date: Thu, 01 Oct 2026 11:04:55 GMT
server: uvicorn
content-length: 198
content-type: application/json

[{"id":1,"title":"Learn FastAPI","done":false},{"id":2,"title":"Build Todo API","done":false},{"id":3,"title":"Submit FlyRank assignment","done":false},{"id":4,"title":"A1 submission","done":false}]

## Run

```bash
pip install "fastapi[standard]"
fastapi dev main.py

