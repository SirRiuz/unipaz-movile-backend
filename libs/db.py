# Libs
import pymongo
from pymongo.database import Database
from settings import DATABASE_HOST, DATABASE_PORT


class Database:

    def get_conection(self) -> (Database):
        """ Get conection of mongo database """
        client = pymongo.MongoClient(DATABASE_HOST, DATABASE_PORT)
        return client.test
