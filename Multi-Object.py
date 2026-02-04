class Device:
    def __init__(self, name, type, status):
        self.__name = name
        self.__type = type
        self.__status = status

    def get_name(self):  # GETTER
        return self.__name

    def set_name(self, value):  # SETTER
        self.__name = value

    def get_type(self):  # GETTER
        return self.__type

    def set_type(self, value):  # SETTER
        self.__type = value

    def get_status(self):  # GETTER
        return self.__status

    def set_status(self, value):  # SETTER
        self.__status = value

    def display_details(self):
        print(f"Name: {self.__name}, Type: {self.__type}, Status: {self.__status}")

devices = [
    Device("Printer", "Peripheral", "Online"),
    Device("Router", "Network", "Offline"),
    Device("Monitor", "Display", "Online")
]

while True:
    print("\nDEVICE MANAGEMENT SYSTEM")
    print("1. View All Devices")
    print("2. Add New Device")
    print("3. Update Device")
    print("4. Delete Device")
    print("5. Encapsulation Test")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        if not devices:
            print("No device records found.")
        else:
            for i, d in enumerate(devices, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                d.display_details()

    elif choice == "2":
        name = input("Enter device name: ")
        type = input("Enter device type: ")
        status = input("Enter device status: ")
        devices.append(Device(name, type, status))  # OBJECT CREATION
        print(f"'{name}' added successfully.")

    elif choice == "3":
        update_name = input("Enter device name to update: ")
        found = False
        for d in devices:
            if d.get_name().lower() == update_name.lower():
                new_type = input("Enter new type: ")
                new_status = input("Enter new status: ")
                d.set_type(new_type)
                d.set_status(new_status)
                print("Device updated.")
                found = True
                break
        if not found:
            print("Device not found.")

    elif choice == "4":
        delete_name = input("Enter device name to delete: ")
        for d in devices:
            if d.get_name().lower() == delete_name.lower():
                devices.remove(d)
                print(f"Device '{delete_name}' deleted.")
                break
        else:
            print("Device not found.")

    elif choice == "5":  # ENCAPSULATION TEST
        for d in devices:
            print(f"{d.get_name()} | Type: {d.get_type()} | Status: {d.get_status()}")

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")