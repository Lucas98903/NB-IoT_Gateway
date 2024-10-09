import time
import socket
import traceback
import threading

from services.decode.do201 import DO201
from database.DAO import updatedDAO
from log import log


interpretedData = ""
equipmentIMEI = ""

'''
Possivel problema!

Recebe o dado do equipamente, faz o decode e depois envia para o MongoDB (Banco de dados)

E se o tempo do decode estou o tempo do banco de dados?
'''


def upload(data, data_type):
    response = None
    if data_type == 1:
        response = updatedDAO.upload_0x01_0x02(data)
        
    elif data_type == 3:
        response = updatedDAO.upload_0x03(data)
    
    if response:
        print(f'Documento inserido com ID: {response}')

    else:
        print(f"Data not sent to the database. 'response' not defined!")
        log.logger.error(f"Data not sent to the database. 'response' not defined!")
    
    return None


#"address" será usado caso o código receba dado de mais de um equipamento.
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

        #====================- MongoDB -==============================
        thread = threading.Thread(
            target=upload, args=(interpretedData, data_type)
        )
        thread.start()
        #==================================================
        
        time.sleep(1)
        client.close()
        time.sleep(1)
        log.logger.info("")
        print("Finish")
        
    except socket.timeout:
        print("Time out or bug occurred")
        log.logger.warning("Time out or bug occurred")
        log.logger.info("")
        client.close()
        return None
    