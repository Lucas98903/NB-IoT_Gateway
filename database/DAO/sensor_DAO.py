import traceback
from database import Database
from log import log


class UploadStatusSensor:
    def __init__(self):
        # Atribui a instância do Database
        self.db = Database('NB-IOT_Gateway', 'equipementDATA')

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

        except:
            detail_error = traceback.format_exc()
            print(f"Ocorreu um erro ao enviar para o MongoDB:\n {detail_error}")
            log.logger.error(f"{type(data)} Error upload_0x01_0x02 {detail_error}, \n data: {data}")
            return None

    def upload_0x03(self, data):
        try:
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

        except:
            detail_error = traceback.format_exc()
            print(f"Ocorreu um erro ao enviar para o MongoDB:\n {detail_error}")
            log.logger.error(f"{type(data)} Error upload_0x01_0x03 : {detail_error}, \n data: {data}")
            return None
