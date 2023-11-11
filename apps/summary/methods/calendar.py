# python
import calendar
import urllib.parse
import datetime
from typing import Optional, List, Dict

# libs
from libs.robots import Cliet, BaseClient
from settings import URLS
from helpers.calendar import to_format_date
from apps.summary.methods.payloads import CALENDAR_BODY
from apps.summary.methods.codes import *


class Calendar(BaseClient):


    def get_calendar_days(self) -> (list):
        """ Get list of the week days """
        day_list = []
        WEEKS_DAY = list(calendar.day_name)
        TODAY_DATA = datetime.datetime.now()
        TODAY_DAY = TODAY_DATA.strftime("%A")
        positive_day_count = 0
        negative_day_count = 0


        for positive_day in range(WEEKS_DAY.index(TODAY_DAY), len(WEEKS_DAY)):
            DAY_NAME = WEEKS_DAY[positive_day]
            day_list.append(
                {
                    "name": DAY_NAME.lower(),
                    "day": (
                        TODAY_DATA + datetime.timedelta(days=positive_day_count)
                    ).day,
                    "is_today": DAY_NAME == TODAY_DAY,
                }
            )
            positive_day_count += 1

        for negative_day in range(WEEKS_DAY.index(TODAY_DAY), 0, -1):
            DAY_NAME = WEEKS_DAY[negative_day_count]
            day_list.append(
                {
                    "name": DAY_NAME.lower(),
                    "day": (TODAY_DATA - datetime.timedelta(
                        days=negative_day)).day,
                    "is_today": DAY_NAME == TODAY_DAY,
                }
            )
            negative_day_count += 1

        return sorted(day_list, key=lambda x: x["day"])


    def get_class(self, option = None) -> (list):
        """ Get calendar data """
        if self.credentials:
            CLASS_LIST = []
            BODY = CALENDAR_BODY.replace("%OPTION%", option) if option else "vista=AI"
            data = Cliet(
                {
                    "method": "post",
                    "headers": {
                        "Content-Type": "application/" + "x-www-form-urlencoded"
                    },
                    "data": BODY,
                    "url": URLS["CALENDAR"],
                    "credentials": self.credentials,
                    "redirect": True,
                    "useCache": True,
                }
            ).get_html_object()

            if not data:
                return []

            CALENDAR_DATA = data.find(
                "table",
                {
                    "border": "1",
                    "cellspacing": "0",
                    "xmlns:estilos": "http://www.oracle.com/XSL/Transform/"
                    + "java/es.ocu.uxxi_general.util.propiedades.EstilosPortal",
                },
            )

            if not CALENDAR_DATA:
                return []

            day_index = 0
            calendar_items = CALENDAR_DATA.find_all("td", {"class": "PortletBodyColor"})

            for index, calendar_item in enumerate(calendar_items):
                WEEK_DAY = list(calendar.day_name)[index]
                if len(calendar_item) > 0:
                    k = 0
                    map_item = {}
                    for el in calendar_item:
                        if el.name != "hr":
                            map_item[k] = el.text.replace("\xa0", "")
                            map_item["day"] = WEEK_DAY.lower()
                            k += 1
                        else:
                            CLASS_LIST.append(map_item.copy())
                            map_item.clear()
                            k = 0

            result = []
            for item in CLASS_LIST:
                class_meta = item[CLASS_META].replace(" ", "").split("-")
                class_code = class_meta[0]
                class_name = item[CLASS_NAME].capitalize()
                class_teacher = item[TEACHER_NAME].replace("Prof.", "").capitalize()
                class_time = item[TIME].replace("a", "-")
                time = to_format_date(class_time)
                day_name = "nigth" if time["hour_type"].lower() == "pm" else "day"
                location = ({
                        "room": "Salon 22",
                        "loc": "Edicicio de aulas segundo piso",
                    })

                data = ({
                    "code": class_code,
                    "name": class_name,
                    "teacher": class_teacher,
                    "day": item["day"],
                    "location": location,
                    "time": time,
                })

                result.append(data)

        return result
