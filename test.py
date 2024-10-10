from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Define um modelo Pydantic para os dados que serão enviados no POST
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Rota POST que recebe dados de um 'Item'
@app.post("/items/")
async def create_item(item: Item):
    print(item)
    return {
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "tax": item.tax
    }

