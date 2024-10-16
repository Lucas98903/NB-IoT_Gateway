from fastapi import APIRouter

from controller.controller_comand import ManagerCommand
from model.commands import Preferences

router = APIRouter()
manager = ManagerCommand()


@router.get("/status_park")
def get_status_alarm_park():
    return manager.get_status_park()

