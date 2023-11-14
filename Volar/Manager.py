from db_connection import create_connection, close_connection

class HangarManager:
    def __init__(self):
        self.__id = None
        self.__username = None
        self.__rol = None
        self.__password = None

    @staticmethod
    def register_aircraft(registration, model, manufacturer, status):
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

    @staticmethod
    def list_aircraft():
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

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def rol(self):
        return self.__rol

    @rol.setter
    def rol(self, rol):
        self.__rol = rol

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

if __name__ == "__main__":
    # Example usage:
    manager = HangarManager()
    manager.register_aircraft(registration="ABC123", model="Boeing 747", manufacturer="Boeing", status="Active")
    manager.list_aircraft()
