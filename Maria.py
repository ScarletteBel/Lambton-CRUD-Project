def display_menu():
    print(
        "Welcome to the Device Management System \n 1.\tview all devices\n 2.\tadd a device\n 3.\tdelete a device\n 4.\tupdate a device\n 5.\texit the program ")
    print()


def read_devices():
    devices = []
    with open("devices.txt") as file:
        file = file.readlines()
        for line in file:
            line = line.replace("\n", "")
            devices.append(line)
            print(line)


def main():
    display_menu()
    choice = "y"
    while choice == "y":
        option = int(input('Select one option from the list ( 1, 2, 3, 4, or 5): '))
        if option == 1:
            print()
            read_devices()
        elif option == 2:
            print('add_device')
            #add_device()
        elif option == 3:
            print('delete_devices')
            #delete_devices()
        elif option == 4:
            print('update_devices')
            #update_devices()
        elif option == 5:
            break
        else:
            print("This is an invalid selection, try again.\n")
        print()
        choice = input("Continue? (y/n): ")
    print()
    print("Thanks for using the application !")


if __name__ == "__main__":
    main()
