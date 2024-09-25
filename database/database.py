import pymongo
from pymongo.collection import Collection

class Database:
    def __init__(self, database, collection):
        self.db: Database
        self.collection: Collection
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            #connectionString = "mongodb://localhost:27017"  # -> Local
            connectionString = "mongodb+srv://Rick98903:28465chaos@cluster0.ryq35.mongodb.net/" #-> Iflow

            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)