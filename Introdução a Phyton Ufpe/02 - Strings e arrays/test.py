import random
matriz = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
listaMultiplosDeSeis =[]
const = 0
for linha in range(0,4):
    for coluna in range(0,8):
        matriz[linha][coluna] = random.randrange(10)
        print(f'[{matriz[linha][coluna]:^8}]', end='')
    print()

for coluna in range(0,8):
    for linha in range(0,4):
        const = int(matriz[linha][coluna])
        if const % 6 == 0:
            listaMultiplosDeSeis.append(const)
print(listaMultiplosDeSeis)