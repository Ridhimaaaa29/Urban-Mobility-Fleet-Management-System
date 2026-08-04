from vehicle import Vehicle

def main():
    print("=" * 50)
    print(" Welcome to Eco-Ride Urban Mobility System ")
    print("=" * 50)

    vehicle = Vehicle(
        vehicle_id="EV101",
        model="Tesla Model 3",
        battery_percentage=92.5
    )

    print("\nVehicle Details")
    print("-" * 30)
    vehicle.display_details()


if __name__ == "__main__":
    main()