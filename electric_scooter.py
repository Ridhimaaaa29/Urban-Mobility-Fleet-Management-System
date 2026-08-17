from vehicle import Vehicle

class ElectricScooter(Vehicle):

    def __init__(self, vehicle_id, model, battery_percentage, maintenance_status, rental_price, max_speed_limit):

        super().__init__(vehicle_id, model, battery_percentage, maintenance_status, rental_price)
        self.max_speed_limit = max_speed_limit

    def display_details(self):

        super().display_details()
        print(f"Max Speed Limit   : {self.max_speed_limit} km/h")

    def calculate_trip_cost(self, minutes: float) -> float:
        base_cost = 1.0
        cost_per_minute = 0.15
        return base_cost + (cost_per_minute * minutes)