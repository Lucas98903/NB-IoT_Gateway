import time
import socket
import traceback

from decode.do201 import DO201
from database.DAO import updatedDAO
from log import log

interpretedData = ""
equipmentIMEI = ""

def handle(client, address):
    try:
        global interpretedData
        global equipmentIMEI
        
        client.settimeout(30)
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

        try:
            str_subreq = str(request_str[int(start):int(end + 2)])
            log.logger.info(str_subreq)
            response = DO201.parse_data_DO201(str_subreq.strip().upper()) 
            
            if response:
                data_type, interpretedData, equipmentIMEI = response
                
            else:
                raise Exception("Problem doing when decoding hexadecimal!")

            print(f"Data interpreted: {interpretedData}")
            log.logger.info(f"Data interpreted: {interpretedData}")
            
        except:
            detail_error = traceback.format_exc()
            log.logger.error(f"Error while decode: {detail_error}")
            print(detail_error)
            log.logger.info(detail_error)
            client.close()
            return None

        #====================- MongoDB -==============================
        response = None
        if data_type == 1:
            response = updatedDAO.upload_0x01_0x02(interpretedData)
        elif data_type == 3:
            response = updatedDAO.upload_0x03(interpretedData)
        
        if response:
            print(f'Documento inserido com ID: {response}')
            log.logger.info(f"Uploaded to MongoDB")

        else:
            log.logger.error(f"Data not sent to the database. 'response' not defined!")
            client.close()
            log.logger.info("")
            return None
        #==================================================
        
        time.sleep(1)
        client.close()
        time.sleep(1)
        log.logger.info("close device connection. With SUCESS!!!")
        log.logger.info("")
        
    except socket.timeout:
        print("time out")
        log.logger.warning("Time out")
        log.logger.info("")
        client.close()
        return None
    