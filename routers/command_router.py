from fastapi import APIRouter

from controller.controller_comand import ManagerCommand
from model.commands import Preferences

router = APIRouter()
manager = ManagerCommand()


@router.post("/preferences")
async def create_item(preferences: Preferences):
    out_of_range = manager.insert_object(preferences)
    return out_of_range
