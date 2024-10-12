"""
Amostra do feedback esperado do sensor:
firmware='1.2', 
uploadInterval=24,
detectInterval=5,
levelThreshold=60, 
magnetThreshold=60, 
batteryThreshold=20, 
ip='120.92.89.122', 
port=9090
"""


class EquipmentConfiguration:
    def __init__(self):
        self.start_packet = '80029999'
        self.end_packet = '81'

    def set_upload_time(self, time):
        # Time in hours 01-168 (h)
        if 1 <= int(time) <= 168:
            hexadecimal = str(hex(int(time)))[2:4].upper()
            command = str(self.start_packet + '01' +
                          hexadecimal + self.end_packet)
            return command

        else:
            return None

    def set_height_threshold(self, height):
        # Heigh in centimeter 5-255 (cm)
        if 15 <= int(height) <= 255:
            hexadecimal = str(hex(int(height)))[2:4].upper()
            command = str(self.start_packet + '02' +
                          hexadecimal + self.end_packet)
            return command

        else:
            return None

    def set_battery_alarm(self, level):
        # level in percentual 5-99 (%)
        if 5 <= int(level) <= 99:
            hexadecimal = str(hex(int(level)))[2:4].upper()
            command = str(self.start_packet + '05' +
                          hexadecimal + self.end_packet)
            return command

        else:
            return None

    def set_cycle_detection(self, time):
        # time in minute 01-60 (min)
        if 1 <= int(time) <= 60:
            hexadecimal = str(hex(int(time)))[2:4].upper()
            command = str(self.start_packet + '08' +
                          hexadecimal + self.end_packet)
            return command

        else:
            return None

    def set_magnetic_threshold(self, gauss):
        # magnetic in Gauss 00001 - 655535
        if 1 <= int(gauss) < 655535:
            hexadecimal = str(hex(int(gauss)))[2:4].upper()
            command = str(self.start_packet + '0F' +
                          hexadecimal + self.end_packet)
            return command

        else:
            return None

    # =================Experimental==============
    @staticmethod
    def restart_sensor():
        command = str('80029999090281')
        return command

    @staticmethod
    def open_serial():
        command = str('80029999090B81')
        return command

    @staticmethod
    def close_serial():
        command = str('80029999090C81')
        return command

    @staticmethod
    def open_bluetooth():
        command = str('80029999091281')
        return command

    @staticmethod
    def close_bluetooth():
        command = str('80029999091181')
        return command

    # ==========================================

    '''
        Configuração das APN e Portas nao estão programadas
    '''
