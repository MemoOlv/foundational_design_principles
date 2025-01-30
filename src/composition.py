class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        if self.engine.start():
            return "Car started"


class Plane:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        if self.engine.start():
            return "Plane started"


class Engine:
    def start(self):
        print("Engine started")
        return True
