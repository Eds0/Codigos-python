n = int(input('Digite a quantidade de alunos:'))
while n < 0:
    n = int(input('Digite a quantidade de alunos:'))
vtotal = []
vmaior = []
media = 0
soma = 0
for c in range(0, n):
    n1 = float(input(f'Digite a nota do {c+1}° aluno:'))
    soma += n1
    vtotal.append(n1)
media = soma/n
for c in range(0,n):
    if vtotal[c] > media:
        vmaior.append(vtotal[c])
print(f'As notas dos alunos foram: {vtotal}')
print(f'A média dos alunos foi {media} e as notas que ficaram acima da média foram: {vmaior}')