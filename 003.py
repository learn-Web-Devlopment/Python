# create Database
import mysql.connector 

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )

mycursor = con.cursor()
mycursor.execute("create database db1")
print("Database Created")