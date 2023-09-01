# Create Table
import mysql.connector 

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
    )

mycursor = con.cursor()
mycursor.execute("create table stud (rno int, nm varchar(20))")
print("Table Created")