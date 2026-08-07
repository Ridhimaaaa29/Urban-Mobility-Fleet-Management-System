from vehicle import Vehicle


class Hub:

    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):

        if not isinstance(vehicle, Vehicle):
            print("Only Vehicle objects can be added.")
            return

        self.vehicles.append(vehicle)
        print(f"{vehicle.model} added successfully to '{self.name}' Hub.")

    def display_vehicles(self):

        print(f"\nHub : {self.name}")
        print("-" * 50)

        if not self.vehicles:
            print("No vehicles available.")
            return

        for vehicle in self.vehicles:
            vehicle.display_details()
            print("-" * 50)