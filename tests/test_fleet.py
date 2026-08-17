from fleet import Fleet
from hub import Hub
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


def create_car(vehicle_id, model, battery=80, price=100):

    return ElectricCar(
        vehicle_id,
        model,
        battery,
        "Available",
        price,
        5
    )


def create_scooter(vehicle_id, model, battery=60, price=50):

    return ElectricScooter(
        vehicle_id,
        model,
        battery,
        "On Trip",
        price,
        40
    )


def add_test_data(fleet):

    hub = Hub("Chandigarh")

    car = create_car(
        "C101",
        "Tesla",
        90,
        1000
    )

    scooter = create_scooter(
        "S101",
        "Ola",
        85,
        500
    )

    hub.add_vehicle(car)
    hub.add_vehicle(scooter)

    fleet._Fleet__hubs["Chandigarh"] = hub

    fleet.vehicle_categories["Electric Car"].append(car)
    fleet.vehicle_categories["Electric Scooter"].append(scooter)


def test_find_hub():

    fleet = Fleet()

    hub = Hub("Chandigarh")

    fleet._Fleet__hubs["Chandigarh"] = hub

    assert fleet.find_hub("Chandigarh") is hub
    assert fleet.find_hub("Delhi") is None


def test_get_vehicle_type():

    car = create_car("C101", "Tesla")
    scooter = create_scooter("S101", "Ola")

    assert Fleet.get_vehicle_type(car) == "Electric Car"
    assert Fleet.get_vehicle_type(scooter) == "Electric Scooter"


def test_vehicle_categories():

    fleet = Fleet()

    car = create_car("C101", "Tesla")

    fleet.vehicle_categories["Electric Car"].append(car)

    assert car in fleet.vehicle_categories["Electric Car"]


def test_advanced_sort_by_battery(monkeypatch, capsys):

    fleet = Fleet()

    hub = Hub("Chandigarh")

    car = create_car("C101", "Tesla", 90, 1000)
    scooter = create_scooter("S101", "Ola", 70, 500)

    hub.add_vehicle(car)
    hub.add_vehicle(scooter)

    fleet._Fleet__hubs["Chandigarh"] = hub

    inputs = iter(["Chandigarh", "1"])
                   
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    fleet.advanced_sort()

    captured = capsys.readouterr()
    assert captured.out.index("C101") < captured.out.index("S101")

