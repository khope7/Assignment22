#importing SQL connection and regex methods
from Connect_MYSQL_Fitness import connect_database
import re

#Writing code for Task1

#Creating add_member function for cursor to add data to fitness center SQL table members
def add_member(id, name, age):
    query = "INSERT INTO members (id, name, age) VALUES (%s, %s, %s)"
    cursor.execute(query, (id, name, age))

#Setting conn to run connect database
conn = connect_database()
if conn is not None:
#Creating cursor
    cursor = conn.cursor()

#Creating add member query function to add member to member table
    def add_member_query():
#Creating while True method to reloop after incorrect entry
        while True:
#Using try except blocks to manage incorrect entries for member id
            try:
#Creating cursor query to show current members for id creation
                query = "SELECT * FROM members"

                cursor.execute(query)

                print("Here are the current members:")
                for row in cursor.fetchall():
                    print(row)
#Asking for member id, UNIQUE id method within SQL fitness center members database to avoid duplicate entries with exception block for error handling
                member_id = input("Please enter a unique member id for the new member:\n")
                
                name_try = input("Please enter the first and last name of the new member:\n").title()
#Using regex split method to turn user entry into temporary list and eliminating spacing
                parts = re.split(r" ", name_try)
#Sends user back to function upon incorrect entry type
                if len(parts) < 2 or len(parts) > 2:
                    print("Apologies, entry must have first and last name. Numbers and special characters are accepted.")
                    add_member_query()
#Returns user name detail and reformats
                else:
                    member_name = parts[0] + " " + parts[1]
                
#Asking user for age with exception field catching for incorrect entries and if statement to catch out of range number entries
                member_age_try = (int(input("Please enter the member age:\n")))
                if member_age_try < 0 or member_age_try > 110:
                    print("Apologies, age must be a number greater than 0 and less than 110.")
                    add_member_query()
                else:
                    member_age = member_age_try

#Passing parameters into add member function and calling for SQL data entry
                add_member(member_id, member_name, member_age)
#Saving new user to table
                conn.commit()
#Printing confirmation and reprinting members with additional member added
                print(f"Member {member_name}: added.")
                query = "SELECT * FROM members"

                cursor.execute(query)

                print("Here are the current members:")
                for row in cursor.fetchall():
                    print(row)    
                break

            except Exception as e:
                print("Apologies, member id entry must be unique and a number")
                add_member_query()
                break

#Closing cursor and connection upon successful entry
            finally:
                cursor.close()
                conn.close()

#Running add_member_query function upon intial run
    add_member_query()


