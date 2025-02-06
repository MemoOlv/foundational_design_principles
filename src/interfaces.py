from abc import ABC, abstractmethod


class MyInterface(ABC):
    @abstractmethod
    def do_something(self, param: str):
        pass


class MyClass(MyInterface):
    def do_something(self, param: str):
        return f"Doing something with: {param}"


class ConsoleLogger:
    pass
