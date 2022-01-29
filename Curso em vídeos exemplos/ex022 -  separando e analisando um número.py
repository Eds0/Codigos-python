num = int(input('digite um número de 4 digítos:'))
uni = num//1%10
dez = num//10%10
cen = num//100%10
mil = num//1000%10
print('Possui {} unidades'.format(uni))
print('Possui {} dezenas'.format(dez))
print('Possui {} centanas'.format(cen))
print('Possui {} milhares'.format(mil))
