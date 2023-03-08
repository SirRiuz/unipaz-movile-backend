# Python
from typing import Dict, Union, Optional

# Libs
from libs.db import Database
from bson.objectid import ObjectId


class Todo:

    def __init__(self, user:str):
        self.user = user
        self.DB = Database().get_conection()

    def update(self, id:str, data:Dict) -> Dict[str, str]:
        pass

    def get(self, id:Optional[str] = None) -> (Union[Dict, list]):
        """ Get list todo or the data of only todo """
        if not id:
            TODOS_LIST:list[Dict[str, str]] = []
            todos = self.DB.todo.find({"user": self.user})
            for todo in todos:
                TODOS_LIST.append({
                    "_id": str(todo["_id"]),
                    "title": todo["title"],
                    "notes": todo["notes"]
                })
            
            return TODOS_LIST

        try:
            TODO = self.DB.todo.find_one({
                "user": self.user,
                "_id": ObjectId(id)
            })
            if TODO:
                return ({
                    "id": str(TODO["_id"]),
                    "title": TODO["title"],
                    "notes": TODO["notes"]
                })

        except Exception:
            pass


    def create(self, data:Dict[str, str]) -> Dict[str, str]:
        """ Create todo in the database """
        self.DB.todo.insert_one({
            "title": data["title"],
            "notes": data.get("notes", ""),
            "user": self.user
        })
        return data
    
    def delete(self, id):
        self.DB.todo.delete_one({
            "user": self.user,
            "_id": ObjectId(id)
        })
