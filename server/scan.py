import socket
import asyncio
from services.logger import log
from server.conection import Handle

port_number = 810
max_clients = 10


async def scanner():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setblocking(False)  # Configurando o socket para não bloquear
    server_socket.bind(("0.0.0.0", port_number))
    server_socket.listen(max_clients)

    while True:
        print("Waiting for connection...")
        client_socket, client_address = await asyncio.get_event_loop().sock_accept(
            server_socket
        )

        print(f"=======- {str(client_address)} user connected! -=======")
        log.logger.info(f"=======- {str(client_address)} user connected! -=======")

        handler = Handle()
        asyncio.create_task(
            handler.connection(client_socket, client_address)
        )  # Executando a conexão de forma assíncrona
        log.logger.debug("=======- after handle_client_process close! -=======")
