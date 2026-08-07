from fleet import Fleet


def heading(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def display_menu():
    print("\n1. Add a New Hub")
    print("2. Add Vehicle to Existing Hub")
    print("3. Display Fleet")
    print("4. Search Vehicles by Hub")
    print("5. Search Vehicles by Battery (>80%)")
    print("6. Categorized View")
    print("7. Exit")


def main():

    fleet = Fleet()

    heading("Welcome to Eco-Ride Urban Mobility System")

    while True:

        display_menu()

        try:
            choice = int(input("\nEnter your choice (1-6): "))
        
            if choice == 1:
                fleet.add_hub()

            elif choice == 2:
                fleet.add_vehicle()

            elif choice == 3:
                heading("Fleet Details")
                fleet.view_hub()

            elif choice == 4:
                heading("Search Vehicles by Hub")
                fleet.search_by_hub()

            elif choice == 5:
                heading("Search Vehicles by Battery (>80%)")
                fleet.search_by_battery()

            elif choice == 6:
                heading("Categorized View")
                fleet.categorized_view()

            elif choice == 7:
                heading("Thank you for using Eco-Ride Urban Mobility System.")
                break
            
            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
                print("Invalid input. Please enter a number.")
    

if __name__ == "__main__":
    main()