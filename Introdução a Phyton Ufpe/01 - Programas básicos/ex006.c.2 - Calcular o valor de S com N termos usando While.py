#QUESTÃO 06: Calcular o valor da série com N termos utilizando while.
a = 37
b = 38
n = int(input('Digite a quantidade de termos da série:'))
while n < 0:
    n = int(input('Você digitou um número inválido, digite um novo número inteiro:'))
cont = s = 0
while cont < n:
    s += (a-cont)*(b-cont)/(cont+1)
    cont+=1
print(f'O valor total de S é {s:.2f}')
