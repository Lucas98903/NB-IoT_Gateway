from fastapi import FastAPI

import threading
import traceback

from services.receiver.scan import scanner
from log import log

thread = threading.Thread(target=scanner)
thread.start()

app = FastAPI()



