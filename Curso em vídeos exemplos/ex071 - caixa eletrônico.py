cont1 = cont10 = cont20 = cont50 = 0
print('='*30)
print('{:^30}'.format('BANCO EDSON JÚNIOR'))
print('='*30)
n = int(input('Digite quanto você quer sacar'))
while True:
    if n >= 50:
        n -= 50
        cont50 += 1
    elif n>=20:
        n -= 20
        cont20 += 1
    elif n>=10:
        n -= 10
        cont10 += 1
    elif n>=1:
        n -= 1
        cont1 +=1
    elif n == 0:
        break
print(f'Total de {cont50} cédulas de 50 R$')
print(f'Total de {cont20} cédulas de 20 R$')
print(f'Total de {cont10} cédulas de 10 R$')
print(f'Total de {cont1} cédulas de 1 R$')
