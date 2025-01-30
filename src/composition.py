class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()

class Plane:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()

class Engine:
    def start(self):
        return "Engine started"