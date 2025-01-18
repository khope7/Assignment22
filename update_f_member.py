#importing SQL connection and regex methods
from Connect_MYSQL_Fitness import connect_database

#Writing code for Task3

#Creating add_member function for cursor to update data in fitness center SQL table members
def update_member(age, id):
    query = "UPDATE members SET age = %s WHERE id = %s"
    cursor.execute(query, (age, id))

#Setting conn to run connect database
conn = connect_database()
if conn is not None:
#Creating cursor
    cursor = conn.cursor()

#Creating update member query function to update member in member table
    def update_member_query():
#Creating while True method to reloop after incorrect entry
        while True:
#Using try except blocks to manage incorrect entries for member id
            try:
#Creating cursor query to show current members for age update
                query = "SELECT * FROM members"

                cursor.execute(query)

                print("Here are the current members:")
                for row in cursor.fetchall():
                    print(row)
#Asking for member id, PRIMARY KEY id method within SQL fitness center members database avoids incorrect entries with exception block for error handling
                member_id = input("Please enter the member id for the member you would like to update:\n")
                
#Asking user for age with exception field catching for incorrect entries and if statement to catch out of range number entries
                member_age_try = (int(input("Please enter the member's new age:\n")))
                if member_age_try < 0 or member_age_try > 110:
                    print("Apologies, age must be a number greater than 0 and less than 110.")
                    update_member_query()
                else:
                    member_age = member_age_try
                
                update_member(member_age, member_id)

#Saving new user to table
                conn.commit()
#Printing confirmation and reprinting members with additional member added
                print(f"Member {member_id}: updated.")
                query = "SELECT * FROM members"

                cursor.execute(query)

                print("Here are the current members:")
                for row in cursor.fetchall():
                    print(row)    
                break

            except Exception as e:
                print("Apologies, member id entry must be unique and a number")
                update_member_query()
                break

#Closing cursor and connection upon successful entry
            finally:
                cursor.close()
                conn.close()

#Running update_member_query function upon intial run
    update_member_query()