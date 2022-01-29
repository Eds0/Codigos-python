lista = []
dado = []
cont = 0
pesado = []
leve = []
while True:
    nome = str(input('Nome:'))
    lista.append(nome)
    peso = float(input('Peso:'))
    lista.append(peso)
    dado.append(lista[:])
    lista.clear()
    cont += 1
    resp = str(input('Deseja continuar? [S/N]')).upper()
    if 'N' in resp:
        break
for c in dado:
    if c==0:
        pesado.append(c)
        leve.append(c)
    elif c[1] > pesado[1]:
        pesado.clear()
        pesado.append(c)
    elif c[1] == pesado[1]:
        pesado.append(c)
    elif c[1] < leve[1]:
        leve.clear()
        leve.append(c)
print(f'Foram cadastradas {cont} pessoas.')
if len(pesado) > 1:
    print(f'Os mais pesados foram: {pesado}')
else:
    print(f'O mais pesado é: {pesado}')
if len(leve) > 1:
    print(f'Os mais leves foram: {leve}')
else:
    print(f'O mais leve é: {leve}')