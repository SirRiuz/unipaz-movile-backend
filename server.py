# Libs
from fastapi import FastAPI

app = FastAPI()

# Views
from modules.auth.views import *

