from fastapi import APIRouter

from controller.controller_comand import managerCommand
from services.preference.configuration import equipmentConfiguration
from model.commands import preferences

from pydantic import BaseModel

router = APIRouter()

@router.post("/preferences")
async def create_item(preferences: preferences):
    managerCommand(preferences)
    return None
