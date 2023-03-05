# Libs
from libs.robots import BaseClient, Cliet
from settings import URLS
from typing import Dict


class User(BaseClient):

    def get_info(self) -> Dict[str, str]:
        """ Get personal data of the user """
        USER_DATA = Cliet({
            "url": URLS["STUDENT_INFO"],
            "credentials": self.credentials
        }).get_html_object()
        if not USER_DATA:
            return None
        
        USER_NAME = USER_DATA.find("span", {
            "class": "titleid710344siteid35"
        })
        USER_DATA = USER_DATA.find_all("td", {
            "class": "PortletBodyColor"
        })
        MAP_DATA = {}
        MAP_DATA["-1"] = USER_NAME.text.capitalize()
        
        for index in range(len(USER_DATA)):
            if len(USER_DATA[index].text) >= 3:
                MAP_DATA[index] = USER_DATA[index]\
                    .text.capitalize()
                MAP_DATA[index] = MAP_DATA[index]\
                    [:(len(MAP_DATA[index]) - 1)]

        return MAP_DATA
