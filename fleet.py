from hub import Hub
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


class Fleet:

    def __init__(self):
        self.__hubs = {}

    def get_maintenance_status(self):

        print("\nSelect Maintenance Status")
        print("1. Good")
        print("2. Average")
        print("3. Bad")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return "Good"
        elif choice == "2":
            return "Average"
        elif choice == "3":
            return "Bad"
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

        if hub_name not in self.__hubs:
            print(f"Hub '{hub_name}' does not exist.")
            return

        print("\nSelect Vehicle Type")
        print("1. Electric Car")
        print("2. Electric Scooter")

        vehicle_choice = input("Enter your choice (1-2): ")

        vehicle_id = input("Enter Vehicle ID: ")
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

            self.__hubs[hub_name].add_vehicle(vehicle)

        except ValueError as error:
            print(error)

    def display_hub(self):

        hub_name = input("Enter the Hub Name: ").strip()

        if hub_name not in self.__hubs:
            print(f"Hub '{hub_name}' does not exist.")
            return

        self.__hubs[hub_name].display_vehicles()

    def view_hub(self):

        if not self.__hubs:
            print("No hubs available.")
            return

        for hub in self.__hubs.values():
            hub.display_vehicles()