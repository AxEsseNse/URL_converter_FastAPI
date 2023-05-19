class DataBaseException(Exception):
    def __init__(self, api: str):
        self.api = api
