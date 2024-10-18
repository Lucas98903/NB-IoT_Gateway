import json
from pydantic import BaseModel
from datetime import datetime

class Memory:
    def __init__(self):
        self.data = None
        self.address = None

    def storage_data(self, data, address):
        # Verifica se o dado é uma instância de BaseModel (Pydantic) e converte para dicionário
        if isinstance(data, BaseModel):
            data = data.dict()

        # Função recursiva para converter datetime para string no formato ISO 8601
        def convert_datetime(item):
            if isinstance(item, dict):
                return {k: convert_datetime(v) for k, v in item.items()}
            elif isinstance(item, list):
                return [convert_datetime(v) for v in item]
            elif isinstance(item, datetime):
                return item.isoformat()
            else:
                return item  # Retorna o valor sem modificação se não for datetime

        # Converte apenas se houver datetime
        data = convert_datetime(data)

        # Salva os dados no arquivo
        with open(address, "w") as file:
            json.dump(data, file)

    def get_data(self, address):
        try:
            with open(address, "r") as file:
                read = json.load(file)
            return read
        except FileNotFoundError:
            return None
