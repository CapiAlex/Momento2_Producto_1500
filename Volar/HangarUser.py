from db_connection import create_connection, close_connection


class HangarUser:
    def __init__(self, id, username, password):
        self.__id = id
        self.__username = username
        self.__password = password

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def user_menu(self):
        while True:
            print("User Menu")
            print("1. Request Aircraft")
            print("2. Return Aircraft")
            print("3. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                aircraft_registration = input("Enter the registration code of the aircraft you want to request: ")
                self.request_aircraft(aircraft_registration)
            elif choice == '2':
                aircraft_registration = input("Enter the registration code of the aircraft you want to return: ")
                self.return_aircraft(aircraft_registration)
            elif choice == '3':
                break
            else:
                print("Invalid option. Please try again.")

    def request_aircraft(self, aircraft_registration):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT status FROM Aircraft WHERE registration = %s", (aircraft_registration,))
            aircraft_status = cursor.fetchone()

            if aircraft_status and aircraft_status[0] == "Active":
                cursor.execute("UPDATE Aircraft SET status = 'Reserved' WHERE registration = %s", (aircraft_registration,))
                cursor.execute("INSERT INTO Reservations (user_id, aircraft_registration) VALUES (%s, %s)", (self.id, aircraft_registration))
                connection.commit()
                print("Aircraft requested successfully.")
            else:
                print("The aircraft is not available for request.")

        except Exception as e:
            print("Error requesting the aircraft:", str(e))

        finally:
            cursor.close()
            close_connection(connection)

    def return_aircraft(self, aircraft_registration):
        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()

        try:
            # Check if the aircraft is reserved by the user
            cursor.execute("SELECT id FROM Reservations WHERE user_id = %s AND aircraft_registration = %s", (self.id, aircraft_registration))
            reservation_id = cursor.fetchone()

            if reservation_id:
                # Update the status of the aircraft to "Active"
                cursor.execute("UPDATE Aircraft SET status = 'Active' WHERE registration = %s", (aircraft_registration,))
                # Delete the reservation record
                cursor.execute("DELETE FROM Reservations WHERE id = %s", (reservation_id[0],))
                connection.commit()
                print("Aircraft returned successfully.")
            else:
                print("The aircraft is not reserved by this user.")

        except Exception as e:
            print("Error returning the aircraft:", str(e))

        finally:
            cursor.close()
            close_connection(connection)
