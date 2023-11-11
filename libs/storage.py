# Libs
import json
import datetime
import redis
from settings import REDIS_HOST, REDIS_PORT


class Storage:

    def __init__(self):
        self.__storage = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def get(self, key: str) -> bool:
        """ Check key in the storage """
        DATA = self.__storage.get(key)
        if DATA:
            DATA = json.loads(DATA)
            if self.__is_expired(DATA["expire"]):
                self.__storage.delete(key)
                return

            return DATA["data"]

    def __is_expired(self, date: str) -> bool:
        """ Check if data expired """
        TODAY = datetime.datetime.now()
        EXPIRE_DATE = datetime.datetime.strptime(date, "%Y-%m-%d").date()

        return TODAY.date() > EXPIRE_DATE

    def set(self, request_hash: str, data: str) -> dict:
        """ Set data in the storage """
        EXPIRE_DATA = datetime.datetime.now() + datetime.timedelta(weeks=10)
        payload_data = {"expire": EXPIRE_DATA.date().__str__(), "data": data}
        self.__storage.set(request_hash, json.dumps(payload_data))
