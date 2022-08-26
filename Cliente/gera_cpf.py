from random import randint
from random import choice


def geracpf(num):
    novo_cpf = num  # 9 números aleatórios
    reverso = 10  # Contador reverso
    total = 0  # O total das multiplicações

    # Loop do CPF
    for index in range(19):
        if index > 8:  # Primeiro índice vai de 0 a 9,
            index -= 9  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1  # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:  # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0  # Zera o total
            novo_cpf += str(d)  # Concatena o digito gerado no novo cpf
    return novo_cpf


def estado(num):
    if num == "1":
        lista = ['DF', 'GO', 'MS', 'MT', 'TO']
        return choice(lista)

    elif num == "2":
        lista = ['AC', 'AM', 'AP', 'PA', 'RO', 'RR']
        return choice(lista)

    elif num == "3":
        lista = ['CE', 'MA', 'PI']
        return choice(lista)

    elif num == "4":
        lista = ['AL', 'PB', 'PE', 'RN']
        return choice(lista)

    elif num == "5":
        lista = ['BA', 'SE']
        return choice(lista)

    elif num == "6":  # MG
        return 'MG'

    elif num == "7":
        lista = ['ES', 'RJ']
        return choice(lista)

    elif num == "8":  # SP
        return 'SP'

    elif num == "9":
        lista = ['PR', 'SC']
        return choice(lista)

    else:  # RS
        return 'RS'


if __name__ == '__main__':
    def chamada():
        numero = str(randint(100000000, 999999999))
        cl = geracpf(num=numero)
        es = estado(num=numero[8])
        return cl, es
    print(chamada())
