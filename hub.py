from vehicle import Vehicle


class Hub:

    def __init__(self, hub_name):
        self.__hub_name = hub_name
        self.__vehicles = []

    def get_hub_name(self):
        return self.__hub_name

    def get_vehicles(self):
        return self.__vehicles

    def vehicle_exists(self, vehicle_id):

        duplicate_vehicle = [
            existing_vehicle
            for existing_vehicle in self.__vehicles
            if existing_vehicle.get_vehicle_id() == vehicle_id
        ]

        return len(duplicate_vehicle) > 0
    
    def add_vehicle(self, vehicle):

        if not isinstance(vehicle, Vehicle):
            print("Only Vehicle objects can be added.")
            return False
        
        duplicate_vehicle = [
            existing_vehicle
            for existing_vehicle in self.__vehicles
            if existing_vehicle == vehicle
        ]

        if duplicate_vehicle:
            print(f"Vehicle ID '{vehicle.get_vehicle_id()}' already exists in '{self.__hub_name}' Hub.")
            return False

        self.__vehicles.append(vehicle)
        print(f"{vehicle.model} added successfully to '{self.__hub_name}' Hub.")
        return True

    def display_vehicles(self):

        print(f"\nHub : {self.__hub_name}")
        print("-" * 50)

        if not self.__vehicles:
            print("No vehicles available.")
            return

        for vehicle in self.__vehicles:
            vehicle.display_details()
            print("-" * 50)

    def sort_vehicles(self):

        return sorted(
            self.__vehicles,
            key=lambda vehicle: vehicle.get_model().lower()
        )

    def __str__(self):
        return f"Hub : {self.__hub_name}"      