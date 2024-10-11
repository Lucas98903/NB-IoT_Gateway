from fastapi import APIRouter

from controller.controller_comand import managerCommand
from services.preference.configuration import Equipmentconfiguration
from model.commands import Preferences

from pydantic import BaseModel

router = APIRouter()


@router.post("/preferences")
async def create_item(preferences: Preferences):
    managerCommand(preferences)
    return None
