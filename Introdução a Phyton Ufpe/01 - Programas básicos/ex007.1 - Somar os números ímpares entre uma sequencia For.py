#QUESTÃO 07: Somar os inteiros ímpares entre dois valores inteiros informados pelo usuário usando For.
n1= int(input('Digite o limite inferior:'))
while n1 < 0:
    n1 = int(input('Você digitou um número inválido, digite um novo número inteiro:'))
n2= int(input('Digite o limite superior:'))
while n2 < 0:
    n2 = int(input('Você digitou um número inválido, digite um novo número inteiro:'))
aux = n1
soma = 0
if n1 > n2:
    n1 = n2
    n2 = aux
for c in range(n1+1, n2):
    if c%2 == 1:
        soma += c
print(f'o limite inferior é: {n1} e o limite superior é: {n2} e a soma {soma}')
