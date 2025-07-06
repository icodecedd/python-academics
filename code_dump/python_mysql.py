import mysql.connector

# Connect to MySQL (XAMPP)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lesson10"
)

sqlCursor = mydb.cursor()

# User input
# studID = input("Student ID: ")
# fName = input("First Name: ")
# lName = input("Last Name: ")
# midInit = input("Middle Initial: ")
# sex = input("Sex: ")
# birthDate = input("Birthdate [YYYY-MM-DD]: ")  # Fix date format
#
# # Correct SQL query using placeholders
# query = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s)"
# info = (studID, fName, lName, midInit, sex, birthDate)
#
# # Execute the query safely
# sqlCursor.execute(query, info)
# mydb.commit()
#
# print("Student record inserted successfully!")

# Fetch all records
sqlCursor.execute("SELECT * FROM student")
rows = sqlCursor.fetchall()

print("\nCurrent Student Records:")
for column in rows:
    print(column[0])
    print(column[1])
    print(column[2])
    print(column[3])
    print(column[4])
    print(column[5].__str__())

# Close connection
sqlCursor.close()
mydb.close()
