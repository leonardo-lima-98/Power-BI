from random import randint
from random import choice
from Cliente.connDB import mydb, mycursor


mydb.cursor()
v = 3768
mycursor.execute(f"SELECT id, cpf, uf FROM power_bi.client WHERE id IN ({v});")

myresult = mycursor.fetchall()

print(myresult)

