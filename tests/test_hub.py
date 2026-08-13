from hub import Hub
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


def create_car(vehicle_id, model):

    return ElectricCar(
        vehicle_id,
        model,
        80,
        "Available",
        100,
        5
    )


def create_scooter(vehicle_id, model):

    return ElectricScooter(
        vehicle_id,
        model,
        70,
        "On Trip",
        50,
        40
    )


def test_hub_creation():

    hub = Hub("Chandigarh")

    assert hub.get_hub_name() == "Chandigarh"
    assert hub.get_vehicles() == []


def test_add_vehicle():

    hub = Hub("Chandigarh")

    car = create_car("C101", "Tesla")

    result = hub.add_vehicle(car)

    assert result is True
    assert len(hub.get_vehicles()) == 1


def test_duplicate_vehicle():

    hub = Hub("Chandigarh")

    car1 = create_car("C101", "Tesla")
    car2 = create_car("C101", "BMW")

    hub.add_vehicle(car1)

    result = hub.add_vehicle(car2)

    assert result is False
    assert len(hub.get_vehicles()) == 1


def test_vehicle_exists():

    hub = Hub("Chandigarh")

    car = create_car("C101", "Tesla")

    hub.add_vehicle(car)

    assert hub.vehicle_exists("C101") is True
    assert hub.vehicle_exists("C999") is False


def test_invalid_vehicle():

    hub = Hub("Chandigarh")

    result = hub.add_vehicle("Not a vehicle")

    assert result is False


def test_sort_vehicles():

    hub = Hub("Chandigarh")

    hub.add_vehicle(create_car("C101", "Tesla"))
    hub.add_vehicle(create_car("C102", "Audi"))
    hub.add_vehicle(create_scooter("S101", "BMW"))

    sorted_vehicles = hub.sort_vehicles()

    models = [
        vehicle.get_model()
        for vehicle in sorted_vehicles
    ]

    assert models == ["Audi", "BMW", "Tesla"]


def test_hub_string():

    hub = Hub("Chandigarh")

    assert str(hub) == "Hub : Chandigarh"

def test_display_vehicles(capsys):

    hub = Hub("Chandigarh")

    hub.add_vehicle(create_car("C101", "Tesla"))

    hub.display_vehicles()

    captured = capsys.readouterr()

    assert "Chandigarh" in captured.out
    assert "C101" in captured.out
    assert "Tesla" in captured.out


def test_display_empty_hub_outputs_no_vehicles(capsys):
    hub = Hub("EmptyHub")
    hub.display_vehicles()

    captured = capsys.readouterr()
    assert "No vehicles available." in captured.out


def test_add_multiple_vehicles_and_count():
    hub = Hub("MultiHub")

    hub.add_vehicle(create_car("C201", "Alpha"))
    hub.add_vehicle(create_scooter("S201", "Beta"))
    hub.add_vehicle(create_car("C202", "Gamma"))

    assert len(hub.get_vehicles()) == 3


def test_sort_vehicles_case_insensitive():
    hub = Hub("SortHub")

    hub.add_vehicle(create_car("C301", "alpha"))
    hub.add_vehicle(create_scooter("S301", "Beta"))
    hub.add_vehicle(create_car("C302", "CHARLIE"))

    sorted_vehicles = hub.sort_vehicles()

    models = [v.get_model() for v in sorted_vehicles]
    assert models == ["alpha", "Beta", "CHARLIE"]


def test_add_non_vehicle_prints_message(capsys):
    hub = Hub("BadHub")
    result = hub.add_vehicle("not a vehicle")

    captured = capsys.readouterr()
    assert result is False
    assert "Only Vehicle objects can be added." in captured.out


def test_add_vehicle_prints_success(capsys):
    hub = Hub("SuccessHub")
    hub.add_vehicle(create_car("C701", "SuccessCar"))

    captured = capsys.readouterr()
    assert "SuccessCar added successfully" in captured.out


def test_duplicate_vehicle_prints_message(capsys):
    hub = Hub("DupHub")
    car1 = create_car("C801", "ModelA")
    car2 = create_car("C801", "ModelB")

    hub.add_vehicle(car1)
    result = hub.add_vehicle(car2)

    captured = capsys.readouterr()
    assert result is False
    assert "already exists" in captured.out


def test_vehicle_exists_case_sensitive():
    hub = Hub("CaseHub")
    hub.add_vehicle(create_car("C901", "CaseModel"))

    assert hub.vehicle_exists("c901") is False


def test_sort_returns_list_type():
    hub = Hub("ListHub")
    hub.add_vehicle(create_car("C1001", "Zed"))
    hub.add_vehicle(create_scooter("S1001", "Alpha"))

    sorted_vehicles = hub.sort_vehicles()
    assert isinstance(sorted_vehicles, list)