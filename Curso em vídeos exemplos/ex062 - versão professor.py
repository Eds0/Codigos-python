a1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
pa = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total+= mais
    while cont <= total:
        print('{} -> '.format(pa), end='')
        pa += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos valores você quer a mais?'))
print('Você fez uma P.A. com {} termos'.format(total))
print('FIM DA P.A.')
