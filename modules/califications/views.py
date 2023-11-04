# Libs
from server import app
from fastapi import Request, Response

# Modules
from modules.calendar.calendar import Calendar
from modules.calendar.filter import Filter
from modules.califications.califications import Califications


@app.get("/califications/")
async def actualCalifications(request: Request, old: bool = False) -> (Response):
    """Get a data califications"""
    CREDENTIALS = request.state.credentials
    CALIFICATIONS = Califications(credentials=CREDENTIALS)
    OPTIONS_LIST = CALIFICATIONS.options()
    return {
        "actual": CALIFICATIONS.get_actual_califications(OPTIONS_LIST),
        "old": CALIFICATIONS.get_old_califications(),
    }
