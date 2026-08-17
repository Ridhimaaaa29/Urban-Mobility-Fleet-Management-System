import pytest

from electric_car import ElectricCar
from electric_scooter import ElectricScooter
from vehicle import Vehicle


class ConcreteVehicle(Vehicle):

    def calculate_trip_cost(self, trip_value):
        return trip_value

def create_vehicle():

    return ConcreteVehicle(
        "V101",
        "Test Vehicle",
        80,
        "Available",
        100
    )

def test_calculate_trip_cost():

    vehicle = create_vehicle()
    assert vehicle.calculate_trip_cost(10) == 10

def test_vehicle_creation():

    vehicle = create_vehicle()

    assert vehicle.get_vehicle_id() == "V101"
    assert vehicle.get_model() == "Test Vehicle"
    assert vehicle.get_battery_percentage() == 80
    assert vehicle.get_maintenance_status() == "Available"
    assert vehicle.get_rental_price() == 100


def test_invalid_maintenance_status():

    with pytest.raises(ValueError):

        ConcreteVehicle(
            "V101",
            "Test Vehicle",
            80,
            "Invalid",
            100,
        )

def test_invalid_battery():
    with pytest.raises(ValueError):
        ConcreteVehicle(
            "V101",
            "Test Vehicle",
            120,
            "Available",
            100,
        )

def test_negative_rental_price():
    with pytest.raises(ValueError):
        ConcreteVehicle(
            "V101",
            "Test Vehicle",
            80,
            "Available",
            -100,
        )

def test_vehicle_equality():

    vehicle1 = create_vehicle()

    vehicle2 = ConcreteVehicle(
        "V101",
        "Another Model",
        50,
        "On Trip",
        200,
    )

    assert vehicle1 == vehicle2

def test_vehicle_not_equal():

    vehicle1 = create_vehicle()

    vehicle2 = ConcreteVehicle(
        "V102",
        "Test Vehicle",
        80,
        "Available",
        100,
    )

    assert vehicle1 != vehicle2

def test_vehicle_string():

    vehicle = create_vehicle()

    result = str(vehicle)

    assert "V101" in result
    assert "Test Vehicle" in result
    assert "80" in result
    assert "Available" in result

def test_electric_car_trip_cost():

    car = ElectricCar(
        "C101",
        "Tesla",
        90,
        "Available",
        1000,
        5
    )

    assert car.calculate_trip_cost(10) == 10.0

def test_electric_scooter_trip_cost():

    scooter = ElectricScooter(
        "S101",
        "Ola",
        80,
        "Available",
        500,
        40
    )

    assert scooter.calculate_trip_cost(10) == 2.5


def test_display_details_output(capsys):
    vehicle = create_vehicle()
    vehicle.display_details()

    captured = capsys.readouterr()

    assert "Vehicle ID" in captured.out
    assert "Model" in captured.out
    assert "Battery Percentage" in captured.out
    assert "Maintenance Status" in captured.out


def test_eq_with_non_vehicle():
    vehicle = create_vehicle()

    assert (vehicle == object()) is False


def test_rental_price_format_in_str():
    vehicle = create_vehicle()

    s = str(vehicle)

    # price should be formatted with two decimals
    assert "$100.00" in s


def test_set_battery_edge_values():
    vehicle = create_vehicle()

    vehicle.set_battery_percentage(0)
    assert vehicle.get_battery_percentage() == 0

    vehicle.set_battery_percentage(100)
    assert vehicle.get_battery_percentage() == 100


def test_set_rental_price_zero():
    vehicle = create_vehicle()

    vehicle.set_rental_price(0)
    assert vehicle.get_rental_price() == 0


def test_electric_car_display_details(capsys):
    car = ElectricCar(
        "EC101",
        "ModelX",
        75,
        "Available",
        300,
        4
    )

    car.display_details()
    captured = capsys.readouterr()
    assert "Seating Capacity" in captured.out


def test_electric_scooter_display_details(capsys):
    scooter = ElectricScooter(
        "ES101",
        "Scoot",
        65,
        "Available",
        50,
        30
    )

    scooter.display_details()
    captured = capsys.readouterr()
    assert "Max Speed Limit" in captured.out


def test_calculate_trip_cost_zero():
    vehicle = create_vehicle()
    assert vehicle.calculate_trip_cost(0) == 0


def test_invalid_battery_negative():
    with pytest.raises(ValueError):
        ConcreteVehicle(
            "V200",
            "NegBattery",
            -1,
            "Available",
            10,
        )


def test_set_maintenance_status_valid():
    vehicle = create_vehicle()
    vehicle.set_maintenance_status("On Trip")
    assert vehicle.get_maintenance_status() == "On Trip"


def test_vehicle_eq_reflexive():
    v = create_vehicle()
    assert v == v


def test_str_includes_currency_symbol():
    v = create_vehicle()
    assert "$" in str(v)