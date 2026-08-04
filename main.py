from vehicle import Vehicle
from electric_car import ElectricCar
from electric_scooter import ElectricScooter

def main():
    print("=" * 50)
    print(" Welcome to Eco-Ride Urban Mobility System ")
    print("=" * 50)

    # ---------------- UC2 ----------------

    vehicle = Vehicle(
        vehicle_id="EV101",
        model="Tesla Model 3",
        battery_percentage=92.5,
        maintenance_status="Good",
        rental_price=1200,
    )

    print("\nVehicle Details")
    print("-" * 50)
    vehicle.display_details()
    print("\nUpdating Battery...\n")
    vehicle.set_battery_percentage(95)
    vehicle.display_details()

    # ---------------- UC3 : Electric Car ----------------

    print("\n" + "=" * 50)
    print(" Electric Car Details ")
    print("=" * 50)

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

    print("\n" + "=" * 50)
    print(" Electric Scooter Details ")
    print("=" * 50)

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

    print("\n" + "=" * 50)
    print(" Inheritance Check ")
    print("=" * 50)
    print(f"Is ElectricCar a Vehicle?      {isinstance(car, Vehicle)}")
    print(f"Is ElectricScooter a Vehicle?  {isinstance(scooter, Vehicle)}")

if __name__ == "__main__":
    main()