from abc import ABC, abstractmethod
class Vehicle(ABC):

    def __init__(self, vehicle_id: str, model: str, battery_percentage: float, maintenance_status: str, rental_price: float):
        self.vehicle_id = vehicle_id
        self.model = model

        self.__battery_percentage = 0
        self.__maintenance_status = maintenance_status
        self.__rental_price = rental_price

        self.set_battery_percentage(battery_percentage)

    def get_battery_percentage(self):
        return self.__battery_percentage

    def get_maintenance_status(self):
        return self.__maintenance_status

    def get_rental_price(self):
        return self.__rental_price

    def set_battery_percentage(self, battery_percentage):

        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            print("Battery percentage must be between 0 and 100.")

    def set_maintenance_status(self, maintenance_status):
        self.__maintenance_status = maintenance_status

    def set_rental_price(self, rental_price):

        if rental_price >= 0:
            self.__rental_price = rental_price
        else:
            print("Rental price cannot be negative. Please provide a valid value.")

    @abstractmethod
    def calculate_trip_cost(self, trip_distance: float) -> float:
        pass

    def display_details(self):
        print(f"Vehicle ID        : {self.vehicle_id}")
        print(f"Model             : {self.model}")
        print(f"Battery Percentage: {self.get_battery_percentage()}%")
        print(f"Maintenance Status: {self.get_maintenance_status()}")
        print(f"Rental Price      : {self.get_rental_price()}/-")