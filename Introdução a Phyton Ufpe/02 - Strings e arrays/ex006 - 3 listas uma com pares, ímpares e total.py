#QUESTÃO 06: 3 listas com pares, ímpares e total
n = int(input('Digite o tamanho do seu Vetor:'))
while n < 0:
    n = int(input('Digite o tamanho do seu Vetor:'))
vpar = []
vimpar = []
vtotal = []
for c in range(0, n):
    n1 = int(input(f'Digite o {c+1}° número para o vetor 1:'))
    vtotal.append(n1)
    if n1%2 == 0:
        vpar.append(n1)
    else:
        vimpar.append(n1)
print(f'O vetor com todos os números digitados é, vtotal: {vtotal}')
print(f'O vetor apenas com os números pares é, vpares: {vpar}')
print(f'O vetor apenas com os números ímpares é, vimpar: {vimpar}')