from src.composition import Car, Plane


def test_car_with_engine():
    obtained = Car()
    assert obtained.start() == "Car started"


def test_plane_with_engine():
    obtained = Plane()
    assert obtained.start() == "Plane started"
