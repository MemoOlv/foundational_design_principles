from src.interfaces import MyClass

def test_class_as_interface():
    myclass = MyClass()
    parameters = "a"
    obtained = myclass.do_something(parameters)
    expected = "Doing something with: a"
    assert expected == obtained
