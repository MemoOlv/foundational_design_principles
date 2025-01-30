from src.composition import Car, Plane

def test_car_with_engine():
    obtained = Car()
    assert obtained.start() == "Engine started"

def test_plane_with_engine():
    obtained = Plane()
    assert obtained.start() == "Engine started"
