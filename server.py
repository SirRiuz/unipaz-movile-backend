# Libs
from fastapi import FastAPI

# Middlewares
from middlewares.token import token_middleware

app = FastAPI()
app.middleware("http")(token_middleware)


# Views
from modules.auth.views import *
from modules.calendar.views import *
from modules.user.views import *
from modules.todo.views import *
from modules.califications.views import *
