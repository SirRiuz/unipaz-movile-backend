# Libs
from typing import List, Optional, Dict
import pandas


class Filter:

    def __init__(self, data:List) -> None:    
        self.__pandas = pandas.DataFrame(data)
        self.__data = data

    def filter(self, week_days:List[Dict],
               day:Optional[str] = None) -> List[Dict]:
        """ Filter the data for days of the weeks """

        if not self.__data:
            return None

        if day or day != "today":
            self.__pandas = self.__pandas\
                [self.__pandas["day"] == day]
            return self.__pandas.to_dict(
                orient="records")
        
        day = None
        for day_data in week_days:
            if day_data["is_today"]:
                day = day_data["name"]

        self.__pandas = self.__pandas\
            [self.__pandas["day"] == day]
        return self.__pandas.to_dict(
            orient="records")
