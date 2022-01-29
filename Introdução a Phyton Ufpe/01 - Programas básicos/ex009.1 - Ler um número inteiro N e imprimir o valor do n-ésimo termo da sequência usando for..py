#QUESTÃO 09: Ler um número inteiro N e imprimir o valor do nésimo termo da sequência a seguir: [-1, 0, 5, 6, 11, 12, 17, 18, ...]
n = int(input('Digite a quantidade de termos a ser mostrado:'))
while n < 0:
    n = int(input('Você digitou um número inválido, digite um novo número inteiro:'))
a1 = 0
cont = 0
if n <=0:
    print(f'Você digitou uma número inválido para posição então não será mostrado nenhum número!')
else:
    for c in range(0, n):
        cont += 1
        if cont == 1:
            a1 = - 1
        else:
            if cont%2 == 0:
                a1 += 1
            else:
                a1 += 5
    print(f'O termo esperado é {a1}')