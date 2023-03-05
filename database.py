import pymongo
client = pymongo.MongoClient("localhost", 27017)

DB = client.test

#DB.users.insert_one({"name": "Camila"})
#DB.users.delete_one({"name": "Camila"})
#DB.users.find({"name": "Camila"})
DB.users.find({"name": "Camila"})

# for user in DB.users.find():
#     print(user)

from modules.todo.todo import Todo

todo = Todo(user="1193096338").update()
print(todo)
