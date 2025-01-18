#importing SQL connection
from Connect_MYSQL_Fitness import connect_database

#Writing code for Task2

#Creating add_workout_session function for cursor to add data to fitness center SQL table workoutsessions
def add_workout_session(member_id, session_date, duration_minutes, calories_burned):
    query = "INSERT INTO workoutsessions (member_id, session_date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (member_id, session_date, duration_minutes, calories_burned))

#Setting conn to run connect database
conn = connect_database()
if conn is not None:
#Creating cursor
    cursor = conn.cursor()

#Creating add session query function to add session to workoutsessions table
    def add_session_query():
#Creating while True method to reloop after incorrect entry
        while True:
#Using try except blocks to manage incorrect entries
            try:
#Creating cursor query to show current members for session creation
                query = "SELECT * FROM members"

                cursor.execute(query)

                print("Here are the current members:")
                for row in cursor.fetchall():
                    print(row)
                    
#Asking for member id, UNIQUE PRIMARY KEY id method within SQL fitness center members database to avoid duplicate entries with exception block for error handling
                id = input("Please enter the member id for the session member:\n")

#Asking for member session date, date method within SQL fitness center members database avoids incorrect entries with exception block for error handling                
                date = input("Please enter the date of the session member (YYYY-MM-DD):\n")
                
#Asking user for duration in minutes with exception field catching for incorrect entries and if statement to catch out of range number entries
                duration_try = (int(input("Please enter the session duration in minutes:\n")))
                if duration_try < 0 or duration_try > 1000:
                    print("Apologies, duration must be a number greater than 0 and less than 1000.")
                    add_session_query()
                else:
                    duration = duration_try

#Asking user for calories burned with exception field catching for incorrect entries and if statement to catch out of range number entries
                calories_try = (int(input("Please enter the calories burned:\n")))
                if calories_try < 0 or calories_try > 1000:
                    print("Apologies, calories burned must be a number greater than 0 and less than 1000.")
                    add_session_query()
                else:
                    calories = calories_try

#Passing parameters into add workout session function and calling for SQL data entry
                add_workout_session(id, date, duration, calories)
#Saving new session to table
                conn.commit()
#Printing user confirmation and printing sessions with additional session added
                print(f"Session added:")
                query = "SELECT * FROM workoutsessions"

                cursor.execute(query)

                print("Here are the current member's sessions:")
                for row in cursor.fetchall():
                    print(row)    
                break

            except Exception as e:
                print("Apologies, fields were entered incorrectly.")
                add_session_query()
                break

#Closing cursor and connection upon successful entry
            finally:
                cursor.close()
                conn.close()

#Running add_session_query function upon intial run
    add_session_query()
