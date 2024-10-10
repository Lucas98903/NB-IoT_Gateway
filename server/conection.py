import time
import socket
import traceback
import threading

from services.upload.uploader import upload
from services.decode.do201 import DO201
from database.DAO import updatedDAO
from log import log

'''
-Vai ser chamado sempre que a varredura detectar uma conexão
-Depois de ser chamado vai ler o dado recebido e enviar para controller_client em paralelo

'''


class handle():
    def __init__(self):
        self.timeout = int(59)

    def _receive_data(self, client):
        counter = 10
        start = int(-1)
        end = int(-1)
        while True:
            counter += 1

            if not client._closed:
                request_bytes = request_bytes + client.recv(1024)
                
            request_str = request_bytes.hex()
            start = str(request_str).find("8000")
            end = str(request_str).find("81")

            if start != -1 and end != -1:
                print(request_str)
                return str(request_str[int(start):int(end + 2)])
        
            if counter >= 10:
                return None

    def set_preferences(self, codes):
        pass


    def connection(self, client, command):
        self.request_bytes = b""
        self.request_str = ""
        
        client.settimeout(self.timeout)

        try:
            str_subreq = self._receive_data(client)
            try:
                response = DO201.parse_data_DO201(str_subreq.strip().upper()) 
                
                if response:
                    data_type, interpretedData, equipmentIMEI = response
                    upload(interpretedData, data_type)
                else:
                    raise Exception("Problem doing when decoding hexadecimal!")
                
            except:
                print()
                detail_error = traceback.format_exc()
                log.logger.error(f"Error while decode: {detail_error}")
                print(detail_error)
                log.logger.info("")
                client.close()
                return None

        except socket.timeout:
            print("Time out occurred")
            log.logger.warning("TIMEOUT occurred")
            log.logger.info("")
            client.close()
            return None






def handle(client, address):
    try:
        global interpretedData
        global equipmentIMEI
        
        client.settimeout(10)
        request_bytes = b""
        request_str = ""
        start = int(-1)
        end = int(-1)
        
        while True:
            if not client._closed:
                request_bytes = request_bytes + client.recv(1024)
                
            if not request_bytes:
                break
            
            request_str = request_bytes.hex()
            start = str(request_str).find("8000")
            end = str(request_str).find("81")

            if start != -1:
                print(request_str)
                break
    except:
        pass
    
    try:
        str_subreq = str(request_str[int(start):int(end + 2)])
        response = DO201.parse_data_DO201(str_subreq.strip().upper()) 
        
        if response:
            data_type, interpretedData, equipmentIMEI = response
            
        else:
            raise Exception("Problem doing when decoding hexadecimal!")

        print(f"Data interpreted: {interpretedData}")
    except:
            print()
            detail_error = traceback.format_exc()
            log.logger.error(f"Error while decode: {detail_error}")
            print(detail_error)
            log.logger.info("")
            print()
            client.close()
            return None