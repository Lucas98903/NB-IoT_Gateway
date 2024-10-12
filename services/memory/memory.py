import pickle

from log import log


class Memory:
    def __init__(self):
        self.data = None

    def storage(self, dado):
        self.data = dado

    def read(self):
        return self.data

    def save(self, arquivo):
        with open(arquivo, 'wb') as f:
            pickle.dump(self.data, f)

    def load(self, arquivo):
        try:
            with open(arquivo, 'rb') as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            print("File not found. Starting empty memory.")
            log.logger.error("File not found. SFtarting empty memory.")
            self.data = []
