from fastapi import APIRouter

from controller.controller_comand import ManagerCommand
from model.commands import Preferences

router = APIRouter()
manager = ManagerCommand()


@router.post("/preferences")
async def create_item(preferences: Preferences):
    return manager.insert_object(preferences)


@router.get("/status-configuration")
def get_status_preferences():
    return manager.get_status_preferences()
