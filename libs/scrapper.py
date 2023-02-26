# Libs
from bs4 import BeautifulSoup
from core.codes import *


class Scrapper:

    def __init__(self, html_code:str) -> None:
        self.bs = BeautifulSoup(html_code, 'html.parser')

    
    def is_chage_error(self) -> bool:
        return self.bs.find_all("td", {"class": "x5o"})

    def stract_data(self) -> dict:
        index = 0
        field_map = {
            DNI: "DNI",
            YEARS_OLD: "YEARS",
            GENDER: "GENDER",
            CITY: "CITY",
            ADDRESS: "ADRESS",
            PHONE_NUMBER: "PHONE_NUMBER",
            EMAIL: "EMAIL"
        }
        user_name = self.bs.find_all("span",{"class":"titleid710344siteid35"})
        user_name = user_name[0].text if user_name else None

        for tags in self.bs.find_all("span", {"class":"PortletText1"}):
            if index in field_map:
                field_map[index] = tags.text.replace('\u00a0', '')

            index += 1

        return ({ USER_NAME: user_name,**field_map })



