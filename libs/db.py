# Libs
import pymongo
from pymongo.database import Database


class Database:

    def get_conection(self) -> Database:
        """ Get conection of mongo database """
        client = pymongo.MongoClient("localhost", 27017)
        return client.test
