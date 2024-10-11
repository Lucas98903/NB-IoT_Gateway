from services.preference.configuration import Equipmentconfiguration


class ManagerCommand:
    def __init__(self, upload_time=None, height_threshold=None, alarm_battery=None,
                 cycle_detection=None, magnetic_threshold=None, restart_sensor=None,
                 action_serial=None, action_bluetooth=None):
        self.upload_time = upload_time
        self.height_threshold = height_threshold
        self.alarm_battery = alarm_battery
        self.cycle_detection = cycle_detection
        self.magnetic_threshold = magnetic_threshold
        self.restart_sensor = restart_sensor
        self.action_serial = action_serial
        self.action_bluetooth = action_bluetooth

    @staticmethod
    def manager_command(preferences):
        configuration = Equipmentconfiguration()
        codes = []
        out_of_range = []

        if preferences.upload_time:
            code = configuration.set_upload_time(preferences.upload_time)
            if code:
                codes.append(code)
            else:
                out_of_range.append(
                    {'upload_time': f"Value: {preferences.upload_time} - out of range time in hour 01~168 (h)"}
                )

        if preferences.height_threshold:
            code = configuration.set_height_threshold(preferences.height_threshold)
            if code:
                codes.append(code)
            else:
                out_of_range.append(
                    {"height_threshold": f"Value: {preferences.height_threshold} - out of range 5-255 (cm)"}
                )

        if preferences.alarm_battery:
            # Verifique se o método set_alarm_battery existe na classe equipmentConfiguration
            code = configuration.set_battery_alarm(preferences.alarm_battery)
            if code:
                codes.append(code)
            else:
                out_of_range.append(
                    {"alarm_battery": f"Value: {preferences.alarm_battery} - out of range level in percentage 5-99 (%)"}
                )

        if preferences.cycle_detection:
            code = configuration.set_cycle_detection(preferences.cycle_detection)
            if code:
                codes.append(code)
            else:
                out_of_range.append(
                    {"cycle_detection": f"Value: {preferences.cycle_detection} - out of range time in minute 01-60 (min)"}
                )

        if preferences.magnetic_threshold:
            code = configuration.set_magnetic_threshold(preferences.magnetic_threshold)
            if code:
                codes.append(code)
            else:
                out_of_range.append(
                    {"magnetic_threshold": f"Value: {preferences.magnetic_threshold} - out of range magnetic in Gauss 00001 - 655535"}
                )

        if preferences.restart_sensor is not None:
            code = configuration.restart_sensor()
            codes.append(code)

        if preferences.action_serial is not None:
            if preferences.action_serial:
                code = configuration.open_serial()
            else:
                code = configuration.close_serial()

            codes.append(code)

        if preferences.action_bluetooth is not None:
            if preferences.action_bluetooth:
                code = configuration.open_bluetooth()
            else:
                code = configuration.close_bluetooth()

            codes.append(code)

        return codes, out_of_range
