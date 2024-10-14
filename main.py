from fastapi import FastAPI
import asyncio
from routers.command_router import router as command_router
from server.scan import scanner

app = FastAPI()

# Iniciando o scanner como uma tarefa assíncrona
@app.on_event("startup")
async def start_scanner():
    asyncio.create_task(scanner())

# Incluindo o router
app.include_router(
    command_router, prefix='/command'
)

@app.get("/")
async def read_root():
    return {"message": "Hello dear"}
