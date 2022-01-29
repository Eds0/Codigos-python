a1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
pa = a1
cont = 10
while cont >= 1:
    print('{} -> '.format(pa), end='')
    pa += r
    cont -= 1
    if cont == 0:
        cont = int(input('Quantos valores você quer a mais?'))
print('FIM DA P.A.')

