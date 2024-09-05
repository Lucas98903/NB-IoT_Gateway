# Gateway for URBAN-EVO sensor NB-IoT version gateway
# change log Sep 02, 2024. change the created threading not close automatically.
# coding: utf-8

import socket
import threading
import time
import decode.do201 as do201
from pymongo import MongoClient

#Chave do banco de dados
client = MongoClient("mongodb+srv://Rick98903:28465chaos@cluster0.ryq35.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client['NB-IOT_Gateway']
colecao = db['equipementDATA']


from log.Logger import Logger

port_number = 810
max_clients = 10
interpretedData = ""
equipmentIMEI = ""

log = Logger(r"log\all.log", level="debug")

def handle_client(client, address):
    try:
        client.settimeout(10)
        request_bytes = b""
        global interpretedData
        request_str = ""
        global equipmentIMEI
        start = int(-1)
        end = int(-1)
        while True:
            if not client._closed:
                request_bytes = request_bytes + client.recv(1024)
            if not request_bytes:
                break
            request_str = request_bytes.hex()
            start = str(request_str).find("8000") #Começa a transmissão
            end = str(request_str).find("81") #Finaliza transmissão
            if start != -1 and end != -1:
                print(request_str) #Mosta o HEX no terminal
                break
            
        try:
            str_subreq = str(request_str[int(start):int(end + 2)]) #Ajusta a a informacao
            interpretedData, equipmentIMEI = do201.DO201.parse_data_DO201(str_subreq.strip().upper()) #Faz o DECODE dos dados
        except Exception as e:
            log.logger.error(f"Error while decode: {e}")
            client.close()
            return None
        
        print("Data interpreted"+interpretedData+" IMEI of equipment is "+equipmentIMEI)
        log.logger.info(f"Data interpreted-> {interpretedData} IMEI of equipment is {equipmentIMEI}")
        
        #T==================================================
        try:
            resultado = colecao.insert_one(interpretedData)
            print(f'Documento inserido com ID: {resultado.inserted_id}')
        except Exception as e:
            print(f"Ocorreu um erro ao subir no MONGODB-> {e}")
        #T==================================================
        
        
        
        time.sleep(1)
        client.close()
        time.sleep(1)
        log.logger.debug("close device connection")
    except socket.timeout:
        print("time out")
        client.close()


if __name__ == "__main__":
    try:
        interpretedData = ""
        
        ###Criação do SOCKET
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", port_number))
        server_socket.listen(max_clients)
        
        while True:
            print("Waiting Connection")
            client_socket, client_address = server_socket.accept()
            log.logger.info(f"=======- {str(client_address)} user connected! -=======")
            thread = threading.Thread(
                target=handle_client, args=(client_socket, client_address)
            )
            thread.start()
            log.logger.debug("=======- after handle_client_process close! -=======")
    except Exception as e:
        print(e)
        log.logger.error(e)
