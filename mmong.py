from pymongo import MongoClient
import datetime

cluster = "mongodb+srv://pmcumm:MjO5YAGLBMsZ6myA@cluster0.kbtdehi.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(cluster)

print(client.list_database_names())

db = client.test

print(db.list_collection_names())


#MjO5YAGLBMsZ6myA

todo1 = {
        "name": "Patrick",
        "text": "My first to do",
        "status": "open",
        "tags": ["python","coding"],
        "date": str(datetime.datetime.utcnow())
        }

todo2 = [{ "name": "Patrick",
        "text": "My second to do",
        "status": "open",
        "tags": ["python","coding"],
        "date": str(datetime.datetime.utcnow())},
        { "name": "Mary",
        "text": "My third to do",
        "status": "open",
        "tags": ["C++","coding"],
        "date": str(datetime.datetime(2023,7,7,10,45))}]

todos = db.todos

#results = todos.insert_one(todo1)
#results = todos.insert_many(todo2)

#result = todos.find_one( {"name": "Mary"})
#result = todos.find_one({"tags": "C++"})
dbs = client.list_database_names()
print(dbs)
#d = datetime.datetime(2023,2,7,1,1)

#results = todos.find()

#print(todos.count_documents({}))
#for result in results:
#    print(result)

#print(result)
