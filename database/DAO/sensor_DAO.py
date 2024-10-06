from pymongo import MongoClient
from database import Database
from log import log

class upload_status_sensor:
    def __init__(self):
        self.db = Database('NB-IOT_Gateway', 'equipementDATA')  # Atribui a instância do Database
        
    def upload_0x01_0x02(self, data):
        try:
            # Use self.db.collection.update_one para acessar o método correto da coleção MongoDB
            resultado = self.db.collection.update_one(
                {"_id": "66edf95eeca3507f52f66f4a"},
                {
                    "$push": {
                        "volt": data.volt,
                        "alarmBattery": data.alarmBattery,
                        "level": data.level,
                        "alarmPark": data.alarmPark,
                        "alarmLevel": data.alarmLevel,
                        "alarmMagnet": data.alarmMagnet,
                        "xMagnet": data.xMagnet,
                        "yMagnet": data.yMagnet,
                        "zMagnet": data.zMagnet,
                        "timestamp": data.timestamp,
                        "temperature": data.temperature,
                        "humidity": data.humidity,
                        "RSRP": data.RSRP,
                        "frame_counter": data.frame_counter
                    }
                },
                upsert=True 
            )
            log.logger.info("upload_0x01_0x02 with SUCCESS")
            return resultado
        
        except Exception as e:
            print(f"Ocorreu um erro ao enviar para o MongoDB:\n {e}")
            log.logger.error(f"{type(data)} Error upload_0x01_0x02 : {e}, data: {data}")
            return None
        
    def upload_0x03(self, data):
        try:
            # Use self.db.collection.update_one para acessar o método correto da coleção MongoDB
            resultado = self.db.collection.update_one(
                {"_id": "66edf95eeca3507f52f66f4b"},
                {
                    "$push": {
                        "firmware": data.firmware,
                        "uploadInterval": data.uploadInterval,
                        "detectInterval": data.detectInterval,
                        "levelThreshold": data.levelThreshold,
                        "magnetThreshold": data.magnetThreshold,
                        "batteryThreshold": data.batteryThreshold
                    }
                },
                upsert=True
            )
            log.logger.info("upload_0x03 with SUCCESS")
            return resultado
            
        except Exception as e:
            print(f"Ocorreu um erro ao enviar para o MongoDB:\n {e}")
            log.logger.error(f"Error upload_0x03 : {e}, data: {data}")
            return None