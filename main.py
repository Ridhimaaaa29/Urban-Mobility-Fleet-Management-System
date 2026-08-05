from fleet import Fleet
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


def heading(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def display_menu():
    print("\n1. Add New Hub")
    print("2. Add Vehicle to Existing Hub")
    print("3. Display Fleet")
    print("4. Exit")


def create_vehicle():

    print("\nSelect Vehicle Type")
    print("1. Electric Car")
    print("2. Electric Scooter")

    vehicle_choice = input("Enter your choice (1-2): ")

    vehicle_id = input("Enter Vehicle ID: ")
    model = input("Enter Vehicle Model: ")
    battery_percentage = float(input("Enter Battery Percentage: "))
    maintenance_status = input("Enter Maintenance Status: ")
    rental_price = float(input("Enter Rental Price: "))

    if vehicle_choice == "1":

        seating_capacity = int(input("Enter Seating Capacity: "))

        return ElectricCar(
            vehicle_id,
            model,
            battery_percentage,
            maintenance_status,
            rental_price,
            seating_capacity,
        )

    elif vehicle_choice == "2":

        max_speed_limit = int(input("Enter Maximum Speed Limit: "))

        return ElectricScooter(
            vehicle_id,
            model,
            battery_percentage,
            maintenance_status,
            rental_price,
            max_speed_limit,
        )

    else:
        print("Invalid vehicle type selected.")
        return None


def add_hub(fleet):

    hub_name = input("Enter Hub Name: ")
    fleet.add_hub(hub_name)


def add_vehicle(fleet):

    hub_name = input("Enter the Hub where you want to add the vehicle: ")

    vehicle = create_vehicle()

    if vehicle is not None:
        fleet.add_vehicle_to_hub(hub_name, vehicle)


def main():

    fleet = Fleet()

    heading("Welcome to Eco-Ride Urban Mobility System")

    while True:

        display_menu()

        choice = input("\nSelect an option (1-4): ")

        if choice == "1":

            add_hub(fleet)

        elif choice == "2":

            add_vehicle(fleet)

        elif choice == "3":

            heading("Fleet Details")
            fleet.display_hubs()

        elif choice == "4":

            print("\nThank you for using Eco-Ride Urban Mobility System.")
            break

        else:

            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()