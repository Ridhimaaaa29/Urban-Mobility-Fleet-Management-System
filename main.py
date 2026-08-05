from vehicle import Vehicle
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


def print_heading(title):
    print(f"\n{'=' * 50}")
    print(f" {title.center(50)} ")
    print(f"{'=' * 50}")

def main():
    print_heading(" Welcome to Eco-Ride Urban Mobility System ")

    # ---------------- UC3 : Electric Car ----------------

    print_heading(" Electric Car Details ")

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

    print_heading(" Electric Scooter Details ")

    scooter = ElectricScooter(
        vehicle_id="ES201",
        model="Ather 450X",
        battery_percentage=85,
        maintenance_status="Good",
        rental_price=600,
        max_speed_limit=90,
    )

    scooter.display_details()

    # ---------------- Inheritance Check ----------------

    print_heading(" Inheritance Check ")
    print(f"Is ElectricCar a Vehicle?      {isinstance(car, Vehicle)}")
    print(f"Is ElectricScooter a Vehicle?  {isinstance(scooter, Vehicle)}")

if __name__ == "__main__":
    main()