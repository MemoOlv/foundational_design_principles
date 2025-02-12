import pathlib

from src.interfaces import MyClass, ConsoleLogger, log_message, FileLogger


def test_class_as_interface():
    myclass = MyClass()
    parameters = "a"
    obtained = myclass.do_something(parameters)
    expected = "Doing something with: a"
    assert expected == obtained


def test_loggers():
    console_log_message = "A console log"
    console_logger = ConsoleLogger()
    obatined_console_logger = log_message(console_logger, console_log_message)
    assert obatined_console_logger == "Console: A console log"

    file_logger_message = "A file log"
    file_log_path = "tests/data/log.txt"
    file = pathlib.Path(file_log_path)

    if file.exists():
        file.unlink()

    file_logger = FileLogger(file_log_path)
    obtained_file_logger = log_message(file_logger, file_logger_message)
    assert obtained_file_logger == "File: A file log"

    if file.exists():
        file.unlink()
