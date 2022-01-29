# QUESTÃO 13: ler 2 números inteiros positivos e determinar o MDC destes 2 números.
def mdc():
    n1 = int(input('Digite um número positivo'))
    while n1 < 0:
        n1 = int(input('Você digitou um número inválido digite outro:'))
    n2 = int(input('Digite um número positivo'))
    while n2 < 0:
        n2 = int(input('Você digitou um número inválido digite outro:'))
    menor = n1
    maiordiv = 1
    if n1 > n2:
        menor = n2
    for c in range(1, menor):
        if n1%c == 0 and n2%c == 0:
            maiordiv = c
    print(f'o maior divisor de {n1} e {n2} é: {maiordiv}')


mdc()
