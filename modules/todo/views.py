# Libs
from server import app
from settings import JWT_SECRET_KEY
from modules.user.user import User
from modules.todo.todo import Todo
from fastapi import Request, Response


@app.delete("/tasks/{todo_id}/")
@app.get("/tasks/{todo_id}/")
@app.get("/tasks/")
@app.post("/tasks/")
async def tasks(
    request: Request, respnse: Response, data: dict = {}, todo_id: str = None
) -> (Response):
    CREDENTIALS = request.state.credentials
    user_data = User(CREDENTIALS).get_info()
    USER_ID = user_data[0]

    if request.method == "GET":
        todos = Todo(USER_ID).get(todo_id)
        if todos or not todo_id:
            return {"data": todos}
        respnse.status_code = 404
        return {"messege": "Task not found"}

    if request.method == "DELETE":
        Todo(USER_ID).delete(todo_id)
        return {"messege": "Task deleted!"}

    if request.method == "POST":
        return {
            "data": Todo(USER_ID).create(
                {
                    "user": USER_ID,
                    "notes": data.get("notes", ""),
                    "title": data.get("title", ""),
                }
            )
        }
