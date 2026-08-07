from hub import Hub
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


class Fleet:

    def __init__(self):
        self.__hubs = {}

    def find_hub(self, hub_name):
        return self.__hubs.get(hub_name)

    def get_maintenance_status(self):

        print("\nSelect Maintenance Status")
        print("1. Good")
        print("2. Needs Maintenance")
        print("3. Under Repair")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return "Good"
        elif choice == "2":
            return "Needs Maintenance"
        elif choice == "3":
            return "Under Repair"
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

            hub.add_vehicle(vehicle)

        except ValueError as error:
            print(error)

    def view_hub(self):

        if not self.__hubs:
            print("No hubs available.")
            return

        for hub in self.__hubs.values():
            hub.display_vehicles()

    def search_by_hub(self):

        hub_name = input("Enter the Hub Name: ").strip()
        hub = self.find_hub(hub_name)

        if hub is None:
            print(f"Hub '{hub_name}' does not exist.")
            return

        hub.display_vehicles()

    def search_by_battery(self):
        vehicles = []

        for hub in self.__hubs.values():
            vehicles.extend(hub.get_vehicles())

        high_battery_vehicles = list(
            filter(
                lambda vehicle: vehicle.get_battery_percentage() > 80,
                vehicles,
            )
        )

        if not high_battery_vehicles:
            print("No vehicles found with battery greater than 80%.")
            return

        print("\nVehicles with Battery Percentage greater than 80%")
        print("-" * 50)

        for vehicle in high_battery_vehicles:
            vehicle.display_details()
            print("-" * 50)