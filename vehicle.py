class Vehicle:

    def __init__(self, vehicle_id: str, model: str, battery_percentage: float):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage

    def display_details(self):
        print(f"Vehicle ID        : {self.vehicle_id}")
        print(f"Model             : {self.model}")
        print(f"Battery Percentage: {self.battery_percentage}%")