from pydantic import BaseModel
from datetime import datetime
from typing import Any


class data_0X01_0X02(BaseModel):
    volt: float
    alarmBattery: bool
    level: int
    alarmPark: bool
    alarmLevel: bool
    alarmMagnet: bool
    xMagnet: int
    yMagnet: int
    zMagnet: int
    timestamp: datetime  
    temperature: int  
    humidity: int                     
    RSRP: Any      
    frame_counter: int
    
class data_0X03(BaseModel):
    firmware: Any | None = None
    uploadInterval: Any | None = None
    detectInterval: Any | None = None
    levelThreshold: Any | None = None
    magnetThreshold: Any | None = None
    batteryThreshold: Any | None = None