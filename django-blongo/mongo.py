import pymongo

conn = pymongo.MongoClient("mongodb://127.0.0.1:27017")

databases = conn.database_names()

for database in databases:
    print(database)

conn.close()