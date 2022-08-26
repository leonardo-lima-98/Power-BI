from Cliente.gera_cpf import geracpf
from Cliente.gera_cpf import estado
from Cliente.connDB import mydb, mycursor
from random import randint


def chamada():
    numero = str(randint(100000000, 999999999))
    cl = geracpf(num=numero)
    es = estado(num=numero[8])
    return cl, es


nus = int(input("Quantos clientes serão inseridos? "))
x = True
print(f'{nus} linhas sendo inseridas')

while x:
    val = chamada()
    if nus != 0:
        sql = "INSERT INTO client (cpf, uf) VALUES (%s, %s)"
        mycursor.execute(sql, val)

        mydb.commit()
        nus -= 1
    else:
        x = False
        print("Process complete.")



