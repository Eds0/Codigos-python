#QUESTÃO 10: Matriz M por N mostrar número por coluna e o múltiplo de 6
matriz = []
mult6 = []
a = [0]
l = int(input('Digite um número inteiro para menor igual a 4 para ser a quantidade de linhas da matriz:'))
while l > 4 and l <=0:
    l = int(input('Digite um número inteiro para menor igual a 4 para ser a quantidade de linhas da matriz:'))
col = int(input('Digite um número inteiro para menor igual a 8 para ser a quantidade de colunas da matriz:'))
while col > 8 and col <=0:
    col = int(input('Digite um número inteiro para menor igual a 8 para ser a quantidade de colunas da matriz:'))

for linha in range(0, l):
    matriz.append([0]*col)
for linha in range(0, l):
    for coluna in range(0, col):
        matriz[linha][coluna] = input('digite um número para a matriz:')

for coluna in range(0, col):
    for linha in range(0, l):
        a = int(matriz[linha][coluna])
        if a % 6 == 0:
            mult6.append(a)
print(f'O Vetor com os múltiplos de 6 é: {mult6}')
print('A matriz formada foi:')
for linha in range(0, l):
    print(matriz[linha])

