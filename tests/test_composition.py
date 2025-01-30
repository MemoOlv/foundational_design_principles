from src.composition import Car

def test_car_with_engine():
    obtained = Car()
    assert obtained.start() == "Engine started"
