import mysql.connector

mydb = mysql.connector.connect(
  host="localhost:80",
  user="yourusername",
  password="yourpassword"
)

print(mydb)
