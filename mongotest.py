import pymongo
client = pymongo.MongoClient("mongodb+srv://Aarush:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Dip",
    "email_id": "Dip@inueron.ai",
    "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)