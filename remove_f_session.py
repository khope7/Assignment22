#importing SQL connection
from Connect_MYSQL_Fitness import connect_database

#Writing code for Task4

#Creating add_workout_session function for cursor to add data to fitness center SQL table workoutsessions
def remove_workout_session(date, id):
    query = "DELETE FROM workoutsessions WHERE session_date = %s AND member_id = %s"
    cursor.execute(query, (date, id))

#Setting conn to run connect database
conn = connect_database()
if conn is not None:
#Creating cursor
    cursor = conn.cursor()

#Creating remove_session_query function to remove session from workoutsessions table
    def remove_session_query():
#Creating while True method to reloop after incorrect entry
        while True:
#Using try except blocks to manage incorrect entries
            try:
#Creating cursor query to show current sessions for session deletion
                query = "SELECT * FROM workoutsessions"

                cursor.execute(query)

                print("Here are the current sessions:")
                for row in cursor.fetchall():
                    print(row)
#Asking for member id, UNIQUE PRIMARY KEY/FOREIGN KEY id method within SQL fitness center members database to avoid incorrect entries with exception block for error handling
                id = input("Please enter the member id for the session member:\n")

#Asking for member session date, DATE and DELETE method within SQL fitness center members database avoids incorrect entries with exception block for error handling                
                date = input("Please enter the date of the session to delete (YYYY-MM-DD):\n")

#Passing parameters into remove_workout_session function and calling for SQL data entry
                remove_workout_session(date, id)

#Saving new session to table
                conn.commit()
#Printing user confirmation and printing sessions with additional session added
                print(f"Session date: {date} for member id: {id} removed:")
                query = "SELECT * FROM workoutsessions"

                cursor.execute(query)

                print("Here are the current member's sessions:")
                for row in cursor.fetchall():
                    print(row)    
                break

            except Exception as e:
                print("Apologies, fields were entered incorrectly.")
                remove_session_query()
                break

#Closing cursor and connection upon successful entry
            finally:
                cursor.close()
                conn.close()

#Running remove_session_query function upon intial run
    remove_session_query()