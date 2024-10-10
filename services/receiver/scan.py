import socket
import threading
import traceback

from log import log
from controller.handle_client import handle

port_number = 810
max_clients = 10

def scanner():
    try:
        interpretedData = ""
        token_deviceid = ""

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", port_number))
        server_socket.listen(max_clients)
        
        while True:
            print("Waiting Connection")
            client_socket, client_address = server_socket.accept()
            print(f"=======- {str(client_address)} user connected! -=======")
            print(f"Socket: {client_socket}")
            log.logger.info(f"=======- {str(client_address)} user connected! -=======")
            thread = threading.Thread(
                target=handle, args=(client_socket, client_address)
            )
            thread.start()
            log.logger.debug("=======- after handle_client_process close! -=======")
            
    except:
        detail_error = traceback.format_exc()
        log.logger.error(f"Error while decode: {detail_error}")
        print(detail_error)
        print("Process iterruption!")        
