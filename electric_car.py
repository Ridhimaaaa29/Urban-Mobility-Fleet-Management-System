from vehicle import Vehicle
class ElectricCar(Vehicle):

    def __init__(self, vehicle_id, model, battery_percentage, maintenance_status, rental_price, seating_capacity):

        super().__init__(vehicle_id, model, battery_percentage, maintenance_status, rental_price)
        self.seating_capacity = seating_capacity

    def display_details(self):

        super().display_details()
        print(f"Seating Capacity  : {self.seating_capacity}")

    def calculate_trip_cost(self, trip_distance: float) -> float:
        base_cost = 5.0
        cost_per_km = 0.5
        return base_cost + (trip_distance * cost_per_km)