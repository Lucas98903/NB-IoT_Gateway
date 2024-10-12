class Item(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    quantidade: int

print(len(Item))