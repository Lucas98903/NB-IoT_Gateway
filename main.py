from fastapi import FastAPI

import threading
import traceback

from routers import command_router
from routers.command_router import router as command_router
from server.scan import scanner


thread = threading.Thread(target=scanner)
thread.start()

app = FastAPI()

app.include_router(
    command_router, prefix='/command'
)

app.get("/")


def read_root():
    return {"message": "Hello dear"}
