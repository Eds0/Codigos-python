from math import sqrt
c0 = float(input('Digite o valor do Cateto Oposto:'))
c1 = float(input('Digite o valor do Cateto Adjacente:'))
h = sqrt(c0**2+c1**2)
print('A hipotenusa dos catetos {} e {}, é {}'.format(c0, c1, h))
