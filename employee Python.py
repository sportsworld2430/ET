#Inserting
from Pymongo import Mongoclient
import pprint
client=MongoClient("localhost",27017)
db=Client.myDatabase
employee={
    "id":"101",
    "name":"Maaz",
    "Profession":"Software Engineer"
    }
employee=db.employees
employee.insert_one(employee)
pprint.pprint(employee.find_one())
on command propmt
db.employees.find()




#Delete
from Pymongo import Mongoclient
import pprint
client=MongoClient("localhost",27017)
db=Client.myDatabase
employee={
    "id":"102",
    "name":"Huzaifa",
    "Profession":"Software Engineer"
    }
employee=db.employees
employee.delete_one(employee)
pprint.pprint(employee.find_one())
on command propmt
db.employees.find()


#update
from Pymongo import Mongoclient
import pprint
client=MongoClient("localhost",27017)
db=Client.myDatabase
employee={
    "id":"101",
    "name":"Maaz",
    "Profession":"Software Engineer"
    }
employee=db.employees
employee.update_one({"id":"102"},{"$set":{"name":"Saif"}})
pprint.pprint(employee.find_one({"id":"102"}))
on command propmt
db.employees.find()


#retrieving
from Pymongo import Mongoclient
import pprint
client=MongoClient("localhost",27017)
db=Client.myDatabase
employee={
    "id":"102",
    "name":"Huzaifa",
    "Profession":"Software Engineer"
    }
employee=db.employees
employee.insert_one(employee)
pprint.pprint(employee.find_one())
on command propmt
db.employees.find()
