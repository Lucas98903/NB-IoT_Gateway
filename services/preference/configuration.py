import socket
import traceback

from services.decode.do201 import DO201
from log import log
import time

'''
Amostra do feedback esperado do sensor:
firmware='1.2', uploadInterval=24, detectInterval=5, levelThreshold=60, magnetThreshold=60, batteryThreshold=20, ip='120.92.89.122', port=9090
'''

class equipmentConfiguration():
    def __init__(self,):
        self.start_packet = '80029999'
        self.end_packet = '81'
    
    def _send_to_equipment(self, command):
        start = int(-1)
        end = int(-1)
        counter = 0
        
        preference = bytes.fromhex(command)
        # Create socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                while True:
                    counter += 1
                    
                    # Connect device
                    s.connect((self.equipment_ip, self.equipment_port))
                    print(f"Conectado a {self.equipment_ip}:{self.equipment_port}")

                    # send command
                    s.sendall(preference)
                    print("Comando enviado!")

                    # Receives response from equipment
                    request_bytes = s.recv(1024)
                    request_str = request_bytes.hex()
                    
                    start = str(request_str).find("8000")
                    end = str(request_str).find("81")
        
                    if start != -1:
                        print(f"Resposta recebida: {request_str}")
                        break
                    
                    time.sleep(1)
                    if counter >= 10:
                        log.logger.critical("Not recept hexadecimal")
                        return None        
            except:
                detail_error = traceback.format_exc()
                print(f"Error connecting or sending command: \n DETAIL ERROR: \n{detail_error}")
                log.logger.error(f"Error connecting or sending command: \n DETAIL ERROR: \n{detail_error}")
                return None

            str_subreq = str(request_str[int(start):int(end + 2)])
            response = DO201.parse_data_DO201(str_subreq.strip().upper())

            return response
    
    def set_upload_time(self, time):
        # Time in hours 01-168 (h)
        if 1 <= int(time) <= 168:
            hexadecimal = str(hex(int(time)))[2:4].upper()
            command = str(self.start_packet + '01' + hexadecimal + self.end_packet)            
            response = self._send_to_equipment(command)
            return response
        
        else:
            return None
    
    def set_height_Threshold(self, height):
        # Heigh in centimeter 5-255 (cm)
        if 15 <= int(height) <= 255:
            hexadecimal = str(hex(int(height)))[2:4].upper()
            command = str(self.start_packet + '02' + hexadecimal + self.end_packet)            
            response = self._send_to_equipment(command)
            return response
        
        else:
            return None
        
    def set_battery_alarm(self, level):
        # level in percentual 5-99 (%)
        if 5 <= int(level) <= 99:
            hexadecimal = str(hex(int(level)))[2:4].upper()
            command = str(self.start_packet + '05' + hexadecimal + self.end_packet)            
            response = self._send_to_equipment(command)
            return response
        
        else:
            return None
    
    def set_cycle_detection(self, time):
        # time in minute 01-60 (min)
        if 1 <= int(time) <= 60:
            hexadecimal = str(hex(int(time)))[2:4].upper()
            command = str(self.start_packet + '08' + hexadecimal + self.end_packet)            
            response = self._send_to_equipment(command)
            return response
        
        else:
            return None
    
    def set_magnetic_threshold(self, Gauss):
        # magnetic in Gauss 00001 - 655535
        if 1 <= int(Gauss) < 655535:
            hexadecimal = str(hex(int(Gauss)))[2:4].upper()
            command = str(self.start_packet + '0F' + hexadecimal + self.end_packet)            
            response = self._send_to_equipment(command)
            return response
        
        else:
            return None

#=================Experimental==============
    def restart_sensor(self):
        command = str('80029999090281')
        response = self._send_to_equipment(command)
        return response
    
    def open_serial(self):
        command = str('80029999090B81')
        response = self._send_to_equipment(command)
        return response
    
    def close_serial(self):
        command = str('80029999090C81')
        response = self._send_to_equipment(command)
        return response
        
    def open_bluetooth(self):
        command = str('80029999091281')
        response = self._send_to_equipment(command)
        return response
        
    def close_bluetooth(self):
        command = str('80029999091181')
        response = self._send_to_equipment(command)
        return response
#==========================================

    '''
        Configuração das APN e Portas nao estão programadas
    '''
