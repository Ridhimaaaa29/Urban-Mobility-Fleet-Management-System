from collections import defaultdict
from hub import Hub
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


class Fleet:

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
                print("-" * 50)

                for vehicle in sorted_vehicles:
                    print(vehicle)
                    print("-" * 50)

        except ValueError:
            print("Invalid numeric input.")
            return

            print("-" * 50)

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