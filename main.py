from electric_car import ElectricCar
from electric_scooter import ElectricScooter

def heading(title):
    print(f"\n{'=' * 50}")
    print(title.center(50))
    print(f"{'=' * 50}")
def display_trip_costs(vehicles, trip_data):

    for vehicle in vehicles:
        trip_value, unit = trip_data[vehicle]
        trip_cost = vehicle.calculate_trip_cost(trip_value)
        print(f"Model      : {vehicle.model}")
        print(f"Trip       : {trip_value} {unit}")
        print(f"Trip Cost  : {trip_cost:.2f}")
        print("-" * 50)

def main():
    heading(" Welcome to Eco-Ride Urban Mobility System ")

    # ---------------- UC3 : Electric Car ----------------

    heading(" Electric Car Details ")

    car = ElectricCar(
        vehicle_id="EC202",
        model="Nissan Leaf",
        battery_percentage=96,
        maintenance_status="Excellent",
        rental_price=15000,
        seating_capacity=5,
    )

    car.display_details()

    # ---------------- UC3 : Electric Scooter ----------------

    heading(" Electric Scooter Details ")

    scooter = ElectricScooter(
        vehicle_id="ES201",
        model="Ather 450X",
        battery_percentage=85,
        maintenance_status="Good",
        rental_price=600,
        max_speed_limit=90,
    )

    scooter.display_details()

    # ---------------- Polymorphism Demonstration ----------------

    heading("Trip Cost Calculation")
    vehicles = [car, scooter]
    trip_data = {
    car: (20, "km"),
    scooter: (30, "minutes"),
    }

    display_trip_costs(vehicles, trip_data)

if __name__ == "__main__":
    main()