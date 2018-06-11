
class MxRecord(dict):
    def __init__(self):
        self.records = {}

    def add(self, key, value):
        self.records[key] = value

    def get(self):
        return self.records
