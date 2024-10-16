from services.preference.configuration import EquipmentConfiguration
from services.memory.memory import Memory
from model.commands import OutRange


class ManagerCommand:
    def __init__(self):
        self.address_memory_code = str(r"services\memory\data\code.json")
        self.address_memory_return = str(r"services\memory\data\return_code.json")
        self.address_memory_alarm_park = str(r"services\memory\data\alarm_park.json")
        self.memory = Memory()

        self.upload_time = None
        self.height_threshold = None
        self.alarm_battery = None
        self.cycle_detection = None
        self.magnetic_threshold = None
        self.restart_sensor = None
        self.action_serial = None
        self.action_bluetooth = None
        self.imei = None

    def _assembler_command(self):
        configuration = EquipmentConfiguration()
        codes = []
        out_of_range = {}
        if self.upload_time:
            code = configuration.set_upload_time(self.upload_time)
            if code:
                codes.append(code)
                out_of_range["upload_time"] = "OK"
            else:
                out_of_range["upload_time"] = (
                    f"Value: {
                self.upload_time} - out of range time in hour 01~168 (h)"
                )
        else:
            out_of_range["upload_time"] = "N/A"

        if self.height_threshold:
            code = configuration.set_height_threshold(self.height_threshold)
            if code:
                codes.append(code)
                out_of_range["height_threshold"] = "OK"
            else:
                out_of_range["height_threshold"] = (
                    f"Value: {
                self.height_threshold} - out of range 5-255 (cm)"
                )
        else:
            out_of_range["height_threshold"] = "N/A"

        if self.alarm_battery:
            code = configuration.set_battery_alarm(self.alarm_battery)
            if code:
                codes.append(code)
                out_of_range["alarm_battery"] = "OK"
            else:
                out_of_range["alarm_battery"] = (
                    f"Value: {
                self.alarm_battery} - out of range level in percentage 5-99 (%)"
                )
        else:
            out_of_range["alarm_battery"] = "N/A"

        if self.cycle_detection:
            code = configuration.set_cycle_detection(self.cycle_detection)
            if code:
                codes.append(code)
                out_of_range["cycle_detection"] = "OK"
            else:
                out_of_range["cycle_detection"] = (
                    f"Value: {
                self.cycle_detection} - out of range time in minute 01-60 (min)"
                )
        else:
            out_of_range["cycle_detection"] = "N/A"

        if self.magnetic_threshold:
            code = configuration.set_magnetic_threshold(self.magnetic_threshold)
            if code:
                codes.append(code)
                out_of_range["magnetic_threshold"] = "OK"
            else:
                out_of_range["magnetic_threshold"] = (
                    f"Value: {
                self.magnetic_threshold} - out of range magnetic in Gauss 00001 - 655535"
                )
        else:
            out_of_range["magnetic_threshold"] = "N/A"

        if self.restart_sensor is not None:
            code = configuration.restart_sensor()
            codes.append(code)
            out_of_range["restart_sensor"] = "OK"
        else:
            out_of_range["restart_sensor"] = "N/A"

        if self.action_serial is not None:
            if self.action_serial:
                code = configuration.open_serial()
            else:
                code = configuration.close_serial()

            codes.append(code)
            out_of_range["action_serial"] = "OK"
        else:
            out_of_range["action_serial"] = "N/A"

        if self.action_bluetooth is not None:
            if self.action_bluetooth:
                code = configuration.open_bluetooth()
            else:
                code = configuration.close_bluetooth()

            out_of_range["action_bluetooth"] = "OK"
            codes.append(code)
        else:
            out_of_range["action_bluetooth"] = "N/A"

        object_range = OutRange(
            upload_time=self.out_of_range["upload_time"],
            height_threshold=self.out_of_range["height_threshold"],
            alarm_battery=self.out_of_range["alarm_battery"],
            cycle_detection=self.out_of_range["cycle_detection"],
            magnetic_threshold=self.out_of_range["magnetic_threshold"],
            restart_sensor=self.out_of_range["restart_sensor"],
            action_serial=self.out_of_range["action_serial"],
            action_bluetooth=self.out_of_range["restart_sensor"],
            imei=self.imei,
        )

        return object_range, codes

    def _manager_command(self):
        object_range, codes = self._assembler_command()

        if len(codes) > 0:
            self.memory.storage_data(self.codes, self.address_memory_code)

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

        return self._manager_command()

    def get_status_preferences(self):
        return self.memory.get_data(self.address_memory_return)

    def get_adress(self):
        return (
            self.address_memory_code,
            self.address_memory_return,
            self.address_memory_alarm_park,
        )
