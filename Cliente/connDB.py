import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="81855688lima",
    database="power_bi"
)

mycursor = mydb.cursor()
