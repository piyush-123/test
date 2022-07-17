import pymongo

client = pymongo.MongoClient("mongodb+srv://piyush1304:System909@cluster0.gocvn.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
#c
d = {
    "name" : "piyush",
    "email" : "piyush@gmail.com",
    "surname" : "aggarwal"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
