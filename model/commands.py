from pydantic import BaseModel


class preferences(BaseModel):
    upload_time: int = None
    alarmBattery: int = None
    height_threshold: int = None
    battery_alarm: int = None
    cycle_detection: int = None
    magnetic_threshold: int = None
    restart_sensor: bool = None 
    action_serial: bool = None 
    action_bluetooth: bool = None 
