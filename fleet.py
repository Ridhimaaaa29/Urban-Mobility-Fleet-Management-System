from hub import Hub


class Fleet:

    def __init__(self):
        self.__hubs = []

    def add_hub(self, hub_name):

        hub_name = hub_name.strip()

        if not hub_name:
            print("Hub name cannot be empty.")
            return

        hub = Hub(hub_name)
        self.__hubs.append(hub)

        print(f"{hub_name} Hub added successfully.")

    def get_hub(self, hub_name):

        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name.lower():
                return hub

        return None

    def add_vehicle_to_hub(self, hub_name, vehicle):

        hub = self.get_hub(hub_name)

        if hub:
            hub.add_vehicle(vehicle)
        else:
            print("Hub not found.")

    def display_hubs(self):

        if not self.__hubs:
            print("\nNo hubs available.")
            return

        for hub in self.__hubs:
            hub.display_vehicles()