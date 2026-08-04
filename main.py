from vehicle import Vehicle

def main():
    print("=" * 50)
    print(" Welcome to Eco-Ride Urban Mobility System ")
    print("=" * 50)

    vehicle = Vehicle(
        vehicle_id="EV101",
        model="Tesla Model 3",
        battery_percentage=92.5,
        maintenance_status="Good",
        rental_price=1200
    )

    print("\nVehicle Details")
    print("-" * 30)
    vehicle.display_details()
    print("\nUpdating Battery...\n")
    vehicle.set_battery_percentage(95)
    vehicle.display_details()

if __name__ == "__main__":
    main()