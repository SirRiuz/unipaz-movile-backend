# python
import calendar
import urllib.parse
import datetime
from typing import Optional, List, Dict

# libs
from libs.robots import Cliet
from settings import URLS
from helpers.calendar import to_format_date
from modules.calendar.payloads import CALENDAR_BODY
from modules.calendar.codes import *


class Calendar:

    def __init__(self, credentials):
        self.credentials = credentials

    def options(self) -> list:
        """ Get the options for filter the data """
        if self.credentials:
            OPTION_LIST = []
            data = Cliet({
                "url": URLS["CALENDAR"],
                "credentials": self.credentials,
                "useCache": True
            }).get_html_object()
            OPTIONS = data.find("select", {
                "name": "curso"
            }).findAll("option")
            for option in OPTIONS:
                OPTION_LIST.append({
                    "value": urllib.parse.quote(option["value"]),
                    "text": option.text
                })

            return OPTION_LIST
        
    def get_calendar_days(self) -> List[Dict]:
        """ Get list of the week days """
        WEEKS_DAY = list(calendar.day_name)
        TODAY_DAY = datetime.datetime.now().strftime('%A')
        day_list = []
        for day in WEEKS_DAY:
            day_list.append({
                "name": day.lower(),
                "is_today": day == TODAY_DAY
            })
        
        return day_list

    def get_class(self, option:Optional[str] = None) -> List[Dict]:
        """ Get calendar data """
        if self.credentials:
            CLASS_LIST:list[dict] = []
            BODY = CALENDAR_BODY.replace("%OPTION%" ,option) \
                if option else None

            data = Cliet({
                "method": "post",
                "headers": {
                    "Content-Type": "application/"\
                        + "x-www-form-urlencoded"
                },
                "data": BODY,
                "url": URLS["CALENDAR"],
                "credentials": self.credentials,
                "redirect": True,
                "useCache": True
            }).get_html_object()

            if not data:
                return []

            CALENDAR_DATA = data.find_all("table",{"class": "tabla"})

            if not CALENDAR_DATA:
                return []
            
            CALENDAR_DATA = CALENDAR_DATA[1].find_all("tr")
            
            for item in CALENDAR_DATA:
                k = 0
                for calendar_items \
                    in item.find_all("td", {"class": "PortletBodyColor"}):
                    CALENDAR_SPAN_DATA = calendar_items.find_all("span")
                    if len(CALENDAR_SPAN_DATA) > 0:
                        # TODO : Solucionar error en calendario
                        # salen clases en el dia domingo
                        WEEK_DAY = list(calendar.day_name)\
                            [k].lower()
                        CLASS_LIST.append({
                            "day": WEEK_DAY,
                            "time":  to_format_date(
                                item.find("td", {"class": "PortletHeaderColor"}
                            ).text),
                            "name": CALENDAR_SPAN_DATA[CLASS_NAME]\
                                .text.capitalize(),
                            "teacher": (CALENDAR_SPAN_DATA[TEACHER_NAME].text)\
                                .replace("Prof.\u00a0", "").capitalize()
                        })
                    k += 1

        return CLASS_LIST
