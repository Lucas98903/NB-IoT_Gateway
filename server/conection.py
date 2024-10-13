import time
import socket
import traceback

from controller.controller_comand import ManagerCommand
from services.upload.uploader import upload
from services.memory.memory import Memory
from services.decode.do201 import DO201
from log import log


class Handle:
    def __init__(self):
        manager = ManagerCommand()
        self.memory = Memory()

        address_memory_code, self.address_memory_return = manager.get_adress()
        self.memory.load(address_memory_code)
        self.codes = self.memory.read()

        self.client = None
        self.timeout = int(59)

    def _receive_data(self):
        counter = 0
        request_bytes = b""

        while True:
            counter += 1

            if self.client.fileno() != -1:
                request_bytes = request_bytes + self.client.recv(1024)

            request_str = request_bytes.hex()
            start = request_str.find("8000")
            end = request_str.find("81")

            if start != -1 and end != -1:
                print(request_str)
                log.logger.info(request_str)
                return request_str[start:end + 2]

            time.sleep(1)
            if counter >= 10 or not request_bytes:
                return None

    def _set_preferences(self, code):
        if self.client.fileno() != -1:
            command = bytes.fromhex(code)
            self.client.sendall(command)

        else:
            raise Exception(
                "The connection to the client was closed before sending the commands")

    def _decode_upload_data(self, str_sub_request):
        str_sub_request = DO201.parse_data_do201(
            str_sub_request.strip().upper())

        if str_sub_request:
            data_type, interpreted_data, equipment_imei = str_sub_request

            self.memory.storage(interpreted_data)
            self.memory.save(self.address_memory_code)

            upload(interpreted_data, data_type)

        else:
            raise Exception("Problem when decoding hexadecimal!")

    def connection(self, client, command):
        self.client = client
        self.client.settimeout(self.timeout)

        try:
            str_sub_request = self._receive_data()

            if str_sub_request is None:
                raise ValueError("No data received from client.")

            try:
                self._decode_upload_data(str_sub_request)

            except Exception as e:
                print(f"An error occurred: {e}")
                detail_error = traceback.format_exc()
                log.logger.error(f"Error while decoding: {detail_error}")
                print(detail_error)
                log.logger.info("")

            try:
                if len(self.codes) > 0:
                    for code in self.codes:
                        self._set_preferences(code)
                        str_sub_request = self._receive_data()

                    if str_sub_request:
                        self._decode_upload_data(str_sub_request)

                    else:
                        raise ValueError(
                            "Not receive data before send command")

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
