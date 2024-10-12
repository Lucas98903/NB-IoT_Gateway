from services.preference.configuration import Equipmentconfiguration
from services.memory.memory import Memory
from model.commands import Preferences

class ManagerCommand:
    def __init__(self, preferences):
        self.address_memory = str(r'services\memory\data')
        self.out_of_range = {}
        self.codes = []
        self.memomry = Memory()

    def _assembler_command(self):
        configuration = Equipmentconfiguration()
        self.codes = []

        if self.upload_time:
            code = configuration.set_upload_time(self.upload_time)
            if code:
                self.codes.append(code)
                self.out_of_range = {"upload_time": "OK"}
            else:
                self.out_of_range = {
                    "upload_time": f"Value: {self.upload_time} - out of range time in hour 01~168 (h)"
                }
        else:
                self.out_of_range = {"upload_time": "N/A"}

        if self.height_threshold:
            code = configuration.set_height_threshold(self.height_threshold)
            if code:
                self.codes.append(code)
                self.out_of_range = {"height_threshold": "OK"}
            else:
                self.out_of_range = {"height_threshold":
                                f"Value: {self.height_threshold} - out of range 5-255 (cm)"
                                     }
        else:
            self.out_of_range = {"height_threshold": "N/A"}

        if self.alarm_battery:
            code = configuration.set_battery_alarm(self.alarm_battery)
            if code:
                self.codes.append(code)
                self.out_of_range = {"alarm_battery": "OK"}
            else:
                self.out_of_range = {
                    "alarm_battery": f"Value: {self.alarm_battery} - out of range level in percentage 5-99 (%)"
                }
        else:
            self.out_of_range = {"alarm_battery": "N/A"}
            
        if self.cycle_detection:
            code = configuration.set_cycle_detection(self.cycle_detection)
            if code:
                self.codes.append(code)
                self.out_of_range = {"cycle_detection": "OK"}
            else:
                self.out_of_range = {
                    "cycle_detection": f"Value: {self.cycle_detection} - out of range time in minute 01-60 (min)"
                }
        else:
            self.out_of_range = {"cycle_detection": "N/A"}

        if self.magnetic_threshold:
            code = configuration.set_magnetic_threshold(self.magnetic_threshold)
            if code:
                self.codes.append(code)
                self.out_of_range = {"magnetic_threshold": "OK"}
            else:
                self.out_of_range = {
                    "magnetic_threshold": f"Value: {self.magnetic_threshold} - out of range magnetic in Gauss 00001 - 655535"
                }
        else:
            self.out_of_range = {"magnetic_threshold": "N/A"}

        if self.restart_sensor is not None:
            code = configuration.restart_sensor()
            self.codes.append(code)
            self.out_of_range = {"restart_sensor": "OK"}
        else:
            self.out_of_range = {"restart_sensor": "N/A"}

        if self.action_serial is not None:
            if self.action_serial:
                code = configuration.open_serial()
            else:
                code = configuration.close_serial()

            self.codes.append(code)
            self.out_of_range = {"action_serial": "OK"}
        else:
            self.out_of_range = {"action_serial": "N/A"}


        if self.action_bluetooth is not None:
            if self.action_bluetooth:
                code = configuration.open_bluetooth()
            else:
                code = configuration.close_bluetooth()
            
            self.out_of_range = {"action_bluetooth": "OK"}
            self.codes.append(code)
        else:
            self.out_of_range = {"action_bluetooth": "N/A"}

        object_range = Preferences(
            upload_time = self.out_of_range["upload_time"],
            height_threshold = self.out_of_range["height_threshold"],
            alarm_battery = self.out_of_range["alarm_battery"],
            cycle_detection = self.out_of_range["cycle_detection"],
            magnetic_threshold = self.out_of_range["magnetic_threshold"],
            restart_sensor = self.out_of_range["restart_sensor"],
            action_serial = self.out_of_range["action_serial"],
            action_bluetooth = self.out_of_range["restart_sensor"],
            imei = self.imei
        )

        return object_range

    def insert_object(self, preferences):
        self.upload_time = preferences.upload_time
        self.height_threshold = preferences.height_threshold
        self.alarm_battery = preferences.alarm_battery
        self.cycle_detection = preferences.cycle_detection
        self.magnetic_threshold = preferences.magnetic_threshold
        self.restart_sensor = preferences.restart_sensor
        self.action_serial = preferences.action_serial
        self.action_bluetooth = preferences.action_bluetooth
        self.imei = preferences.imei

    def manager_command(self):
        object_range = self._assembler_command()

        if len(self.codes) > 0:
            self.memomry.store(self.codes)
            self.memomry.save(self.address_memory)
        
        return object_range

    def get_adress(self):
        return self.address_memory
