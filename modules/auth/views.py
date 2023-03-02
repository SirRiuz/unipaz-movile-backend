# Python
import json

# Libs
import jwt
from fastapi import Request, Response
from settings import JWT_SECRET_KEY

# Modules
from modules.auth.auth import Auth
from modules.user.user import User
from server import app


@app.post("/auth/check/")
async def check(request:Request) -> Response:
    """ Check the jwt token and the cookies sesion """
    IS_VALID = False
    TOKEN = request.headers.get("Authorization", "")\
        .replace("token ", "")
    try:
        DATA = jwt.decode(
            TOKEN, JWT_SECRET_KEY,
            algorithms=["HS256"]
        )
        data = User(json.loads(DATA["credentials"]))\
            .get_info()
        IS_VALID = bool(data)
    except Exception as e:
        pass

    return({"is_valid": IS_VALID})


@app.post("/auth/")
async def auth(data: dict, response:Response) -> Response:
    """ Get acces token of the user """
    USER = data.get("user", "")
    PASSWORD = data.get("password", "")
    CREDENTIALS = Auth(USER, PASSWORD).login()
    if CREDENTIALS:
        TOKEN = jwt.encode({
            "credentials": json.dumps(CREDENTIALS)
        }, JWT_SECRET_KEY, algorithm="HS256")
        return ({
            "token": TOKEN,
            "user": User(CREDENTIALS).get_info(),
            "need_change": (USER == PASSWORD)
        })

    response.status_code = 400
    return ({"messege": "Invalid user or password"})
