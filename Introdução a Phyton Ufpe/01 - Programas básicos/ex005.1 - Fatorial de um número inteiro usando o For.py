#QUESTÃO 05: Fatorial de um número usando o for.
n = int(input('Digite um número inteiro:'))
while n < 0:
    n = int(input('Você digitou um número inválido, digite um novo número inteiro:'))
fatorial = 1
for c in range(n, 0, -1):
    fatorial *= c
print(f'O fatorial de {n} é {fatorial}')
