# Libs
import requests
from typing import Dict
from settings import URLS
from libs.robots import BaseClient, Cliet
from helpers.auth import parse_cookies
from modules.user.payloads import CHANGE_PAYLOAD


class User(BaseClient):
    def get_info(self) -> (Dict[str, str]):
        """Get personal data of the user"""
        USER_DATA = Cliet(
            {"url": URLS["STUDENT_INFO"], "credentials": self.credentials}
        ).get_html_object()
        if not USER_DATA:
            return None

        USER_NAME = USER_DATA.find("span", {"class": "titleid710344siteid35"})
        USER_DATA = USER_DATA.find_all("td", {"class": "PortletBodyColor"})
        MAP_DATA = {}
        MAP_DATA["-1"] = USER_NAME.text.capitalize()

        for index in range(len(USER_DATA)):
            if len(USER_DATA[index].text) >= 3:
                MAP_DATA[index] = USER_DATA[index].text.capitalize()
                MAP_DATA[index] = MAP_DATA[index][: (len(MAP_DATA[index]) - 1)]

        return MAP_DATA

    def change_password(self, data) -> (bool):
        CHANGE_AUTH_TOKEN = None
        RESPONSE = requests.get(
            url=URLS["CHANGE_PASSWORD"],
            headers={"Content-Type": "application/" + "x-www-form-urlencoded"},
            cookies=self.credentials,
            allow_redirects=False,
        )
        if RESPONSE.is_redirect:
            TOKEN = requests.get(
                url=RESPONSE.headers["Location"],
                cookies=self.credentials,
                allow_redirects=False,
            )
            if "Location" in TOKEN.headers:
                if TOKEN.is_redirect:
                    CHANGE_TOKEN = requests.get(
                        url=TOKEN.headers["Location"],
                        cookies=self.credentials,
                        allow_redirects=False,
                    )
                    CHANGE_AUTH_TOKEN = parse_cookies(CHANGE_TOKEN)

        OLD = data.get("old", "")
        NEW = data.get("password", "")
        CONFIRM = data.get("confirm", "")
        PAYLOAD = (
            CHANGE_PAYLOAD.replace("%OLD%", OLD)
            .replace("%NEW%", NEW)
            .replace("%CONFIRM%", CONFIRM)
        )

        if CHANGE_AUTH_TOKEN:
            CHANGE_RESPONSE = Cliet(
                {
                    "debug": True,
                    "method": "post",
                    "debug": True,
                    "url": URLS["CHANGE_PASSWORD"],
                    "headers": {
                        "Content-Type": "application/" + "x-www-form-urlencoded"
                    },
                    "data": PAYLOAD,
                    "credentials": {**self.credentials, **CHANGE_AUTH_TOKEN},
                }
            ).get_html_object()

            IS_INVALID = CHANGE_RESPONSE.find_all("td", {"class": "x5o"})
            return not bool(IS_INVALID)
