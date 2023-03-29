import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Phat@123'
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create Database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
