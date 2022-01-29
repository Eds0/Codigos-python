#QUESTÃO 07: Somar os inteiros ímpares entre dois valores inteiros informados pelo usuário usando While.
n1 = int(input('Digite o limite inferior:'))
while n1 < 0:
    n1 = int(input('Você digitou um número inválido, digite um novo número inteiro:'))
n2 = int(input('Digite o limite superior:'))
while n2 < 0:
    n2 = int(input('Você digitou um número inválido, digite um novo número inteiro:'))
cont = n1
soma = 0
if n1 > n2:
    n1 = n2
    n2 = cont
    cont = n1
while cont != n2:
    cont += 1
    if cont%2 == 1:
        soma += cont
print(f'o limite inferior é: {n1} e o limite superior é: {n2} e a soma {soma}')
