# Libs
from datetime import datetime

def to_format_date(str_date:str) -> dict:
    """ Parse str format '07:00 - 09:00' to dict """
    if "-" in str_date:
        DATA = str_date.replace(' ','').split('-')
        START_DATE = datetime.strptime(DATA[0], "%H:%M").time()
        TYPE = START_DATE.strftime("%I:%M#%p").split("#")[1]

        #START_DATE = START_DATE.strftime("%I:%M %p")
        #START_DATE = datetime.strptime(START_DATE, "%H:%M %p").time()

        END_DATE = datetime.strptime(DATA[1], "%H:%M").time()
        #END_DATE = END_DATE.strftime("%I:%M %p")
        #END_DATE = datetime.strptime(END_DATE, "%H:%M %p").time()


        CLASS_HOURS = (END_DATE.hour - START_DATE.hour)
        return {
            "start_class": START_DATE.hour,
            "end_class": END_DATE.hour,
            "total_hours": f"{CLASS_HOURS}h",
            "hour_type": TYPE
        }
