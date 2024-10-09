import socket
import traceback

from services.decode.do201 import DO201
from log import log

'''
Ver como progedir aqui
'''

ip = 'COLOCAR UM IP'
port = 8000






class equipmentConfiguration():
    def __init__(self, ip, port):
        self.start_packet = '80029999'
        self.end_packet = '81'
        self.equipment_ip = ip
        self.equipment_port = port
    '''
    Amostra do feedback esperado do sensor:
    firmware='1.2', uploadInterval=24, detectInterval=5, levelThreshold=60, magnetThreshold=60, batteryThreshold=20, ip='120.92.89.122', port=9090
    '''
    
    def _send_to_equipment(self, command):
        preference = bytes.fromhex(command)
        # Create socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                # Connect device
                s.connect((self.equipment_ip, self.equipment_port))
                print(f"Conectado a {self.equipment_ip}:{self.equipment_port}")

                # send command
                s.sendall(preference)
                print("Comando enviado!")

                # Receber a resposta (caso o dispositivo envie)
                request_bytes = s.recv(1024)
                request_str = request_bytes.hex()
                
                start = str(request_str).find("8000")
                end = str(request_str).find("81")
            
                print(f"Resposta recebida: {request_str}")

            except:
                detail_error = traceback.format_exc()
                print(f"Erro ao conectar ou enviar comando: {detail_error}")
                log.logger.error(f"Erro ao conectar ou enviar comando: {detail_error}")
    
    def set_upload_time(self, time):
        # Time in hours 01-24 (h)
        if 1 <= int(time) <= 24:
            hexadecimal = str(hex(int(time)))[2:4].upper()
            command = str(self.start_packet + '01' + hexadecimal + self.end_packet)            
            return command
        
        else:
            return None
    
    def set_height_Threshold(self, height):
        # Heigh in centimeter 5-255 (cm)
        if 15 <= int(height) <= 255:
            hexadecimal = str(hex(int(height)))[2:4].upper()
            command = str(self.start_packet + '02' + hexadecimal + self.end_packet)            
            return command
        
        else:
            return None
        
    def set_battery_alarm(self, level):
        # level in percentual 5-99 (%)
        if 5 <= int(level) <= 99:
            hexadecimal = str(hex(int(level)))[2:4].upper()
            command = str(self.start_packet + '05' + hexadecimal + self.end_packet)            
            return command
        
        else:
            return None
    
    def set_cycle_detection(self, time):
        # time in minute 01-60 (min)
        if 1 <= int(time) <= 60:
            hexadecimal = str(hex(int(time)))[2:4].upper()
            command = str(self.start_packet + '08' + hexadecimal + self.end_packet)            
            return command
        
        else:
            return None
    
    def set_magnetic_threshold(self, Gauss):
        # magnetic in Gauss 00001 - 655535
        if 1 <= int(Gauss) < 655535:
            hexadecimal = str(hex(int(Gauss)))[2:4].upper()
            command = str(self.start_packet + '0F' + hexadecimal + self.end_packet)            
            return command
        
        else:
            return None

    '''
        Configuração das APN e Portas nao estão programadas
    '''


#=================Experimental==============
    def restart_sensor(self):
        command = str('80029999090281')
    
    def open_serial(self):
        command = str('80029999090B81')
    
    def close_serial(self):
        command = str('80029999090C81')
        
    def open_bluetooth(self):
        command = str('80029999091281')
        
    def close_bluetooth(self):
        command = str('80029999091181')
#==========================================
    
    
    # 0x09 Reboot/Open debug mode
    
    
    
    pass
    
    
    


