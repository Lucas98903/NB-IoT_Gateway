import pickle

from services.logger import log


class Memory:
    def __init__(self):
        self.data = None
        self.address = None

    def storage(self, dado):
        self.data = dado

    def read(self):
        return self.data

    def save(self, arquivo):
        self.address = arquivo
        with open(arquivo, 'wb') as f:
            pickle.dump(self.data, f)

    def load(self, arquivo):
        try:
            with open(arquivo, 'rb') as f:
                self.data = pickle.load(f)

        except FileNotFoundError:
            print(f"File not found. Starting empty memory. -> {self.data}")
            log.logger.warning(
                f"File not found. Starting empty memory. -> {self.data}")
            self.data = None