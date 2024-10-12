from pydantic import BaseModel


class Preferences(BaseModel):
    upload_time: int = None
    alarm_battery: int = None
    height_threshold: int = None
    battery_alarm: int = None
    cycle_detection: int = None
    magnetic_threshold: int = None
    restart_sensor: bool = None
    action_serial: bool = None
    action_bluetooth: bool = None
    imei: int = None


class OutRange(BaseModel):
    upload_time: str = None
    height_threshold: str = None
    alarm_battery: str = None
    cycle_detection: str = None
    magnetic_threshold: str = None
    restart_sensor: str = None
    action_serial: str = None
    action_bluetooth: str = None
    imei: int = None
