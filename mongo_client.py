from pymongo import MongoClient

try:
    conn = MongoClient('mongodb://coddicted:mayap14%40NYU@localhost:27017')
    print("connection successful")
except:
    print("could connect to MongoDB@172.20.0.2")

just_ask_db = conn['just_ask']
questions_collection = just_ask_db['questions']
cursor = questions_collection.find()
for record in cursor:
    print(record)
