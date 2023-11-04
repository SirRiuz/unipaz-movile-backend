# Python
import re
import json

# Libs
from settings import URLS
from libs.robots import Cliet, BaseClient
from helpers.califications import get_future_califications
from modules.califications.payloads import CALENDAR_BODY, OLD_CALIFICATIONS


class Califications(BaseClient):
    def __get_options(self, options) -> (list):
        """Get all signatures id"""
        SCRIPT_TEXT = options.text
        OPTIONS = re.findall(r"\d+", SCRIPT_TEXT)
        OPTIONS_LIST = []
        for item in OPTIONS:
            if len(item) == 5:
                OPTIONS_LIST.append(item)

        return OPTIONS_LIST

    def __total_signatures(self) -> (list):
        if self.credentials:
            response = Cliet(
                {
                    "url": URLS["MY_SIGNATURES"],
                    "credentials": self.credentials,
                    "render": True,
                    "useCache": True,
                }
            ).get_html_object()
            SIGNATURES_TABLE = response.find(
                "table", {"class": "tabla", "sort": "true"}
            )
            if SIGNATURES_TABLE:
                return len(SIGNATURES_TABLE) - 1

    def get_actual_califications(self, options) -> (list):
        """Get califications of the actual semester"""
        if self.credentials and options:
            CALIFICATION_DATA = []
            for id in options:
                DATA = {}
                califications = []
                OPTION = CALENDAR_BODY.replace("<OPTION>", id)
                response = Cliet(
                    {
                        "headers": {
                            "Content-Type": "application/" + "x-www-form-urlencoded"
                        },
                        "url": URLS["CALIFICATIONS_OPTIONS"],
                        "credentials": self.credentials,
                        "method": "post",
                        "debug": True,
                        "data": OPTION,
                    }
                ).get_html_object()
                ROOT_TABLE = response.find(
                    "div", {"id": "imprimible_706515_" + "MISNOTASPARCIALES_22125922"}
                )

                if ROOT_TABLE:
                    MESSEGES = ROOT_TABLE.find_all("span", {"class": "PortletHeading1"})

                    CALIFICATION_TABLE = ROOT_TABLE.find(
                        "table", {"align": "center", "border": "1"}
                    )
                    CALIFICATIONS = CALIFICATION_TABLE.find_all("tr")
                    CLASS_TITLE = MESSEGES[len(MESSEGES) - 1]
                    CLASS_TITLE = CLASS_TITLE.text.split("-")[1].capitalize()
                    DATA["signature"] = CLASS_TITLE

                    for item in range(1, len(CALIFICATIONS)):
                        TABLE_DATA = CALIFICATIONS[item].find_all("td")
                        CALIFICATION = TABLE_DATA[1].text
                        CALIFICATION = CALIFICATION if CALIFICATION else None

                        CALIFICATION = (
                            float(CALIFICATION.replace(",", "."))
                            if CALIFICATION
                            else None
                        )

                        isBadCalification = CALIFICATION < 3.0 if CALIFICATION else None

                        califications.append(
                            {
                                "porcentaje": f"{TABLE_DATA[3].text}%",
                                "calification": CALIFICATION if CALIFICATION else "--",
                                "isBadCalification": isBadCalification,
                            }
                        )
                    DATA["califications"] = califications
                    DATA["predictions"] = get_future_califications(califications)
                    CALIFICATION_DATA.append(DATA)

            return CALIFICATION_DATA

    def __old_options(self) -> (list):
        """Get options of the old semesters"""
        OPTIONS_LIST = []
        if self.credentials:
            response = Cliet(
                {
                    "url": URLS["OLD_CALIFICATIONS"],
                    "credentials": self.credentials,
                    "render": True,
                    "useCache": True,
                }
            ).get_html_object()
            OPTIONS = response.find("select", {"name": "cursoMatriculado"})
            if OPTIONS:
                OPTIONS = OPTIONS.find_all("option")
                for option in OPTIONS:
                    OPTIONS_LIST.append({"value": option["value"], "text": option.text})

        return OPTIONS_LIST

    def get_old_califications(self) -> (list):
        CALIFICATIONS = []
        if self.credentials:
            for option in self.__old_options():
                PAYLOAD = OLD_CALIFICATIONS.replace("<OPTION>", option["value"])
                response = Cliet(
                    {
                        "headers": {
                            "Content-Type": "application/" + "x-www-form-urlencoded"
                        },
                        "url": URLS["OLD_CALIFICATIONS"],
                        "credentials": self.credentials,
                        "method": "post",
                        "debug": True,
                        "data": PAYLOAD,
                    }
                ).get_html_object()

                DATA_TABLE = response.find_all(
                    "table", {"cellpadding": "2", "class": "tabla", "border": "1"}
                )
                for table in DATA_TABLE:
                    SEMESTER_CALIFICATIONS = []
                    for i in table:
                        TABLE_DATA = i.find_all("span", {"class": "PortletText3"})
                        if TABLE_DATA:
                            CALIFICATION = TABLE_DATA[4].text.replace("   ", "")
                            CALIFICATION = CALIFICATION.replace(",", ".")
                            CALIFICATION = float(CALIFICATION)
                            SIGNATURE = (
                                TABLE_DATA[0].text.replace("   ", "").capitalize()
                            )
                            FAILS = TABLE_DATA[6].text
                            IS_APROVE = CALIFICATION >= 3
                            SEMESTER_CALIFICATIONS.append(
                                {
                                    "signature": SIGNATURE,
                                    "calification": CALIFICATION,
                                    "is_aprove": IS_APROVE,
                                    "fails": FAILS,
                                }
                            )

                    CALIFICATIONS.append(SEMESTER_CALIFICATIONS.copy())
                    SEMESTER_CALIFICATIONS.clear()

            return CALIFICATIONS

    def options(self) -> (list):
        """List of the actual signatures id"""
        if self.credentials:
            response = Cliet(
                {
                    "url": URLS["CALIFICATIONS_OPTIONS"],
                    "credentials": self.credentials,
                    "debug": True,
                    "useCache": True,
                }
            ).get_html_object()
            if response:
                SCRIPT_OPTIONS = response.find("script", {"language": "Javascript"})
                OPTIONS_LIST = self.__get_options(SCRIPT_OPTIONS)
                SIZE = self.__total_signatures()

                return OPTIONS_LIST[0:SIZE] if (SIZE and OPTIONS_LIST) else None
