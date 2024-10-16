import socket
import traceback
import asyncio  # Importar asyncio para funções assíncronas

from controller.controller_comand import ManagerCommand
from services.upload.uploader import upload
from services.memory.memory import Memory
from services.decode.do201 import DO201
from services.logger import log


class Handle:
    def __init__(self):
        manager = ManagerCommand()
        self.memory = Memory()

        (
            self.address_memory_code,
            self.address_memory_return,
            self.address_memory_alarm_park,
        ) = manager.get_adress()

        self.codes = self.memory.get_data(self.address_memory_code)

        self.client = None
        self.timeout = int(59)

    async def _receive_data(self):
        counter = 0
        request_bytes = b""

        while True:
            counter += 1

            try:
                request_bytes = request_bytes + await asyncio.get_event_loop().sock_recv(self.client, 1024)

                if request_bytes != b"":
                    log.logger.warning("Close connection")

            except socket.error as e:
                detail_error = traceback.format_exc()
                log.logger.error(f"Error receiving data: {e} \n {detail_error}")

            request_str = request_bytes.hex()
            start = request_str.find("8000")
            end = request_str.find("81")

            if start != -1 and end != -1:
                print(request_str)
                log.logger.info(request_str)
                return request_str[start : end + 2]

            await asyncio.sleep(1)
            if counter >= 10 or not request_bytes:
                return None

    async def _set_preferences(self, code):
        if self.client.fileno() != -1:
            command = bytes.fromhex(code)
            await asyncio.get_event_loop().sock_sendall(self.client, command)
        else:
            raise Exception(
                "The connection to the client was closed before sending the commands"
            )

    async def _decode_upload_data(self, str_sub_request):
        str_sub_request = DO201.parse_data_do201(str_sub_request.strip().upper())

        if str_sub_request:
            data_type, interpreted_data, equipment_imei = str_sub_request

            if data_type == 1:
                self.memory.storage_data(interpreted_data.alarmPark, self.address_memory_alarm_park)
            elif data_type == 3:
                self.memory.storage_data(interpreted_data, self.address_memory_return)

            upload(interpreted_data, data_type)

        else:
            raise Exception("Problem when decoding hexadecimal!")

    async def connection(self, client, command):
        self.client = client
        self.client.settimeout(self.timeout)

        try:
            str_sub_request = await self._receive_data()

            if str_sub_request is None:
                raise ValueError("No data received from client - 0x01")

            try:
                await self._decode_upload_data(str_sub_request)

            except Exception as e:
                print(f"An error occurred: {e}")
                detail_error = traceback.format_exc()
                log.logger.error(f"Error while decoding: {detail_error}")
                print(detail_error)
                log.logger.info("")

            #Verifica se há configurações para enviar para o equipamento
            try:
                if self.codes != None:
                    if len(self.codes) > 0:
                        for code in self.codes:
                            await self._set_preferences(code)

                        str_sub_request = await self._receive_data()
                        if str_sub_request:
                            await self._decode_upload_data(str_sub_request)

                        else:
                            raise ValueError("Not receive data before send command. - 0x03")

            except Exception as e:
                detail_error = traceback.format_exc()
                print(f"\n {e} \n {detail_error}")
                log.logger.error(f"Error occuried: \n{detail_error} \n{e}")

        except socket.timeout:
            print("Timeout occurred")
            log.logger.warning("Timeout occurred")

        except ValueError as ve:
            print(f"Value error: {ve}")
            log.logger.error(f"Value error: {ve}")

        finally:
            self.client.close()
