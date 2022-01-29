#QUESTÃO 03: Apresentar o menor de 3 números.
menor = 0
for c in range(0, 3):
    n = float(input(f'Digite o {c+1}° número:'))
    if c == 0:
        menor = n
    if n <= menor:
        menor = n
print(f'O menor número digitado foi {menor}!')