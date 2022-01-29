#QUESTÃO 04: Somar todos os números inteiros entre 50 e 100 usando for.
soma = 0
for c in range(50, 101,2):
    soma += c
print(f'A soma dos números pares entre 50 e 100 com o 100 incluso é: {soma}')