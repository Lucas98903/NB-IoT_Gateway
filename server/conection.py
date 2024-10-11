import time
import socket
import traceback
import threading

from services.upload.uploader import upload
from services.decode.do201 import DO201
from database.DAO import updatedDAO
from log import log


class Handle:
    def __init__(self):
        self.timeout = int(59)

    @staticmethod
    def _receive_data(client):
        counter = 10
        request_bytes = b""

        while True:
            counter += 1

            if client.fileno() != -1:
                request_bytes += client.recv(1024)

            request_str = request_bytes.hex()
            start = request_str.find("8000")
            end = request_str.find("81")

            if start != -1 and end != -1:
                print(request_str)
                return request_str[start:end + 2]

            time.sleep(1)
            if counter >= 10 or not request_bytes:
                return None

    def set_preferences(self, codes):
        pass

    def connection(self, client, command):
        client.settimeout(self.timeout)

        try:
            str_sub_request = self._receive_data(client)

            if str_sub_request is None:
                raise ValueError("No data received from client.")

            try:
                response = DO201.parse_data_do201(str_sub_request.strip().upper())

                if response:
                    data_type, interpreted_data, equipment_imei = response
                    upload(interpreted_data, data_type)
                else:
                    raise Exception("Problem when decoding hexadecimal!")

            except Exception as e:
                print(f"An error occurred: {e}")
                detail_error = traceback.format_exc()
                log.logger.error(f"Error while decoding: {detail_error}")
                print(detail_error)
                log.logger.info("")

        except socket.timeout:
            print("Timeout occurred")
            log.logger.warning("Timeout occurred")
            log.logger.info("")

        except ValueError as ve:
            print(f"Value error: {ve}")
            log.logger.error(f"Value error: {ve}")

        finally:
            client.close()
