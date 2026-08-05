from vehicle import Vehicle


class Hub:

    def __init__(self, hub_name):
        self.__hub_name = hub_name
        self.__vehicles = []

    def get_hub_name(self):
        return self.__hub_name

    def get_vehicles(self):
        return self.__vehicles

    def add_vehicle(self, vehicle):

        if not isinstance(vehicle, Vehicle):
            print("Only Vehicle objects can be added.")
            return

        self.__vehicles.append(vehicle)
        print(f"{vehicle.model} added successfully to {self.__hub_name} Hub.")

    def display_vehicles(self):

        print(f"\nHub : {self.__hub_name}")
        print("-" * 50)

        if not self.__vehicles:
            print("No vehicles available.")
            return

        for vehicle in self.__vehicles:
            vehicle.display_details()
            print("-" * 50)

    def __str__(self):
        return f"Hub : {self.__hub_name}"