import json
from pydantic import BaseModel

class Memory:
    def __init__(self):
        self.data = None
        self.address = None

    def storage_data(self, data, address):
        if isinstance(data, BaseModel):
            data = data.dict()
            
        with open(address, "w") as file:
            json.dump(data, file)

    def get_data(self, address):
        try:
            with open(address, "r") as file:
                read = json.load(file)
            return read
        except FileNotFoundError:
            return None
        