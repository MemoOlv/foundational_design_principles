from src.protocols import ConsoleLogger, FileLogger
from src.interfaces import log_message
import pathlib


def test_loggers():
    console_log_message = "A console log"
    console_logger = ConsoleLogger()
    obatined_console_logger = log_message(console_logger, console_log_message)
    assert obatined_console_logger == "Console protocol: A console log"

    file_logger_message = "A file log"
    file_log_path = "tests/data/log_protocol.txt"
    file = pathlib.Path(file_log_path)

    if file.exists():
        file.unlink()

    file_logger = FileLogger(file_log_path)
    obtained_file_logger = log_message(file_logger, file_logger_message)
    assert obtained_file_logger == "File protocol: A file log"

    if file.exists():
        file.unlink()
