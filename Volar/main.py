from Manager import HangarManager
from HangarUser import HangarUser

def main():
    print("Welcome to the Hangar Management System")
    while True:
        print("Main Menu")
        print("1. Register")
        print("2. Log In")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter your username: ")
            role = input("Enter your role (manager/user): ")
            password = input("Enter your password: ")

            id = 0

            HangarManager.register(id, username, role, password)
            print("Registration successful")
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user_id, username, role = HangarManager.login(username, password)
            if role == 'manager':
                HangarManager(id=user_id, username=username, password=password).manager_menu()
            elif role == 'user':
                HangarUser(id=user_id, username=username, password=password).user_menu()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
