import socket
import threading

from log import log
from handle.handle_client import handle

port_number = 810
max_clients = 10

if __name__ == "__main__":
    try:
        interpretedData = ""
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", port_number))
        server_socket.listen(max_clients)
        
        while True:
            print("Waiting Connection")
            client_socket, client_address = server_socket.accept()
            log.logger.info(f"=======- {str(client_address)} user connected! -=======")
            thread = threading.Thread(
                target=handle, args=(client_socket, client_address)
            )
            thread.start()
            log.logger.debug("=======- after handle_client_process close! -=======")
    except Exception as e:
        print(e)
        log.logger.error(e)