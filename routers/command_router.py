from fastapi import APIRouter

from services.preference.configuration import equipmentConfiguration
from model.commands import preferences

@app.post("/items/")
async def create_item(preferences: preferences):

    return None

