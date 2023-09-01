# Insert Record in stud table
import mysql.connector 

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
    )

mycursor = con.cursor()
mycursor.execute("insert into stud values(1,'abc')")
con.commit()
print("Record Inserted")