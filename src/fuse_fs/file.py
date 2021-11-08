from random import uniform

class File:
    def __init__(self, name: str, type_: str):
        self.name = name
        self.type = type_
        self.content = ""