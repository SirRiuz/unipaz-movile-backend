# Python
import jwt
import json

# Libs
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from settings import JWT_SECRET_KEY, NO_REQUIRE_AUTH
from jwt.exceptions import InvalidTokenError


async def token_middleware(request: Request, call_next):

    if request.url.path in NO_REQUIRE_AUTH:
        response = await call_next(request)
        return response

    response = None
    TOKEN = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        DATA = jwt.decode(TOKEN, JWT_SECRET_KEY, algorithms=["HS256"])
        request.state.credentials = json.loads(DATA["credentials"])
        response = await call_next(request)
    except InvalidTokenError as e:
        return JSONResponse(status_code=400, content={"error": "invalid token"})

    return response
