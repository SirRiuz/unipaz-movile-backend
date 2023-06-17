# Libs
import pymongo
from settings import DATABASE_HOST, DATABASE_PORT

client = pymongo.MongoClient(DATABASE_HOST, DATABASE_PORT)
DB = client.test
