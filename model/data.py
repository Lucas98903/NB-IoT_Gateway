from pydantic import BaseModel
from datetime import datetime
from typing import Any


class Data0x010x02(BaseModel):
    volt: float
    alarmBattery: int
    level: int
    alarmPark: int
    alarmLevel: int
    alarmMagnet: int
    xMagnet: int
    yMagnet: int
    zMagnet: int
    timestamp: datetime
    temperature: int
    humidity: int
    RSRP: int
    frame_counter: int


class Data0x03(BaseModel):
    firmware: Any | None = None
    uploadInterval: Any | None = None
    detectInterval: Any | None = None
    levelThreshold: Any | None = None
    magnetThreshold: Any | None = None
    batteryThreshold: Any | None = None
    ip: Any | None = None
    port: Any | None = None
    time: str | None = None
