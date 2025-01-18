#importing SQL connection
from Connect_MYSQL_Fitness import connect_database

#Writing code for Task2.1

#Creating get_members_in_age_range function for cursor to find range of members via age from user entry and printing
def members_in_age_range(cursor, start_age, end_age):
    query = "SELECT * FROM members WHERE age BETWEEN %s AND %s"
    cursor.execute(query, (start_age, end_age))
    print(f"Members between {start_age} and {end_age}:")
    for member in cursor.fetchall():
        print(member)


#Creating age_range_query function to gather min and max age ranges
def age_range_query():
    conn = connect_database()
    if conn is not None:
#Creating while True method to reloop after incorrect entry
        while True:
#Using try except blocks to manage incorrect entries
            try:
#Creating cursor
                cursor = conn.cursor()
#Creating cursor query to show current members for age ranges
                query = "SELECT * FROM members"

                cursor.execute(query)

                print("Here are the current members:")
                for row in cursor.fetchall():
                    print(row)

#Asking user for low age range
                first_age_try = (int(input("Please enter the low range of age:\n")))
                if first_age_try < 0 or first_age_try > 110:
                    print("Apologies, duration must be a number greater than 0 and less than 110.")
                    age_range_query()
                else:
                    first_age = first_age_try

#Asking user for high age range
                last_age_try = (int(input("Please enter the end range of age:\n")))
                if last_age_try < first_age_try or last_age_try > 110:
                    print(f"Apologies, duration must be a number greater than or equal to {first_age_try} and less than 110.")
                    age_range_query()
                else:
                    last_age = last_age_try

#Passing parameters into get_members_in_age_range function and calling for SQL data entry
                members_in_age_range(cursor, first_age, last_age)                      
                break
            
#Catching errors for incorrect entries
            except Exception as e:
                print(f"Apologies, fields were entered incorrectly.")
                print(e)
                age_range_query()
                break

#Closing cursor and connection upon successful entry
            finally:
                cursor.close()
                conn.close()

#Running age_range_query function upon intial run
age_range_query()