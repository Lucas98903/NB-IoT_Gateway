from fastapi import APIRouter

from controller.controller_comand import ManagerCommand
from services.preference.configuration import Equipmentconfiguration
from model.commands import Preferences

from pydantic import BaseModel


router = APIRouter()
manager = ManagerCommand()

@router.post("/preferences")
async def create_item(preferences: Preferences):
    #ajustar melhor essa parte
    manager.insert_object(preferences)
    out_of_range = manager.manager_command()

    return out_of_range
