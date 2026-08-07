from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(
        self,
        vehicle_id,
        model,
        battery_percentage,
        maintenance_status,
        rental_price,
    ):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = 0
        self.__maintenance_status = ""
        self.__rental_price = 0.0

        self.set_battery_percentage(battery_percentage)
        self.set_maintenance_status(maintenance_status)
        self.set_rental_price(rental_price)


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


    def set_battery_percentage(self, percentage):

        if 0 <= percentage <= 100:
            self.__battery_percentage = percentage
        else:
            print("Battery percentage must be between 0 and 100.")

    def set_maintenance_status(self, status):

        valid_status = ["Good", "Needs Maintenance", "Under Repair"]

        if status in valid_status:
            self.__maintenance_status = status
        else:
            print("Invalid maintenance status.")

    def set_rental_price(self, price):

        if price >= 0:
            self.__rental_price = price
        else:
            print("Rental price cannot be negative.")


    @abstractmethod
    def calculate_trip_cost(self, trip_value):
        pass


    def display_details(self):

        print(f"Vehicle ID         : {self.vehicle_id}")
        print(f"Model              : {self.model}")
        print(f"Battery Percentage : {self.__battery_percentage}%")
        print(f"Maintenance Status : {self.__maintenance_status}")
        print(f"Rental Price       : ${self.__rental_price:.2f}")

    def __eq__(self, other):

        if isinstance(other, Vehicle):
            return self.vehicle_id == other.get_vehicle_id()

        return False

    def __str__(self):

        return (
            f"{self.model} "
            f"(ID: {self.vehicle_id}, "
            f"Battery: {self.__battery_percentage}%)"
        )