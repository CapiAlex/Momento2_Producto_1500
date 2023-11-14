from db_connection import create_connection, close_connection

class AircraftRegistrar:
    def __init__(self, id, username, password):
        self.__id = id
        self.__username = username
        self.__password = password

    def aircraft_registrar_menu(self):
        while True:
            print("Aircraft Registrar Menu")
            print("1. Register Aircraft")
            print("2. List Aircraft")
            print("3. Exit to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                self.register_aircraft()
            elif choice == '2':
                self.list_aircraft()
            elif choice == '3':
                break
            else:
                print("Invalid option. Please try again.")

    def register_aircraft(self):
        registration = input("Aircraft Registration: ")
        model = input("Aircraft Model: ")
        manufacturer = input("Aircraft Manufacturer: ")
        status = input("Aircraft Status (active/inactive): ")

        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO Aircraft (registration, model, manufacturer, status) VALUES (%s, %s, %s, %s)",
                           (registration, model, manufacturer, status))
            connection.commit()
            print(f"Aircraft successfully registered: Registration {registration}, Model {model}")

        except Exception as e:
            print("Error registering the aircraft:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    def list_aircraft(self):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT registration, model, manufacturer, status FROM Aircraft")
            aircraft_list = cursor.fetchall()

            if aircraft_list:
                print("List of aircraft:")
                for aircraft in aircraft_list:
                    registration, model, manufacturer, status = aircraft
                    print(f"Registration: {registration}, Model: {model}, Manufacturer: {manufacturer}, Status: {status}")
            else:
                print("No aircraft registered in the database.")

        except Exception as e:
            print("Error listing aircraft:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

if __name__ == "__main__":
    # Example usage:
    registrar = AircraftRegistrar(id=1, username="user", password="pass")
    registrar.aircraft_registrar_menu()
