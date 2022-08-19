import uuid
import datetime
import pymongo

client = pymongo.MongoClient("mongodb+srv://greatwindmill:ptm5oyCJ0FW1dFkx@gwd.boccfcn.mongodb.net/?retryWrites=true&w=majority")
db = client.MyDatabase
collection = db.MyCollection

def save_to_db(kecepatan,latitude,longitude) -> tuple:
    try:
        data = {
            "ID_Transaksi": str(uuid.uuid4()),
            "Kecepatan": kecepatan,
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": datetime.datetime.now()
        }
        # insert data
        rec_id1 = collection.insert_one(data)

        print("Data inserted with record ids",rec_id1)
        return True,None
    except Exception as e:
        return False,str(e)

