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
    print("7. Fleet Analytics")
    print("8. Sort Vehicles Alphabetically by Model")
    print("9. Advanced Sorting Options")
    print("10. Save and Exit")


def main():

    fleet = Fleet()

    # Load previously saved fleet data from CSV file
    fleet.load_from_csv()

    heading("Welcome to Eco-Ride Urban Mobility System")

    while True:

        display_menu()

        try:
            choice = int(input("\nEnter your choice (1-10): "))
        
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
                heading("Fleet Analytics")
                fleet.fleet_analytics()

            elif choice == 8:
                heading("Vehicles Sorted Alphabetically by Model")
                fleet.alphabetical_sort()

            elif choice == 9:
                heading("Advanced Sorting Options")
                fleet.advanced_sort()

            elif choice == 10:
                fleet.save_to_csv()
                print("Fleet data saved. Thank you for using Eco-Ride Urban Mobility System!")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
                print("Invalid input. Please enter a number.")
    

if __name__ == "__main__":
    main()