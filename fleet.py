import csv
import json
from collections import defaultdict

from hub import Hub
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


class Fleet:

    CSV_FILE = "fleet.csv"
    JSON_FILE = "fleet.json"

    def __init__(self):
        self.__hubs = {}
        self.__vehicle_categories = defaultdict(list)

    def find_hub(self, hub_name):
        return self.__hubs.get(hub_name)

    @property
    def vehicle_categories(self):
        return self.__vehicle_categories

    @staticmethod
    def get_vehicle_type(vehicle):

        if isinstance(vehicle, ElectricCar):
            return "Electric Car"
        
        elif isinstance(vehicle, ElectricScooter):
            return "Electric Scooter"
        
        return None
        
    def get_maintenance_status(self):

        print("\nSelect Maintenance Status")
        print("1. Available")
        print("2. On Trip")
        print("3. Under Maintenance")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return "Available"
        elif choice == "2":
            return "On Trip"
        elif choice == "3":
            return "Under Maintenance"
        else:
            print("Invalid maintenance status selected.")
            return None

    def add_hub(self):

        hub_name = input("Enter the Hub Name: ").strip()

        if not hub_name:
            print("Hub name cannot be empty.")
            return

        if hub_name in self.__hubs:
            print(f"Hub '{hub_name}' already exists.")
            return

        self.__hubs[hub_name] = Hub(hub_name)
        print(f"Hub '{hub_name}' added successfully.")


    def add_vehicle(self):

        hub_name = input("Enter the Hub Name: ").strip()

        hub = self.find_hub(hub_name)

        if hub is None:
            print(f"Hub '{hub_name}' does not exist.")
            return

        print("\nSelect Vehicle Type")
        print("1. Electric Car")
        print("2. Electric Scooter")

        vehicle_choice = input("Enter your choice (1-2): ")

        vehicle_id = input("Enter Vehicle ID: ")
        
        if hub.vehicle_exists(vehicle_id):
            print(f"Vehicle ID '{vehicle_id}' already exists in '{hub_name}' Hub.")
            return

        model = input("Enter Vehicle Model: ")
        battery_percentage = float(input("Enter Battery Percentage: "))

        maintenance_status = self.get_maintenance_status()

        if maintenance_status is None:
            return
        
        rental_price = float(input("Enter Rental Price: "))

        try:

            if vehicle_choice == "1":

                seating_capacity = int(input("Enter Seating Capacity: "))

                vehicle = ElectricCar(
                    vehicle_id,
                    model,
                    battery_percentage,
                    maintenance_status,
                    rental_price,
                    seating_capacity
                )

            elif vehicle_choice == "2":

                max_speed_limit = int(input("Enter Maximum Speed Limit: "))

                vehicle = ElectricScooter(
                    vehicle_id,
                    model,
                    battery_percentage,
                    maintenance_status,
                    rental_price,
                    max_speed_limit
                )

            else:
                print("Invalid vehicle type selected.")
                return

            added = hub.add_vehicle(vehicle)

            if added:
                vehicle_type = self.get_vehicle_type(vehicle)

                if vehicle_type in ["Electric Car", "Electric Scooter"]:
                    self.vehicle_categories[vehicle_type].append(vehicle)

        except ValueError:
            print("Invalid numeric input.")
            return


    def view_hub(self):

        if not self.__hubs:
            print("No hubs available.")
            return

        for hub in self.__hubs.values():
            hub.display_vehicles()

    def categorized_view(self):
        if not self.vehicle_categories:
            print("No vehicles available.")
            return

        print("\n" + "=" * 50)
        print("Vehicles Categorized by Type".center(50))
        print("=" * 50)

        for vehicle_type, vehicles in self.vehicle_categories.items():
            print(f"\n{vehicle_type}:")
            print("-" * 50)

            if not vehicles:
                print("No vehicles available in this category.")
                continue

            for vehicle in vehicles:
                vehicle.display_details()
                print("-" * 50)

    def fleet_analytics(self):

        status_count = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0
        }

        for hub in self.__hubs.values():
            for vehicle in hub.get_vehicles():
                status = vehicle.get_maintenance_status()
                status_count[status] = status_count.get(status, 0) + 1

        print("\n" + "=" * 50)
        print("VEHICLE STATUS SUMMARY".center(50))
        print("=" * 50)

        print(f"Available             : {status_count['Available']}")
        print(f"On Trip               : {status_count['On Trip']}")
        print(f"Under Maintenance     : {status_count['Under Maintenance']}")
        print("-" * 50)
        print(f"{'Total Vehicles':<22}: {sum(status_count.values())}")

    def alphabetical_sort(self):
        hub_name = input("Enter the Hub Name: ").strip()

        hub = self.find_hub(hub_name)

        if hub is None:
            print(f"Hub '{hub_name}' does not exist.")
            return

        vehicles = hub.get_vehicles()

        if not vehicles:
            print("No vehicles available in this hub.")
            return

        sorted_vehicles = hub.sort_vehicles()

        print("\n" + "=" * 50)
        print(f"Vehicles in '{hub_name}' Sorted Alphabetically".center(50))
        print("=" * 50)

        for vehicle in sorted_vehicles:
            print(vehicle)
            print("-" * 50)

    def advanced_sort(self):
        hub_name = input("Enter the Hub Name: ").strip()

        hub = self.find_hub(hub_name)

        if hub is None:
            print(f"Hub '{hub_name}' does not exist.")
            return

        vehicles = hub.get_vehicles()

        if not vehicles:
            print("No vehicles available in this hub.")
            return

        print("\nSort Vehicles By")
        print("1. Battery Percentage (Highest First)")
        print("2. Rental Price (Highest First)")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":

            sorted_vehicles = sorted(
                vehicles,
                key=lambda vehicle: vehicle.get_battery_percentage(),
                reverse=True,
            )

            print("\nVehicles Sorted by Battery Percentage")

        elif choice == "2":

            sorted_vehicles = sorted(
                vehicles,
                key=lambda vehicle: vehicle.get_rental_price(),
                reverse=True,
            )

            print("\nVehicles Sorted by Rental Price")

        else:
            print("Invalid choice.")
            return

        print("-" * 50)

        for vehicle in sorted_vehicles:
            print(vehicle)
            print("-" * 50)


    def save_to_csv(self):

        fieldnames = [
            "hub_name",
            "vehicle_type",
            "vehicle_id",
            "model",
            "battery",
            "status",
            "rental_price",
            "seating_capacity",
            "max_speed_limit"
        ]

        with open(self.CSV_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for hub_name, hub in self.__hubs.items():

                for vehicle in hub.get_vehicles():

                    vehicle_type = self.get_vehicle_type(vehicle)

                    row = {
                        "hub_name": hub_name,
                        "vehicle_type": vehicle_type,
                        "vehicle_id": vehicle.get_vehicle_id(),
                        "model": vehicle.get_model(),
                        "battery": vehicle.get_battery_percentage(),
                        "status": vehicle.get_maintenance_status(),
                        "rental_price": vehicle.get_rental_price(),
                        "seating_capacity": "",
                        "max_speed_limit": ""
                    }

                    if isinstance(vehicle, ElectricCar):
                        row["seating_capacity"] = vehicle.seating_capacity

                    elif isinstance(vehicle, ElectricScooter):
                        row["max_speed_limit"] = vehicle.max_speed_limit

                    writer.writerow(row)

        print("Fleet data saved successfully.")

    def load_from_csv(self):
        
        try:
            with open(self.CSV_FILE, "r", newline="", encoding="utf-8") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    hub_name = row["hub_name"]
                    vehicle_type = row["vehicle_type"]

                    # Create hub if it does not already exist
                    if hub_name not in self.__hubs:
                        self.__hubs[hub_name] = Hub(hub_name)

                    hub = self.__hubs[hub_name]

                    if vehicle_type == "Electric Car":

                        vehicle = ElectricCar(
                            row["vehicle_id"],
                            row["model"],
                            float(row["battery"]),
                            row["status"],
                            float(row["rental_price"]),
                            int(row["seating_capacity"])
                        )

                    elif vehicle_type == "Electric Scooter":

                        vehicle = ElectricScooter(
                            row["vehicle_id"],
                            row["model"],
                            float(row["battery"]),
                            row["status"],
                            float(row["rental_price"]),
                            int(row["max_speed_limit"])
                        )

                    else:
                        print(f"Unknown vehicle type: {vehicle_type}")
                        continue

                    added = hub.add_vehicle(vehicle)

                    if added:
                        self.__vehicle_categories[
                            vehicle_type
                        ].append(vehicle)

            print("Fleet data loaded successfully.")

        except FileNotFoundError:
            print("No existing fleet data found. Starting with an empty fleet.")

    def view_csv(self):
        try:
            with open(self.CSV_FILE, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                print("\n" + "=" * 80)
                print("SAVED CSV DATA".center(80))
                print("=" * 80)

                found = False

                for row in reader:
                    found = True

                    print(f"Hub              : {row['hub_name']}")
                    print(f"Vehicle Type     : {row['vehicle_type']}")
                    print(f"Vehicle ID       : {row['vehicle_id']}")
                    print(f"Model            : {row['model']}")
                    print(f"Battery          : {row['battery']}%")
                    print(f"Status           : {row['status']}")
                    print(f"Rental Price     : {row['rental_price']}")

                    if row["vehicle_type"] == "Electric Car":
                        print(f"Seating Capacity : {row['seating_capacity']}")

                    elif row["vehicle_type"] == "Electric Scooter":
                        print(f"Max Speed Limit  : {row['max_speed_limit']}")

                    print("-" * 80)

                if not found:
                    print("CSV file is empty.")

        except FileNotFoundError:
            print("CSV file does not exist.")

    def view_json(self):
        try:
            with open(self.JSON_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            print("\n" + "=" * 80)
            print("SAVED JSON DATA".center(80))
            print("=" * 80)

            print(json.dumps(data, indent=4))

        except FileNotFoundError:
            print("JSON file does not exist.")

    def save_to_json(self):

        data = {
            "hubs" : []
        }

        for hub_name, hub in self.__hubs.items():

            hub_data = {
                "hub_name": hub_name,
                "vehicles": []
            }

            for vehicle in hub.get_vehicles():

                vehicle_data = {
                    "vehicle_type": self.get_vehicle_type(vehicle),
                    "vehicle_id": vehicle.get_vehicle_id(),
                    "model": vehicle.get_model(),
                    "battery": vehicle.get_battery_percentage(),
                    "status": vehicle.get_maintenance_status(),
                    "rental_price": vehicle.get_rental_price()
                }

                if isinstance(vehicle, ElectricCar):

                    vehicle_data["seating_capacity"] = (
                        vehicle.seating_capacity
                    )

                elif isinstance(vehicle, ElectricScooter):

                    vehicle_data["max_speed_limit"] = (
                        vehicle.max_speed_limit
                    )

                hub_data["vehicles"].append(vehicle_data)

            data["hubs"].append(hub_data)

        with open(self.JSON_FILE, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4
            )

        print("Fleet data saved to JSON successfully.")

    def load_from_json(self):
        try:

            with open(self.JSON_FILE, "r", encoding="utf-8") as file:

                data = json.load(file)

            # Clear current fleet before loading
            self.__hubs.clear()
            self.__vehicle_categories.clear()

            for hub_data in data.get("hubs", []):

                hub_name = hub_data["hub_name"]

                hub = Hub(hub_name)
                self.__hubs[hub_name] = hub

                for vehicle_data in hub_data.get("vehicles", []):

                    vehicle_type = vehicle_data["vehicle_type"]

                    if vehicle_type == "Electric Car":

                        vehicle = ElectricCar(
                            vehicle_data["vehicle_id"],
                            vehicle_data["model"],
                            float(vehicle_data["battery"]),
                            vehicle_data["status"],
                            float(vehicle_data["rental_price"]),
                            int(vehicle_data["seating_capacity"])
                        )

                    elif vehicle_type == "Electric Scooter":

                        vehicle = ElectricScooter(
                            vehicle_data["vehicle_id"],
                            vehicle_data["model"],
                            float(vehicle_data["battery"]),
                            vehicle_data["status"],
                            float(vehicle_data["rental_price"]),
                            int(vehicle_data["max_speed_limit"])
                        )

                    else:
                        print(
                            f"Unknown vehicle type: {vehicle_type}"
                        )
                        continue

                    added = hub.add_vehicle(vehicle)

                    if added:

                        self.__vehicle_categories[
                            vehicle_type
                        ].append(vehicle)

            print("Fleet data loaded from JSON successfully.")

        except FileNotFoundError:

            print(
                "No JSON fleet data found. "
                "Starting with an empty fleet."
            )