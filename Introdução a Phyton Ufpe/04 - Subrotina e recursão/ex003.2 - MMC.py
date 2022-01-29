def mmc():
    n1 = int(input('Digite um número positivo'))
    while n1 <= 0:
        n1 = int(input('Você digitou um número inválido digite outro:'))
    n2 = int(input('Digite um número positivo'))
    while n2 <= 0:
        n2 = int(input('Você digitou um número inválido digite outro:'))
    div = 2
    mmc = 1
    maior = n1
    if n2 > n1:
        maior = n2
    while div != maior:
        if n1%div == 0 or n2%div == 0:
            mmc *= div
            if (n1%div == 0):
                n1 = n1/div
            if (n2%div == 0):
                n2 = n2/div
        else:
            div += 1
    print(f'O MMC é: {mmc}')


mmc()
