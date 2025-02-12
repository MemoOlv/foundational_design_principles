from typing import Protocol
import pathlib

class Logger(Protocol):
    def log(self, message: str):
        pass

class ConsoleLogger:
    def log(self, message: str):
        return f"Console protocol: {message}"
    
class FileLogger:
    def __init__(self, file_path: str):
        self.file = pathlib.Path(file_path)

    def log(self, message: str):
        if not self.file.exists():
            self.file.touch()
        self.file.write_text(f"File protocol: {message}")
        return self.file.read_text()