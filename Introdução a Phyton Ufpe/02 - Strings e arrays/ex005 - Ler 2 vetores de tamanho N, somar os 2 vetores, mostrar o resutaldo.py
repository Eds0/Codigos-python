#QUESTÃO 05: Ler 2 vetores e somar e mostrar o resultado
n = int(input('Digite o tamanho do seu Vetor:'))
while n < 0:
    n = int(input('Digite o tamanho do seu Vetor:'))
v1 = []
v2 = []
vsoma = []
for c in range(0, n):
    n1 = int(input(f'Digite o {c+1}° número para o vetor 1:'))
    v1.append(n1)
for c in range(0, n):
    n2 = int(input(f'Digite o {c+1}° número para o vetor 2:'))
    v2.append(n2)
for c in range(0, n):
    vsoma.append(v1[c] + v2[c])
print(f'vetor 1:{v1}, vetor 2: {v2} e vetor soma {vsoma}')
