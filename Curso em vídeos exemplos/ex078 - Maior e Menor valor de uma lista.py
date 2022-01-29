lista = list()
ma = list()
me = list()
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite o número da pos {c}:')))
    if c == 0:
        maior = lista[c]
        menor = lista[c]
    if lista[c] >= maior:
        maior = lista[c]
    if lista[c] <= menor:
        menor = lista[c]
print(f'O maior número foi {maior} e apareceu nas posições ', end='')
for p,v in enumerate(lista):
    if v == maior:
        print(f'{p}.', end='')
print()
print(f'o menor número foi {menor} e apareceu nas posições ', end='')
for p,v in enumerate(lista):
    if v == menor:
        print(f'{p}.', end='')
print()


