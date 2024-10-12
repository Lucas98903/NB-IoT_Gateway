import pymongo
import traceback
from pymongo.collection import Collection
from pymongo.database import Database as PyMongoDatabase  # Import correto para o tipo
from typing import Optional  # Adiciona o Optional para indicar que pode ser None

from log import log


class Database:
    def __init__(self, database: str, collection: str):
        self.clusterConnection: Optional[
            pymongo.MongoClient] = None  # Inicializa como None, mas pode ser do tipo MongoClient
        self.db: Optional[PyMongoDatabase] = None  # Pode ser None ou PyMongoDatabase
        self.collection: Optional[Collection] = None  # Pode ser None ou Collection
        self.connect(database, collection)

    def connect(self, database: str, collection: str):
        try:
            # connectionString = "mongodb://localhost:27017"  # -> Local
            connection_string = "mongodb+srv://Rick98903:28465chaos@cluster0.ryq35.mongodb.net/"  # -> Iflow

            self.clusterConnection = pymongo.MongoClient(
                connection_string,
                tlsAllowInvalidCertificates=True
            )

            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")

        except:
            detail_error = traceback.format_exc()
            print(f"Erro ao conectar ao banco de dados: {detail_error}")
            log.logger.error(
                f"Erro ao conectar ao banco de dados: {detail_error}")
