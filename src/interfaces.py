from abc import ABC, abstractmethod
import pathlib


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

class FileLogger(Logger):
    def __init__(self, file_path: str):
        self.file = pathlib.Path(file_path)

    def log(self, message: str):
        if not self.file.exists():
            self.file.touch()
        self.file.write_text(f"File: {message}")
        return self.file.read_text()

def log_message(logger: Logger, message: str):
    return logger.log(message)