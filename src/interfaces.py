from abc import ABC, abstractmethod


class MyInterface(ABC):
    @abstractmethod
    def do_something(self, param: str):
        pass


class MyClass(MyInterface):
    def do_something(self, param: str):
        return f"Doing something with: {param}"


class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class ConsoleLogger(Logger):
    def log(self, message: str):
        return f"Console: {message}"


def log_message(logger: Logger, message: str):
    return logger.log(message)