import time
import socket

import decode.do201 as do201
from database.DAO import updatedDAO
from log import log

interpretedData = ""
equipmentIMEI = ""

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
            
            if start != -1 and end != -1:
                print(request_str)
                break
            
        try:
            str_subreq = str(request_str[int(start):int(end + 2)])
            data_type, interpretedData, equipmentIMEI = do201.DO201.parse_data_DO201(str_subreq.strip().upper()) 
            print("Data interpreted"+interpretedData+
                  "\n IMEI of equipment is "+equipmentIMEI)
            log.logger.info(f"Data interpreted-> {interpretedData} IMEI of equipment is {equipmentIMEI}")
        
        except Exception as e:
            log.logger.error(f"Error while decode: {e}")
            client.close()
            return None
    
        #====================- MongoDB -==============================
        resultado = None
        if data_type == 1:
            resultado = updatedDAO.upload_0x01_0x02(interpretedData)
        elif data_type == 3:
            resultado = updatedDAO.upload_0x03(interpretedData)
            
        if resultado:
            print(f'Documento inserido com ID: {resultado.inserted_id}')
        else:
            client.close()
            return None
        #==================================================
        
        time.sleep(1)
        client.close()
        time.sleep(1)
        log.logger.debug("close device connection")
    except socket.timeout:
        print("time out")
        client.close()
        return None