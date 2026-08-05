from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(
        self,
        vehicle_id: str,
        model: str,
        battery_percentage: float,
        maintenance_status: str,
        rental_price: float,
    ):
        self.vehicle_id = vehicle_id
        self.model = model

        self.__battery_percentage = 0
        self.__maintenance_status = ""
        self.__rental_price = 0.0

        self.set_battery_percentage(battery_percentage)
        self.set_maintenance_status(maintenance_status)
        self.set_rental_price(rental_price)

    # ---------------- Getters ---------------- #

    def get_vehicle_id(self):
        return self.vehicle_id

    def get_model(self):
        return self.model

    def get_battery_percentage(self):
        return self.__battery_percentage

    def get_maintenance_status(self):
        return self.__maintenance_status

    def get_rental_price(self):
        return self.__rental_price

    # ---------------- Setters ---------------- #

    def set_battery_percentage(self, battery_percentage):

        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            raise ValueError("Battery percentage must be between 0 and 100.")

    def set_maintenance_status(self, maintenance_status):

        if not maintenance_status.strip():
            raise ValueError("Maintenance status cannot be empty.")

        self.__maintenance_status = maintenance_status

    def set_rental_price(self, rental_price):

        if rental_price >= 0:
            self.__rental_price = rental_price
        else:
            raise ValueError("Rental price cannot be negative.")

    # ---------------- Abstract Method ---------------- #

    @abstractmethod
    def calculate_trip_cost(self, trip_value: float) -> float:
        pass

    # ---------------- Utility Methods ---------------- #

    def display_details(self):

        print(f"Vehicle ID         : {self.vehicle_id}")
        print(f"Model              : {self.model}")
        print(f"Battery Percentage : {self.__battery_percentage}%")
        print(f"Maintenance Status : {self.__maintenance_status}")
        print(f"Rental Price       : ₹{self.__rental_price:.2f}")

    def __str__(self):

        return (
            f"{self.model} "
            f"(ID: {self.vehicle_id}, "
            f"Battery: {self.__battery_percentage}%)"
        )