def test_advanced_sort_by_price(monkeypatch, capsys):

    fleet = Fleet()

    hub = Hub("Chandigarh")

    car = create_car("C101", "Tesla", 90, 1000)
    scooter = create_scooter("S101", "Ola", 70, 500)

    hub.add_vehicle(car)
    hub.add_vehicle(scooter)

    fleet._Fleet__hubs["Chandigarh"] = hub

    inputs = iter(["Chandigarh", "2"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    fleet.advanced_sort()

    captured = capsys.readouterr()

    assert captured.out.index("C101") < captured.out.index("S101")

def test_csv_save_and_load(tmp_path):

    csv_file = tmp_path / "test_fleet.csv"

    fleet = Fleet()
    fleet.CSV_FILE = str(csv_file)

    hub = Hub("Chandigarh")

    car = create_car(
        "C101",
        "Tesla",
        90,
        1000
    )

    scooter = create_scooter(
        "S101",
        "Ola",  
        85,
        500
    )

    hub.add_vehicle(car)
    hub.add_vehicle(scooter)

    fleet._Fleet__hubs["Chandigarh"] = hub

    fleet.save_to_csv()

    assert csv_file.exists()

    new_fleet = Fleet()
    new_fleet.CSV_FILE = str(csv_file)

    new_fleet.load_from_csv()

    loaded_hub = new_fleet.find_hub("Chandigarh")

    assert loaded_hub is not None
    assert len(loaded_hub.get_vehicles()) == 2

    vehicles = loaded_hub.get_vehicles()

    assert vehicles[0].get_vehicle_id() == "C101"
    assert vehicles[0].get_model() == "Tesla"

    assert vehicles[1].get_vehicle_id() == "S101"
    assert vehicles[1].get_model() == "Ola"

def test_json_save_and_load(tmp_path):

    json_file = tmp_path / "test_fleet.json"

    fleet = Fleet()
    fleet.JSON_FILE = str(json_file)

    hub = Hub("Chandigarh")

    car = create_car(
        "C101",
        "Tesla",
        90,
        1000
    )

    scooter = create_scooter(
        "S101",
        "Ola",
        85,
        500
    )

    hub.add_vehicle(car)
    hub.add_vehicle(scooter)

    fleet._Fleet__hubs["Chandigarh"] = hub

    fleet.save_to_json()

    assert json_file.exists()

    new_fleet = Fleet()
    new_fleet.JSON_FILE = str(json_file)

    new_fleet.load_from_json()

    loaded_hub = new_fleet.find_hub("Chandigarh")

    assert loaded_hub is not None
    assert len(loaded_hub.get_vehicles()) == 2

    vehicles = loaded_hub.get_vehicles()

    assert vehicles[0].get_vehicle_id() == "C101"
    assert vehicles[0].get_model() == "Tesla"
    assert vehicles[0].get_battery_percentage() == 90

    assert vehicles[1].get_vehicle_id() == "S101"
    assert vehicles[1].get_model() == "Ola"
    assert vehicles[1].get_battery_percentage() == 85


def test_get_maintenance_status_choices(monkeypatch):
    fleet = Fleet()

    # Test valid choices
    for choice, expected in [("1", "Available"), ("2", "On Trip"), ("3", "Under Maintenance")]:
        monkeypatch.setattr("builtins.input", lambda _=None: choice)
        assert fleet.get_maintenance_status() == expected

    # Invalid choice returns None
    monkeypatch.setattr("builtins.input", lambda _=None: "9")
    assert fleet.get_maintenance_status() is None


def test_add_hub_empty_name(monkeypatch, capsys):
    fleet = Fleet()
    monkeypatch.setattr("builtins.input", lambda _=None: "")

    fleet.add_hub()

    captured = capsys.readouterr()
    assert "Hub name cannot be empty." in captured.out


def test_alphabetical_sort_hub_not_exist(monkeypatch, capsys):
    fleet = Fleet()
    monkeypatch.setattr("builtins.input", lambda _=None: "NoSuchHub")

    fleet.alphabetical_sort()

    captured = capsys.readouterr()
    assert "Hub 'NoSuchHub' does not exist." in captured.out


def test_advanced_sort_invalid_choice(monkeypatch, capsys):
    fleet = Fleet()
    hub = Hub("TestHub")

    car = create_car("C401", "CarX", 50, 100)
    hub.add_vehicle(car)
    fleet._Fleet__hubs["TestHub"] = hub

    inputs = iter(["TestHub", "9"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    fleet.advanced_sort()

    captured = capsys.readouterr()
    assert "Invalid choice." in captured.out


def test_view_csv_file_not_exist(tmp_path, capsys):
    fleet = Fleet()
    fleet.CSV_FILE = str(tmp_path / "nope.csv")

    fleet.view_csv()

    captured = capsys.readouterr()
    assert "CSV file does not exist." in captured.out


def test_view_json_file_not_exist(tmp_path, capsys):
    fleet = Fleet()
    fleet.JSON_FILE = str(tmp_path / "nope.json")

    fleet.view_json()

    captured = capsys.readouterr()
    assert "JSON file does not exist." in captured.out


def test_save_to_csv_writes_headers(tmp_path):
    csv_file = tmp_path / "out.csv"
    fleet = Fleet()
    fleet.CSV_FILE = str(csv_file)

    hub = Hub("CSVHub")
    car = create_car("C501", "CarY", 90, 200)
    scooter = create_scooter("S501", "ScootY", 80, 50)

    hub.add_vehicle(car)
    hub.add_vehicle(scooter)

    fleet._Fleet__hubs["CSVHub"] = hub

    fleet.save_to_csv()

    assert csv_file.exists()

    # Check header present
    with open(csv_file, "r", encoding="utf-8") as f:
        header = f.readline()
    assert "hub_name" in header and "vehicle_type" in header


def test_categorized_view_no_vehicles(capsys):
    fleet = Fleet()
    fleet.categorized_view()

    captured = capsys.readouterr()
    assert "No vehicles available." in captured.out


def test_fleet_analytics_counts(capsys):
    fleet = Fleet()
    hub = Hub("AnalyticsHub")

    car1 = create_car("C601", "A", 80, 100)
    car2 = create_car("C602", "B", 70, 100)
    scooter = create_scooter("S601", "C", 60, 50)

    # Set different statuses
    car1.set_maintenance_status("Available")
    car2.set_maintenance_status("On Trip")
    scooter.set_maintenance_status("Under Maintenance")

    hub.add_vehicle(car1)
    hub.add_vehicle(car2)
    hub.add_vehicle(scooter)

    fleet._Fleet__hubs["AnalyticsHub"] = hub

    fleet.fleet_analytics()

    captured = capsys.readouterr()
    assert "Available" in captured.out
    assert "On Trip" in captured.out
    assert "Under Maintenance" in captured.out


def test_load_from_csv_file_not_found(tmp_path, capsys):
    fleet = Fleet()
    fleet.CSV_FILE = str(tmp_path / "does_not_exist.csv")

    fleet.load_from_csv()

    captured = capsys.readouterr()
    assert "No existing fleet data found." in captured.out


def test_load_from_json_file_not_found(tmp_path, capsys):
    fleet = Fleet()
    fleet.JSON_FILE = str(tmp_path / "does_not_exist.json")

    fleet.load_from_json()

    captured = capsys.readouterr()
    assert "No JSON fleet data found." in captured.out or "Starting with an empty fleet." in captured.out


def test_get_vehicle_type_none_for_unknown():
    fleet = Fleet()

    class OtherVehicle:
        pass

    assert fleet.get_vehicle_type(OtherVehicle()) is None


def test_view_hub_no_hubs(capsys):
    fleet = Fleet()
    fleet.view_hub()

    captured = capsys.readouterr()
    assert "No hubs available." in captured.out


def test_add_vehicle_invalid_hub(monkeypatch, capsys):
    fleet = Fleet()
    monkeypatch.setattr("builtins.input", lambda _=None: "NonExistentHub")

    fleet.add_vehicle()

    captured = capsys.readouterr()
    assert "Hub 'NonExistentHub' does not exist." in captured.out


def test_save_to_json_creates_file(tmp_path):
    json_file = tmp_path / "out_fleet.json"
    fleet = Fleet()
    fleet.JSON_FILE = str(json_file)

    hub = Hub("JSONHub")
    hub.add_vehicle(create_car("C1101", "JCar", 80, 120))
    fleet._Fleet__hubs["JSONHub"] = hub

    fleet.save_to_json()
    assert json_file.exists()


def test_view_csv_empty_file(tmp_path, capsys):
    csv_file = tmp_path / "empty.csv"
    # create file with header only
    with open(csv_file, "w", encoding="utf-8") as f:
        f.write("hub_name,vehicle_type,vehicle_id,model,battery,status,rental_price,seating_capacity,max_speed_limit\n")

    fleet = Fleet()
    fleet.CSV_FILE = str(csv_file)

    fleet.view_csv()
    captured = capsys.readouterr()
    assert "CSV file is empty." in captured.out


def test_add_vehicle_maintenance_invalid_flow(monkeypatch, capsys):
    fleet = Fleet()
    hub = Hub("FlowHub")
    fleet._Fleet__hubs["FlowHub"] = hub

    # inputs: hub name, vehicle type (1), vehicle id, model, battery, maintenance choice invalid
    inputs = iter(["FlowHub", "1", "VX101", "FlowModel", "80", "9"])
    monkeypatch.setattr("builtins.input", lambda _=None: next(inputs))

    fleet.add_vehicle()
    captured = capsys.readouterr()
    assert "Invalid maintenance status selected." in captured.out


def test_alphabetical_sort_prints_vehicles(monkeypatch, capsys):
    fleet = Fleet()
    hub = Hub("AlphaHub")
    hub.add_vehicle(create_car("C1201", "Beta"))
    hub.add_vehicle(create_scooter("S1201", "Alpha"))
    fleet._Fleet__hubs["AlphaHub"] = hub

    monkeypatch.setattr("builtins.input", lambda _=None: "AlphaHub")
    fleet.alphabetical_sort()
    captured = capsys.readouterr()
    assert "Beta" in captured.out or "Alpha" in captured.out