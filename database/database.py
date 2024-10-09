import pymongo
import traceback
from pymongo.collection import Collection
from pymongo.database import Database as PyMongoDatabase  # Import correto para o tipo

from log import log
class Database:
    def __init__(self, database, collection):
        self.db: PyMongoDatabase  # Tipo correto da classe Database do pymongo
        self.collection: Collection  # O tipo Collection já estava correto
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            # connectionString = "mongodb://localhost:27017"  # -> Local
            connectionString = "mongodb+srv://Rick98903:28465chaos@cluster0.ryq35.mongodb.net/"  # -> Iflow

            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            
            self.db = self.clusterConnection[database]  # Atribui o banco de dados
            self.collection = self.db[collection]  # Atribui a coleção do banco de dados
            print("Conectado ao banco de dados com sucesso!")
            
        except:
            detail_error = traceback.format_exc()
            print(f"Erro ao conectar ao banco de dados: {detail_error}")
            log.logger.error(f"Erro ao conectar ao banco de dados: {detail_error}")
