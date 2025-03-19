import pymongo

class DatabaseHandler:
    def __init__(self, connection_string, database_name, collection_name):
        try:
            self.client = pymongo.MongoClient(connection_string)
            self.db = self.client[database_name]
            self.collection = self.db[collection_name]
            print("Connected to MongoDB")
        except pymongo.errors.ConnectionFailure as e:
            print(f"Could not connect to MongoDB: {e}")
            raise

    def insert_data(self, data):
        self.collection.insert_one(data)