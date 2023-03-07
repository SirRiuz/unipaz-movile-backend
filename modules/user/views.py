# Python
import json

# Libs
from fastapi import Request, Response

# Modules
from modules.user.user import User
from server import app


@app.post("/change_password/")
async def change_password(data: dict, response:Response,
                            request:Request) -> Response:
    CREDENTIALS = request.state.credentials
    changed = User(credentials=CREDENTIALS).change_password({
        "old": data.get("old", ""),
        "password": data.get("password", ""),
        "confirm": data.get("confirm", "")
    })
    return ({"changed": changed})
