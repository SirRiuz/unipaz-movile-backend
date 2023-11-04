# Libs
from server import app
from fastapi import Request, Response

# Modules
from modules.calendar.calendar import Calendar
from modules.calendar.filter import Filter


@app.get("/calendar/")
async def calendar(
    request: Request, response: Response, day: str = None, all: bool = False
) -> (Response):
    """Get calendar data of the user"""
    CREDENTIALS = request.state.credentials
    calendar = Calendar(CREDENTIALS)
    filter_data = Filter(data=calendar.get_class()).filter(
        week_days=calendar.get_calendar_days(), day=day, all=all
    )
    if all:
        return {
            "days": calendar.get_calendar_days(),
            "data": filter_data,
        }

    return {"data": filter_data}


@app.get("/calendar/days/")
async def days(request: Request) -> (Response):
    """Get days of the week"""
    CREDENTIALS = request.state.credentials
    calendar = Calendar(CREDENTIALS).get_calendar_days()
    return {"data": calendar}


@app.get("/calendar/options/")
async def options(request: Request, day: str = None) -> (Response):
    """Get options filter of calendar"""
    CREDENTIALS = request.state.credentials
    calendar = Calendar(CREDENTIALS).options()
    return {"data": calendar}
