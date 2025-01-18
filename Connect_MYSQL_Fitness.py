#Connecting to database and retieving tables
import mysql.connector
from mysql.connector import Error

def connect_database():
    #Database connection parameters
    db_name = "workout_session_db"
    user = "root"
    password = "CodingTemple.1" #I understand this password is public
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            print("Connected to MySQL database successfully")
            return conn
        
    except Error as e:
        print(f"Error: {e}")
        return None