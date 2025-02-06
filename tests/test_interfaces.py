from src.interfaces import MyClass, ConsoleLogger, log_message

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