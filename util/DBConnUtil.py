import pyodbc

class DBConnUtil:
    @staticmethod
    def getDBConn():
        # Define your SQL Server connection parameters
        server = 'DESKTOP-MB0Q7BK'
        database = 'LoanManagementSystem'
        Trusted_Connection = True

        # Construct the connection string
        conn_str = f'DRIVER={{SQL Server}};SERVER=DESKTOP-MB0Q7BK;DATABASE=LoanManagementSystem;Trusted_Connection=True'

        try:
            # Establish the connection
            connection = pyodbc.connect(conn_str)
            print("Database connection successful.")
            return connection
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            return None
